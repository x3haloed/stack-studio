#!/usr/bin/env python3
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("audit_stack.py")
SPEC = importlib.util.spec_from_file_location("audit_stack", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
StackAuditor = MODULE.StackAuditor


class StackAuditorTests(unittest.TestCase):
    def make_repo(self):
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
        (root / "README.md").write_text("# Test\n\n[Skill](skills/example/SKILL.md)\n", encoding="utf-8")
        skill = root / "skills" / "example"
        skill.mkdir(parents=True)
        (skill / "SKILL.md").write_text("---\nname: example\ndescription: Use when testing an example.\n---\n\n# Example\n", encoding="utf-8")
        for folder in (".claude-plugin", ".codex-plugin"):
            (root / folder).mkdir()
            (root / folder / "plugin.json").write_text(json.dumps({"name": "test-stack", "version": "1.0.0", "description": "Test", "skills": "./skills/"}), encoding="utf-8")
        return temp, root

    def test_valid_repo_is_structure_verified_not_behavior_verified(self):
        temp, root = self.make_repo()
        self.addCleanup(temp.cleanup)
        auditor = StackAuditor(str(root))
        self.assertTrue(auditor.audit())
        self.assertEqual("structure-verified", auditor.platform_support["claude"]["level"])
        self.assertEqual("structure-verified", auditor.platform_support["openai"]["level"])
        self.assertEqual("not-claimed", auditor.platform_support["cursor"]["level"])
        self.assertNotIn("%", auditor.generate_report())

    def test_name_mismatch_is_error(self):
        temp, root = self.make_repo()
        self.addCleanup(temp.cleanup)
        path = root / "skills" / "example" / "SKILL.md"
        path.write_text(path.read_text(encoding="utf-8").replace("name: example", "name: other"), encoding="utf-8")
        auditor = StackAuditor(str(root))
        self.assertFalse(auditor.audit())
        self.assertTrue(any("does not match directory" in item for item in auditor.errors))

    def test_declared_manifest_path_must_exist(self):
        temp, root = self.make_repo()
        self.addCleanup(temp.cleanup)
        manifest = root / ".codex-plugin" / "plugin.json"
        data = json.loads(manifest.read_text(encoding="utf-8"))
        data["skills"] = "./missing/"
        manifest.write_text(json.dumps(data), encoding="utf-8")
        auditor = StackAuditor(str(root))
        self.assertFalse(auditor.audit())
        self.assertTrue(any("path does not exist" in item for item in auditor.errors))

    def test_platform_filter_limits_support_report(self):
        temp, root = self.make_repo()
        self.addCleanup(temp.cleanup)
        auditor = StackAuditor(str(root), target_platform="openai")
        auditor.audit()
        self.assertEqual(["openai"], list(auditor.platform_support))


if __name__ == "__main__":
    unittest.main()
