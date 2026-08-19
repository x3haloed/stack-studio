---
name: create-stack
description: Use to create or modify a "*-stack" bundle of related skill files like the popular "gstack".
---

# Stack Studio

**Important:** read [skill-studio-init](../stack-studio-init/SKILL.md) if you haven't yet to ensure you've got all the context you need about stack-studio skills. This is a one-time operation.

Stack Studio is a suite of skills to help you design... skill suites. Popular examples include:
- [gstack](https://github.com/garrytan/gstack)
- [Matt Pocock's Skills](https://github.com/mattpocock/skills)
- [pstack](https://github.com/cursor/plugins/tree/main/pstack)

## Goal

Deliver a folder or repo of related skills that can be easily installed into a coding or agentic harness to support agents and humans in specific goals.

## Directions

1. Clarify the target repo/dir. Where is the work product located? Is this a brand new endeavor, or is there existing work somewhere?
2. Work iteratively. Don't expect to achieve the final result in a single turn or pass.
3. Continually clarify and reorient on the user's goal. What do they want the stack to do? What should the experience be like for the user?
4. Don't forget to perform review passes after long stretches of work to ensure the product repo is clean and free of errors.

## Tips for Success

1. Unless excessively frictionful in the environment or directed otherwise by the user, aim for broad compatibility with the most popular coding and agentic harnesses' "plugin" systems. This allows the stack to be easily installed and removed as a group of related skills. Ref: https://developers.openai.com/plugins/build/plugins
2. Routing vs. context tension: breaking workflows into individual skills can help steer the consuming agent into regimes at appropriate times. This helps guard against smoothing risks -- when a complex workflow is reduced to "yeah, I get the idea" by an agent. On the other hand, when installed into a harness, all skill frontmatter is loaded into context, which is its own cost. Carefully balance the risks and benefits.
3. Determinism vs. probabilism: favor pushing all deterministic logic into executable scripts while keeping judgement and selection in the hands of the user and the agent. Scripting determinstic flows will improve reliability and predictability while lowering token costs for the user and context window bloat for the agent. The following table summarizes the tradeoffs: 

  | Kind of flow | Who decides? | Script? |
  |---|---|---|
  | Deterministic / mechanical | System | **Yes** |
  | Requires judgment | Agent or human user | **No** |
  | Requires accountable human authority | Human | **No** |
  