---
title: "AI时代我们应该怎么审核代码：从审核到审计"
date: 2026-07-04
draft: false
image: https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/2026/07/code-review-in-the-ai-era-from-review-to-audit/cn/banner.png
tags: ["Code Review", "AI编程", "Agent", "软件工程", "ABS"]
categories: ["AI 哲学"]
---

# AI时代我们应该怎么审核代码：从审核到审计

## PR Review的迷思
在这个时代最迷茫的一群人就是程序员，程序员每天做的最迷茫的一件事情就是review PR。
- agent写代码太快了，行数太多了，人工review不过来。大部分都是机械式的点approve
- agent写代码基本不犯低级错误，看了感觉也是白看

![AI时代的PR review](https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/2026/07/code-review-in-the-ai-era-from-review-to-audit/cn/01.png)

于是有人就想出让一个agent去review另一个agent的PR。但是这样做的效果并不好。你经常会发现真正的模式问题agent并不能发现，agent发现的都是一些无关紧要的小问题，有些甚至都不是问题。

也有的人建立了一些skill来让agent更好的review代码。但是我们反过来想，是不是把这些规则直接放到项目的ABS(Agent Behavior Specification)文件中，让agent直接根据这些规则写出合规的代码，不就好了?

## 问题出在哪里

PR Code Review 这个行为在手写代码的时代非常有用。因为人手写代码经常犯错。别的程序员可以帮你看代码从而
- 发现你代码中的错误
- 通过看你的代码熟悉项目
- 发现你代码中的 code smell
- 发现你代码中不符合项目规范的地方

而对于 agent 来说：
- 按照目前agent写代码的水平，你几乎不可能发现低级错误
- agent 不需要看某个 PR 来熟悉项目
- code smell 问题 agent 看不出来
- 如果你做的好，可以让 agent 加载项目规范，就没有不合规的问题

我经常说 agent 写出来的代码没有小问题，只有大问题。
我观察到两个现象：
- 项目从多人维护慢慢转为单人维护单项目。这样的话很难review别人的代码，因为跨项目review需要的上下文不具备。
- agent写的PR越来越大。当PR大到一定程度的时候，review也变成了不可能的任务

## 新的审核

所以我认为在AI时代我们的审核方式需要革命性的改变。具体有以下的改变。
### 新的时间点

以前 Review PR的一个好处就是，人跟人之间的信息是不共享的，思维方式也不一样。所以一个人可能可以发现另外一个人的问题。这个问题在agent coding的场景下几乎不存在。所以review别人的PR意义并不大。

但是不是说不需要review了。而是我们应该尽量在代码**还未被commit的时候review**。review的时间节点改变了。我们应该在把agent写出的意大利面式的代码推送到repo之前喊停，避免大量的无用代码被推送到服务器，并浪费别的engineer的注意力。

有人说这不是废话吗？agent写完代码我肯定会看一眼。还真不是。因为你会发现agent有时候会说帮你写完代码后自动就commit&push了。你需要显式的叫停agent，不让它自动commit&push。可以通过设置提交锁和hook来实现。

我自己是建立了一套标准，让agent写完代码后生成一个临时的**提交锁**文件，名叫CR(commit request)，并在agent的hook中增加检测CR的行为。如果该提交锁文件存在，则拒绝commit。CR文件必须是你自己手动删掉的，或者通过一套标准删掉。我自己是设置了规则，只有我说approve的时候agent才会删掉CR文件，并提交代码。
### 新的标准

在AI时代，review代码的重点应该从发现代码的小错误转变为：
- 看是否有code smell
- 看是否过度设计
- 看是否有跟项目风格不统一的实现
- 看是否符合需求
- 新的关注点：**看这个PR是否过大**

最后一个关注点是随着agent写代码后产生的。一个过大的PR本身就是一个问题。如果这个PR大到上千行，并且不能被精简。那么说明这个task过大了。应该被拆分成多个可被检验的小task，分步实现。一个PR不应该大到不可被review。如果这样的话这本身也是一个code smell。

一个合理的PR应该是只关注一件事情，而且这件事情虽然代码可能多，但是核心的思路应该是简单，容易理解的。比如你批量修改了某个符合固定模式的代码，虽然代码多，但是你可以很容易的看出其重复的部分。人脑会跳过这些重复的代码。它们并不会对你的思维造成负担，分散你的注意力。

### 新的动作

**阅读变为询问**：以前review的时候是我们自己去一行一行的看代码。现在我们应该努力的多问agent的代码意图和设计。通过不停的问来让你快速理解代码。我发现经常在问的过程中agent自己也会发现问题所在。

**改代码改为改规则**：当review发现了agent写的代码的问题之后，我们并不应该手动的去修改代码。因为就算你改了这一次，下一次agent依然会犯同样的错误。我们应该指示agent去修改代码。然后指示agent去修改规则文档。我把这些规则文档称之为ABS(Agent Behavior Specification)。比如 CLAUDE.md, BEST_PRACTICE.md, 等

![改代码改为改规则](https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/2026/07/code-review-in-the-ai-era-from-review-to-audit/cn/02.png)

### 新的频次

以前我们每个PR都要有人approve才能merge。由于现在的情况变了：
- 单人项目增多
- agent产出效率高于人工审核
- agent对于类似需求可以根据规则重复的做出相同质量的代码

所以我们不需要在整个项目的整个周期中review每一次的代码改动。而是转为：
- 项目初期review所有的代码改动，并逐渐建立规则库
- 项目中后期对于简单需求的代码改动可以skip review，但是设置阈值。当skip review的次数达到阈值后，人工review观察是否需要完善规则

## 新的名字：代码审计

这种新的review方式具有以下特点：
- 在项目初期完整审核，在项目转为大型项目后抽检
- 重要的不是保证代码的正确，而是保证写代码的方式的合规

这很像财务审计。所以我觉得新的项目代码审核方式应该叫代码审计更合适。

![从审核到审计](https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/2026/07/code-review-in-the-ai-era-from-review-to-audit/cn/03.png)

---

## 关于作者

我是代码Plato。

我相信，人类的创造力才是 AI Coding 的真实之树，而代码与模型不过是投射在洞穴墙上的影子。

微博：@代码Plato
主页：https://weibo.com/u/1041257881
