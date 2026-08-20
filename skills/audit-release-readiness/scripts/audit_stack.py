#!/usr/bin/env python3
"""Deterministic release-readiness checks for an agent skill stack."""

import argparse
import json
import os
import re
import sys
from pathlib import Path

PLATFORMS = ("claude", "openai", "cursor", "antigravity", "copilot")


class StackAuditor:
    """Report only properties established from repository contents."""

    def __init__(self, root_dir, strict=False, target_platform=None):
        self.root = Path(root_dir).resolve()
        self.strict = strict
        self.target_platform = target_platform
        self.errors, self.warnings = [], []
        self.skills_found, self.manifests_found = [], {}
        self.platform_support = {}

    def audit(self):
        if not self.root.is_dir():
            self.errors.append("Root path does not exist or is not a directory")
            return False
        self._audit_skills()
        self._audit_manifests()
        self._audit_links()
        self._audit_scripts()
        self._audit_cleanliness()
        self._classify_support()
        return not self.errors

    def _frontmatter(self, path):
        lines = path.read_text(encoding="utf-8").splitlines()
        if not lines or lines[0].strip() != "---":
            return None, "missing opening YAML frontmatter delimiter"
        try:
            end = next(i for i, line in enumerate(lines[1:], 1) if line.strip() == "---")
        except StopIteration:
            return None, "missing closing YAML frontmatter delimiter"
        data = {}
        for line in lines[1:end]:
            if line and not line[0].isspace() and ":" in line:
                key, value = line.split(":", 1)
                data[key.strip()] = value.strip().strip("\"'")
        return data, None

    def _audit_skills(self):
        paths = sorted((self.root / "skills").glob("*/SKILL.md"))
        if not paths:
            self.errors.append("No skills/<name>/SKILL.md files found")
        for path in paths:
            rel = path.relative_to(self.root).as_posix()
            try:
                data, problem = self._frontmatter(path)
            except OSError as exc:
                self.errors.append(f"[{rel}] cannot read file: {exc}")
                continue
            if problem:
                self.errors.append(f"[{rel}] {problem}")
                continue
            name, description = data.get("name", "").strip(), data.get("description", "").strip()
            if not name:
                self.errors.append(f"[{rel}] missing required 'name'")
            elif name != path.parent.name:
                self.errors.append(f"[{rel}] name '{name}' does not match directory '{path.parent.name}'")
            if not description:
                self.errors.append(f"[{rel}] missing required 'description'")
            elif len(description) > 1024:
                self.errors.append(f"[{rel}] description exceeds 1024 characters")
            if description and not description.startswith("Use when"):
                self.warnings.append(f"[{rel}] description does not begin with 'Use when'")
            if len(path.read_text(encoding="utf-8").splitlines()) > 500:
                self.warnings.append(f"[{rel}] SKILL.md exceeds 500 lines; consider progressive disclosure")
            self.skills_found.append({"path": rel, "name": name, "description": description})

    def _load_manifest(self, label, path):
        if not path.exists():
            return
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            self.errors.append(f"[{label}] invalid JSON: {exc}")
            return
        if not isinstance(data, dict):
            self.errors.append(f"[{label}] manifest must be a JSON object")
            return
        self.manifests_found[label] = data
        name = data.get("name")
        if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
            self.errors.append(f"[{label}] 'name' must be a non-empty kebab-case string")
        for field in ("version", "description"):
            if field in data and not isinstance(data[field], str):
                self.errors.append(f"[{label}] '{field}' must be a string")
        for field in ("skills", "commands", "agents", "hooks", "mcp", "apps"):
            values = data.get(field)
            if values is None:
                continue
            values = values if isinstance(values, list) else [values]
            if not all(isinstance(value, str) for value in values):
                self.errors.append(f"[{label}] '{field}' must be a path string or list")
                continue
            for value in values:
                target = (self.root / value).resolve()
                try:
                    target.relative_to(self.root)
                except ValueError:
                    self.errors.append(f"[{label}] '{field}' path escapes repository: {value}")
                    continue
                if not target.exists():
                    self.errors.append(f"[{label}] '{field}' path does not exist: {value}")

    def _audit_manifests(self):
        self._load_manifest("claude", self.root / ".claude-plugin" / "plugin.json")
        self._load_manifest("openai", self.root / ".codex-plugin" / "plugin.json")
        for path in (self.root / "plugin.json", self.root / ".cursor-plugin" / "plugin.json"):
            if path.exists():
                self.warnings.append(f"[{path.relative_to(self.root)}] is not evidence for a documented harness contract")

    def _audit_links(self):
        paths = [self.root / "README.md"] + [self.root / s["path"] for s in self.skills_found]
        link_pattern = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
        for path in paths:
            if not path.exists():
                if path.name == "README.md":
                    self.errors.append("README.md is required for release handoff")
                continue
            for link in link_pattern.findall(path.read_text(encoding="utf-8")):
                raw = link.strip().split("#", 1)[0]
                if not raw or "://" in raw or raw.startswith(("mailto:", "<")):
                    continue
                target = (path.parent / raw).resolve()
                try:
                    target.relative_to(self.root)
                except ValueError:
                    self.errors.append(f"[{path.relative_to(self.root)}] link escapes repository: {link}")
                    continue
                if not target.exists():
                    self.errors.append(f"[{path.relative_to(self.root)}] broken relative link: {link}")

    def _audit_scripts(self):
        if os.name != "posix":
            return
        for path in self.root.glob("skills/*/scripts/**/*"):
            if not path.is_file():
                continue
            try:
                first = path.open(encoding="utf-8").readline()
            except (OSError, UnicodeDecodeError):
                continue
            if first.startswith("#!") and not os.access(path, os.X_OK):
                self.errors.append(f"[{path.relative_to(self.root)}] shebang entrypoint is not executable")

    def _audit_cleanliness(self):
        for path in self.root.rglob("*"):
            if ".git" in path.parts:
                continue
            if path.name in (".DS_Store", "__pycache__") or path.suffix in (".pyc", ".pyo"):
                self.errors.append(f"[{path.relative_to(self.root)}] generated or platform-local artifact must not ship")

    def _classify_support(self):
        contracts = {"claude": "claude", "openai": "openai", "cursor": None, "antigravity": None, "copilot": None}
        selected = [self.target_platform] if self.target_platform else PLATFORMS
        for platform in selected:
            key = contracts[platform]
            contract_present = key in self.manifests_found and bool(self.skills_found)
            verified = contract_present and not self.errors
            if verified:
                level = "structure-verified"
                evidence = [f"validated {'.claude-plugin' if platform == 'claude' else '.codex-plugin'}/plugin.json", "validated skill inventory"]
            elif contract_present:
                level = "structure-incomplete"
                evidence = [f"deterministic audit has {len(self.errors)} error(s)"]
            else:
                level = "not-claimed"
                evidence = ["no deterministic harness contract is implemented"]
            self.platform_support[platform] = {
                "level": level,
                "evidence": evidence,
                "limits": "Discovery and behavior require recorded tests in the target harness.",
            }

    def generate_report(self, as_json=False):
        passed = not self.errors and (not self.strict or not self.warnings)
        data = {"root": self.root.name, "passed": passed, "skills_count": len(self.skills_found), "skills": self.skills_found, "manifests": sorted(self.manifests_found), "errors": self.errors, "warnings": self.warnings, "platform_support": self.platform_support}
        if as_json:
            return json.dumps(data, indent=2)
        lines = ["STACK STUDIO RELEASE-READINESS AUDIT", f"Repository: {self.root.name}", f"Skills: {len(self.skills_found)}", "", "SUPPORT EVIDENCE:"]
        for platform, result in self.platform_support.items():
            lines.append(f"  {platform}: {result['level']}")
            lines.extend(f"    - {item}" for item in result["evidence"])
            lines.append(f"    - limit: {result['limits']}")
        if self.errors:
            lines.extend(["", "ERRORS:"] + [f"  - {item}" for item in self.errors])
        if self.warnings:
            lines.extend(["", "WARNINGS:"] + [f"  - {item}" for item in self.warnings])
        lines.extend(["", f"RESULT: {'PASSED' if passed else 'FAILED'}"])
        return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Audit deterministic release-readiness properties")
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--platform", choices=PLATFORMS)
    args = parser.parse_args()
    auditor = StackAuditor(args.root, args.strict, args.platform)
    auditor.audit()
    print(auditor.generate_report(args.json))
    sys.exit(0 if not auditor.errors and (not args.strict or not auditor.warnings) else 1)


if __name__ == "__main__":
    main()
