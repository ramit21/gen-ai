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


---
---

## Developing with Bedrock AgentCore (Python)

In this lesson, we move from "Instruction-based" agents to "Code-based" agents using the **AgentCore SDK**. This allows us to use standard libraries like LangChain while benefiting from AWS managed infrastructure.

See eg. of included Python agent (agent_for_agent_core.py) that uses Langchain. 

### Core Differences in the Code:
* **Annotations (`@Agent`):** Replaces manual prompt engineering with a structured definition that AWS uses to register the agent in the **AgentCore Gateway**.
* **Managed Imports:** We use `aws_agentcore` to handle the "Heavy Lifting" of security and networking.
* **The `@trace` Decorator:** Essential for production debugging. It allows you to see the "Chain of Thought" directly in the AWS Console, showing exactly what was pulled from memory vs. what the LLM generated.

### Managed Memory Types in AgentCore:
Unlike standard LLMs that have a "Goldfish Memory" (forgetting everything once the session ends), AgentCore offers three distinct types:

1.  **Short-term (Session) Memory:** Standard "Chat History" that lasts only for the current conversation. (With standalone Langraph you would use 'Checkpoints' instead)
2.  **Episodic Memory (Used in Example):** Remembers specific events or facts across different days (e.g., "The user mentioned they weighed 80kg last Tuesday"). 
3.  **Semantic Memory:** A "Personal RAG." It stores concepts and summaries rather than exact quotes, helping the agent understand the user’s long-term goals.

### Bedrock Strands

Strands Agents SDK is an open-source framework (originally developed internally to power Amazon Q) used for writing agent logic.

They are essentially utility-first wrappers. Instead of you writing a complex "while" loop to handle the AI's reasoning, Strands provides a Standardized Agent Loop. You define any Python function and use the @tool decorator. Strands then automatically generates the JSON schema the LLM needs to understand that function.

Strands comes with a library called strands-agents-tools. These are pre-wrapped utility methods for common tasks (e.g., "Search S3," "Query Dynamo," "Generate Diagram") that you can import and drop directly into an agent.

```
# --- WRITTEN WITH STRANDS ---
from strands import Agent, tool
from strands_tools.aws import s3_utils # A pre-built "Strand" utility

@tool
def get_report(report_id: str):
    """Fetches a specific health report."""
    # Uses a Strand utility method under the hood
    return s3_utils.fast_read(bucket="my-reports", key=f"{report_id}.json")

# Create the agent logic
my_agent = Agent(
    role="Health Assistant",
    tools=[get_report],
    # --- DEPLOYED TO AGENTCORE ---
    # When this runs on AgentCore, the "EpisodicMemory" 
    # we discussed earlier is injected right here.
)
```
Strands acts as the brain of the agent, Agentcore provides the infrastucture to run it.

So you write your agent using Strands, or using langchain/langraph.

Strands is for when the task is too complex to map out manually, and you want to leverage the LLM’s ability to "plan-act-reflect" on its own.

LangGraph is for when you don't trust the AI to make the right decision and you want to "hand-hold" every step. You can still use Strands utility methods even when using Langraph.

---

### Steps to Deploy to AWS AgentCore:

1.  **Containerize:** AgentCore agents run as containers. Create a `Dockerfile` using the `public.ecr.aws/agentcore/python:3.11` base image.
2.  **Push to ECR:** Upload your image to an **Amazon Elastic Container Registry** (ECR) repository.
3.  **Create AgentCore Resource:**
    * Go to the Bedrock Console -> **AgentCore**.
    * Select **Create Agent from Image**.
    * Point to your ECR URI.
4.  **Configure Gateway:** Define which **MCP Servers** (like your Jira or GitHub tools) this agent is allowed to access.
5.  **Assign IAM Roles:** Ensure the agent has the `AgentCoreRuntimeExecution` role to allow it to read/write to its own Memory store.
6.  **Alias & Deploy:** Create an 'Alias' (e.g., `prod` or `dev`) to get a permanent ARN/URL for your agent.

