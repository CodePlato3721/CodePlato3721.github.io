Okay, I'll admit the title is a bit of an overstatement. But once you filter out developers who aren't using AI at all, there's a real possibility that people with *lower* token usage are actually more productive. Let me tell you a story, and maybe it'll start to make sense.

## A True Story

In the early days of software development — the 1960s through the 1980s — there was a popular metric called LOC: Lines of Code per Man-Month.

```text
Productivity = LOC / MM
```

Put simply, it measured a programmer's output by how many lines of code they wrote. Absurd by today's standards, but in that era, it was widely used. And it led to some fascinating consequences — like programmers who would rather hand-roll their own implementations than import a library, because importing a library adds zero lines to their count.

Bill Gates once said (he really did say this):

```text
Measuring software progress by lines of code is like measuring aircraft construction progress by weight.
```

Now replace LOC with TOC — Tokens of Code — and you have the modern equivalent: measuring a developer's productivity by how many tokens they consume.

## The Context Trap

At this point, you might be thinking: "Sure, I can see the analogy. But using tokens means using AI, and AI is faster than humans at writing code, right?" Is it? What I'm about to share is something many managers don't fully understand. The AI we're talking about isn't AGI — it's LLM. Plenty of people use LLMs every day without really understanding how they work.

Have you ever been confused by an LLM's "memory"? Why does a chat app seem to remember you? Why does switching to a new chat window make it forget everything you said before? How does an LLM decide what to remember? Does it even have memory at all?

### The Context Problem

#### How LLM Memory Works

The answer is actually quite simple. A raw LLM model has no memory whatsoever. Every single request is a completely fresh start. So why does it seem to know you when you use a chat app? Because the app itself saves your conversation history and stitches it back into the prompt with every new message. It built a memory system from scratch.

Even when you type something as simple as "Hello," the app might be sending the model something like this:

"You are an AI assistant named XX. The user's name is XXXXX. They like blah blah blah. Please respond based on the following user input: Hello."

That's why the model seems to know who you are and what you like. No magic — just prompt engineering.

#### Session Memory

So why can't the model remember what you said in a previous chat window? In the LLM world, "chat" is more precisely called a Session. Memory systems typically have two layers:

- App-level memory
- Session-level memory

Session-level memory is more granular, but it's not globally shared. You might be thinking: "Then why not just remember everything?" Simple — LLMs have a finite context window. If you tried to cram everything in, the context would overflow almost immediately. Sessions are a necessity.

But that creates a new problem. Even with sessions, as a conversation grows longer, the context keeps expanding. So what do you do?

#### Context Compression

The answer people landed on is context compression: summarizing accumulated history into a few sentences. Most of what's been said probably isn't that important anyway.

For casual chat, this usually works fine. For coding, it's a significant problem. You might have explicitly told the model "don't do it this way," and then after many rounds of conversation, it suddenly starts doing exactly that again. It's usually not the model being stubborn — you triggered context compression, and those critical instructions got thrown away in the process.

<en-image-01>

#### Attention Dilution

When context gets too long, the issue isn't just hitting the ceiling — the bigger problem is attention dilution. The longer the context, the more the model has to attend to, and it may start focusing on irrelevant details while losing track of what actually matters.

Think about reading a very long, very dry academic paper. Your focus gradually drifts, and by the end you may not even be sure what the paper was about. Often you'd be better off reading an outline first, then diving into the sections that interest you. LLMs face the same issue — this is what's known as Attention Dilution. A massively long context doesn't make the model work better; often it makes it produce worse code.

<en-image-02>

### The Problem with the Tokenmaxxing Leaderboard

I'm on Claude's monthly subscription plan. Once, I asked the model to summarize 10 moderately-sized Markdown documents and hit a "1M context limit reached" error. The system told me I'd need to purchase API tokens to continue with contexts over 1M. I was stunned — those 10 documents combined were nowhere near 1M tokens in total word count. Who knows how much front-loaded system context the Claude client was injecting.

#### How to Rank High on the Leaderboard

Back to the main topic. How does someone climb the Tokenmaxxing leaderboard? It's straightforward: keep loading large documents, or keep asking sweeping, open-ended questions. The model's context will explode, and token consumption will skyrocket right along with it.

But the biggest problem isn't the token bill. As context grows longer:

- The model thinks noticeably slower;
- Attention scatter degrades code quality;
- Context compression gradually erases best practices;
- The model starts repeating the same mistakes.

Worse code means more bugs; more bugs means more tokens spent on fixes. You end up in a cycle that benefits the employee's leaderboard ranking but harms the company:

Longer context → more tokens → worse code → more bugs → even more token consumption.

#### How to Rank Low on the Leaderboard

Virtually 100% of my code is now generated by Claude Code. But that doesn't mean:

1. I code especially fast;
2. I don't know what Claude Code is doing.

If anything, compared to many AI-assisted developers, I'm on the slower side.

I once refactored a Python project with a Streamlit frontend into a "Python backend + React frontend" architecture. Handed off to Claude Code in one shot, it might have been done in under 20 minutes. It took me three days.

Two reasons. First, I wasn't familiar with several of the technologies involved. Having Claude Code meant I could venture into unfamiliar stacks without fear of the project spiraling out of control or the timeline stretching forever — I could learn as I built. Second, I broke every task down into very small pieces. I'd read each generated file line by line, refactor continuously, adjust the rules, then have Claude Code internalize the updated best practices. Beyond that, I used a lot of other techniques — too many to cover in a single post; I'll unpack them gradually in future articles.

In the end, I shipped a project with clean, elegant code. Three days is longer than 20 minutes, but I'm confident the bug count will stay low for a long time. More importantly, without the model's help, I might not have been capable of building it at all — a month at best. Cutting that from a month to three days is something I'm genuinely satisfied with.

As my Claude Code experience has grown, I've gone from burning through my entire weekly usage limit every week to using roughly 25% of it. I'll boldly claim that what I ship probably surpasses what many people produce spending $1,000 in API costs — and that's before accounting for the reduced maintenance burden from having fewer bugs.

So where would I rank on the Tokenmaxxing leaderboard? Near the bottom, I'd guess.

## Conclusion

Of course, none of this means everyone near the top of the leaderboard is gaming the system. But it does prove one thing: token consumption is not a measure of productivity — and it may actively harm a company's engineering culture.

Longer contexts make the model think longer, sometimes for tens of minutes at a stretch. I've heard of cases where a single problem kept the model running for hours. And after all that inefficiency, the resulting code quality still may not be better.

You think you're saving time. In reality, you're just borrowing against future maintenance costs. Before you even notice, it's already eroding your product quality and your users' trust. Compared to those long-term costs, the wasted token spend is almost a footnote.
