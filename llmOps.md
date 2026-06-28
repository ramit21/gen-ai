# Observability vs Monitoring (LLMOps Context)

Monitoring tells you **what** happened.  
Observability tells you **why** it happened — essential for debugging non-deterministic LLM behaviour, prompt sensitivity, tool failures, and hidden reasoning.

## AgentOps vs LLMOps

**AgentOps** focuses on multi-step agent behaviour, orchestration, and workflow correctness.  
Examples:

- Tracing agent reasoning across planner → architect → coder nodes  
- Debugging why an agent looped infinitely or chose the wrong tool  
- Inspecting state transitions inside a LangGraph workflow  

**LLMOps** focuses on the model layer, evaluation, and data quality.  
Examples:

- Prompt versioning to track changes and rollback  
- Evaluating hallucinations or relevance using LLM-as-a-judge  
- Monitoring token usage, latency, and cost across model calls  

**AgentOps = orchestration + behaviour**  
**LLMOps = model + data + evaluation**  
Both are required for production-grade agent systems.

---

# LLMOps — Core Pillars

## Agent Observability & Tracing

Understanding multi-step agent behaviour, tool usage, reasoning paths, and failure points.

## Prompt Versioning

Tracking prompt changes over time for reproducibility, rollback, and controlled experimentation.

### Data Management & Evaluation

Managing datasets for RAG, fine-tuning, and automated evaluation pipelines.

---

# Opik — LLMOps Platform

Opik is an **LLMOps platform** providing full observability and evaluation for LLM applications.

## Key Features

- Input, output, and reasoning traces  
- Latency and cost per trace  
- Cookbooks for easy setup across LLM providers  

## Human Feedback

Feedback can be attached at:

- trace level  
- span level  
- conversation thread level  

This enables structured human‑in‑the‑loop evaluation.

### Built-in Evaluation Metrics

Two categories:

#### Heuristic Metrics

- hallucination detection  
- answer relevance  
- harmful content moderation  
- context precision  
- context recall  

**Precision** — how much of the retrieved context was actually relevant.  
**Recall** — how much of the relevant context was successfully retrieved.

#### LLM-as-a-Judge Metrics

- Use an LLM to evaluate another LLM's output  
- Custom judge prompts can be created for domain-specific evaluation  

---

# Prompt Optimisation

Opik includes a prompt optimiser that can be enabled with a few lines of code.  
It rewrites or compresses prompts to reduce cost and improve performance.

---

# Opik vs LangGraph vs LangSmith

## Opik

- Open-source, free, self-hostable  
- Framework-agnostic (works with LangChain, LangGraph, custom agents)  
- Strong focus on observability + evaluation  

## LangSmith

- Licensed product  
- Designed specifically for LangChain / LangGraph ecosystems  
- Provides tracing, dataset management, and evaluation  
- Not open-source  

## Other Competitors

- Langfuse  
- Galileo AI  
- Helicone  

---

# Pydantic & Pydantic Logfire

## Pydantic

A Python library for data validation, type enforcement, and structured state modelling.  
Used internally by major LLM providers to ensure predictable, validated inputs and outputs.

## Pydantic Logfire

A full-stack observability solution built on OpenTelemetry.

Key features:

- Unified tracing across LLM calls + backend services  
- Single timeline view of model calls, tool calls, API requests, and backend operations  
- Removes the need to combine Opik for LLM + Datadog for backend  
- Provides end-to-end visibility for Python applications  

