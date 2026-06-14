# From Code to ABS: A New Development Paradigm for the AI Era

## Perspectives

There are roughly three schools of thought on AI-assisted programming today:

1. **Distrust AI entirely** — use it only as a code snippet generator. Copy the output into your project, but keep your development workflow exactly as it was before.
2. **Trust AI completely** — pure Vibe Coding. Never read the generated code; just keep feeding in best practices you find online and increasingly detailed acceptance criteria. As long as the criteria pass and enough constraints are in place, you get a working product.
3. **Partial trust** — hand all code-writing to AI, but not design or testing. Stay involved through Ask mode to guide architecture, or have the AI scaffold tests while you write the actual test cases.

Which of these is actually the right direction?

<en-image-01>

## The Confusion

In this era, with the rise of Loop Engineering, source code no longer seems to belong to the programmer. UI design no longer seems to belong to the designer; test scripts no longer belong to the QA engineer; even requirements docs are no longer fully owned by the product manager.

And yet, without any human involvement at all, it's genuinely difficult to ship a usable product. So what work is left for humans? Where exactly is the gap between the human brain and the model?

## A New Paradigm

### From Circuit Boards to Integrated Circuits

My undergraduate degree was actually in electrical engineering, not computer science. Early circuit design meant hand-soldering discrete components onto boards — transistors and other logic-capable devices included. Then integrated circuits arrived and all that low-level logic got encapsulated. Engineers started writing HDL, and complex circuit structures were generated automatically.

No one cares anymore how one transistor is wired to another. Our thinking shifted to a higher level of abstraction — away from the connections between components, toward bigger, more abstract problems.

### From Code to ABS

#### What Is ABS?

ABS stands for **Agent Behavior Specification**.

Files like `AGENTS.md`, `CLAUDE.md`, and `MEMORY.md` that you see in projects today are, at their core, files that specify how an Agent should behave. They all belong to ABS.

<en-image-02>

#### How to Practice It

An engineer's job should not be writing code line by line — nor auditing code line by line. But it's also not about ignoring the Agent's implementation entirely and only checking the final result. Engineers still need to retain the ability to dive into details. You'll still do deep code reviews during early project phases or at certain critical milestones.

But the *nature* of that review has changed. In the past, you reviewed code in order to ship. Now you review code in order to *calibrate the Agent*. After reading it, instead of immediately fixing code, docs, or config, you ask yourself: Why did the Agent do this? What rule was missing? What experience deserves to be distilled?

Then you let the Agent make the fix while you draw the lesson and write it into the ABS. For example:

1. Areas for improvement go into a best-practices file, like `BEST_PRACTICES.md`.
2. Mistakes that must never be repeated go into a prohibitions file, like `NEVER.md`.
3. Architectural adjustments go into an architecture definition, like `ARCHITECTURE.md`.
4. Other long-term rules continue to accumulate in the appropriate ABS files.

In the AI era, an engineer's most important output is no longer the code itself — it's the ABS files. **ABS is the new source code. Code is just the compiled output of ABS.**

#### Single File vs. Multiple Files

Is one `CLAUDE.md` or `AGENTS.md` enough, or should you split things into `ARCHITECTURE.md`, `STACK.md`, `NEVER.md`, and so on? The community already has many different approaches. Which is better?

Once you accept that ABS is the new source code, this question answers itself.

First, which granularity is better? Multiple files. For exactly the same reasons as traditional software engineering: clearer separation of concerns, better support for team collaboration, easier maintenance, easier debugging, and fewer conflicts.

Second, which naming convention is better — `STACK.md` or `ARCHITECTURE.md`? It doesn't really matter. Just like software development today, what matters isn't the file name — it's whether you've achieved a sensible division of responsibilities. You need to know which content belongs at the architecture layer, which belongs at the best-practices layer, and which belongs at the prohibitions layer. The specific file names are secondary. The organizational thinking is what counts.

### A Day in the Life

So what does an engineer's workday actually look like in the AI era? The following scenario might give you a feel for where software development is headed.

Tom arrives at the office at 9 a.m., makes a cup of coffee, and sits down to start his day.

#### The Orchestration Panel

He opens the Agentic Development Workflow panel (the name is long enough to be self-explanatory). First, he checks the status of each Agent. Which ones are blocked? How many PRs did each Agent submit overnight? Which ones are showing a noticeable drop in throughput? These signals set the agenda for his day.

#### Editing the ABS

He spots an Agent that's stuck — it needs human-in-the-loop support. He resolves the issue and writes the solution into `NEVER.md` so other Agents don't run into the same problem later.

After unblocking everything, he reviews yesterday's monitoring data. He notices one Agent wrote hundreds of lines of unit tests for an extremely simple feature. Something feels off. He reads the tests carefully and finds the Agent produced a brittle, implementation-coupled test suite — heavily mocked, tightly bound to internal details.

He asks the Agent to rewrite the tests, this time leaning toward the Chicago school rather than the London school. Then he adds the lesson to `BEST_PRACTICES.md`.

#### Agent Behavior Monitoring

The system panel pings him with a notification: one Agent has been running unattended for 10 consecutive iterations. Based on the threshold he configured, it's time to switch to human-assisted mode.

In this mode, the Agent no longer auto-commits or auto-reviews code — every step requires human sign-off. Reviewing the recent work log, he spots early signs of architectural drift. Suspecting other Agents may have similar issues, he audits a few others and updates `ARCHITECTURE.md` and `BEST_PRACTICES.md` accordingly.

#### Tackling a Hard Problem

In the afternoon, his manager hands him a particularly difficult task — a large-scale architectural change that the model can't yet handle on its own.

He switches the Agent into human-assisted mode. Over the next few hours, he and the Agent work together on the architecture design, solution validation, and implementation. Meanwhile, the more routine tasks — bug fixes, UI tweaks, config updates — continue to run autonomously on other Agents.

And that's the day.

Tom shuts his laptop and heads home.

His Agents keep working.

<en-image-03>