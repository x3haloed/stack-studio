# Current Agent Journey

## Probe

A fresh agent with no prior design discussion received only this request and
the Stack Studio repository:

> Can you use this repo to help me build an ETL stack?

The agent was instructed to inspect naturally, make no changes, avoid sibling
repositories, and report its orientation sequence before suggesting any
redesign. The findings below preserve the observed baseline for comparison with
future revisions.

## Observed orientation sequence

1. Read `AGENTS.md`, `README.md`, `plugin.json`, and the visible skill inventory.
2. Read `stack-studio-init` because its metadata requires one-time use before
   other Stack Studio skills.
3. Detected macOS and followed the initializer's shim fallback because the
   repository skills were not installed in the active harness catalog.
4. Used the shim's metadata inventory to select `create-stack`,
   `iterate-toward-outcomes`, `writing-skills`, and `audit-and-publish`.
5. Read `create-stack` and inferred that it owned target selection, intent,
   stack composition, iteration, and eventual audit.
6. Read `iterate-toward-outcomes` and inferred that it owned continued progress,
   evidence assimilation, and conditional transitions.
7. Read `writing-skills` and inferred that it owned authoring and evaluating
   each individual skill.
8. Read `audit-and-publish` and inferred that it owned structural validation and
   publication readiness.
9. Consulted human-evidence, work-frontier, layout, and platform references to
   understand conditional user participation and packaging.

The agent did not inspect an ETL target or begin implementation because no
target repository had been identified.

## Inferred authorities

- **Human:** Desired outcome and consequential judgments not answerable from
  repository or automated evidence.
- **`create-stack`:** Stack domain, target location, capability composition,
  desired experience, and review cadence.
- **`iterate-toward-outcomes`:** Persistent work selection, observation,
  reorientation, and exceptional transitions.
- **Target repository:** Authoritative implementation state.
- **Work frontier:** Optional supplemental decision state.
- **`writing-skills`:** Individual skill authoring and behavioral evaluation.
- **`audit-and-publish`:** Structural and packaging readiness.

No instruction explicitly assigns authority for stack-level behavioral
coherence or for an actual publication transaction.

## Coordination edges

```text
stack-studio-init
        |
        v
   create-stack
        :----> iterate-toward-outcomes   implied; no explicit handoff
        :----> writing-skills            inferred from metadata
        :----> wizard                    conditional; no explicit edge
        |
        v
 audit-and-publish
        :----> publication destination   unspecified
```

`iterate-toward-outcomes` explicitly routes to its generic transition handlers.
Those edges are internally documented, unlike its relationship to
`create-stack`.

## Representations and boundaries

The workflow is represented across skill metadata and bodies, optional frontier
state, target-repository artifacts, manifests, agent instructions, evaluation
artifacts, and audit reports.

Material boundaries are:

- Stack Studio versus the target stack repository.
- Stack-level composition versus individual-skill quality.
- Judgment-bearing instructions versus deterministic scripts.
- Automated evidence versus accountable human judgment.
- Local publication preparation versus external release systems.

## Material gaps

- `create-stack` and `iterate-toward-outcomes` divide stack-level control without
  an explicit transition or ownership rule.
- `create-stack` does not explicitly compose `writing-skills` or `wizard`.
- Individual-skill evaluation and repository auditing do not establish
  stack-level routing coherence or end-to-end outcome coverage.
- `audit-and-publish` prepares a repository but does not publish it.
- The auditor's compatibility scores are presence heuristics rather than
  semantic compatibility checks.
- Some documented audit requirements are manual or not enforced by the script.
- Platform guidance is described as exact without recorded provenance or
  version boundaries.

## Baseline conclusion

The repository exposes most of the relevant capabilities, and a diligent agent
can infer a plausible workflow. The complete stack-building loop is nevertheless
an emergent interpretation rather than an explicitly owned and connected path.

