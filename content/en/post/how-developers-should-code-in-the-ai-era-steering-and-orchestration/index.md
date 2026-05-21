---
title: "How Developers Should Code in the AI Era: Steering and Orchestration"
date: 2026-05-20
draft: false
image: https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/2026/05/how-developers-should-code-in-the-ai-era-steering-and-orchestration/en/banner.png
tags: ["AI Coding", "LLM", "Software Engineering", "Vibe Coding", "Agent"]
categories: ["AI Philosophy"]
---

## The Confusion

Developers have never been this confused about their own profession. I keep seeing wildly different takes:

1. A manager mandating that AI must write over 70% of all code
2. Developers writing code by hand, then using AI only for unit tests
3. Someone getting offended in a job interview when asked if they've used Claude Code
4. People calling vibe coding a gamble
5. Claims that programmers are obsolete — that we no longer need them at all
6. Claims that TDD/BDD is the answer and will keep projects stable
7. Reports that AI-generated code passes all tests, then crashes in production
8. Arguments that AI coding is a scam — just a marketing ploy to sell tokens

---

## Two Pieces of Bad News

All of these takes are partially right, and partially wrong. But I want to start with two pieces of bad news:

1. Cursor will die. JetBrains will die. Even Copilot will probably die. Nearly the entire IDE industry may eventually cease to exist.
2. Yes, a lot of developers have already been laid off — but not enough of them.

I don't enjoy delivering bad news. But I like pretending everything is fine even less. Ignoring a serious diagnosis doesn't make the disease go away. It just makes the outcome worse.

---

## The Limits of AI Coding

The past few months have felt like an unstoppable march. AI coding seems invincible, like it's going to take over the world. And honestly, we haven't come close to reaching its ceiling yet.

But AI coding does have a ceiling.

Here's the thing: the AI we use for coding isn't AGI. As professionals, we should stop using the vague term "AI" and be precise: what we're actually working with is a **Large Language Model (LLM)**.

At its core, an LLM predicts the next token. That's fundamentally different from abstract thinking, systems-level reasoning, or genuine creativity.

This leads to four critical failure modes:

- **Architectural drift**: If you let an LLM work autonomously for too long, it will gradually veer off course — sometimes ending up somewhere you never intended.
- **Software entropy**: Ask an LLM to build a large project on its own and you'll likely end up with a mess. You don't even need a large project — a moderately complex module can spiral into unreadable code. I've even seen it write terrible unit tests for a single class.
- **Context dilemma**: As context grows, LLM performance degrades — too much context causes it to "lose focus." You're stuck in a bind: compress the context and lose information; leave it uncompressed and watch quality drop. Techniques like summarization and progressive disclosure help, but they cost performance. Every edit can become a slow, expensive operation.
- **Token abuse**: Tokens cost money. You don't have unlimited budget. And because unsupervised AI tends to write poor logic and bloated tests, fixing things later costs more and more tokens. Maintenance becomes increasingly expensive over time.

---

## What Developers Are Actually For

Developers won't disappear — but "the developer who writes code" as a job description will.

The way we write software is about to change fundamentally. And it will happen in two phases: **steering** and **orchestration**.

---

### Steering

People often ask: what's the right ratio of AI-written code?

My answer: 100%.

When farmers got tractors, what percentage of seeds were planted by hand? Zero.

Once AI writes the code, there's no reason to go back to the slow, typo-prone process of typing it yourself. Your real job becomes **steering**.

Steering means compensating for those four failure modes.

Most of a developer's time will no longer be spent writing code. It will be spent reviewing AI-generated code, identifying problems, giving corrective feedback, and preventing the same mistakes from repeating. It means guiding the AI toward better practices and cleaner architecture.

Design patterns, clean code, code taste, refactoring, writing good unit tests — all of these things that used to feel like advanced topics are now table stakes.

Not for the sake of elegance. For a very practical goal:

**Write code that's maintainable, less buggy, and cheaper to operate.**

![Steering diagram](https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/2026/05/how-developers-should-code-in-the-ai-era-steering-and-orchestration/en/01.png)

#### The End of the IDE

If steering is the future of coding, traditional IDEs become largely irrelevant.

IDEs were built for humans writing code. If AI-generated code doesn't need autocomplete, doesn't make typos, and humans aren't typing anymore — then most of what an IDE does loses its purpose.

There may still be IDEs in the future, but they'll be minimal: fast to launch, simple in feature set, retaining only the essentials. That's not a recipe for a high-margin industry. Something that simple will inevitably be replicated by open-source alternatives.

Like film processing labs and video rental stores, this industry will fade.

---

### Orchestration

Running a single agent to write code still isn't efficient enough.

Think about how you actually work when you get a new requirement. You don't just start coding.

You clarify the requirements. You design an approach. Sometimes you build a quick POC to validate the design. Only then do you write the actual code and test it.

The entire software development lifecycle will eventually be handled by AI. But the context problem means you can't hand everything to a single agent.

And to be clear: this isn't the kind of limitation that gets solved by a longer context window. It's a limitation baked into how LLMs fundamentally work.

So the real development environment of the future will look like a complete **AI workflow** — a pipeline with agents filling different roles:

**Solution Architect + N Developers + Test Architect + N Testers**

![AI workflow orchestration diagram](https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/2026/05/how-developers-should-code-in-the-ai-era-steering-and-orchestration/en/02.png)

Notice there's no "Requirements Analyst" agent. That role should stay with humans. Even a small misread of the requirements can corrupt the entire architecture downstream.

But building this workflow isn't a one-time setup. If you let it run unchecked, it will burn through tokens and produce an unmaintainable codebase. That's architectural drift at scale.

OpenAI and Anthropic are both researching long-running AI development projects — but think of those as idealized lab conditions. They don't have to worry about token costs. You do.

And I'm willing to bet that even their "autonomous" projects have human oversight built in — people continuously adding rules and correcting the AI's behavior.

This is what people are increasingly calling **Harness Engineering**.

Which means the developer's ultimate job becomes:

**Building, tuning, and operating the AI workflow.**

Because you still need to steer it.

---

## Conclusion

Because LLMs have fundamental limitations that can't be engineered away for now, the developer profession will survive — in a different form — for the foreseeable future.

Until true AGI arrives.

But I'd encourage everyone to start transitioning now. Because those who don't may find themselves left behind by the time that moment comes.
