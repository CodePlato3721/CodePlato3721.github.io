---
title: "From Code to ABS: A New Development Paradigm for the AI Era"
date: 2026-06-18
draft: false
image: https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/2026/06/from-code-to-abs-a-new-development-paradigm-for-the-ai-era/en/banner.png
tags: ["AI Development", "ABS", "Agent", "Software Engineering"]
categories: ["AI Philosophy"]
---

There are roughly three schools of thought on AI-assisted programming today: distrust AI entirely (use it only as a snippet generator), trust AI completely (pure Vibe Coding, never read the output), or partially trust it (AI writes code, humans handle design and testing). But as models get stronger, the real question becomes: what work is actually left for humans?

## The Core Shift: From Code to ABS

ABS — **Agent Behavior Specification** — is the answer. Files like `AGENTS.md`, `CLAUDE.md`, and `MEMORY.md` that appear in modern AI-driven projects are all ABS: structured specifications that tell an Agent how to behave.

The analogy is circuit design. When integrated circuits arrived, engineers stopped hand-wiring individual transistors and started writing HDL — thinking at a higher level of abstraction. The same shift is happening in software: engineers are moving from writing code to writing ABS.

## How to Practice It

An engineer's job today is not to write code line by line — nor to ignore what the Agent produces. The shift is in *why* you review code.

Before: you reviewed code in order to ship.  
Now: you review code in order to **calibrate the Agent**.

After reading, instead of immediately fixing code or config, you ask: Why did the Agent do this? What rule was missing? What lesson deserves to be distilled? Then you let the Agent make the fix, while you write the insight into ABS:

- Improvement areas → `BEST_PRACTICES.md`
- Mistakes to never repeat → `NEVER.md`
- Architecture decisions → `ARCHITECTURE.md`

**ABS is the new source code. Code is just the compiled output of ABS.**

## What This Looks Like Day-to-Day

In the near future, a developer's day revolves around an Agentic Development Workflow panel: checking which Agents are blocked, reviewing overnight PRs, and watching for throughput drops. When an Agent produces brittle, over-mocked tests for a trivial feature, you don't just fix the tests — you add the lesson to `BEST_PRACTICES.md` so it doesn't happen again.

Hard architectural problems — the ones models can't yet handle alone — still require deep human involvement. Everything else runs autonomously.

The engineer goes home. The Agents keep working.

Read the full article on Hackernoon: https://hackernoon.com/agent-behavior-specification-a-new-development-for-the-ai-era
