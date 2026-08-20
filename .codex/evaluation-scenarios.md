# Stack Studio Evaluation Scenarios

These scenarios define the initial baseline for judging whether Stack Studio
orients an agent through a complete stack-building journey. Run each with a
fresh agent that receives no prior Stack Studio discussion. Preserve the raw
transcript and generated artifacts. Do not edit the checks while comparing the
current repository with a candidate reorganization.

## Shared protocol

For every scenario:

1. Give the agent the Stack Studio repository, the named target repository, and
   only the scenario prompt.
2. Allow ordinary repository inspection and user questions that the workflow
   itself elicits.
3. Record the agent's orientation sequence, invoked skills, user-decision
   requests, repository changes, verification, and stopping condition.
4. Distinguish instructions explicitly supplied by Stack Studio from workflow
   connections inferred by the agent.
5. Evaluate the journey and artifact. A persuasive plan without useful action
   does not pass, and structurally valid files without stack-level coherence do
   not pass.

The user or test operator may answer bounded questions, but must not teach the
agent Stack Studio's intended internal architecture.

## Scenario 1: Greenfield domain stack

### Target

`/Users/chad/Repos/etl-stack`, beginning from its README and work frontier.

### Prompt

> Use Stack Studio to help me turn this ETL stack concept into a coherent stack
> for reproducible, auditable AI-assisted data transformation. Work with me
> iteratively and carry it through implementation and verification.

### Checks

- The agent identifies and preserves the target's stated outcome and existing
  invariants before choosing a skill decomposition.
- It treats the target repository—not Stack Studio—as the implementation home.
- It resolves consequential ETL scope questions with the user without making
  the user prescribe Stack Studio's workflow.
- It designs skill boundaries, routing conditions, shared representations, and
  deterministic tooling as one system rather than generating disconnected
  skills.
- It obtains behavioral evidence for the assembled stack, including at least
  one end-to-end ETL journey, rather than relying only on frontmatter checks.
- It verifies reproducibility, auditability, source immutability, and useful
  reconciliation reporting against the target's recorded invariants.
- It reaches a clear release-ready or externally blocked state and identifies
  any publication action that remains outside Stack Studio.

## Scenario 2: Evolution of an existing stack

### Target

`/Users/chad/Repos/vm-stack`, preserving its current registry contract and
working VM-management capabilities.

### Prompt

> Use Stack Studio to evaluate and improve vm-stack as a coherent agent skill
> stack. Preserve its working VM lifecycle behavior while making the complete
> experience easier for an agent and human to use reliably across its supported
> platforms. Work iteratively and verify the result.

### Checks

- The agent inspects existing skills, scripts, schemas, manifests, and repository
  guidance before proposing a new topology.
- It identifies preservation requirements and distinguishes them from accepted
  revisions instead of treating a rewrite as greenfield work.
- It evaluates cross-skill routing and end-to-end VM journeys, not merely each
  `SKILL.md` in isolation.
- It preserves the registry as the declared configuration authority and routes
  VM operations through the management script unless evidence supports an
  explicit architectural change.
- It observes relevant executable or runtime evidence proportionate to the
  environment and does not run interactive wizards in a non-interactive shell.
- It uses human judgment for consequential experience or compatibility choices,
  not for correctness that repository inspection or scripts can establish.
- The resulting stack remains structurally valid and practically installable
  across its claimed harnesses.

## Scenario 3: Self-hosting reorganization

### Target

`/Users/chad/Repos/stack-studio`.

### Prompt

> Use Stack Studio to define, refine, and reorganize Stack Studio so that an
> agent can reliably use it to produce coherent, tested, publishable skill
> stacks from incomplete human goals. Preserve its useful authoring, evaluation,
> auditing, and cross-harness capabilities while removing duplicated or
> competing workflow authority. Work with me iteratively and verify the result.

### Checks

- The agent recognizes the recursive task and uses Stack Studio's documented
  operating model rather than inventing an unrelated project process.
- It establishes the human outcome and preservation envelope before committing
  to a replacement organization.
- It traces current authorities and coordination edges, including the split
  between `create-stack` and the inherited generic iteration loop.
- It treats the `project-skills` lineage as reusable evidence rather than a
  synchronization or compatibility obligation.
- It produces one explicit authority for continued stack-level progress and
  explicit transitions to supporting capabilities.
- It establishes an owner and evidence path for stack-level behavioral
  coherence.
- It preserves working deterministic tools unless evidence justifies replacing
  them, and verifies their relevant contracts after structural changes.
- A subsequent fresh agent can derive the intended end-to-end workflow with
  less unsupported inference than the baseline in `current-agent-journey.md`.

## Baseline interpretation

The current repository has passed only an orientation probe for Scenario 1. It
showed that a diligent agent can discover the relevant ingredients, but must
infer critical transitions and authorities. No scenario has yet passed its full
artifact and outcome checks.

