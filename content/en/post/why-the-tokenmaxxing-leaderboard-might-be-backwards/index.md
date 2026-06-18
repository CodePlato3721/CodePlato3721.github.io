---
title: "Why the Tokenmaxxing Leaderboard Might Be Backwards"
date: 2026-06-10
draft: false
image: https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/2026/06/why-the-tokenmaxxing-leaderboard-might-be-backwards/en/banner.png
tags: ["AI", "Productivity", "LLM"]
categories: ["AI Philosophy"]
---

Okay, I'll admit the title is a bit of an overstatement. But once you filter out developers who aren't using AI at all, there's a real possibility that people with *lower* token usage are actually more productive.

## The LOC Analogy

In the 1960s–80s, a metric called LOC (Lines of Code per Man-Month) was widely used to measure programmer productivity. It led to absurd behavior — developers avoiding libraries just to keep their line count high. Bill Gates famously said: "Measuring software progress by lines of code is like measuring aircraft construction progress by weight."

Now replace LOC with TOC — Tokens of Code — and you have the modern equivalent.

## The Context Trap

LLMs have no inherent memory. Chat apps simulate memory by stitching conversation history back into every prompt. As a session grows, the context expands — until something has to give.

The solution is context compression: summarizing accumulated history into a few sentences. For casual chat, this works fine. For coding, it's a real problem — critical instructions you gave earlier ("don't do it this way") get thrown away in the compression, and the model starts making the same mistakes again.

Worse, longer contexts cause *attention dilution*. The model has to attend to more, spreads thin, and starts focusing on irrelevant details while losing track of what matters. A massively long context often produces worse code, not better.

## The Leaderboard Problem

Climbing the Tokenmaxxing leaderboard is easy: keep loading large documents or asking sweeping, open-ended questions. But as context grows longer, the model thinks slower, attention scatter degrades code quality, and you end up in a feedback loop — worse code → more bugs → more tokens spent on fixes.

Meanwhile, developers who work in small, deliberate steps — breaking tasks down, reading each generated file, continuously refining the model's understanding — produce cleaner code with fewer bugs, and consume far fewer tokens doing it.

Token consumption is not a measure of productivity. It may actively harm a company's engineering culture.

Read the full article on HackerNoon: https://hackernoon.com/why-the-tokenmaxxing-leaderboard-might-be-backwards
