import json
import tempfile
import unittest
from pathlib import Path

import stack_eval


SCENARIOS = {
    "schema_version": 1,
    "scenarios": [
        {
            "id": "example",
            "name": "Example scenario",
            "target": "./example-stack",
            "prompt": "Use the stack to complete an example.",
            "checks": [
                {"id": "first-check", "text": "The first behavior is present."},
                {"id": "second-check", "text": "The second behavior is present."},
            ],
        }
    ],
}


class StackEvalTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.scenarios = self.root / "scenarios.json"
        self.scenarios.write_text(json.dumps(SCENARIOS))

    def tearDown(self):
        self.temp_dir.cleanup()

    def complete_run(self, name, statuses):
        run_dir = self.root / name
        stack_eval.init_run(self.scenarios, "example", name, run_dir)
        (run_dir / "raw-output.md").write_text(f"Raw output for {name}.\n")
        assessment = json.loads((run_dir / "assessment.json").read_text())
        for result, status in zip(assessment["checks"], statuses):
            result["status"] = status
            result["evidence"] = f"Evidence for {result['id']}."
        (run_dir / "assessment.json").write_text(json.dumps(assessment))
        stack_eval.finalize_run(run_dir)
        return run_dir

    def test_init_and_finalize(self):
        run_dir = self.complete_run("candidate", ["pass", "not_exercised"])
        summary = (run_dir / "summary.md").read_text()
        self.assertIn("Pass: 1", summary)
        self.assertIn("Not exercised: 1", summary)

    def test_finalize_rejects_unassessed_check(self):
        run_dir = self.root / "candidate"
        stack_eval.init_run(self.scenarios, "example", "candidate", run_dir)
        (run_dir / "raw-output.md").write_text("Raw output.\n")
        with self.assertRaisesRegex(stack_eval.EvalError, "still unassessed"):
            stack_eval.finalize_run(run_dir)

    def test_compare_reports_improvement_without_choosing_winner(self):
        baseline = self.complete_run("baseline", ["pass", "fail"])
        candidate = self.complete_run("candidate", ["pass", "pass"])
        output = self.root / "comparison"
        stack_eval.compare_runs(baseline, candidate, output)
        result = json.loads((output / "comparison.json").read_text())
        self.assertEqual(result["improvements"], ["second-check"])
        self.assertEqual(result["regressions"], [])
        self.assertNotIn("winner", result)

    def test_compare_rejects_nonempty_output(self):
        baseline = self.complete_run("baseline", ["pass", "fail"])
        candidate = self.complete_run("candidate", ["pass", "pass"])
        output = self.root / "comparison"
        output.mkdir()
        (output / "keep.txt").write_text("preserve")
        with self.assertRaisesRegex(stack_eval.EvalError, "not empty"):
            stack_eval.compare_runs(baseline, candidate, output)


if __name__ == "__main__":
    unittest.main()
