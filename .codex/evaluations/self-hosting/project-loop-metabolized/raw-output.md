## Raw self-hosting analysis

### Orientation and preservation envelope

The current repository is already in the middle of the requested reorganization, not at a clean starting point. The working tree contains uncommitted changes that:

- delete six generic project-loop skills;
- add `skills/create-stack/references/adaptive-stack-loop.md`;
- revise `create-stack` to absorb those skills’ transition logic;
- update the work frontier and historical self-hosting probe; and
- initialize, but not complete, a `project-loop-metabolized` evaluation run.

I treated those changes as the candidate under evaluation and did not modify them.

The preservation envelope is explicit in `.codex/work-frontier.md`:

- an agent-facing interface from incomplete human goals;
- stack-level coherence rather than isolated valid skills;
- responsiveness to user and runtime evidence;
- self-hosting;
- one truthful authority per behavior;
- domain adaptation rather than mechanical reproduction of generic project skills;
- separation of deterministic mechanics, agent judgment, and consequential human authority;
- calibrated cross-harness claims.

That envelope matches the user request closely and is more precise than the README alone.

### Derived operating model

The repository now describes one primary control loop:

```text
Human outcome authority
          |
          v
     create-stack
      /    |     \
     /     |      \
writing-  stack-   audit-release-
skills    level    readiness
          eval
     \
      wizard, only for durable human-operated procedures

Target repository = implementation authority
Work frontier = supplemental decision state only
Scripts = deterministic mechanics only
External destination process = publication authority
```

The concrete model is:

1. `stack-studio-init` ensures the Stack Studio skill set is visible.
2. `create-stack` owns continued end-to-end progress:
   - outcome clarification;
   - preservation discovery;
   - topology design;
   - work-unit selection;
   - adaptive transitions;
   - assembled-stack evaluation;
   - release-readiness transition.
3. The target repository remains the authoritative implementation record.
4. `.codex/work-frontier.md` persists only decision state not authoritative elsewhere.
5. `writing-skills` owns individual-skill authoring and skill-level evaluation.
6. `audit-release-readiness` owns deterministic structural checks and the release-readiness handoff.
7. `wizard` is invoked only when the produced stack needs a durable, human-operated procedure.
8. Actual publication belongs to a separately authorized destination-specific process.

Evidence: `skills/create-stack/SKILL.md`, `skills/create-stack/references/adaptive-stack-loop.md`, `skills/create-stack/references/work-frontier-template.md`, `skills/audit-release-readiness/SKILL.md`, and `.codex/work-frontier.md`.

### Authority and transition assessment

The competing progress authority visible in the historical baseline has been removed from the candidate topology.

The historical `.codex/current-agent-journey.md` records the former ambiguity:

- `create-stack` owned composition and iteration;
- `iterate-toward-outcomes` separately owned continued progress and evidence assimilation;
- their handoff was implied rather than specified;
- stack-level behavioral evaluation had no explicit owner.

The current candidate corrects that in two stages:

- The already-committed `create-stack` makes itself the explicit end-to-end controller and explicitly owns stack-level evaluation.
- The uncommitted candidate goes further by removing the six independently discoverable generic transition skills and metabolizing their decision gates into `adaptive-stack-loop.md`.

The current transitions are explicit:

- Individual skill creation or material revision → `writing-skills`.
- Long-running or uncertain stack design → `iterative-stack-patterns.md`.
- Prediction errors, human ambiguity, learned invariants, reorientation, frontier compaction, or evaluation-regime change → the relevant section of `adaptive-stack-loop.md`.
- Durable human-only operational procedure → `wizard`.
- Substantial stack comparison → `stack-evaluation.md` plus `stack_eval.py`.
- Meaningful structural change or release preparation → `audit-release-readiness`.
- External publication → an authorized destination-specific process outside Stack Studio.

This is a coherent ownership model. The six deleted peer skills were not independent capabilities in practice; their only active orchestration edge came from `create-stack`, and together they recreated a second abstract project-control subsystem. Consolidating them into a conditional reference reduces trigger surfaces and prevents an agent from reconstructing a single workflow across multiple nominal authorities.

One small residual routing weakness remains in `stack-studio-init`: it uses visibility of `create-stack` as the proxy for availability of the entire suite. That is enough to enter the primary workflow, but it does not actually verify that every support skill is discoverable.

### Project-skills lineage

The project-skills lineage creates no synchronization obligation in the current design.

The strongest repository evidence is explicit: `skills/create-stack/references/iterative-stack-patterns.md` says that `adaptive-stack-loop.md` is the source of the methodology inside Stack Studio and that there is “no synchronization obligation with a separate generic project-skills package.”

That claim is architecturally consistent with the rest of the candidate:

- Stack Studio preserves useful concepts—outcome orientation, invariants, prediction errors, bounded human evidence, frozen evaluation epochs, and frontier compaction.
- It treats them as conceptual roles rather than a required one-skill-per-concept decomposition.
- It instructs produced stacks to express transitions in target-domain language and create separate trigger surfaces only when a meaningful operational boundary justifies them.
- The local implementation is therefore a forked/metabolized body of evidence whose future evolution should be governed by Stack Studio’s own outcome and evaluations, not by file parity with a sibling repository.

The appropriate lineage obligation is provenance and deliberate learning: inspect upstream ideas when useful and port evidence-backed improvements intentionally. It is not synchronization, compatibility, or structural mirroring.

### Stack-level evaluation preservation

Stack-level evaluation is now explicitly preserved and separately owned from individual-skill evaluation.

`skills/create-stack/SKILL.md` states that:

- `create-stack` owns assembled-stack evaluation;
- `writing-skills` can evaluate one skill but cannot prove stack coherence;
- `audit-release-readiness` can validate repository structure but cannot prove behavior;
- realistic fresh-agent prompts must test routing, handoffs, representations, deterministic outputs, bounded human input, and final outcomes;
- raw transcripts must remain separate from assessment;
- candidate comparisons must hold the criterion fixed.

`skills/create-stack/references/stack-evaluation.md` defines a concrete evidence contract:

- scenarios in JSON;
- isolated fresh-agent execution;
- unedited `raw-output.md`;
- evidence-bearing `assessment.json`;
- `pass`, `fail`, and `not_exercised` semantics;
- deterministic finalization and same-scenario comparison.

The bundled `.codex/evaluation-scenarios.json` includes greenfield, existing-stack, and self-hosting journeys. The self-hosting scenario directly tests authority collapse, project lineage, stack evaluation ownership, deterministic tool preservation, and inference burden.

The committed comparison evidence is meaningful:

- pre-collapse: 3 pass, 3 fail, 2 not exercised;
- authority-collapse: 7 pass, 0 fail, 1 not exercised;
- improvements were recorded for lineage treatment, single progress authority, stack-level evaluation ownership, and reduced inference burden;
- no regression was recorded.

However, the latest `project-loop-metabolized` run is incomplete: `raw-output.md` is empty, all assessment fields remain `unassessed`, and `stack_eval.py finalize` correctly rejects it. Thus the latest consolidation is not yet behaviorally verified.

### Deterministic tooling preservation

The repository retains three distinct deterministic tool families:

- `skills/create-stack/scripts/stack_eval.py`: stack-evaluation workspace initialization, validation, summary generation, and comparison.
- `skills/audit-release-readiness/scripts/audit_stack.py`: deterministic structure and packaging audit.
- `skills/writing-skills/scripts/*`: individual-skill validation, evaluation, report generation, review, packaging, and adapter-driven trigger/description loops.

The authority boundaries are appropriate: scripts execute repeatable mechanics, while `create-stack` decides what evidence matters and whether the outcome is satisfied.

I ran the two repository test files independently with bytecode writing disabled:

- `skills/create-stack/scripts/test_stack_eval.py`: 4 tests passed.
- `skills/audit-release-readiness/scripts/test_audit_stack.py`: 4 tests passed.

The stack-level and audit implementations therefore remain internally tested after the topology change.

The repository itself does not currently pass its strict deterministic audit. The audit reports one error:

```text
[skills/stack-studio-init/SKILL.md] broken relative link: scripts/skill_shim.bat
```

Only `skill_shim.sh` exists and is tracked. Consequently, both Claude and OpenAI are currently reported as `structure-incomplete`, despite their manifests being present. This is a real release-readiness blocker and evidence that preserving the auditor was useful: the candidate cannot honestly be called release-ready yet.

The repository claims deterministic packaging contracts only for Claude Code and OpenAI. Cursor, Antigravity, and Copilot correctly remain unclaimed. Discovery and behavior are not inferred from manifest presence. Evidence: `README.md`, `audit-release-readiness/SKILL.md`, `references/platforms.md`, and the auditor’s JSON output.

### Current state classification

At this checkpoint:

- The operating model is substantially coherent.
- The competing project-loop authority has been removed in the candidate.
- Stack-level evaluation ownership and tooling are preserved.
- Deterministic tests pass.
- The latest candidate is not yet behaviorally verified.
- The repository is not currently structurally release-ready because of the broken Windows shim reference.
- Nothing in the repository proves an external publication transaction.

Therefore the truthful state is: promising self-hosting candidate with tested deterministic tools, but neither fully behaviorally verified nor release-ready.

### Next useful work unit

The next coherent work unit should be verification and closure of the current candidate, not another architectural redesign:

1. Use this fresh-agent report as the raw evidence for the initialized `project-loop-metabolized` self-hosting run.
2. Assess every fixed self-hosting check with evidence and finalize the run.
3. Compare it against `authority-collapse` under the unchanged scenario.
4. Resolve the broken `skill_shim.bat` contract by either restoring a working Windows shim or removing the unsupported Windows-path instruction; choose based on the intended platform contract.
5. Rerun both deterministic test files and the strict repository audit.
6. If the comparison shows no regression and the strict audit passes, compact the frontier by removing the resolved project-loop item from active decision state and stop architectural work.

The stopping condition should be:

- current self-hosting candidate finalized under the fixed evaluation regime;
- no material regression against the authority-collapse candidate;
- strict audit passing;
- Claude/OpenAI claims limited to the evidence level actually demonstrated;
- no unresolved prediction error capable of changing the topology;
- publication left explicitly pending unless a destination-specific transaction is separately authorized.

At that point, further reorganization would be churn unless a realistic greenfield or existing-stack journey exposes a new failure.
