# Course: Use of GenAI for Coding

------------------------------------------------------------------------

## 1. IntelliSense vs Generative AI

### IntelliSense

-   Traditional code completion feature in IDEs.
-   Suggests variables, methods, and syntax based on context.
-   Rule-based and limited to known APIs and patterns.

### Generative AI

-   Uses large language models trained on massive datasets.
-   Can generate entire functions, classes, or applications.
-   Understands natural language prompts.
-   Assists with documentation, refactoring, debugging, and testing.

------------------------------------------------------------------------

## 2. Code Generation Tools

### GitHub Copilot

-   Trained on large code datasets.
-   Supports many programming languages.
-   Provides inline code suggestions.
-   Can be used in the terminal (e.g., Ctrl + I).
-   Add a comment like: \# add a function to do xyz Then press Enter ---
    Copilot suggests code. Press Tab to accept suggestions.

### Tabnine

-   Supports local/on-prem setup for privacy concerns.
-   Learns from your coding style and makes personalized suggestions.
-   Strong support for writing unit test cases.

### Blackbox AI

-   Extension available for VS Code.
-   Also provides a web interface.
-   Integrates Claude, Gemini, Codex, and other models into one
    interface.
-   Developers do not need to switch between tools.

### GitLab Copilot

-   Extension for Visual Studio.
-   Similar AI-assisted coding features.

### Cursor

-   AI-native IDE.
-   Fork of Visual Studio Code (similar interface).
-   Unlike GitHub Copilot (which suggests code), Cursor can:
    -   Create files
    -   Modify entire codebases
    -   Execute large changes using prompts

### Windsurf

-   Another AI-native coding tool.
-   Supports prompt-driven development workflows.

### Roo code

An AI agent framework that can read and modify files, run commands, and automate development tasks, with the ability to connect directly to MCP servers. It requires at least one LLM model—either through an API key, a URL endpoint, or a local runtime such as Ollama—to act as the agent’s reasoning engine. Chat‑based models like Llama 3 work well because all interaction with the Roo agent happens through conversational messages, while coding‑focused models such as Qwen2‑Coder in Ollama offer stronger code‑generation and refactoring performance. Roo Code runs as an extension inside IDEs such as VS Code and, through a compatibility layer, JetBrains IDEs like IntelliJ. 

Document on running Roocode pointing to local Ollama models: 
https://docs.roocode.com/providers/ollama#:~:text=Roo%20Code%20supports%20running%20models,setup%20and%20a%20powerful%20computer.

Roo Code can be guided using project‑local instruction files stored in a .roo directory. These files help the agent follow consistent rules across all developer machines. They are useful for enforcing expectations such as “never assume missing details,” “ask clarifying questions before generating code,” or “do not read certain configuration files.” Keeping these rules in the repository ensures Roo behaves predictably and aligns with your project’s conventions.

A recommended structure for the .roo/rules/ directory is:
- 01-general.md — project philosophy, architectural guidelines, naming conventions
- 02-coding-style.md — linting rules, formatting standards, folder structure
- 03-tech-stack.md — approved frameworks, libraries, and preferred patterns
- 04-security.md — authentication rules, secrets handling, validation requirements
- 
These files act as persistent, shared instructions that shape how Roo interacts with the codebase and prevent unintentional deviations in behaviour.

### Continue.dev  

Continue.dev is an open‑source AI coding assistant that runs as an extension inside existing IDEs such as VS Code and JetBrains. It provides chat, autocomplete, inline code edits, and optional agent‑style workflows, with the primary goal of improving developer productivity inside the editor. Its strength is tight IDE integration: autocomplete, quick edits, PR checks, and configurable MCP tools.

Roo Code, by contrast, is an AI agent framework designed for deeper autonomy. It can read and write files, run commands, plan multi‑step tasks, orchestrate workflows, and interact with tools. Instead of being just an assistant inside the IDE, Roo behaves more like an AI operator that can drive your development environment.

A key architectural difference is that Continue.dev  focuses on assistive coding, while Roo Code focuses on agentic execution.

Windsurf, Cursor, and Antigravity are full AI IDEs, not extensions. They ship with their own agent engines and do not require Continue.dev  or Roo Code. They offer a polished, integrated experience but are not free.

Using Ollama, you can build a fully local, free agentic IDE setup by pointing Continue.dev to local models. This setup typically requires three model types:
- a chat model (e.g., Llama 3) for reasoning and conversation
- a coding model (e.g., Qwen2‑Coder) for strong code generation and refactoring
- an embedding model for search, context retrieval, and RAG‑style features

### Kiro

Kiro is a spec‑driven AI IDE built by Amazon, designed to behave less like a code autocomplete tool and more like a structured feature‑delivery system. You give it a prompt or workflow, and it first generates a formal spec document, then turns that into user stories and executable tasks. Each task becomes a unit of code generation, with Kiro maintaining consistency across files, tests, and project structure. It also supports automation hooks (for example, “whenever a new */py file is created, update the README”), making it feel like an opinionated, process‑first engineering environment rather than a traditional IDE. Unlike Roo Code or other AI‑augmented editors, Kiro is not model‑agnostic: it only supports Claude models because it runs entirely on AWS Bedrock, which currently exposes Claude but not OpenAI models. This makes Kiro more structured and enterprise‑aligned, while tools like Roo Code or Cursor are more flexible, open, and model‑agnostic.

Kiro ends up costing more because its workflow sits on three separate pricing layers: a paid IDE subscription, AWS Bedrock request charges, and Claude model usage on top of Bedrock. Every feature run triggers multiple model calls (spec → stories → tasks → code → hooks), so token usage is naturally higher. In contrast, Roo Code with OpenAI is far cheaper because it has no IDE fee, no Bedrock middle layer, and you pay only for direct OpenAI model calls, which are already priced lower than Claude‑via‑Bedrock. For practical budgeting, Kiro is the high‑structure, high‑cost option; Roo Code with OpenAI is the flexible, low‑cost option.

### Claude Code

Claude Code is an AI‑assisted development environment built around Anthropic’s Claude models, designed to work inside editors such as VS Code and Cursor. Other than IDE plugins, Claude can also be accessed by terminal or Claude web console. It focuses on conversational, context‑aware coding rather than simple autocomplete. Claude Code can read files, propose edits, refactor code, generate tests, and perform multi‑file reasoning, but it does not execute shell commands or act as a fully autonomous agent. Its strength lies in high‑quality reasoning, safe transformations, and natural‑language workflows.

Claude models in decreasing order of cost and efficiency: Opus, sonnet, Haiku.

Claude has a free mode for web chat based interface, but for using with coding and itegration with IDEs/Terminal, you need to buy a pro or max account.

Claude Code supports multimodal input, which allows it to work directly from screenshots, UI mockups, diagrams, or design images. You can provide a screenshot of a webpage or application layout, and Claude can generate a complete HTML/CSS/JS implementation that matches the design. Because the workflow is conversational, you can iteratively refine the output—adjust spacing, change colors, add animations, convert to React, or restructure components—simply by chatting with the model. This makes Claude particularly effective for rapid prototyping, front‑end scaffolding, and design‑to‑code workflows.

Claude Code also supports a project‑local configuration system through a `.claude/` directory. This directory allows you to define persistent instructions that shape how Claude behaves across sessions and across developer machines. The most common file is `CLAUDE.md`, which acts as a project‑level guide describing coding conventions, architectural expectations, naming rules, and behavioural constraints. Claude loads this file automatically and uses it as a baseline for all coding tasks.

The `.claude/` directory may also contain auto‑generated memory files created by Claude Code itself. These files store patterns it has learned from your corrections and preferences, helping it maintain consistency without requiring repeated instructions. Unlike Roo Code, Claude does not use skills or multi‑agent roles; instead, it relies on a single, unified instruction layer plus optional auto‑memory.

A typical `.claude/` directory structure looks like:

- **CLAUDE.md** — primary project instructions, coding style, architecture notes  
- **auto/** — optional auto‑generated memory files created by Claude Code  
- **rules/** (optional) — additional rule files for fine‑grained behaviour control  

These files allow Claude Code to behave more like a teammate who understands your codebase, rather than a stateless assistant. They help enforce expectations such as asking clarifying questions before generating code, avoiding assumptions about missing context, or following specific project patterns.

You can also keep a more global .claude directory in your $HOME for workspace-wide instructions.

If you already have an existing repository, you can run the `/init` command. This scans your project—source files, documentation, README.md, and other relevant context—and compiles that information into a `claude.md` file inside the `.claude` directory. By storing this context once, Claude no longer needs to re‑read the entire repository on every request, which significantly reduces token usage and speeds up subsequent interactions.

------------------------------------------------------------------------

## 3. Leadership Concerns with GenAI Coding Tools

### Code Quality & Responsibility

-   Who owns the generated code?
-   Who is accountable for bugs?

### Code Maintainability

-   Generated code may not follow internal standards.
-   Risk of inconsistent architecture patterns.

### Skill Rot

-   Over-reliance may reduce developer problem-solving skills.

### Policy Violations

-   Internal compliance issues.

### Copyright Violation

-   Risk of generating copyrighted code.

### Open Source License Risk

-   Generated code may resemble GPL or other licensed code.

### Proprietary Data Leak

-   Sensitive code may be exposed to third-party models.

### Security Risks

-   AI may generate insecure code patterns.

------------------------------------------------------------------------

## 4. How to Mitigate These Concerns

### Start Small

-   Run a pilot project before full adoption.

### Manual Code Reviews

-   Ensure all AI-generated code is reviewed.

### Brown Bag Sessions

-   Conduct informal training sessions.
-   Upskill employees on responsible AI usage.

### Secure AI Supply Chain

-   Host models on-prem if required.
-   Understand whether vendor tools auto-train on your code.
-   Evaluate third-party risk carefully.

### Use Custom LLM Models

-   Deploy private fine-tuned models where possible.

### Anonymize Data

-   Remove sensitive data before sending prompts to models.

------------------------------------------------------------------------

## 5. Using GenAI for Requirement Analysis

Use ChatGPT-style tools for requirement gathering.

Example workflow:

1.  Provide an initial requirement draft.
2.  Ask the AI: "Ask me clarifying questions to complete this document."
3.  Refine requirements based on AI feedback.

------------------------------------------------------------------------

## 6. Generating User Stories

Once requirements are finalized, prompt:

-   "Create main user stories based on this document."
-   "Make user stories specific to software developers."
-   "Create implementation tasks."
-   "Project stack: Flask (backend), S3 (file storage), React
    (frontend)."

AI can generate:

-   Epics
-   User Stories
-   Tasks

------------------------------------------------------------------------

## 7. Export to Project Management Tools

You can:

-   Export generated content as CSV.
-   Import into Azure DevOps.
-   Automatically create:
    -   Epics
    -   User Stories
    -   Tasks

------------------------------------------------------------------------

## 8. Generating Architecture Diagrams

Use AI tools to generate diagrams in:

-   Mermaid format
-   draw.io format

These diagrams can represent:

-   System architecture
-   Data flow
-   Microservices
-   Deployment pipelines

------------------------------------------------------------------------

## 9. How to choose a model

Choosing a model is a balance between **accuracy**, **speed**, **hardware limits**, and **cost**. The three variables that matter most are **model size**, **architecture (dense vs MoE)**, and **quantisation level**.

### Model size and capability
Larger models generally reason better, follow instructions more reliably, and handle complex tasks, while smaller models are faster and cheaper.

- **Small models (3B–14B)** — fast, low‑cost, good for autocomplete, coding, and simple reasoning.
- **Medium models (30B–70B)** — strong reasoning and balanced performance.
- **Large models (100B+)** — highest reasoning ability but expensive and slow unless quantised.

Dense models scale linearly: more parameters require more VRAM and compute.

### Dense vs MoE (Mixture‑of‑Experts)
MoE models have many total parameters but only a small subset (“experts”) active per token.

- **Dense models** — all parameters active every token; highest stability and accuracy; high VRAM needs.
- **MoE models** — huge total parameters but behave like a smaller model at inference; faster and cheaper; slightly less consistent on edge cases.

MoE is ideal when you want **big‑model intelligence with small‑model hardware cost**.

### Quantisation (4‑bit, 8‑bit, FP16)
Quantisation compresses the model by **reducing the precision of weight‑vector values** (e.g., from 16‑bit floats to 4‑bit integers), cutting memory use and speeding up inference.

- **4‑bit quantisation (Int4, NF4, AWQ)** — ~75% VRAM reduction, much faster inference, small accuracy drop; enables 14B–32B models on 8–12 GB GPUs.
- **8‑bit quantisation** — moderate VRAM savings, minimal accuracy loss; good for production inference.
- **FP16/BF16** — full precision, highest accuracy, requires large GPUs; best for training or high‑stakes reasoning.

Quantisation is the single biggest enabler for running large models on consumer hardware.

### Practical decision flow
1. **Match to hardware**
   - 8–12 GB GPU → 4‑bit 7B–14B or MoE models  
   - 16–24 GB GPU → 4‑bit 30B–70B or FP16 14B–30B  
   - 48 GB+ GPU → FP16 70B+  

2. **Match to use case**
   - Coding → 7B–14B is enough; 32B+ improves reasoning  
   - Chat + reasoning → 30B–70B dense or MoE  
   - Math, logic, planning → 70B dense or high‑end MoE  
   - Fast inference → 4‑bit quantised  
   - Maximum accuracy → FP16 dense  

3. **Choose speed vs intelligence**
   - Speed → smaller or MoE + 4‑bit  
   - Intelligence → larger dense models (FP16 or 8‑bit)

### Quick reference table

| Factor | Option | When to choose |
|--------|--------|----------------|
| **Model size** | 7B–14B | Fast, cheap, coding, autocomplete |
| | 30B–70B | Strong reasoning, balanced performance |
| | 100B+ | Best reasoning, expensive |
| **Architecture** | Dense | Highest accuracy, predictable |
| | MoE | Big‑model intelligence on small hardware |
| **Quantisation** | 4‑bit | Max speed + minimal VRAM |
| | 8‑bit | Good balance |
| | FP16 | Highest fidelity |

### One‑sentence rule of thumb
Pick the **smallest model that meets your accuracy needs**, and run it in **4‑bit quantisation** unless you specifically need full‑precision reasoning.


------------------------------------------------------------------------
# Summary

Generative AI tools significantly accelerate coding, requirement
analysis, and project planning. However, organizations must address
governance, security, legal, and skill-development risks.

Responsible adoption, structured training, and strong review processes
are essential for long-term success.
