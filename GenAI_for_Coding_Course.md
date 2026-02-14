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

# Summary

Generative AI tools significantly accelerate coding, requirement
analysis, and project planning. However, organizations must address
governance, security, legal, and skill-development risks.

Responsible adoption, structured training, and strong review processes
are essential for long-term success.
