# Adaptive Stack Loop

Read this reference when building a stack through uncertain, multi-step work or
when deciding whether the produced stack needs its own adaptive control
structure. These are transitions within `create-stack`, not standalone project
workflows or a required skill catalog for the produced stack.

## Reorient without restarting

At a natural milestone, before a substantial next slice, or when recent work is
driving direction more than the outcome:

1. Re-read the outcome, current goal invariants, unresolved prediction errors,
   active evaluation regime, and repository reality.
2. Separate artifact failure from evaluator failure and ordinary implementation
   work from a genuine change in direction.
3. Identify what is established, weakly evidenced, unmet, or newly important.
4. Consider a small set of next moves without assuming the current plan must
   continue.
5. Choose one coherent work unit for outcome leverage, learning value,
   reversibility, and feasible verification.

Preserve sound work that still serves the outcome. Reorientation breaks
unjustified momentum; it does not reward churn or require a redesign.

## Metabolize disagreement with reality

Treat a consequential mismatch between expectation and observation as a
prediction error, including repeated rediscovery, hidden coordination,
unexpectedly broad change impact, or disproportionate verification cost.

Record only:

```text
Expected: the falsifiable expectation
Observed: the result and direct evidence
Uncertain: the smallest assumption now in doubt
Evidence: the reproducible observation
```

Correct ordinary errors without persistent residue. Keep the item open only if
the unresolved discrepancy can change future decisions. When competing
explanations matter, run the cheapest safe discriminating probe. Once
understood, put implementation knowledge into code, tests, tooling, or owned
documentation and remove the frontier item.

If trusted reality contradicts an evaluator rather than the artifact, preserve
the raw observation and use the evaluation-transition gate below.

## Learn properties of success

Admit a goal invariant only when concrete evidence indicates that losing the
property would materially degrade the outcome, the statement can guide more
than one immediate decision, and it describes an observable property rather
than a chosen mechanism.

- Good: `Routine policy changes remain safely implementable without
  reconstructing behavior across multiple systems.`
- Bad: `Keep the code maintainable.`
- Good: `Perceived immediacy is part of the intended editing experience.`
- Bad: `Use incremental rendering.`

Treat invariants as revisable learned beliefs. Merge duplicates and revise or
remove them when later evidence contradicts them. After a change, check whether
the active evaluation can observe the property; do not silently change the
criterion during an unfinished comparison.

## Resolve consequential ambiguity with human evidence

Ask for human observation only when all of these hold:

1. One precise unresolved question has at least two plausible answers that
   would cause materially different next decisions.
2. Existing user decisions, repository inspection, automated checks, and
   cheaper safe probes cannot answer it.
3. Human experience or judgment is the necessary observation surface.
4. A discriminating observation can be named in advance.

State whether the observation explores a direction, judges a candidate under
the active regime, or serves as independent anchor evidence. Design the lowest-
cost faithful evaluation, bring it to a ready-to-use state when authorized, and
ask one bounded question without signaling a preferred answer.

Retain the smallest decision-relevant lesson and raw observation. Remove
disposable prototypes, variants, seeded data, and review scaffolding created for
the probe; never delete pre-existing or user-owned artifacts. Then implement and
verify the chosen direction as finished-grade work. Human review resolves an
ambiguity; it does not complete the corresponding product work.

## Change an evaluation regime only at a boundary

Keep the outcome, goal invariants, evaluation regime, evaluator-independent
anchors, raw evidence, and regime-dependent conclusions distinct. Hold the
active regime fixed throughout a candidate comparison.

Consider a challenger only at a declared checkpoint when evidence indicates
the current regime is saturated, gameable, miscalibrated, blind to a newly
admitted invariant, unable to distinguish plausible improvements, or
disproportionately expensive.

Before promotion:

1. Finish the current observation and pause artifact edits.
2. State the current regime and the evidenced failure.
3. Identify held-out anchors independent of both incumbent and challenger.
4. Predeclare the blind spot, non-regression constraints, acceptable tradeoffs,
   and promotion evidence.
5. Compare both regimes against the same anchors, including repeated evidence
   when results are stochastic.

Retain the incumbent when evidence is tied or materially uncertain. Never
promote a challenger because it scores the current artifact more favorably.

On promotion, advance the evaluation epoch, freeze the new regime, invalidate
old scores and rankings whose meaning depended on the displaced regime, retain
raw artifacts and evaluator-independent evidence, and recompute only summaries
valid under the new regime.

## Compact persistent decision state

Optimize the work frontier for the next decision, not historical completeness.
For every item ask: `Can this still change a future decision?`

Remove resolved discrepancies, implementation facts authoritative elsewhere,
attempt history, stale plans, duplicate invariants, superseded beliefs, generic
advice, and conclusions tied to a displaced evaluation regime. Retain the
outcome, decision-relevant learned invariants, material unresolved prediction
errors, the active evaluation regime and anchors when needed, explicit
uncertainty, and pointers to durable raw evidence.

Preserve the frontier schema in
[work-frontier-template.md](work-frontier-template.md). After compaction, a fresh
agent should be able to choose a useful next move without reconstructing the
prior agent's narrative.

## Adapt the pattern into a produced stack

The same structures may help the stack being produced, but do not copy this
reference or recreate six generic skills mechanically. Use the target domain's
language and operational seams. Make a transition independently triggerable
only when doing so protects a meaningful boundary, prevents an evidenced
failure mode, or avoids loading substantial conditional instructions. Otherwise
keep it inside the target stack's primary workflow or a conditional reference.
