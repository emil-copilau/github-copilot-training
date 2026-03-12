## 🎯 Module V: Agentic Workflow

### 📚 Goal: Master the creation of a Custom Agent and delegate autonomous, multi-step tasks using both the GitHub Issue and the Copilot Chat interface.

**Copilot Coding Agents** 🤖 are **autonomous** AI assistants designed to perform **multi-step, iterative coding tasks** in an **asynchronous** manner. They are the **only** Copilot tools that can run, commit, and open PRs in a loop without human intervention. Agent workflows can be triggered in multiple ways via GitHub UI, GitHub CLI or Chat.

**Custom Agents** are **user-defined agent profiles** that encapsulate a specific workflow or rule set, ensuring specialized, consistent task execution.

## Exercises

| Step | Feature | Instructions |
| :--- | :--- | :--- |
| **5.1** | **Agent Profile** | 1. **Review** the custom agent profile: **.github/agents/MypyFixer.md**. <br>2. Confirm there are Mypy type errors present in the codebase (e.g., in `app/main.py`) but do not fix them. |
| **5.2** | **Delegation via GitHub Issue** | 1. Go to your repository's **Issues** tab on GitHub and create a new issue. e.g. titled: **`@copilot Request: Fix All Outstanding Mypy Errors of the App`**.<br> 2. **Assign** this new issue to the **`@copilot`** agent. <br>3. Use the custom agent profile dropdown to select **`MypyFixer`**. |
| **5.3** | **Delegation via VS Code Chat** | **Chat: MyPyFixer:** Create a simple prompt that initiates the **autonomous workflow** directly from your IDE using the selected agent, resulting in a new PR. Click the cloud icon next to the send button and select the **`GitHub Copilot Cloud Agent`**.|
| **5.4** | **Review the Iteration** | Monitor the issue timeline and the resulting Pull Requests. Observe how the agent iteratively runs mypy, fixes one error, commits, and repeats until mypy passes, showcasing the power of its autonomous loop. |
| **5.5** | **Optional: Delegation via GitHub CLI** | Make sure the GitHub CLI is installed. Delegate the task via the command line: **`gh issue create --title "@copilot Request: ...your Task..." --assignee @copilot`** |
| **5.6** | **Challenge: Design Your Own Agent** | Design and create a new custom agent profile: **`.github/agents/YourAgentName.md`**. Delegate a new task to this Agent while you can focus on the next feature development. |
| **5.7** | **Optional: Run Agent Locally** | **Chat:** Create a simple prompt to assign a task to any of your defined agents. Click the cloud icon next to the send button and select the GitHub Copilot CLI Agent.|
| **5.8** | **External Resources** | Review community collections: **Awesome GitHub Copilot** and **GHCP Tool Library (UBS)** to find example agents, instructions, and MCP servers. |
---

### 🧠 Lesson Learned: Agentic Autonomy and Delegation

Delegating tasks to the autonomous Coding Agent transforms technical debt into an automated, scalable workflow, allowing developers to focus their time on complex feature development.

* **Autonomy is Key:** ☁️ The **Coding Agent** is the only Copilot functionality that runs **asynchronously**, commits changes, and opens a Pull Request **autonomously**. This is the definition of the **Agentic Workflow**.
* **Scalability:** 🚀 The system supports concurrent task execution, allowing multiple colleagues to assign tasks simultaneously.

---

### 💡 References & Further Reading

* [VS Code: Custom Agents](https://code.visualstudio.com/docs/copilot/customization/custom-agents)
* [About Coding Agents](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent)
* [Create and Configure Custom Agents](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents)
* [Delegate from Copilot Chat (VS Code)](https://code.visualstudio.com/docs/copilot/copilot-coding-agent#_method-2-delegate-from-chat)
* [Awesome GitHub Copilot](https://github.com/github/awesome-copilot/) — Community collection of agents, instructions, workflows, and plugins.
