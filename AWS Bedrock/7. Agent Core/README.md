# Agent Core

While the **Swagger/Action Group** approach is excellent for rapid prototyping and simple task-matching, enterprise-grade applications (like Bankline) require a more robust, scalable, and secure framework. This lesson covers **Amazon Bedrock AgentCore**—the managed operations layer for "Prod-Grade" AI agents.

## 1. The Limitations of Swagger-Based Agents
In a production environment, the traditional Swagger/OpenAPI approach faces three primary hurdles:
* **Static Orchestration:** The agent's logic is "locked" to the Swagger file. Any API change requires re-uploading the spec and re-syncing the agent's understanding.
* **Context Window Bloat:** Large Swagger files consume the model's "memory" (context window). As you add more endpoints, the agent becomes slower, more expensive, and more prone to "hallucinating" which API to call.
* **Execution Timeouts:** Lambda functions are capped at 15 minutes. Complex agentic workflows (like multi-step data migrations or code refactoring) often require longer running times.

---

## 2. What is Bedrock AgentCore?
**AgentCore** is the specialized "engine room" for AI agents. It decouples the **Tools** (what the agent can do) from the **Logic** (how it thinks), providing a managed runtime for autonomous operations.

### Key Components:
1.  **AgentCore Runtime:** A serverless environment allowing agents to run for up to **8 hours**, enabling long-running background tasks that Lambda cannot handle.
2.  **AgentCore Gateway (The "Dynamic Tooling" Layer):** Instead of a static Swagger file, the Gateway uses **MCP (Model Context Protocol)** to discover and load tools dynamically only when needed.
3.  **AgentCore Memory:** Provides **Long-term Memory** (Episodic and Semantic). Unlike standard agents that "forget" after a session, AgentCore remembers user preferences and past project contexts across weeks.
4.  **AgentCore Identity:** A dedicated security layer that manages "Agent-to-System" permissions, ensuring the agent only accesses Jira, GitLab, or Databases it is explicitly authorized to touch.

---

## 3. Comparison: Action Groups vs. AgentCore

| Feature | Action Groups (Swagger) | AgentCore (Production) |
| :--- | :--- | :--- |
| **Tool Loading** | Loads all APIs at once (Static) | **Semantic Selection** (Dynamic/On-demand) |
| **Protocol** | REST / HTTP Only | **MCP**, WebSocket, and Bi-directional Streams |
| **Persistence** | Session-only | **Persistent Memory** (Cross-session) |
| **Compute** | Lambda (15 min limit) | **AgentCore Runtime** (8-hour limit) |
| **Observability** | Basic Trace | Full **OpenTelemetry (OTel)** Integration |

---

## 4. The "Production" Advantage
Transitioning to AgentCore is essential for banking-grade reliability:

* **Isolated Sandboxing:** AgentCore executes generated code (like Python data analysis scripts) in a secure, isolated container. Even if the agent writes a "bad" script, it cannot access your underlying VPC or secrets.
* **Multi-Agent Orchestration:** AgentCore supports "Supervisor" patterns. You can have one "Architect" agent that delegates sub-tasks to a "Java Specialist" agent and a "Terraform Specialist" agent.
* **Spec-Driven Development:** Supports **EARS (Easy Approach to Requirements Syntax)**. The agent doesn't just "guess"; it validates user prompts against formal engineering specifications before taking action.

---

## 5. Summary for the Roadmap
> **The Takeaway:** Use Swagger Action Groups for your **MVP (Minimum Viable Product)** to prove the concept. Move to **AgentCore** when you need to enforce architectural standards, handle long-running workflows, and ensure long-term memory for a seamless developer experience.



## Next Steps:
* [ ] Convert current Health Care Lambda into an **MCP Tool**.
* [ ] Define **Steering Files** for Java 21 coding standards.
* [ ] Test **AgentCore Memory** by asking the agent to "remember" a specific report ID from a previous day's session.

