---
title: "Do We Still Need to Practice Programming in the AI Era?"
date: 2026-05-25
draft: false
image: https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/2026/05/do-we-still-need-to-practice-programming-in-the-ai-era/en/banner.png
tags: ["AI", "Programming", "Vibe Coding", "Learning", "Developers"]
categories: ["AI Philosophy"]
---

"Vibe Coding" is having a moment. So — do we still need to practice programming?

My answer is yes.

I've written before about using AI to distill reading material and quickly grasp the structure of an article. But a few fundamental realities won't change just because AI showed up.

1. The rate at which the human brain absorbs knowledge hasn't changed. No matter how fast AI technology advances, your personal learning speed doesn't automatically accelerate with it. There are no real shortcuts to learning.

2. AI was trained on both good code and bad code. Bad code isn't always incorrect code — it can simply be code that smells, is hard to maintain, or has a chaotic architecture. If you can't spot the problem yourself, AI often won't spot it either.

## Example 1

Experienced developers and beginners literally see different things when they look at the same code.

Imagine you're working in React and you come across this:

```js
const phone = {
  name: 'iPhone',
  price: {
    payInFull: 1000,
    monthlyFin: 99
  }
};
```

Your product manager asks you to add a "snapshot page" — a page that displays the product's current state frozen at a point in time, so that even if the product data changes later, the snapshot stays the same.

AI quickly generates this:

```jsx
const phone = {
  name: 'iPhone',
  price: {
    payInFull: 1000,
    monthlyFin: 99
  }
};

<Snapshot {...phone} />
```

You see `{...phone}` and think: "Got it — that's an object copy."

A short while later, customer support files a bug: after the price is updated in the parent component, the price on the snapshot page updates too.

You're baffled. This shouldn't be happening.

After digging in, you realize:

```jsx
<Snapshot {...phone} />
```

is not the same as:

```js
const snapshot = {...phone}
```

The former is just React's props spread syntax sugar.

So you update the code:

```jsx
const snapshot = {...phone};
<Snapshot {...snapshot} />
```

Still broken.

Eventually you find the fix:

```js
const snapshot = structuredClone(phone);
```

Someone who has been burned by this before — or who genuinely studied JavaScript's object reference model — would have spotted the problem immediately. Someone who hasn't would go down the same rabbit hole.

## Example 2

Have you ever felt completely fluent while watching a tutorial, only to draw a total blank the moment you sit down to write the code yourself?

I was working through a Data Science course recently. The material wasn't particularly complex for a software engineer:

```python
top1 = Table.read_table(path_data + 'top_movies_2017.csv')
```

But when I sat down to do the assignment — which asked me to load `top_movies_2017.csv` — my mind went completely empty.

I tried things like:

```python
read_csv
import_csv
```

…and various other guesses.

Strangely, I had seen `Table.read_table` multiple times in the course material.

What I realized: the human brain doesn't learn purely through reading. Learning is a multi-sensory process — it involves sound, touch, the frustration of hitting a wall, the cycle of trying and failing. Those experiences are part of the memory itself.

Knowing something intellectually is not the same as having actually learned it.

## Summary

AI can help you extract an outline, surface key points, and let you skip over sections that aren't relevant to you. In that sense it's a useful map.

But be clear-eyed about what a map is and isn't.

If your underlying ability to absorb knowledge hasn't actually gotten faster, don't be fooled by the optimistic claim that "anyone can code in the AI era."

"Anyone can generate code" is not the same as "anyone can build a maintainable commercial product."

AI can help you go faster.

But it cannot replace the process of genuinely understanding systems, code, and engineering complexity. That part still takes you.
