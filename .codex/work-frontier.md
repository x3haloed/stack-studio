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

- **Purpose-complete temporary resources are released after durable evidence is
  preserved.** Produced stacks should make the purpose, release condition, and
  retention disposition of costly temporary resources explicit rather than
  retaining them by inertia.
  **Evidence:** The vm-stack Windows field trial left two completed validation
  clones consuming substantial disk until the user identified that their
  purpose had been satisfied. Purpose-bound release reclaimed the disposable
  disks while retaining the single reusable base.

- **Produced stacks make calibrated portability claims.** Stack Studio must
  separate shared skill structure, harness-specific packaging, observed
  discovery, observed behavior, and completed publication so an agent never
  promotes file presence into a stronger support claim.
  **Evidence:** The release-readiness contract now defines an evidence ladder
  and deterministic adapters separately for Claude Code and OpenAI packaging.

## Evaluation regime

- **Epoch:** `epoch-1-purpose-bound-resource-lifecycle`
- **Active criterion:** Give a fresh agent only Stack Studio, a target repository,
  and one of the three prompts in `evaluation-scenarios.json`. Observe whether the
  agent derives and follows a complete stack-building loop without relying on
  prior knowledge of Stack Studio. Judge the journey against the predeclared
  scenario checks. For the existing-vm-stack scenario, also observe whether the
  agent gives costly temporary resources a disposition and releases disposable
  resources after preserving evidence. Hold this check set fixed for all
  epoch-1 candidate comparisons.
- **Anchors:** The outcome and goal invariants above; the user's authority over
  consequential intent; repository evidence; preservation of working authoring,
  validation, and cross-harness packaging capabilities; and the raw transcripts
  produced by fresh-agent runs.
- **Dependent evidence:** Any pass/fail judgment, comparison, or conclusion
  derived from the three scenarios under this epoch. Epoch-0 self-hosting
  evidence remains historical and is not rescored under the new check. Current
  self-hosting evidence is stored under `.codex/evaluations/self-hosting/`.

- **Promotion evidence:** The vm-stack Windows field trial independently showed
  that the prior criterion was blind to purpose-complete resource retention.
  The field evidence is stored under
  `.codex/evaluations/field-trials/vm-stack-windows/`.

## Prediction errors

### Unclassified script probing launched human-facing UI

- **Expected:** A fresh agent would inspect the existing stack and obtain
  proportionate runtime evidence without invoking interactive wizards in a
  noninteractive correctness probe.
- **Observed:** The epoch-1 fresh agent ran a bulk `--help` sweep across shell
  scripts. Wrapper entry points delegated into an interactive sanity checker
  and opened several visible Terminal windows that the user had to close.
- **Uncertain:** Whether controller guidance to classify unfamiliar tools before
  execution is sufficient, or whether produced stacks also need deterministic
  enforcement that conventional inspection flags are side-effect free.
- **Evidence:**
  `.codex/evaluations/existing-vm-stack/purpose-bound-resource-lifecycle/summary.md`
