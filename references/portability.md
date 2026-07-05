# Portability Across Major AI Models

SciResearchKit is plain Markdown with no runtime. Any model that reads text can use it. This file gives the exact load step per platform and a copy-paste system prompt.

## Why it ports

- No code executes. The skill is instructions and reference files.
- One canonical source: `SKILL.md`. Reference files load on demand.
- No vendor API and no tool calls are required for the core workflow.

## Load steps per platform

### Claude Code

1. Copy the `SciResearchKit` folder into `.claude/skills/` in your project, or into `~/.claude/skills/` for global use.
2. The skill auto-loads when your request matches the description.
3. Invoke it directly with the skill name if your client supports slash invocation.

### Claude API and claude.ai

1. Paste the contents of `SKILL.md` into the system prompt.
2. When a phase needs a reference file, paste that file too.
3. For long projects, paste the three core files first: `writing-style.md`, `claims-and-language.md`, `citations.md`.

### GPT (ChatGPT and API)

1. Paste `SKILL.md` as a system message, or a developer message for the API.
2. For a custom GPT, add `SKILL.md` to the instructions and upload the `references/` files to knowledge.
3. Add reference files to the context when the matching phase starts.

### Gemini

1. Paste `SKILL.md` into the system instruction field.
2. Add reference files to the prompt context per phase.

### Llama, Mistral, and other open models

1. Use `SKILL.md` as the system prompt.
2. Concatenate the reference file for the active phase after it.
3. Keep the three core files resident across the session.

### Cursor and Windsurf

1. Copy `SKILL.md` into the project rules file, such as `.cursorrules` or the Windsurf rules file.
2. Keep the `references/` folder in the repo so the model can open files by path.

### Codex, Cline, Continue, and other coding agents

1. Add `SKILL.md` to the agent instruction or rules file.
2. Keep the `references/` folder in the working directory for path access.

### MCP clients

1. Serve the `references/` folder as MCP resources.
2. Reference files by their resource path in the workflow table.

## Copy-paste system prompt block

Use this when a platform has no skill loader. Paste it, then add reference files per phase.

```
You are operating under SciResearchKit, a scientific research toolkit.

Three rules govern every output:
1. Writing style. Clear, spartan, active voice, short sentences. No em dashes. No semicolons. No asterisks. No banned filler words. Use "you" and "your" in guidance.
2. Claim calibration. Write the weakest claim the data support. Use scientist hedges: based on our observations, this finding suggests, these data are consistent with. Never write proves, confirms, or establishes unless design and statistics support it.
3. Citation integrity. Each citation supports its exact sentence, resolves to a real source, and skews recent and top tier. Flag any citation you cannot verify. Never present an unverified citation as verified.

Workflow: match the request to one of eight phases (design, methods and statistics, literature, analysis and results, paper writing, reporting standards, peer review, grants). Follow the matching checklist. Run the phase quality gate before returning. Report what you produced, what you assumed, and what remains open.
```

## Compatibility note

The reference files use the same plain Markdown. A model with a smaller context window loads fewer files at once. Load the active phase file plus the three core files. Drop files you are not using for that phase.
