---
name: feature-builder
description: Build a small feature using a research → implement → review subagent workflow
agent: Feature Builder
tools: ['agent', 'read', 'search', 'edit']
---

Feature request:

${input:feature_request:Describe the feature to implement}

Required workflow:

1. Use Repo Researcher as a subagent to inspect the repository and identify the relevant files, patterns, and constraints.
2. Use Implementer as a subagent to make the requested change.
3. Use Reviewer as a subagent to review correctness, type hints, maintainability, and tests.
4. Return one concise final summary with risks and follow-up suggestions.

Keep each step distinct and explicitly attribute findings to the subagent that produced them.
