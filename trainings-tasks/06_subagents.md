## 🎯 Module VI: Subagents — Coordinating Specialized Agents in the IDE

### 📚 Goal: Master the use of GitHub Copilot Subagents to streamline workflows by isolating tasks, delegating specialized work, and integrating results seamlessly within the IDE.

In the previous module, you worked with Custom Agents and autonomous Coding Agent workflows. In this module, you will reuse prepared local agents inside VS Code and learn how Subagents isolate repository research, implementation, and review inside the same Copilot Chat request.

Subagents allow Copilot to delegate focused work into isolated contexts and return only the useful result back to the main chat thread. This helps reduce context overload, improves visibility into multi-step workflows, and makes complex requests easier to structure and inspect.

---

### ⚠️ Version Requirement

This exercise requires:

- **VS Code 1.111 or newer**
- Latest GitHub Copilot Chat extension, **0.39.0 or newer**
- **`chat.customAgentInSubagent.enabled`** enabled

---

## 🧠 Why Subagents Matter

Subagents are useful when one chat session would otherwise become noisy or overloaded.

They let Copilot isolate focused tasks, bring back only the relevant result, and keep the main thread easier to understand.

Typical examples:

- **Research** → inspect the codebase and identify patterns
- **Implementation** → make focused edits
- **Review** → validate correctness, maintainability, type hints, and tests

### ⭐ Key Takeaway

Subagents let Copilot break one complex request into specialized internal runs while preserving one coherent top-level workflow.

This is especially valuable in Copilot because it solves two common problems at once:

- without subagents, you often either write **one very large prompt** that overloads the main context
- or you split the work into **multiple chat messages**, which increases the number of requests

Subagents provide a third option: one top-level request can coordinate multiple focused internal runs, offload context from the main thread, and bring back only the useful results in a more organized way.

This also makes it easier to:

- isolate task-specific work instead of pushing every detail into the main chat thread
- use specialized agents for different responsibilities
- experiment with different worker models
- inspect what each worker contributed back to the final answer

---

## Exercises: Observing and Using Subagents

| Step | Feature | Instructions |
| :--- | :--- | :--- |
| **6.1** | **Enable Subagents** | Open **Copilot Chat**, switch the mode picker to **Agent**, and verify the setting **Chat > Agent in Subagent** (`chat.customAgentInSubagent.enabled`) is enabled. |
| **6.2** | **Review Prepared Agents** | Review the prepared agents in `.github/agents`: `FeatureBuilder`, `RepoResearcher`, `Implementer`, and `Reviewer`. Focus on each agent’s role, tools, and model configuration. |
| **6.3** | **Use the Coordinator** | In Copilot Chat, keep the mode picker on **Agent** and select **Feature Builder** from the custom agent picker. |
| **6.4** | **Run a Structured Task** | **Chat:** `Build a new endpoint to change task status.` |
| **6.5** | **Inspect the Execution** | In the **Copilot Chat window**, expand the collapsed agent calls and identify which subagent ran for each step. Note what each one contributed back to the coordinator. |
| **6.6** | **Review the Reusable Prompt** | Open `feature-builder.prompt.md` and review how it standardizes the same subagent workflow into a reusable slash command. |
| **6.7** | **Make One Meaningful Extension** | Extend the completed workflow with one improvement. Example ideas: add stronger validation, improve the test, refine the response model, or improve the review criteria. |
| **6.8** | **Explore Freely** | Now go beyond the guided task. Change one worker agent, change one model, add a new specialized subagent, or try a new feature request of your own. The goal is to observe how orchestration changes result quality, visibility, and workflow feel. |

---

## 🧠 Lesson Learned: Offloading Context Improves AI Collaboration

Subagents introduce a practical engineering pattern for AI-assisted development:

- **Isolate focused work** so the main thread stays concise
- **Specialize workers for different tasks**, e.g. research, implementation, and review
- **Coordinate results** in one final response
- **Experiment deliberately** with agent roles, models, and output formats

In the previous module, you learned about Agentic Workflows: delegating work to a single autonomous agent handling a task end-to-end. Subagents build on this foundation: not only delegating work, but structuring that delegation across specialized roles so you can inspect, compare, and improve each step independently. This compartmentalization makes multi-step workflows transparent and maintainable.

A practical Copilot-specific takeaway is that subagents help you avoid the usual tradeoff between:
- one oversized prompt that overloads context
- or many separate messages that fragment the workflow

Instead, you can keep one coordinated top-level interaction while letting Copilot distribute focused work internally.

---

## 💡 Go Further

After completing the guided workflow, use the prepared agents as a starting point and explore your own orchestration style.

Try changing:

- one worker agent
- one model
- one prompt structure
- one output format
- or one feature request

The goal is not to memorize one workflow, but to learn how to shape and inspect multi-agent collaboration inside Copilot.

---

## 💡 References & Further Reading

* [VS Code: Subagents](https://code.visualstudio.com/docs/copilot/agents/subagents)
* [VS Code Blog: Your Home for Multi-Agent Development](https://code.visualstudio.com/blogs/2026/02/05/multi-agent-development)
* [GitHub Docs: AI Model Comparison](https://docs.github.com/en/copilot/reference/ai-models/model-comparison)
