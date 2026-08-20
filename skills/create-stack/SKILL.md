---
name: create-stack
description: Use when creating, extending, or substantially reorganizing a "*-stack" repository whose skills, tools, references, routing, evaluation, and packaging must work together to accomplish a shared agent-facing outcome.
---

# Create Stack

Read [stack-studio-init](../stack-studio-init/SKILL.md) once before using this
skill so the supporting Stack Studio capabilities are discoverable.

Own continued progress toward the completed stack. Do not stop at a proposed
skill list, a locally successful skill, or a structurally valid repository.
Continue until the assembled stack has behavioral evidence against its outcome,
is ready for its intended distribution path, or a concrete external blocker or
consequential user decision prevents further authorized work.

## Establish the stack outcome

Identify the target repository and inspect it before asking questions already
answered there. Determine whether the work is greenfield, an extension, or a
reorganization with behavior to preserve.

Clarify the smallest set of consequential uncertainties needed to begin:

- What should an agent or human be able to accomplish with this stack?
- What lived experience or operational properties are part of success?
- Which environments, harnesses, integrations, or existing contracts matter?
- What evidence would let the user trust that the complete stack works?
- Which temporary environments, fixtures, branches, accounts, generated assets,
  or other costly resources may be created, and what observation will end their
  useful life?

Do not require the user to understand Stack Studio's skill catalog or prescribe
the development process. Ask for human judgment when it determines the desired
outcome; derive implementation facts from repositories, tools, and direct
evidence.

## Maintain only decision state

Treat the target repository as the authoritative implementation record. For
long-running or underdetermined work, maintain a single project-local work
frontier using [the template](references/work-frontier-template.md). Keep only:

- the outcome;
- evidence-backed goal invariants discovered during the work;
- unresolved prediction errors that could change future decisions; and
- an active evaluation regime only when the way candidates are judged is itself
  expected to change.

Do not turn the frontier into a plan, status report, decision diary, or duplicate
of facts already authoritative in code, tests, issues, or documentation. Keep
transient state in the task context when persistence across sessions is not
useful.

## Design the stack as a system

Start from the journeys the target agent must complete. Design the smallest
skill topology that reliably supports those journeys:

- Give each behavior one truthful authority.
- Split skills when distinct trigger conditions or operating regimes materially
  improve routing and prevent important instructions from being smoothed over.
- Merge guidance when separate skills would merely duplicate policy or force the
  agent to reconstruct one workflow across several authorities.
- Keep shared representations and contracts explicit; do not make skills infer
  how their outputs connect.
- Put deterministic, repeatable mechanics in scripts. Keep judgment in skill
  instructions and consequential outcome authority with the user.
- Use references for conditional domain detail and assets for material copied
  into outputs.
- Account for the metadata and context cost of every skill exposed to the
  consuming harness.
- Give costly temporary resources an explicit purpose, observable release
  condition, and retention disposition. Default produced resources to
  disposable unless a long-lived use or unresolved decision requires them.

When the target stack must guide long-running adaptive work, read
[iterative-stack-patterns.md](references/iterative-stack-patterns.md) and, when
implementing or using the transitions themselves,
[adaptive-stack-loop.md](references/adaptive-stack-loop.md). Adapt the pattern
to the target domain instead of mechanically reproducing generic project skills.

## Run the stack-building loop

Repeat one useful work unit at a time:

1. Reorient from the outcome, current invariants, active evaluation regime when
   present, unresolved prediction errors, and target-repository reality.
2. Choose work that advances the artifact, tests a consequential assumption, or
   cheaply resolves uncertainty blocking useful progress.
3. Hold the evaluation criterion fixed while changing and judging a candidate.
4. Implement the coherent slice, using [writing-skills](../writing-skills/SKILL.md)
   when authoring or materially revising individual skills.
5. Observe the strongest practical evidence: executed scripts, target-harness
   behavior, realistic agent journeys, tests, generated artifacts, or direct
   user experience.
   Before executing an unfamiliar tool, classify it from owned documentation or
   source as read-only, interactive, mutating, or externally consequential.
   Never substitute a bulk `--help`, smoke, or execution sweep across
   unclassified scripts for targeted contract inspection; wrappers and legacy
   entry points may launch UI or perform setup even when passed conventional
   help flags.
6. Evaluate what the skills do together, not only whether each skill works in
   isolation.
7. After preserving required evidence outside temporary resources, release
   those whose purpose is satisfied in the same work loop. Do not retain them
   merely because they might be useful later.
8. Incorporate only decision-relevant learning into the frontier, then choose
   the next work unit.

Plans may coordinate the immediate work, but replace them when evidence changes
the best direction. Completion means satisfying the outcome, not finishing the
initial task list.

## Handle adaptive transitions inside the loop

Read the relevant section of
[adaptive-stack-loop.md](references/adaptive-stack-loop.md) when:

- a consequential observation contradicts the working model;
- only bounded human experience can resolve a decision-changing ambiguity;
- evidence reveals a previously implicit property of success;
- a milestone, accumulated uncertainty, or implementation momentum makes drift
  plausible;
- persistent decision state becomes stale or expensive to reread; or
- the evaluation criterion is evidenced as saturated, gameable,
  miscalibrated, or blind to a relevant success dimension.

These are state transitions owned by `create-stack`, not peer skills or
mandatory phases. Continue the ordinary loop when no transition is warranted.
Use [wizard](../wizard/SKILL.md) only when the produced stack needs a durable,
human-operated procedure for steps the agent cannot perform itself.

## Evaluate assembled behavior

`create-stack` owns stack-level evaluation. `writing-skills` may evaluate an
individual skill, and `audit-release-readiness` may validate repository structure, but
neither result proves that the assembled stack accomplishes its outcome.

Use realistic end-to-end prompts covering the stack's primary journeys and
material boundaries. Give fresh agents only the context a real user and target
harness would provide. Observe:

- whether the intended skills trigger and irrelevant ones stay out;
- whether authority and handoffs remain clear across skills;
- whether shared artifacts and state retain consistent meaning;
- whether deterministic tools produce verifiable results;
- whether the agent requests human input only where judgment is necessary; and
- whether costly temporary resources are retained only while they still serve
  an explicit purpose or unresolved verification need; and
- whether the final result satisfies the stack-level outcome and invariants.

Preserve raw transcripts and artifacts separately from scores or reviewer
conclusions. Compare candidates under the same criterion. When the criterion
itself must change, complete an explicit evaluation-regime transition before
using the new judgment to guide further work.

For substantial comparisons or repeated evaluations, read
[stack-evaluation.md](references/stack-evaluation.md) and use the bundled
`scripts/stack_eval.py` to initialize runs, validate evidence-backed assessments,
and compare candidates under the same scenario. Fresh-agent execution remains a
harness operation; the script must not simulate independence by invoking the
current agent recursively with hidden context.

## Audit and finish honestly

After meaningful structural changes and before release, use
[audit-release-readiness](../audit-release-readiness/SKILL.md) to verify frontmatter,
permissions, references, manifests, installation guidance, and supported-harness
packaging.

Before declaring the work complete, inventory temporary resources created by
the journey. Preserve durable transcripts, hashes, screenshots, or artifacts
outside resources that will be removed. Release disposable resources whose
declared condition is satisfied; retain only resources with a named continuing
purpose, unresolved dependency, or explicit human retention decision.

Distinguish these states:

- **Behaviorally verified:** End-to-end evidence supports the intended journeys.
- **Release-ready:** Behavioral and structural checks pass and required release
  metadata is prepared.
- **Published:** The authorized external release, registry, or marketplace
  transaction actually succeeded and was verified.

Do not claim publication when only local auditing or packaging occurred. Obtain
authorization before external writes, releases, or marketplace submissions that
were not already included in the user's request.
