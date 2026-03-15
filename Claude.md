
# Claude Code

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

Other than Claude.md at the project level, which is committed to Git, you can also use Claude.local.md added to .gitignore, or a file stored at the user level in the machine as well. You can type a prompt starting with a #, which adds the instruction to memory. You can choose to save the memory at project/local/global level, and accordingly the instruction is added to the respective Claude.md file

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
