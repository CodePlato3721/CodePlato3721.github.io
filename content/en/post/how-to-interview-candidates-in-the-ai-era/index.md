---
title: "How to Interview Candidates in the AI Era"
date: 2026-05-14
draft: false
image: https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/2026/05/how-to-interview-candidates-in-the-ai-era/banner.png
tags: ["AI", "Interview"]
categories: ["Tech"]
---

## Background

In the age of AI, how do we hire the right people? You don't want to end up with someone who's great at LeetCode but has never touched Claude Code and has zero interest in learning AI-assisted programming.

But compared to LeetCode or traditional software knowledge, AI is still very young. So how do we gauge whether a candidate can stay productive at the company over the next few years?

## A Note on Terminology

"AI" is a broad term that works fine for general audiences. But as professionals, we should be precise.

AI covers many subfields — deep learning, supervised learning, large language models, and more. This article focuses specifically on interview questions within the LLM space, so for simplicity I'll use "AI" to mean LLM throughout.

This article also doesn't cover hiring for LLM training roles — that's outside my expertise, and frankly it's a more mature field with established interview practices. The focus here is on LLM application engineering.

## Core Framework

We evaluate candidates across 4 dimensions:

- **Learning velocity:**  
  We're hiring engineers who code with AI. Whether they're building AI features or just using Claude Code day-to-day, they need to have a genuine hunger for staying current.

  In the LLM application space, there's no university course that can keep up. What you learned at the start of the year may already be obsolete by December. Self-directed learning is the only way.

  The best AI engineers are like dogs chasing a ball — they're always running *toward* the technology, not waiting to be pushed by it.

  So our questions don't just test LLM knowledge; they also probe whether the candidate has that chasing instinct.

- **Conceptual understanding:**  
  How well does the candidate understand LLMs at a systems level?

- **Hands-on experience:**  
  Have they actually used AI coding tools in practice?

- **Domain knowledge:**  
  Knowledge of specific frameworks (e.g., LangGraph). This dimension is more relevant for candidates in AI integration roles.

## Sample Questions

The following are example questions along with my own answers.

These aren't "correct" answers — treat them as a reference point. And just like LLMs have a training cutoff, my answers here have a cutoff of June 2026.

### Learning Velocity

1. **What are the major phases in the evolution of LLM application development? Hint: the first phase is prompt engineering.**  
   Answer: Prompt engineering → context engineering → Harness Engineering

2. **What is Harness Engineering?**  
   Harness Engineering is the practice of building the external execution framework around AI agents — including tools, memory, retrieval, validation, workflow, and feedback loops — to improve agent accuracy and controllability.

   Put simply: modern agent architecture = model + harness.

3. **Name a few recent LLM applications you're aware of.**  
   Examples: OpenClaw, Hermes Agent, Happy Codex, etc. (as of May 2026)

4. **Name a few recent LLM models.**  
   Examples: Opus, GPT-5.5, etc. (as of May 2026)

5. **How do you keep up with developments in LLM technology?**  
   Following news sites, specific media outlets, building personal LLM projects and learning as you go, etc.

### Conceptual Understanding

1. **What's the difference between prompt engineering and context engineering?**  
   Prompt engineering is about *how to write a better prompt*. Context engineering is about *how to dynamically construct the entire runtime context for an AI agent*.

   Modern agent performance depends primarily on whether the agent has the right context and tools — not just on how elegant the prompt is.

2. **How do you interpret the phrase "RAG is dead"?**  
   There are two levels to this:

   - With the rise of context engineering, the focus has shifted from "better RAG" to "better context management" as the primary lever for improving agent effectiveness.

   - More precisely: it's not RAG that's dead — it's Naive RAG. The early approach of chunk → embed → similarity search is what's been superseded.

3. **What context engineering methodologies are you familiar with?**  
   Context compression, structured note-taking, sub-agent architectures.

4. **What's the relationship between context engineering and Harness Engineering?**  
   Harness Engineering focuses on the overall execution framework and runtime system for AI agents. Context engineering focuses on how to dynamically organize and deliver the right context to the agent.

   Context engineering can be seen as one of the core components of Harness Engineering.

5. **What is Progressive Disclosure?**  
   Progressive Disclosure is a design principle where a system doesn't surface all information at once, but instead reveals relevant content incrementally as needed — reducing complexity and minimizing context noise.

### Hands-on Experience

The following questions don't have right or wrong answers — except the last one.

1. Walk me through a real scenario where you used Claude Code to write production code.
2. What's the dumbest thing you've seen an AI write?
3. What do you do when the AI keeps failing to fix a bug?
4. Have you compared multiple AI coding tools? Which do you prefer and why?
5. As a developer, how should we think about writing code in the AI era?

I have some thoughts on that last question, but I'll save them for a separate piece: *The AI-Era Engineer Should Steer, Not Type*.

### Domain Knowledge

For this section, tailor the questions to whatever frameworks are relevant to the role — LangGraph, for example, if that's part of the stack.

I'll leave the specifics to you.
