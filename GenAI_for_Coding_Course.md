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

Claude Code is an AI‑assisted development environment built around Anthropic’s Claude models, designed to work inside editors such as VS Code and Cursor. Other than IDE plugins, Claude can also be accessed via the terminal or the Claude web console. It focuses on conversational, context‑aware coding rather than simple autocomplete. Claude Code can read files, propose edits, refactor code, generate tests, and perform multi‑file reasoning, but it does not execute shell commands or act as a fully autonomous agent. Its strength lies in high‑quality reasoning, safe transformations, and natural‑language workflows.

Claude models in decreasing order of capability and cost: **Opus**, **Sonnet**, **Haiku**.

Claude has a free mode for the web chat interface, but for coding workflows and IDE/terminal integration, you need a **Pro** or **Max** account. Always give small tasks and grow your app step by step; large tasks can consume tokens quickly.

Claude Code supports multimodal input, which allows it to work directly from screenshots, UI mockups, diagrams, or design images. You can provide a screenshot of a webpage or application layout, and Claude can generate a complete HTML/CSS/JS implementation that matches the design. Because the workflow is conversational, you can iteratively refine the output—adjust spacing, change colors, add animations, convert to React, or restructure components—simply by chatting with the model. This makes Claude particularly effective for rapid prototyping, front‑end scaffolding, and design‑to‑code workflows.

Claude Code also supports a project‑local configuration system through a `.claude/` directory. This directory allows you to define persistent instructions that shape how Claude behaves across sessions and across developer machines. The most common file is `CLAUDE.md`, which acts as a project‑level guide describing coding conventions, architectural expectations, naming rules, and behavioural constraints. Claude loads this file automatically and uses it as a baseline for all coding tasks.

The `.claude/` directory may also contain auto‑generated memory files created by Claude Code itself. These files store patterns it has learned from your corrections and preferences, helping it maintain consistency without requiring repeated instructions. Unlike Roo Code, Claude does not use skills or multi‑agent roles; instead, it relies on a single unified instruction layer plus optional auto‑memory.

A typical `.claude/` directory structure looks like:

- **CLAUDE.md** — primary project instructions, coding style, architecture notes  
- **auto/** — auto‑generated memory files created by Claude Code  
- **rules/** (optional) — additional rule files for fine‑grained behaviour control  

Other than Claude.md at the project level, which is committed to Git, you can also use Claude.local.md added to .gitignore, or a file stored at the user level in the machine as well.

These files allow Claude Code to behave more like a teammate who understands your codebase, rather than a stateless assistant. They help enforce expectations such as asking clarifying questions before generating code, avoiding assumptions about missing context, or following specific project patterns.

You can also keep a global `.claude` directory in your `$HOME` for workspace‑wide instructions.

If you already have an existing repository, you can run the `/init` command. This scans your project—source files, documentation, README.md, and other relevant context—and compiles that information into a `claude.md` file inside the `.claude` directory. By storing this context once, Claude no longer needs to re‑read the entire repository on every request, which significantly reduces token usage and speeds up subsequent interactions.

In the IDE extension chat window, typing `/` shows options such as switching models or uploading a file.
You can give specific instructions in a md file, for example, ui-component.md, and in the prompt window, just say /ui-component and press enter. The Claude will read md file, and create code as per the instructions given in the file. You can also give specific instructions along with md file to be specific about what component to create and how, eg '/ui-component card | description'. Read the arguments passed as $ARGUMENTS inside the .md file. In ex given, we are passing 2 arguments - component name, and a description of the component. So refer [name] and [description] taken from $ARGUMENTS in the .md file. 

Typing `@` followed by a filename lets you give instructions specific to that file.  
Example:  
`@MyServiceImpl.java add slf4j logging at the start of every method.`

You can select one or more files using @, all these get selected in the context of(shown below the chat box of ice agents). Remember to unselect the file for later actions, which are not just focused on the files selected.

If you open a file and select some lines of text, then those lines will be selected as the context of the Claude prompt window.

Claud code can handle approx 200k tokens of context. To keep context clean and focused, you have a few options:
- /exit to exit chat session
- /clear to clear the entire session context and chat history
- /compact command that compacts the chat and context into a small summary
- Press Escape twice to rewind to the previous point in the session

You can also ask Claude to commit code changes directly from the chat window; it will auto‑populate the commit message based on the modified files. You can reference a git commit ID and say:  
`@NextFile.java apply similar changes to this file as done in git commit <id>`  
Claude will inspect the commit and apply analogous changes.

To give an image as context. You can also upload images to the prompt window by drag and drop. Eg, 'use the styling of the button image uploaded, apply the same styling to all buttons of our project'.

Note that Claude cannot create your AWS resources, but it can generate IAC code, such as Terraform, to create AWS infrastructure. It is important to review the IAC code before changing the AWS infrastructure.

#### Claude Tools
Claude is equipped with a suite of built-in tools designed to perform technical actions directly within a development environment.

Tool Capabilities: Key utilities include bash for command execution, grep for pattern searching, and file manipulation tools. You can find the full technical specifications in the AnthropictTools reference- https://code.claude.com/docs/en/tools-reference.

Security & Permissions: To ensure safety, each tool includes a configurable permission setting. This determines whether the model can execute a command autonomously or if it must prompt the user for explicit approval first. If you're setting up a CI/CD pipeline or a restricted environment, the permission settings are your best friend for balancing automation with security.

Note that Claude does not have a standalone Git tool; instead, it executes git commands through the provided bash tool.

#### MCP support
Claue supports adding MCP servers running in local or remote, at different scope levels:

> claude add mcp <mcp-name> --context local/project/global --transport http linear https://mcp.linear.app/mcp

MCP servers added at the project level will appear as a  mcp.json file in the project.

In claude prompt, if you type /mcp, it will list the active MCP servers connected to.

When giving prompts, you explicitly mention 'use <mcp-name>' to tell Claude to query mcp for this action.

#### Claude Skills

**Claude Skills** are reusable, modular instruction sets that teach Claude how to perform your workflows consistently—without you having to re‑explain your process every time. They act like “custom capabilities” that encode your expertise, procedures, and preferences into a package.

While a `claude.md` file is injected into every prompt (and therefore consumes tokens on each request), **Claude Skills are loaded dynamically**. Every skill has metadata that Claude checks against your input prompt; if the metadata matches the task, Claude automatically pulls in the skill.

If skills did not exist, Claude might search the internet or choose an arbitrary approach for the job. With standard skills, Claude performs tasks using consistent, vetted, and agreed‑upon workflows.

Examples of Claude Skills include:  
- PDF‑related skills (e.g., creating or modifying PDFs)  
- Document‑related skills (e.g., DOCX editing)  
- Design skills (e.g., generating diagrams or visual layouts)  
- Workflow skills (e.g., multi‑step automation patterns)  

**Where do skills live?**  
- Anthropic’s official skills GitHub repository  
- Third‑party marketplaces such as *skills.pub*  
- MCP‑based integrations that expose external tools as skills

**Making a new skill**: TODO

#### Operational Modes
Claude Code uses specialised modes to balance AI autonomy with developer oversight. You can toggle these during a session or set them via startup flags.
- Plan Mode: Read-only exploration. Creates a Plan.md file for review before it touches any code.
- Normal Mode (Default): Takes approval before code changes
- Auto-Accept Mode: Claude applies file edits automatically, though it may still prompt for high-risk shell commands (e.g., git push).

### Subagents

### Hooks



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
