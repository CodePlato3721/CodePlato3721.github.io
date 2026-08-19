There are already quite a few AI coding frameworks out there. GSD and Superpowers for greenfield projects, grill-with-docs leaning toward brownfield, and OpenSpec, which genuinely targets brownfield projects. So do we really need to invent yet another one?

## The Pain Points of AI Coding

**Giant PRs**
Every day you run into a giant PR from a teammate. You ask them about it, and it turns out even they don't fully know what the code is doing. In the end you just click approve and move on.

**False-negative unit tests**
The codebase slowly becomes unmanageable — nobody quite knows which logic lives in which file anymore. When a bug shows up, nobody knows how to fix it, so you let AI handle it. The AI might rewrite a huge chunk of your code, declare the bug fixed, and all the unit tests pass. Then you discover some other part of the production system just broke.

**Context that grows too large**
After chatting with an agent for a while in one session, it has absorbed a lot of your codebase's conventions and anti-patterns. Then you open a new session, and it has forgotten everything again. Or maybe you've already written those conventions into the prompt context, but over time the agent still starts making the same mistakes.

**No best practices built for enterprises**
You think of those well-known frameworks. You search the web and find plenty of great frameworks for building a product from scratch. But what you're actually working with is an old, established project. You can't afford to break it — the consequences would be serious.
OpenSpec looks promising, but it's mostly aimed at individual developers. Over time, it generates a huge pile of specs, and the agent's context keeps running out.

In short, these frameworks are too far removed from what a real programmer's job actually looks like. Let's take a look at a typical day for a programmer working at an enterprise.

### A Programmer's Day
A day for someone who actually works at a company usually looks like this:
A standup meeting every morning.
Pick up a ticket from Jira.
Create a new branch, work on the ticket, test it, commit, and open a PR.

## What Is Plato

I often see people on forums asking: is there a good best practice for this yet? Honestly, I hadn't found one either. But drawing on years of programming experience combined with context management, I put together my own methodology. So I decided to turn that methodology into an open-source framework, hoping it can help others. This framework is called Plato.

### Features
- **Built for brownfield projects:** designed for projects that already carry a lot of context and have a large existing codebase.
- **A fresh session for every task:** each task starts in a brand-new session, keeping the context clean.
- **Context loaded by role:** Plato splits the work for a change into multiple roles, and each role only loads the context it actually needs.
- **Code review through questioning and refactoring:** questioning is the core behavior in Plato. During the design phase, the agent asks you questions; during code review, you're expected to question the agent. This builds the habit of reviewing code by asking questions and refactoring, rather than reading it line by line.
- **Rule-oriented development:** rule documents accumulate gradually over the course of a task. Common rule documents are CLAUDE.md and AGENTS.md, but neither is well suited to enterprise-scale management. Plato splits documentation within a project into role-specific documents and project architecture documents, among others.

## How to Use Plato

Install Plato:
```sql
npx skills@latest add CodePlato3721/plato -y -g
```

Before using it for the first time, run `/plato init` to initialize the project. This creates two folders in your project:
- `.plato`: the rule files Plato needs to run
- `plato-workspace`: the project documentation that Plato and you maintain together — this is an asset that belongs to the project

When using Plato, you'll need at least two terminal windows open: one for the guide session, and one to actually execute tasks. The guide session uses the `/plato` skill to drive the development workflow — it helps you create tickets, tracks task progress, and hands you the actual Claude Code command line to run the task. If you're using VS Code, you can use the Claude Code extension as your guide.

Here's an example. You pick up a Jira ticket, PRJ-123: "Add a shopping cart feature to the system." The steps to execute it:
1. In the Claude Code window acting as the guide, run `/plato PRJ-123`. It will ask you whether this is a feature or a defect. You choose feature, and it then asks whether it's a simple feature or a complex feature.
2. This is a complex feature spanning multiple pages, so you select complex feature. It then creates `plato-workspace/tickets/PRJ-123`.
3. After setting up the workspace for this ticket, it gives you a command to launch the working agent: `claude --dangerously-skip-permissions --session-id "96d8647c-6f2d-4452-afcd-3d6eb725a3e5" --append-system-prompt-file ".plato/designer/..." "ticket-number=PRJ-123..."`
4. Open a second terminal and run this command. In VS Code, you can open a terminal panel and run it there.
5. Once the task is complete, run `/exit` to leave the working agent, then run `/plato PRJ-123` again to get the command for the next working agent. Repeat this process and you'll move through the design, planning, and coding phases until the task is done.

The Plato workflow is essentially this: repeatedly run `/plato <ticket-number>` in the guide session to get a working-agent command, run that command in a separate terminal to execute the task, and once the task is done, review the agent's work by asking questions and keep adding to the project's rule files. Every rule file you refine gets loaded back into the agent as input for the next task, forming a virtuous cycle.

## Framework Philosophy

The philosophy behind this framework is:

**Transparency:** rather than spinning up multiple invisible subagents at once, Plato always has exactly one agent working at a time. It never auto-commits code, and it always asks you to review what it produces. There's no flashy control system — just a plain command line and code.

**Looseness:** the output of every step can be edited by hand. If you're not happy with a step, you can reject the agent's work and start that task over. It's there to assist you, the professional programmer, in your work — not to take it over.

**Questioning:** questioning is the soul of how Plato works. During the design phase, the agent completes the task by asking you questions; during code review, the agent forces you to question it to get the review done. This builds the habit of reviewing code through questioning rather than reading it.

**Rules:** the point Plato emphasizes is that your real output isn't the code — it's the rules you continuously produce while executing tasks. These rules keep getting added to the project's various `.md` files. These rules are the true asset belonging to you and your project, and they're what keeps your agent working efficiently.

## Conclusion

In this AI era, anyone can get an agent to replicate an existing product with a single sentence. But there's a gap between writing code and writing maintainable code that isn't easy to cross. Bridging that gap doesn't take coding ability — it takes the methodology and big-picture judgment built up over years of project experience, something you might call a "sense of design." By using Plato, you can fold that sense of design into your code, producing engineering-grade code that stays maintainable.

Project homepage: https://github.com/CodePlato3721/plato
