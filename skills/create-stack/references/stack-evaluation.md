# Stack Evaluation

Use this protocol when comparing substantial stack revisions, validating
cross-skill behavior, or evaluating a stack whose success depends on more than
one isolated skill.

`create-stack` remains the authority for what evidence matters and whether the
stack satisfies its outcome. The bundled script owns only deterministic
workspace creation, result validation, summarization, and comparison.

## Scenario contract

Store scenarios in JSON:

```json
{
  "schema_version": 1,
  "scenarios": [
    {
      "id": "greenfield-example",
      "name": "Greenfield example",
      "target": "./target-stack",
      "prompt": "Use this stack to...",
      "checks": [
        {
          "id": "preserves-inputs",
          "text": "The agent identifies and preserves immutable inputs."
        }
      ]
    }
  ]
}
```

Checks should describe observable behavior or preserved outcomes. Avoid checks
that merely require particular wording, headings, or internal reasoning.

## Run one scenario

Initialize a run directory:

```bash
python skills/create-stack/scripts/stack_eval.py init \
  --scenarios .codex/evaluation-scenarios.json \
  --scenario self-hosting \
  --candidate candidate-name \
  --output .codex/evaluations/self-hosting/candidate-name
```

Give a fresh agent only `prompt.md`, access to the named target and Stack Studio,
and the ordinary harness context a real user would have. Do not give it the
expected architecture, suspected failures, prior conclusions, or another run's
assessment. Keep generated target artifacts isolated when the evaluation should
not change the working repository.

Save the agent's unedited final report or transcript in `raw-output.md`. Then
fill `assessment.json`:

- `pass`: the evidence directly supports the check;
- `fail`: observed behavior contradicts or omits the check when it should have
  been exercised;
- `not_exercised`: the run did not reach the behavior, so no claim is possible.

Every result needs a concise evidence pointer. Preserve uncertainty; do not turn
`not_exercised` into `pass` because the instructions appear capable of producing
the behavior.

Validate and render the assessment:

```bash
python skills/create-stack/scripts/stack_eval.py finalize \
  .codex/evaluations/self-hosting/candidate-name
```

## Compare candidates

Run candidates against the same scenario and unchanged check set, then compare:

```bash
python skills/create-stack/scripts/stack_eval.py compare \
  .codex/evaluations/self-hosting/baseline \
  .codex/evaluations/self-hosting/candidate-name \
  --output .codex/evaluations/self-hosting/comparison
```

The comparison reports status transitions, improvements, and regressions. It
does not choose a winner: `create-stack` must interpret the result against hard
anchors, qualitative evidence, cost, and unresolved uncertainty.
