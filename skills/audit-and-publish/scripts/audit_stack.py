#!/usr/bin/env python3
"""
Stack Studio Repository Auditor
Validates a stack/plugin repository for structural integrity, skill frontmatter correctness,
script executable permissions, and cross-platform compatibility across major agentic harnesses
(Anthropic Claude Code, Cursor IDE, Google Antigravity, OpenAI Codex, GitHub Copilot).
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple


class StackAuditor:
    def __init__(self, root_dir: str, strict: bool = False, target_platform: Optional[str] = None):
        self.root = Path(root_dir).resolve()
        self.strict = strict
        self.target_platform = target_platform.lower() if target_platform else None

        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.info: List[str] = []
        self.skills_found: List[Dict[str, Any]] = []
        self.manifests_found: Dict[str, Any] = {}
        self.platform_compatibility: Dict[str, Dict[str, Any]] = {}

    def audit(self) -> bool:
        if not self.root.exists() or not self.root.is_dir():
            self.errors.append(f"Root path does not exist or is not a directory: {self.root}")
            return False

        self._audit_skills()
        self._audit_manifests_and_configs()
        self._audit_scripts_and_permissions()
        self._audit_cross_platform_compatibility()

        passed = len(self.errors) == 0
        return passed

    def _parse_yaml_frontmatter(self, file_path: Path) -> Tuple[Optional[Dict[str, str]], List[str]]:
        errors = []
        try:
            content = file_path.read_text(encoding="utf-8")
        except Exception as e:
            return None, [f"Failed to read file: {e}"]

        lines = content.splitlines()
        if not lines or lines[0].strip() != "---":
            return None, ["Missing opening YAML frontmatter delimiter (---) on line 1"]

        fm_lines = []
        closing_found = False
        for idx, line in enumerate(lines[1:], start=2):
            if line.strip() == "---":
                closing_found = True
                break
            fm_lines.append(line)

        if not closing_found:
            return None, ["Missing closing YAML frontmatter delimiter (---)"]

        # Simple robust key-value YAML parser for name and description
        fm_dict: Dict[str, str] = {}
        idx = 0
        while idx < len(fm_lines):
            line = fm_lines[idx]
            if ":" not in line or line.startswith(" ") or line.startswith("\t"):
                idx += 1
                continue

            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()

            # Handle multiline scalar indicators (| or >)
            if value in ("|", "|-", "|+", ">", ">-", ">+"):
                block_lines = []
                idx += 1
                while idx < len(fm_lines):
                    next_line = fm_lines[idx]
                    if next_line.startswith(" ") or next_line.startswith("\t") or not next_line.strip():
                        block_lines.append(next_line.strip())
                        idx += 1
                    else:
                        break
                fm_dict[key] = " ".join(block_lines).strip()
                continue
            else:
                # Strip wrapping quotes if present
                if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
                    value = value[1:-1].strip()
                fm_dict[key] = value

            idx += 1

        return fm_dict, errors

    def _audit_skills(self):
        skill_files = list(self.root.glob("**/SKILL.md"))
        # Exclude common non-project dirs
        skill_files = [
            f for f in skill_files
            if not any(part.startswith(".") and part not in (".claude", ".agents", ".cursor") for part in f.parts)
            and "node_modules" not in f.parts
            and ".venv" not in f.parts
            and "__pycache__" not in f.parts
        ]

        if not skill_files:
            self.warnings.append("No SKILL.md files found in the repository.")
            return

        for sf in skill_files:
            rel_path = sf.relative_to(self.root)
            parent_dir_name = sf.parent.name

            fm, fm_errors = self._parse_yaml_frontmatter(sf)
            if fm_errors:
                for err in fm_errors:
                    self.errors.append(f"[{rel_path}] {err}")
                continue

            if not fm:
                self.errors.append(f"[{rel_path}] Empty or invalid YAML frontmatter")
                continue

            name = fm.get("name", "").strip()
            description = fm.get("description", "").strip()

            if not name:
                self.errors.append(f"[{rel_path}] Frontmatter missing required 'name' field")
            elif name != parent_dir_name:
                self.warnings.append(
                    f"[{rel_path}] Frontmatter name '{name}' does not match parent directory '{parent_dir_name}'"
                )

            if not description:
                self.errors.append(f"[{rel_path}] Frontmatter missing required 'description' field")
            elif len(description) < 15:
                self.warnings.append(f"[{rel_path}] Frontmatter description is very short ({len(description)} chars). Provide concrete triggering conditions.")
            elif len(description) > 600:
                self.warnings.append(f"[{rel_path}] Frontmatter description exceeds recommended length ({len(description)} chars > 600). Keep metadata compact.")

            # Check line length of SKILL.md (progressive disclosure recommendation < 500 lines)
            try:
                line_count = len(sf.read_text(encoding="utf-8").splitlines())
                if line_count > 500:
                    self.warnings.append(
                        f"[{rel_path}] SKILL.md is {line_count} lines long (recommendation: < 500 lines). Consider moving detailed references into references/."
                    )
            except Exception:
                pass

            self.skills_found.append({
                "path": str(rel_path),
                "name": name,
                "description": description,
                "parent_dir": parent_dir_name
            })

    def _audit_manifests_and_configs(self):
        manifest_checks = [
            ("plugin.json", self.root / "plugin.json"),
            (".claude-plugin/plugin.json", self.root / ".claude-plugin" / "plugin.json"),
            (".cursor-plugin/plugin.json", self.root / ".cursor-plugin" / "plugin.json"),
            ("mcp.json", self.root / "mcp.json"),
            ("mcp_config.json", self.root / "mcp_config.json"),
            ("hooks.json", self.root / "hooks.json"),
            ("CLAUDE.md", self.root / "CLAUDE.md"),
            ("AGENTS.md", self.root / "AGENTS.md"),
            ("GEMINI.md", self.root / "GEMINI.md"),
            (".github/copilot-instructions.md", self.root / ".github" / "copilot-instructions.md"),
        ]

        for label, path in manifest_checks:
            if path.exists():
                if path.suffix == ".json":
                    try:
                        data = json.loads(path.read_text(encoding="utf-8"))
                        self.manifests_found[label] = data
                        self.info.append(f"Found valid manifest: {label}")
                    except Exception as e:
                        self.errors.append(f"Invalid JSON in {label}: {e}")
                else:
                    self.manifests_found[label] = True
                    self.info.append(f"Found configuration file: {label}")

    def _audit_scripts_and_permissions(self):
        for script_file in self.root.glob("**/scripts/*"):
            if script_file.is_file() and script_file.suffix in (".sh", ".py", ".bash", ".zsh", ".rb", ".js", ".ts"):
                rel_path = script_file.relative_to(self.root)
                # Check executable bit on POSIX systems
                if os.name == "posix":
                    is_executable = os.access(script_file, os.X_OK)
                    if not is_executable and script_file.suffix in (".sh", ".bash"):
                        self.warnings.append(f"Script [{rel_path}] is not marked executable (chmod +x recommended).")

    def _audit_cross_platform_compatibility(self):
        # 1. Anthropic Claude Code
        claude_score = 0
        claude_reasons = []
        if ".claude-plugin/plugin.json" in self.manifests_found:
            claude_score += 40
            claude_reasons.append("Claude Code plugin manifest (.claude-plugin/plugin.json) present")
        elif (self.root / "SKILL.md").exists():
            claude_score += 40
            claude_reasons.append("Root SKILL.md present for standalone skill discovery")

        if (self.root / "skills").exists() or (self.root / ".claude" / "skills").exists():
            claude_score += 30
            claude_reasons.append("Skills directory available")
        if (self.root / "CLAUDE.md").exists() or (self.root / "AGENTS.md").exists():
            claude_score += 30
            claude_reasons.append("Agent guidelines (CLAUDE.md or AGENTS.md) present")

        # 2. Cursor IDE
        cursor_score = 0
        cursor_reasons = []
        if "plugin.json" in self.manifests_found or ".cursor-plugin/plugin.json" in self.manifests_found:
            cursor_score += 40
            cursor_reasons.append("Plugin manifest (plugin.json or .cursor-plugin/plugin.json) present")
        if (self.root / "skills").exists():
            cursor_score += 30
            cursor_reasons.append("Skills directory present")
        if (self.root / "rules").exists() or (self.root / ".cursorrules").exists() or (self.root / "commands").exists():
            cursor_score += 30
            cursor_reasons.append("Rules or commands present")

        # 3. Google Antigravity
        agy_score = 0
        agy_reasons = []
        if "plugin.json" in self.manifests_found:
            agy_score += 40
            agy_reasons.append("Plugin manifest (plugin.json) present")
        if (self.root / "skills").exists():
            agy_score += 30
            agy_reasons.append("Skills directory present")
        if "mcp_config.json" in self.manifests_found or "mcp.json" in self.manifests_found or "hooks.json" in self.manifests_found or (self.root / "rules").exists():
            agy_score += 30
            agy_reasons.append("MCP, hooks, or rules present")

        # 4. OpenAI Codex
        openai_score = 0
        openai_reasons = []
        if "plugin.json" in self.manifests_found:
            openai_score += 40
            openai_reasons.append("Plugin manifest (plugin.json) present")
        if (self.root / "skills").exists():
            openai_score += 40
            openai_reasons.append("Skills directory present")
        if "mcp.json" in self.manifests_found or (self.root / ".well-known" / "mcp.json").exists():
            openai_score += 20
            openai_reasons.append("MCP discovery present")

        # 5. GitHub Copilot
        copilot_score = 0
        copilot_reasons = []
        if "plugin.json" in self.manifests_found:
            copilot_score += 40
            copilot_reasons.append("Plugin manifest present")
        if (self.root / ".github" / "copilot-instructions.md").exists() or (self.root / "AGENTS.md").exists():
            copilot_score += 30
            copilot_reasons.append("Instructions / AGENTS.md present")
        if (self.root / "skills").exists() or (self.root / "agents").exists():
            copilot_score += 30
            copilot_reasons.append("Skills or custom agents present")

        self.platform_compatibility = {
            "Claude Code": {"score": min(claude_score, 100), "reasons": claude_reasons},
            "Cursor IDE": {"score": min(cursor_score, 100), "reasons": cursor_reasons},
            "Google Antigravity": {"score": min(agy_score, 100), "reasons": agy_reasons},
            "OpenAI Codex": {"score": min(openai_score, 100), "reasons": openai_reasons},
            "GitHub Copilot": {"score": min(copilot_score, 100), "reasons": copilot_reasons},
        }

    def generate_report(self, as_json: bool = False) -> str:
        if as_json:
            report_data = {
                "root": str(self.root),
                "passed": len(self.errors) == 0,
                "skills_count": len(self.skills_found),
                "skills": self.skills_found,
                "manifests": list(self.manifests_found.keys()),
                "errors": self.errors,
                "warnings": self.warnings,
                "platform_compatibility": self.platform_compatibility,
            }
            return json.dumps(report_data, indent=2)

        lines = []
        lines.append("=" * 60)
        lines.append(f"STACK STUDIO AUDIT REPORT: {self.root.name}")
        lines.append("=" * 60)
        lines.append(f"Directory: {self.root}")
        lines.append(f"Skills Found: {len(self.skills_found)}")
        lines.append(f"Manifests / Configs Found: {len(self.manifests_found)}")
        lines.append("")

        if self.skills_found:
            lines.append("SKILLS SUMMARY:")
            for s in self.skills_found:
                lines.append(f"  • {s['name']:<28} ({s['path']})")
            lines.append("")

        lines.append("PLATFORM COMPATIBILITY SCORES:")
        for platform, data in self.platform_compatibility.items():
            status = "✓ Ready" if data["score"] >= 70 else "△ Partial" if data["score"] >= 40 else "✗ Missing"
            lines.append(f"  • {platform:<20} {data['score']:>3}%  [{status}]")
            for r in data["reasons"]:
                lines.append(f"      - {r}")
        lines.append("")

        if self.errors:
            lines.append(f"ERRORS ({len(self.errors)}):")
            for err in self.errors:
                lines.append(f"  [ERROR] {err}")
            lines.append("")

        if self.warnings:
            lines.append(f"WARNINGS ({len(self.warnings)}):")
            for warn in self.warnings:
                lines.append(f"  [WARN]  {warn}")
            lines.append("")

        overall = "PASSED" if len(self.errors) == 0 else "FAILED"
        lines.append("-" * 60)
        lines.append(f"OVERALL STATUS: {overall}")
        lines.append("-" * 60)

        return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Audit a stack/plugin repository for cross-platform compatibility.")
    parser.add_argument("root", nargs="?", default=".", help="Root directory of the stack repository to audit (default: .)")
    parser.add_argument("--json", action="store_true", help="Output report in JSON format")
    parser.add_argument("--strict", action="store_true", help="Fail on warnings as well as errors")
    parser.add_argument("--platform", choices=["claude", "cursor", "antigravity", "openai", "copilot"], help="Filter or target specific platform")

    args = parser.parse_args()

    auditor = StackAuditor(root_dir=args.root, strict=args.strict, target_platform=args.platform)
    passed = auditor.audit()
    print(auditor.generate_report(as_json=args.json))

    if not passed or (args.strict and auditor.warnings):
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
