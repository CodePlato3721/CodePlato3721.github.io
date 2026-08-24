Coding with agents really has surfaced a bunch of problems and challenges we never ran into when writing code by hand. Agents work even faster than you'd expect. That's an advantage — and also a liability.

## The Problem

We're used to discussing the plan with the AI before implementing anything. But I've noticed that, since it hasn't actually built the thing yet, the boundaries the AI discusses with you during design are all imagined. You end up going back and forth arguing over imagined boundaries, which wastes a lot of time. A faster approach is to let the AI implement a rough first version of the design, then have a human try it out in a dev or QA environment, get a feel for it, and revise the design from there.\
 But that brings a new problem. An agent can generate a feature very quickly. It'll tell you roughly what the design is. But in practice, it's hard to actually understand the details of what it's describing. Sometimes I spend a huge amount of time pressing the AI for design details and still don't really get it. I don't even know where to start asking.\
 So the problem we now need to think about isn't just how to communicate with the AI — it's how to get a human brain to quickly understand an agent's design. Put simply: we need to sync the AI's design into our own heads.

## Why We Need to Sync the AI's System Design

In "Architecture, AI agents, and product empathy with Robert C. Martin," Uncle Bob points out that agents writing code lack **a sense of design** and **a sense of crisis**. I agree completely. Let's start with the sense of design.

### Lacking a Sense of Design

The system designs AI produces are like someone continuously patching over one design. An agent will first design the simplest possible solution, then patch in whatever's missing, over and over. So the design ends up feeling convoluted. Since the agent is also the one maintaining the code, and future agents will have plenty of context to work with, this genuinely isn't much of a problem most of the time. But the fear is hitting a production issue where the AI loops endlessly and just can't solve it — or burns an enormous amount of time and tokens trying. At that point a human has to go read the code directly and find the root cause. But by then the system already has a fair amount of complexity, and the human can no longer make sense of the code. That leaves you with a dilemma:

1. Don't refactor the system — push through and try to understand the AI's design. This can eat up a huge amount of time.
2. Refactor right away — which carries a serious risk of breaking the system, with no clear idea how to fix it.\
   If this happens right before a launch, or while a customer is actively running the system and urgently waiting on a fix, it's maddening.

### Lacking a Sense of Crisis

An agent doesn't draw a salary, can't get fired, and never worries about whether the system might break or go down. When an AI makes a design decision, the only criterion is whether the design looks good or bad. But we know that whether a design is "good" is always relative — every design involves trade-offs.\
 Agents seem to have seen so many system design interview questions that they tend to insist on minimal design, trying hard not to over-engineer. That part is good. But then they oversimplify the design, sometimes without even noticing the risk buried inside it. When you push back, they'll say this is an early-stage design and they've already noted down the future problems and how to optimize for them.\
 And that's exactly the problem. **The agent assumes you and it share a synchronized plan for the system's future.** You don't. It doesn't even have one itself, really — because to an LLM, each round of conversation is essentially a new conversation; its thinking in the next round comes from the session context, not from the same continuous mind that thought it up before. So the plan starts drifting.\
 And agents don't worry about mistakes that seem obvious on their face — like overly frequent I/O reads and writes. Call it out, and it'll say something like: "I know about that issue, I just didn't want to complicate the design," or "No, let's not touch the existing design — just patch on top of it."

## Hypothesis-Driven Design

There's a method that works well here: hypothesis-driven design. It breaks down into 3 rounds:

1. **Round one:** Have a brief, shallow discussion with the agent, then have it quickly implement a first-pass design.
2. **Round two:** Tell the agent your own hypothetical design. Then ask it: "By analogy to similar elements in our two designs, explain to me how my design differs from yours." For a human brain, "drawing an analogy" is the fastest way we learn things.
3. **Round three:** Once you and the agent have synced on the design and you've refined your own version, have the agent refactor the system toward your design.

Doing this, the agent will lay out the trade-offs and the shortcomings of your design. By comparing the differences between your design and its design, you can quickly come to understand the system's design yourself — and it comes to understand your thinking too.\
 That last step matters a lot too. Fold in its feedback, refine your design, and ideally have it refactor the system to lean more toward your implementation. Because your implementation is the one a human brain finds easier to understand — which helps a lot, whether it's future-you or your teammates.

## In Practice

Here's a real case I ran into while building an AI voice-translation bot.

### Example 1

I've recently been building an AI voice-translation bot. But the total time for each person's speech to go through recognition + translation + speech generation varies. It's entirely possible that the translated audio for the person who spoke *later* finishes generating before the audio for the person who spoke *earlier* is even done processing.

So I needed to guarantee playback order for the translated audio. The obvious answer: we need a queue, so that a later person's translated audio waits for the earlier person's.

**Round one:** I had the agent quickly build this feature. It also explained the rough design to me — it said the core of it was a `playback-queue`. But once I actually opened up the `playback-queue`, I couldn't make sense of it at all. The design was needlessly convoluted. It had first built a queue with no waiting logic, then patched a wait-queue on top of that. Then, realizing some tasks could fail, it patched in a separate failure-handling path — without reusing anything from the earlier design. Then it introduced a pointer and kept adjusting that pointer's position back and forth. After a pile of patches, the system technically ran and was internally consistent — but the code was borderline unreadable. **This is a textbook case of an agent's missing sense of design.**

**Round two:** No matter. I described my hypothetical design to it: a simple queue whose elements carry different states, managing waiting, skipping, and completion through those states. It said it had built the same thing, then compared the elements in its design against the elements in mine. Through that comparison, **I also spotted the shortcomings in my own design.** I then had it refine the design. The whole process took about an hour. In the old way of working, I'd have had to keep grilling it with questions and might still not have understood its design.

**Round three:** I had it build another pass incorporating our earlier discussion. This time, I could actually follow everything it was saying.

### Example 2

Same AI voice-translation bot. I needed a billing feature. The requirement was simple: meter usage, and when a user's balance runs out, deny service and notify them.

**Round one:** I had the agent quickly implement this. It got it working fast, but as it explained the design to me, something felt off. It kept emphasizing how quickly it could deny service to control losses, and how quickly it could sync the account balance back to the database. Then I realized: it was micromanaging the cost of every single step in the pipeline. A few seconds of audio required 5 database round-trips! When I pushed back, it admitted there were indeed hidden risks, but said it had made a note and would improve it later. **This is a textbook case of an agent's missing sense of crisis about the future.**

**Round two:** I laid out my hypothetical design — I coarsened the granularity of what got recorded, introduced caching, and allowed a user's balance to go negative. Then I discussed the similarities and differences between my design and its design with it. In the process, I also found shortcomings in my own design.

**Round three:** I had it refactor the code to follow the improved plan. The whole process took about 2 hours.

## Summary

Once you're writing code with agents, the only real bottleneck left is the human engineer's time and attention. Figuring out how to make system-level changes fast and efficiently, while keeping those changes controllable and avoiding serious consequences down the road, matters enormously if you want to ship product quickly — because engineers at some other company might be faster and steadier than you.
