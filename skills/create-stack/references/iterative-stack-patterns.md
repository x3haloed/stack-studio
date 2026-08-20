# Iterative Stack Patterns

Read this reference when the stack being produced must guide an agent through
long-running, uncertain, or evidence-driven work. The purpose is to design a
domain-appropriate control structure, not to install a generic project loop.

## Determine whether the pattern belongs

Add explicit iteration support only when the target agent must repeatedly choose
work, observe results, and revise direction before the outcome can be fully
specified. A short deterministic workflow, narrow reference skill, or single
operation normally does not need persistent frontier state or transition
handlers.

Look for these pressures:

- The user's understanding of success can change after seeing real behavior.
- Implementation or integration evidence routinely changes the next useful
  action.
- Work spans enough time or sessions that decision state would otherwise be
  rediscovered.
- Several plausible architectures must remain open while evidence accumulates.
- The way progress is evaluated may itself become saturated or misleading.

## Preserve the useful structures

An adaptive stack may need some of these structures:

- **Outcome orientation:** Periodically derive direction from the requested
  result rather than recent implementation momentum.
- **Goal invariants:** Retain evidence-backed properties discovered to be part of
  success, stated as observable outcomes rather than chosen mechanisms.
- **Prediction errors:** Preserve unresolved discrepancies between expectation
  and reality when they could change future decisions.
- **Bounded human evidence:** Ask a person to discriminate consequential choices
  only when repository inspection, automated evidence, or cheaper probes cannot.
- **Frozen evaluation epochs:** Hold the criterion fixed during a candidate
  comparison and change it only at a declared boundary with independent anchors.
- **Frontier compaction:** Remove resolved, duplicated, stale, or implementation-
  authoritative material so persisted context remains useful for the next
  decision.

These are conceptual roles. They do not imply one skill per concept.

## Choose domain-shaped boundaries

Express transitions in the language and operational seams of the target stack.
Separate a transition into its own skill only when independent triggering
materially improves behavior—for example, when it guards a high-risk boundary,
prevents a common failure mode, or loads substantial instructions needed only in
that regime.

Otherwise keep the behavior inside the primary domain loop or a conditional
reference. Avoid forcing the consuming agent to reconstruct one workflow from a
catalog of abstract skills.

Examples of domain adaptation:

- An ETL stack might record transformation invariants, route reconciliation
  mismatches into an evidence workflow, and request human judgment for ambiguous
  source mappings.
- A deployment stack might preserve rollout invariants, treat environment drift
  as a prediction error, and isolate approval-bearing cutover steps.
- A design stack might use bounded human comparison for experiential choices
  while keeping accessibility and build checks as independent anchors.

## Verify the loop rather than its vocabulary

Test the produced stack with realistic multi-step journeys. Check that the agent
stays oriented, changes direction when evidence warrants it, retains only useful
decision state, and reaches a verified outcome or a genuine blocker. Do not
score the design by whether it uses terms such as “frontier,” “invariant,” or
“prediction error.” The observable behavior is the pattern.

