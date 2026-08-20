#!/usr/bin/env python3
"""Create, validate, finalize, and compare stack-level evaluation runs."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


STATUSES = {"pass", "fail", "not_exercised", "unassessed"}
FINAL_STATUSES = STATUSES - {"unassessed"}


class EvalError(ValueError):
    pass


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text())
    except FileNotFoundError as exc:
        raise EvalError(f"file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise EvalError(f"invalid JSON in {path}: {exc}") from exc


def write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def require_string(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise EvalError(f"{label} must be a non-empty string")
    return value.strip()


def validate_scenario_set(data: Any) -> dict[str, Any]:
    if not isinstance(data, dict):
        raise EvalError("scenario file must contain a JSON object")
    if data.get("schema_version") != 1:
        raise EvalError("scenario file schema_version must be 1")
    scenarios = data.get("scenarios")
    if not isinstance(scenarios, list) or not scenarios:
        raise EvalError("scenarios must be a non-empty array")

    scenario_ids: set[str] = set()
    for index, scenario in enumerate(scenarios):
        label = f"scenarios[{index}]"
        if not isinstance(scenario, dict):
            raise EvalError(f"{label} must be an object")
        scenario_id = require_string(scenario.get("id"), f"{label}.id")
        if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", scenario_id):
            raise EvalError(f"{label}.id must use lowercase letters, digits, and hyphens")
        if scenario_id in scenario_ids:
            raise EvalError(f"duplicate scenario id: {scenario_id}")
        scenario_ids.add(scenario_id)
        require_string(scenario.get("name"), f"{label}.name")
        require_string(scenario.get("target"), f"{label}.target")
        require_string(scenario.get("prompt"), f"{label}.prompt")

        checks = scenario.get("checks")
        if not isinstance(checks, list) or not checks:
            raise EvalError(f"{label}.checks must be a non-empty array")
        check_ids: set[str] = set()
        for check_index, check in enumerate(checks):
            check_label = f"{label}.checks[{check_index}]"
            if not isinstance(check, dict):
                raise EvalError(f"{check_label} must be an object")
            check_id = require_string(check.get("id"), f"{check_label}.id")
            if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", check_id):
                raise EvalError(f"{check_label}.id must use lowercase letters, digits, and hyphens")
            if check_id in check_ids:
                raise EvalError(f"duplicate check id in {scenario_id}: {check_id}")
            check_ids.add(check_id)
            require_string(check.get("text"), f"{check_label}.text")
    return data


def select_scenario(data: dict[str, Any], scenario_id: str) -> dict[str, Any]:
    for scenario in data["scenarios"]:
        if scenario["id"] == scenario_id:
            return scenario
    available = ", ".join(item["id"] for item in data["scenarios"])
    raise EvalError(f"unknown scenario {scenario_id!r}; available: {available}")


def ensure_new_directory(path: Path) -> None:
    if path.exists():
        if not path.is_dir():
            raise EvalError(f"output path exists and is not a directory: {path}")
        if any(path.iterdir()):
            raise EvalError(f"output directory is not empty: {path}")
    else:
        path.mkdir(parents=True)


def init_run(scenarios_path: Path, scenario_id: str, candidate: str, output: Path) -> None:
    data = validate_scenario_set(load_json(scenarios_path))
    scenario = select_scenario(data, scenario_id)
    candidate = require_string(candidate, "candidate")
    ensure_new_directory(output)

    write_json(output / "scenario.json", {"schema_version": 1, **scenario})
    write_json(
        output / "run.json",
        {
            "schema_version": 1,
            "scenario_id": scenario_id,
            "candidate": candidate,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "raw_output": "raw-output.md",
            "assessment": "assessment.json",
        },
    )
    (output / "prompt.md").write_text(
        f"# {scenario['name']}\n\n"
        f"Target: `{scenario['target']}`\n\n"
        f"## Prompt\n\n{scenario['prompt']}\n"
    )
    (output / "raw-output.md").write_text("")
    write_json(
        output / "assessment.json",
        {
            "schema_version": 1,
            "scenario_id": scenario_id,
            "candidate": candidate,
            "checks": [
                {
                    "id": check["id"],
                    "status": "unassessed",
                    "evidence": "",
                }
                for check in scenario["checks"]
            ],
            "notes": "",
        },
    )


def validate_assessment(run_dir: Path, require_final: bool = True) -> tuple[dict[str, Any], dict[str, Any]]:
    scenario = load_json(run_dir / "scenario.json")
    assessment = load_json(run_dir / "assessment.json")
    if not isinstance(scenario, dict) or scenario.get("schema_version") != 1:
        raise EvalError(f"invalid scenario snapshot in {run_dir}")
    if not isinstance(assessment, dict) or assessment.get("schema_version") != 1:
        raise EvalError(f"invalid assessment in {run_dir}")
    if assessment.get("scenario_id") != scenario.get("id"):
        raise EvalError("assessment scenario_id does not match scenario snapshot")

    expected = {check["id"]: check for check in scenario.get("checks", [])}
    results = assessment.get("checks")
    if not isinstance(results, list):
        raise EvalError("assessment.checks must be an array")
    actual: dict[str, dict[str, Any]] = {}
    for result in results:
        if not isinstance(result, dict):
            raise EvalError("each assessment check must be an object")
        check_id = require_string(result.get("id"), "assessment check id")
        if check_id in actual:
            raise EvalError(f"duplicate assessment check: {check_id}")
        status = result.get("status")
        if status not in STATUSES:
            raise EvalError(f"invalid status for {check_id}: {status!r}")
        evidence = result.get("evidence")
        if not isinstance(evidence, str):
            raise EvalError(f"evidence for {check_id} must be a string")
        if require_final and status not in FINAL_STATUSES:
            raise EvalError(f"check {check_id} is still unassessed")
        if require_final and not evidence.strip():
            raise EvalError(f"check {check_id} requires evidence")
        actual[check_id] = result

    if set(actual) != set(expected):
        missing = sorted(set(expected) - set(actual))
        extra = sorted(set(actual) - set(expected))
        raise EvalError(f"assessment check mismatch; missing={missing}, extra={extra}")
    return scenario, assessment


def counts(assessment: dict[str, Any]) -> dict[str, int]:
    result = {status: 0 for status in FINAL_STATUSES}
    for check in assessment["checks"]:
        result[check["status"]] += 1
    return result


def finalize_run(run_dir: Path) -> None:
    raw_output = run_dir / "raw-output.md"
    if not raw_output.exists() or not raw_output.read_text().strip():
        raise EvalError(f"raw agent output is empty: {raw_output}")
    scenario, assessment = validate_assessment(run_dir, require_final=True)
    summary_counts = counts(assessment)
    by_id = {item["id"]: item for item in assessment["checks"]}

    lines = [
        f"# {scenario['name']} — {assessment['candidate']}",
        "",
        "## Result",
        "",
        f"- Pass: {summary_counts['pass']}",
        f"- Fail: {summary_counts['fail']}",
        f"- Not exercised: {summary_counts['not_exercised']}",
        "",
        "## Checks",
        "",
    ]
    for check in scenario["checks"]:
        result = by_id[check["id"]]
        lines.extend(
            [
                f"### {check['id']} — {result['status']}",
                "",
                check["text"],
                "",
                f"Evidence: {result['evidence'].strip()}",
                "",
            ]
        )
    notes = assessment.get("notes", "")
    if isinstance(notes, str) and notes.strip():
        lines.extend(["## Notes", "", notes.strip(), ""])
    (run_dir / "summary.md").write_text("\n".join(lines))


def compare_runs(baseline_dir: Path, candidate_dir: Path, output: Path) -> None:
    base_scenario, baseline = validate_assessment(baseline_dir, require_final=True)
    cand_scenario, candidate = validate_assessment(candidate_dir, require_final=True)
    if base_scenario["id"] != cand_scenario["id"]:
        raise EvalError("cannot compare runs from different scenarios")
    base_checks = {item["id"]: item for item in baseline["checks"]}
    cand_checks = {item["id"]: item for item in candidate["checks"]}
    if set(base_checks) != set(cand_checks):
        raise EvalError("cannot compare runs with different check sets")

    transitions = []
    regressions = []
    improvements = []
    for check in base_scenario["checks"]:
        check_id = check["id"]
        before = base_checks[check_id]["status"]
        after = cand_checks[check_id]["status"]
        transition = {"id": check_id, "before": before, "after": after}
        transitions.append(transition)
        if before == "pass" and after != "pass":
            regressions.append(check_id)
        if before != "pass" and after == "pass":
            improvements.append(check_id)

    result = {
        "schema_version": 1,
        "scenario_id": base_scenario["id"],
        "baseline": baseline["candidate"],
        "candidate": candidate["candidate"],
        "baseline_counts": counts(baseline),
        "candidate_counts": counts(candidate),
        "improvements": improvements,
        "regressions": regressions,
        "transitions": transitions,
    }
    ensure_new_directory(output)
    write_json(output / "comparison.json", result)
    lines = [
        f"# {base_scenario['name']} comparison",
        "",
        f"Baseline: **{baseline['candidate']}**",
        "",
        f"Candidate: **{candidate['candidate']}**",
        "",
        f"Improvements: {', '.join(improvements) if improvements else 'none'}",
        "",
        f"Regressions: {', '.join(regressions) if regressions else 'none'}",
        "",
        "| Check | Before | After |",
        "|---|---|---|",
    ]
    lines.extend(f"| {item['id']} | {item['before']} | {item['after']} |" for item in transitions)
    lines.append("")
    (output / "comparison.md").write_text("\n".join(lines))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate = subparsers.add_parser("validate-scenarios", help="Validate a scenario set")
    validate.add_argument("scenarios", type=Path)

    init = subparsers.add_parser("init", help="Initialize one fresh-agent run directory")
    init.add_argument("--scenarios", type=Path, required=True)
    init.add_argument("--scenario", required=True)
    init.add_argument("--candidate", required=True)
    init.add_argument("--output", type=Path, required=True)

    finalize = subparsers.add_parser("finalize", help="Validate and summarize a completed run")
    finalize.add_argument("run_dir", type=Path)

    compare = subparsers.add_parser("compare", help="Compare two finalized runs")
    compare.add_argument("baseline", type=Path)
    compare.add_argument("candidate", type=Path)
    compare.add_argument("--output", type=Path, required=True)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        if args.command == "validate-scenarios":
            data = validate_scenario_set(load_json(args.scenarios))
            print(f"Valid: {len(data['scenarios'])} scenarios")
        elif args.command == "init":
            init_run(args.scenarios, args.scenario, args.candidate, args.output)
            print(args.output)
        elif args.command == "finalize":
            finalize_run(args.run_dir)
            print(args.run_dir / "summary.md")
        elif args.command == "compare":
            compare_runs(args.baseline, args.candidate, args.output)
            print(args.output / "comparison.md")
    except EvalError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

