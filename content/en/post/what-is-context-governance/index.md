---
title: "Context Governance Explained with Examples"
date: 2026-05-19
draft: false
image: https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/2026/05/what-is-context-governance/en/banner.png
tags: ["AI", "Agent", "Context Engineering", "Context Governance"]
categories: ["AI Philosophy"]
---

Context Governance is a part of Context Engineering. In my opinion, it's the most interesting part.

That might sound abstract at first — I felt the same way. But once you look at how a few mainstream AI agents handle their context governance, the concept becomes immediately intuitive.

In this post, I'll compare four agents' approaches to context governance, walking from simple to complex, from basic to advanced.

---

## Codex

First up is OpenAI's Codex. Ironically, despite OpenAI being the first company to build a large language model, their agent product is the newest of the bunch.

And fittingly, its context governance is also the simplest. Inside the `.codex/` directory, there's a file called `AGENTS.md`. Here's a minimal example:

```md
# Repository Guidelines

## Project Structure
- `src/` — application code
- `tests/` — test code

## Common Commands
- Run tests: `npm test`
- Run linter: `npm run lint`

## Coding Conventions
- Prefer TypeScript
- Avoid default exports
- Use async/await instead of raw Promises
```

Before starting any work, Codex reads this file. You maintain it manually, adding rules over time.

Beyond this file, there's a folder: `~/.codex/memories/` — as the name suggests, it's the "memory." Codex writes to it automatically.

The rough structure looks like this:

| Type | Contents |
|------|----------|
| summaries | Session summaries |
| durable | Long-term stable memories |
| recent | Recent context |
| evidence | Source evidence |

As you can see, Codex's context governance is quite lightweight. At its core, it's just:

- One rules file
- One auto-managed memory directory

That's it.

---

## Claude Code

Claude Code takes a different approach.

The officially supported mechanisms are similar to Codex:

- `CLAUDE.md`
- `~/.claude/projects/<project>/memory/`

Just these two. The names speak for themselves. But the Claude Code community has expanded this significantly over time, evolving into something like:

| Name | Type | Purpose | Manual / Auto |
|------|------|---------|---------------|
| `CLAUDE.md` | File | Project rules, agent behavior | Manual |
| `MEMORY.md` | File | Long-term memory, preferences, lessons | Semi-auto |
| `NOTES.md` | File | Scratch notes, working scratchpad | Manual |
| `DECISIONS.md` | File | Key architecture / tech decision history | Manual |
| `ARCHITECTURE.md` | File | System structure, module relationships, data flow | Manual |
| `LEARNINGS.md` | File | Lessons learned, pitfall records | Semi-auto |
| `TASKS.md` | File | Current task list, TODOs | Manual |
| `SESSION.md` | File | Current session work log | Semi-auto |
| `docs/` | Folder | Long-form context documents | Manual |
| `memory/` | Folder | Categorized memory storage | Semi-auto |
| `prompts/` | Folder | Prompt templates, workflow prompts | Manual |
| `.cursorrules` | File | Cursor-compatible rules | Manual |

This is far more complex than Codex. But notice: a large number of these files require manual upkeep. And the whole structure looks a lot like the project wiki we'd write for a traditional software project.

That's actually the key insight: for an agent to work well, it should browse the project wiki first — just like we would. People are now turning wiki documents into context Markdown files. With that framing, it all makes sense. Claude Code, grounded in these context documents, increasingly works like a real developer.

---

## Open Claw

Open Claw is positioned differently from Claude Code — it leans more toward a life assistant than a coding tool. The community-extended Claude Code context system requires managing too many files. Unlike Claude Code's typical developer audience, Open Claw's users are more general. Many users never directly edit Open Claw's context files — some don't even know they need to.

Yet Open Claw's context design is actually more "agent-native" than the community Claude Code setup. The latter still carries a strong human project-management mindset. But for an agent, you don't necessarily need that many separate documents.

Open Claw's context governance centers on "persona" and "character." It organizes context into these files:

### Core Instruction Layer (static, manually maintained)

- **`SOUL.md`** — Personality, values, boundaries. Answers "who are you." Defines tone, character, hard constraints.
- **`AGENTS.md`** — Operational procedures and rules. Answers "what you do and how." The largest and most important file; holds complex workflows and step-by-step instructions.
- **`USER.md`** — User profile. Your name, timezone, preferences, work background. The personalization layer.
- **`IDENTITY.md`** — Structured identity record (name, role, goals, tone). For consistently re-applying a known persona. (Personally, I find this slightly redundant.)
- **`TOOLS.md`** — Tool documentation. Doesn't control permissions (that's config's job) — it tells the agent how to use the tools it already has.

### Automation Layer

- **`HEARTBEAT.md`** — Scheduled tasks, effectively a natural-language cron. E.g., "check every 30 minutes," "generate weekly report every Monday at 8am."
- **`BOOTSTRAP.md`** — First-run initialization script. Automatically deletes itself after setup.
- **`BOOT.md`** — Hook that runs on every startup.

### Memory Layer

- **`MEMORY.md`** — Long-term memory. Persistent facts, preferences, decision summaries — effective across weeks and months.
- **`memory/YYYY-MM-DD.md`** — Daily notes. Today's and yesterday's notes load automatically; older entries are retrieved via `memory_search`.
- **`DREAMS.md`** — Diary of the dreaming system, logging the "promotion" of short-term memories to long-term. An experimental feature.

Open Claw is already significantly more sophisticated than the previous two systems. When you use it, you can noticeably feel that it's "smarter."

---

## Hermes Agent

Now for the main event. If you don't understand context governance, Hermes Agent might seem similar to Open Claw. But notice: Open Claw still has many files that need manual maintenance.

Even I — after using Open Claw for a while — only recently realized those files need human upkeep. The result: many of the context structures Open Claw designed were never actually put to use.

Hermes Agent's context governance differs from both Open Claw and Claude Code. Its core design philosophy is:

> "Self-evolution" — the agent writes its own memories and skills.

The entire system lives under `~/.hermes/`.

### Identity Layer (static)

- **`SOUL.md`** — The first slot in the system prompt. Defines personality, tone, values, behavioral boundaries. This is global, loaded from `HERMES_HOME`. You can still manually edit this file.

### Project Context Layer (priority-ordered, only the first match loads)

- `.hermes.md`
- `AGENTS.md`
- `CLAUDE.md`
- `.cursorrules`

First match wins. This means Hermes is natively compatible with both Claude Code and Cursor project config files.

### Memory Layer (three tiers, agent-maintained)

- **`MEMORY.md`** — Long-term memory. Stores environment info, project conventions, tool usage experience.
- **`USER.md`** — User profile. Stores your name, communication preferences, skill level. Note: this time `USER.md` is automatically maintained by the agent.
- **`state.db`** — A SQLite database with FTS5 full-text indexing, storing all conversation history. The agent doesn't load everything by default — it retrieves on demand via `session_search`.

Memory has entered the database era. Only a database can truly support long-horizon context retrieval.

### Skill Layer (Hermes' most distinctive feature)

- **`skills/` directory** — Each skill is its own folder containing a `SKILL.md` (with YAML frontmatter) and optional templates and scripts.

The key difference: skills are not written by humans. After completing a non-trivial task, the agent creates skills on its own via the `skill_manage` tool. Similarly, memory no longer relies primarily on human maintenance — the agent edits `MEMORY.md` and `USER.md` itself between conversations. And skills are loaded on demand: unused skills never enter the context.

This is already approaching true "automated context governance."

### Scheduling Layer

- **cron jobs** — Scheduled tasks, similar to Open Claw's `HEARTBEAT.md`.

At this point, context governance isn't just more complex — it's starting to run itself.

---

## Summary

Whether an AI can actually get work done, and how well it does, is no longer just a question of which model you use. In many cases, better context governance improves agent productivity more than upgrading to a stronger model.

### The Electronic Brain

This raises an interesting question: context is effectively the agent's "electronic brain." The longer you use an agent, the more that accumulated context becomes uniquely *it*. As long as the context survives, even if you swap out the "shell," your assistant is still your assistant. If an agent crashes and needs to be reinstalled, or you want to migrate to a different platform, moving the context along should theoretically keep your assistant alive.

This opens a new question: how do you safely migrate context?

The problem today is that file names, structures, and formats vary wildly across platforms. Context migration is a mess. I believe a more unified, standardized context protocol will emerge. And "context governance" will gradually become one of the core capabilities of any AI agent worth using.
