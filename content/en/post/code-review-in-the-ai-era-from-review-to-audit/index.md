---
title: "Code Review in the AI Era: From Review to Audit"
date: 2026-07-04
draft: false
image: https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/2026/07/code-review-in-the-ai-era-from-review-to-audit/en/banner.png
tags: ["Code Review", "AI Development", "Agent", "Software Engineering"]
categories: ["AI Philosophy"]
---

## The PR Review Paradox

Programmers may be the most disoriented group of people in this era, and the most disorienting thing a programmer does every day is reviewing PRs.

- Agents write code too fast and produce too many lines. Humans can't keep up, so most reviews end with a mechanical click on "Approve."
- Agents rarely make low-level mistakes anymore, so reading their code feels like a waste of time.

![PR review in the AI era](https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/2026/07/code-review-in-the-ai-era-from-review-to-audit/en/01.png)

So some people came up with the idea of having one agent review another agent's PR. It doesn't work well. You'll often find that the agent misses the real structural problems, while the issues it does flag are trivial nitpicks — some of them aren't even problems at all.

Others have built skills to help agents review code better. But think about it the other way around: if we put those rules directly into the project's ABS (Agent Behavior Specification) files and let the agent write compliant code from the start, wouldn't that solve the problem at its root?

## Where the Problem Lies

PR code review was extremely valuable in the era of hand-written code, because humans make mistakes all the time. Another programmer reading your code could:

- Catch bugs in your code
- Get familiar with the project by reading your code
- Spot code smells
- Point out places where your code violates project conventions

But with agents:

- Given how well agents write code today, you almost never find low-level mistakes
- An agent doesn't need to read a particular PR to get familiar with the project
- Agents are bad at spotting code smells in each other's work
- If you set things up properly, the agent loads the project conventions before writing — so compliance issues simply don't arise

I often say that agent-written code has no small problems, only big ones.

I've also observed two trends:

- Projects are shifting from multi-person maintenance to one person per project. That makes reviewing other people's code hard, because you don't have the cross-project context a meaningful review requires.
- Agent-written PRs keep getting bigger. Past a certain size, reviewing a PR becomes mission impossible.

## A New Kind of Review

So I believe the way we review code needs a revolutionary change in the AI era. Specifically, the following changes.

### A New Point in Time

One benefit of the old PR review was that people don't share the same information or think the same way, so one person could catch problems another person missed. In agent coding, this asymmetry barely exists — reviewing someone else's PR doesn't buy you much anymore.

That doesn't mean review is unnecessary. It means we should review the code **before it gets committed**. The timing has changed. We should call a halt before the agent's spaghetti code gets pushed to the repo, preventing piles of useless code from landing on the server and wasting other engineers' attention.

You might say this is obvious — of course you look at the code after the agent finishes. Actually, no. You'll find that agents sometimes announce they've finished the code and have already committed and pushed it for you. You need to explicitly stop the agent from auto-committing and auto-pushing. This can be enforced with a commit lock and hooks.

My own setup is a convention where the agent, after finishing the code, generates a temporary **commit lock** file called a CR (commit request), and the agent's hooks check for the CR file. If the lock file exists, the commit is rejected. The CR file can only be removed by me manually, or through an agreed-upon protocol. My rule is: only when I say "approve" does the agent delete the CR file and commit the code.

### A New Standard

In the AI era, the focus of code review should shift from catching small mistakes to:

- Checking for code smells
- Checking for over-engineering
- Checking for implementations that clash with the project's style
- Checking whether the code actually meets the requirements
- And a new concern: **checking whether the PR is too big**

That last one emerged with agent coding. An oversized PR is a problem in itself. If a PR runs to thousands of lines and can't be trimmed down, the task itself was too big — it should have been split into multiple small, independently verifiable tasks and implemented step by step. A PR should never be too big to review; if it is, that's a code smell in its own right.

A reasonable PR should focus on one thing, and even if that thing involves a lot of code, the core idea should be simple and easy to grasp. For example, if you batch-modify code that follows a fixed pattern, there may be many changed lines, but the repetition is easy to see. The human brain skips over the repeated parts — they don't burden your thinking or scatter your attention.

### New Actions

**Reading becomes asking.** In the old days, reviewing meant going through the code line by line ourselves. Now we should make a habit of asking the agent about its intent and design. Rapid-fire questions are the fastest way to understand the code — and I've found that in the process of answering, the agent often discovers the problems on its own.

**Fixing code becomes fixing rules.** When a review uncovers a problem in agent-written code, we should not fix the code by hand. Even if you fix it this time, the agent will make the same mistake next time. Instead, instruct the agent to fix the code — and then instruct the agent to update the rule documents. I call these documents the ABS (Agent Behavior Specification): files like CLAUDE.md, BEST_PRACTICE.md, and so on.

![Fixing rules instead of fixing code](https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/2026/07/code-review-in-the-ai-era-from-review-to-audit/en/02.png)

### A New Cadence

We used to require a human approval on every PR before merging. But the situation has changed:

- Single-person projects are becoming common
- Agents produce code faster than humans can review it
- Given the same rules, an agent can repeatedly deliver the same quality of code for similar requirements

So we no longer need to review every single change throughout the entire life of a project. Instead:

- In the early phase of a project, review every change, and gradually build up the rule base
- In the mid-to-late phase, skip review for simple changes — but set a threshold. Once the number of skipped reviews hits the threshold, do a human review to see whether the rules need refinement

## A New Name: Code Audit

This new way of reviewing has these characteristics:

- Full review in the early phase of a project; spot checks once the project matures
- What matters is not guaranteeing the code is correct, but guaranteeing that the way the code is written is compliant

That sounds a lot like a financial audit. So I think this new way of reviewing project code deserves a better name: the code audit.

![From review to audit](https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/2026/07/code-review-in-the-ai-era-from-review-to-audit/en/03.png)
