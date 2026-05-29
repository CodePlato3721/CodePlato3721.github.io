---
title: "Agent Skill 制作手册 01：入门篇"
date: 2026-05-28
draft: false
image: https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/2026/05/agent-skill-handbook-01-getting-started/banner.png
tags: ["Agent", "Skill", "LLM", "Claude Code", "提示词工程"]
categories: ["AI Skill 开发手册"]
---

Agent Skill 制作手册是一个系列教程。这是第一篇。

## 什么是 skill

很多程序员问，Agent Skill 是什么？我敢说，Agent Skill 是你们学习编程以来能学到的最简单的技术之一。

### skill 是怎么发展出来的

就像跟人一起工作一样。你有一个新入职的同事，就算他技术再好，也总要先看一些你们公司的 how to 文档，才能开始做事。人们发现，跟 LLM 工作也有同样的模式。你让 LLM 直接做事情，那多半会做出一件偏离你预期的漂亮事，这就很尴尬了。

然后就有人发现，如果先在提示词里面加上做事情的步骤，LLM 就做得好。所以大家就一直给 LLM 喂 how to 手册。

但是 LLM 的上下文有限啊，而且你每次塞这么多上下文，你的钱包先爆了。于是人们又想，其实我们自己工作的时候也记不住 how to 的内容。我们大概记得有那么个 how to 教了我做这件事情，但具体内容不记得了。没关系啊，我们到时候再去 wiki 看看不就得了。那我们也可以让 LLM 只记住这个 how to 是做什么的，具体需要的时候再看呗。于是我们可以把每一个 how to 的描述喂给 LLM，LLM 看描述就知道，需要做事情的时候要找哪个 how to 了。

到这里，我们已经可以推导出一个简单的、给 LLM 量身定做的 how to 了。它只有两个重要属性：`name` 和 `description`，剩下的就是正文了。每次加载只加载 `name` 和 `description`，LLM 自己会判断是否需要读取这个 how to 的正文。

![skill 结构示意图](https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/2026/05/agent-skill-handbook-01-getting-started/01.png)

这就是 skill。其实这个东西叫什么不重要，它可以叫 howto、guide、manual 都可以，但是大家觉得 skill 这个名字够短、好记，还自解释，就用它了。可能在别的平行宇宙里，它叫 guide。

### skill 是哪家的？

这种 `SKILL.md` 形态的 Agent Skill，最早是 Anthropic 系统公开推广的；但 skill 这个词和"让 AI 学技能"的思想并不属于某家公司。OpenAI、OpenClaw、Hermes Agent 都有自己实现的 skill。这只是一个概念，各家有各家自己的实现，这些实现在细节上有些区别，但都是指同一个事情。

## 怎么写 skill

### skill 通用规范

各家的 skill 规范的共同点是：skill 是一个文件夹。结构是：

```text
my-skill/
  SKILL.md        # 必须：元数据 + 指令
  scripts/        # 可选：可执行脚本
  references/     # 可选：文档、说明、规范
```

而其中的 `scripts`、`references` 都不是必须的，只是大家习惯的一种最佳实践而已。最重要的是 `SKILL.md`。有的 skill 只有这一个文件，而这个文件的结构也很简单。

一个最小的 `SKILL.md`，在元数据层面只需要 `name` 和 `description`。正文可以很短，但最好写清楚 agent 被触发后到底要做什么。

```yaml
---
name: skill的名字
description: 解释这个skill是干嘛的，什么时候应该被触发，什么时候不应该被触发等
---
```

当你的 skill 比较复杂，需要一些结构化的数据和逻辑的时候，就可以考虑建立 `scripts` 文件夹，然后在里面写代码。当你的 skill 引用的文档比较多，你怕把上下文给撑爆了，就可以把大部分文档移到 `references` 里面。

### 写一个 skill

来动手写一个 skill 吧。我保证这是你看到的最短的教程。这个 skill 会在你说三次 Hello 的时候回复三个 World。新建 `SKILL.md`，并在里面写：

```yaml
---
name: hello-world
description: 当用户说三次"Hello"（例如"Hello Hello Hello"）时，回复三次"World"："World World World"。
---

# Hello World

当用户的消息中包含恰好三个"Hello"时，只回复：

World World World

不说其他任何内容，只有这三个字。
```

然后安装到你的 AI agent 里面。你问我怎么安装？这都什么年代了，你问你自己的 AI agent 怎么安装，它自会告诉你的。

安装好后就试试吧。

## skill 规范

Codex、Claude Code、OpenClaw、Hermes Agent 它们都对 skill 有自己的一些细节上的规范，我就不在此赘述。不过有几点我觉得有必要提。

### Skill 防触发机制

基本上，是否触发 Skill 是看 LLM 自己决定的。这其实带来另外一个问题，就是 skill 经常被误触发，或者不被触发。对此各家都有各自的措施。

1. 禁止自动触发，但允许手动触发
   - Claude / OpenClaw: `disable-model-invocation: true`
   - Codex: `agents/openai.yaml` 里的 `allow_implicit_invocation: false`

2. 彻底禁用 skill
   - Codex: `[[skills.config]] enabled = false`
   - OpenClaw: `skills.entries.<skillKey>.enabled = false`

从这里可以看出，skill 的优点在于自由，但缺点也是自由。有时候你想触发，却触发不了；不想触发，它却一直被触发。不过在之后的教程中我会介绍一些范式来解决这个问题。

### Skill 的分类

在 skill 慢慢被越来越多的人使用后，skill 也开始出现一些分类方式。

**skill 和 command**

在 OpenClaw 和 Claude 桌面版中，skill 是可以用斜杠（`/`）调用的。区别在于，在 Claude 桌面版中，你安装了 Skill 后，按 `/` + `<skill名>` 就可以触发 skill；而在 OpenClaw 中，你是通过设置 `user-invocable: true` 来让这个 skill 可以用斜杠触发的。

在 OpenClaw 里，一部分 skill 可以被暴露成 slash command。command 是调用方式，不一定是独立分类。这就引发了一个有趣的思考：当你建立一个新 skill 的时候，你可以思考一下，你这个 skill 是一个普通的 skill，还是一个 command。毕竟在手机上找到斜杠，并不像在电脑上这样容易。有些生活类的 skill，你可以依赖 LLM 去猜测；而有些需要精确被触发的，就可以用斜杠。

**工作流式和应用式**

你会发现，有些 skill 仅仅只是定义了一件事情该怎么做，而有些 skill 更像是一个你自己定义的 app。定义了该怎么做的，可以被称为工作流式。

- 比如你让 LLM 帮你归纳一下会议纪要。这样的 skill 就只需要 `SKILL.md` 就够了。如果流程比较复杂，那就把流程抽取到 `references` 里面。
- 如果是应用式的，比如你要做一个购物清单，你需要比较复杂的逻辑和比较规范的数据存储。你就需要将某些逻辑抽取出来写成 `scripts`。但是 `scripts` 不是越多越好，只有需要确定性行为或外部工具时才用 `scripts`。

![skill 分类示意图](https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/2026/05/agent-skill-handbook-01-getting-started/02.png)
