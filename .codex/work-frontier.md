# Work Frontier

## Outcome

An agent can be pointed at Stack Studio with an incomplete human goal for a
"-stack" and use the repository to collaboratively produce or improve a
coherent, tested, publishable skill stack.

Stack Studio keeps the work oriented toward the human's evolving intent,
helps the agent learn from implementation and evaluation evidence, and carries
the stack from initial capability design through reliable use across supported
agent harnesses. The same system can be used to understand, evaluate, and
improve Stack Studio itself.

## Goal invariants

- **The effective interface is agent-facing.** A human should be able to point
  an agent at the repository and state the desired outcome without first
  learning Stack Studio's internal skill catalog or prescribing its workflow.
  **Evidence:** The intended usage described by the user is to ask an LLM agent
  to use this repository to build a stack for a stated purpose.

- **Stack-level coherence is the product.** Success is not merely a collection
  of individually valid skill files; the resulting skills, references, tools,
  routing conditions, and human interactions must work together to steer an
  agent toward the stack's intended outcome.
  **Evidence:** The user identified reliable agent orientation and progress
  toward a coherent, tested, publishable outcome as the central concern.

- **The workflow remains responsive to human goals and observed reality.** The
  agent must repeatedly reorient, incorporate consequential user evidence, and
  revise its working model when results contradict expectations rather than
  treating an initial plan as the target.
  **Evidence:** Stack building was observed to be an iterative project whose
  goals and design become clearer through back-and-forth with the user.

- **Stack Studio is self-hosting.** Its documented operating model and tools
  must be capable of guiding substantive improvements to Stack Studio itself,
  without depending on an undocumented external development process.
  **Evidence:** The recursive ability of a well-constructed Stack Studio to
  produce or improve itself was explicitly identified as important.

- **There is one truthful authority for each part of the workflow.** An agent
  should not have to reconcile duplicated or competing instructions to learn
  who owns stack-level progress, skill-level authoring, evaluation, mechanical
  validation, publication, or consequential human decisions.
  **Evidence:** Duplicate authority between the original `project-skills`
  material and its Stack Studio copies was identified as the primary structural
  problem.

- **Reusable iteration ideas are adapted to the stack being built.** Stack
  Studio may teach and use patterns such as outcome orientation, goal
  invariants, prediction-error handling, bounded human evidence, and evaluation
  discipline, but it must not mechanically reproduce a generic project stack
  when domain-specific structures would steer the target agent more clearly.
  **Evidence:** The generic `project-skills` decomposition was judged useful as
  a pattern but too abstract to preserve automatically as a standalone stack.

- **Deterministic mechanics and accountable judgment remain distinct.** Stable,
  repeatable operations should be executable and verifiable, while design
  judgment remains with the agent and consequential ambiguity about desired
  outcomes remains with the human.
  **Evidence:** This separation is already an explicit Stack Studio design
  principle and supports reliable stack production without displacing human
  authority.

- **Produced stacks make calibrated portability claims.** Stack Studio must
  separate shared skill structure, harness-specific packaging, observed
  discovery, observed behavior, and completed publication so an agent never
  promotes file presence into a stronger support claim.
  **Evidence:** The release-readiness contract now defines an evidence ladder
  and deterministic adapters separately for Claude Code and OpenAI packaging.

## Evaluation regime

- **Epoch:** `epoch-0-current-orientation-baseline`
- **Active criterion:** Give a fresh agent only Stack Studio, a target repository,
  and one of the three prompts in `evaluation-scenarios.json`. Observe whether the
  agent derives and follows a complete stack-building loop without relying on
  prior knowledge of Stack Studio. Judge the journey against the predeclared
  scenario checks; do not change those checks while comparing a candidate
  reorganization with the current repository.
- **Anchors:** The outcome and goal invariants above; the user's authority over
  consequential intent; repository evidence; preservation of working authoring,
  validation, and cross-harness packaging capabilities; and the raw transcripts
  produced by fresh-agent runs.
- **Dependent evidence:** Any pass/fail judgment, comparison, or conclusion
  derived from the three scenarios under this epoch. Current self-hosting
  evidence is stored under `.codex/evaluations/self-hosting/`.

## Prediction errors

### Resolved: publication stops at preparation

- **Expected:** `audit-and-publish` would carry a completed stack through the
  publication outcome named by the skill.
- **Observed:** The skill audits and prepares repositories but specifies no
  versioning, tagging, release, registry, marketplace, or publication
  transaction.
- **Resolution:** Renamed the capability to `audit-release-readiness`; its
  authority ends at an evidence-backed handoff. Destination-specific publishing
  remains a separately authorized external transaction.
- **Evidence:** `skills/audit-release-readiness/SKILL.md` and the deterministic
  auditor's support-evidence report.
