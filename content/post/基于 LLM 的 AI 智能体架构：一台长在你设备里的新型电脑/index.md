---
title: "基于 LLM 的 AI 智能体架构：一台长在你设备里的新型电脑"
date: 2026-05-05
draft: false

image: https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/2026/05/llm-agent-architecture-a-new-kind-of-personal-computer/cn/banner.png

tags:
  - AI
  - LLM
  - Agent
  - Architecture
---

# 基于 LLM 的 AI 智能体架构：一台长在你设备里的新型电脑

过去，我们一直把 AI 理解成一个“聊天机器人”。

但如果从系统架构角度重新观察，会发现未来真正成熟的 AI 智能体，更像是一台安装在你设备里的新型个人电脑。

它拥有：

- 计算核心
- 内存
- 文件系统
- 软件系统
- 输入输出设备
- 长期存储

只是：

它的核心不再是传统 CPU，而是 LLM。

---

# 一、LLM 引擎：没有记忆的“CPU”

LLM 本身其实没有长期记忆。

它更像一个推理引擎：

1. 接收输入
2. 读取上下文
3. 进行推理
4. 输出结果
5. 然后“失忆”

它无法天然记住过去发生的事情。

因此：

> LLM 本身更像 CPU，而不是完整的智能体。

它只负责计算。

真正让 AI “看起来认识你”的，是外部为它提供的上下文。

![LLM CPU](https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/2026/05/llm-agent-architecture-a-new-kind-of-personal-computer/cn/01_llm_cpu.png)

---

# 二、上下文：AI 智能体的内存

如果 LLM 是 CPU，  
那么 Context（上下文）就是 AI 的内存。

而这个内存，其实应该分成两层。

---

## 1. 全局上下文（Global Context）

这一层属于整个智能体。

它记录：

- 用户偏好
- 长期目标
- 常用习惯
- 人格设定
- 长期规则
- 历史知识

例如：

- “用户喜欢 Markdown”
- “用户正在学习 AI Agent”
- “用户习惯使用中文写作”

这些信息会长期影响智能体行为。

---

## 2. 会话上下文（Session Context）

这一层只属于当前对话。

例如：

- 当前正在讨论的话题
- 当前文章结构
- 最近几轮对话
- 临时推理结果

它更像程序运行时的临时内存。

---

## 上下文窗口，本质上是“内存限制”

LLM 的 Context Window 并不是无限的。

这意味着：

- 历史不能无限累积
- 信息会越来越贵
- 超过限制后必须被压缩

于是：

智能体必须像操作系统一样管理内存：

- 压缩历史
- 总结摘要
- 清理低优先级信息
- 转移长期信息
- 动态加载需要的数据

因此：

> Context Window 本质上就是 AI 的内存容量。

![Context Memory](https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/2026/05/llm-agent-architecture-a-new-kind-of-personal-computer/cn/02_context_memory.png)

---

# 三、Markdown 文件：智能体的硬盘

长期数据不应该一直放在上下文里。

否则：

- 成本会越来越高
- 推理速度会下降
- Context 会迅速膨胀

因此：

> 长期记忆应该存在文件系统中。

而一种非常自然的形式，就是 Markdown 文件。

例如：

- 笔记
- 项目资料
- 日记
- 世界观
- 用户档案
- 写作素材
- 长期知识库

都可以直接存成 Markdown。

这意味着：

| 传统电脑 | AI 智能体 |
|---|---|
| 硬盘 | Markdown 文件系统 |

Markdown 有一个巨大优势：

> 它既能被 AI 阅读，也能被人类直接阅读。

因此：

- 人类可以编辑
- AI 可以处理
- Git 可以版本管理
- 文件可以同步
- 即使脱离 AI 依然存在

这会形成一种：

> “人与 AI 共用的知识空间”。

![Markdown Storage](https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/2026/05/llm-agent-architecture-a-new-kind-of-personal-computer/cn/03_markdown_storage.png)

---

# 四、Skill：安装在 AI 上的软件

未来的 AI 智能体，不会只有“知识”。

它还会拥有“技能”。

例如：

- 写作 Skill
- 编程 Skill
- 视频剪辑 Skill
- 数据分析 Skill
- 项目管理 Skill

这些 Skill 可能由：

- Prompt
- 工作流
- Python 代码
- MCP 配置
- Tool 调用规则

共同组成。

它们就像：

> 安装在 AI 身上的软件。

因此：

| 传统电脑 | AI 智能体 |
|---|---|
| 软件 / App | Skill |

Skill 可以：

- 安装
- 卸载
- 更新
- 共享
- 组合

未来甚至可能出现：

- Skill Store
- Skill Marketplace
- 开源 Skill 社区

![Skill Software](https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/2026/05/llm-agent-architecture-a-new-kind-of-personal-computer/cn/04_skill_software.png)

---

# 五、输入输出：不只是文字

传统聊天机器人最大的误导之一，是大家以为 AI 只有文字交互。

实际上未来的 AI 智能体，会拥有完整的多模态输入输出系统。

## 输入

AI 可以读取：

- 文字
- 语音
- 图片
- 视频
- 摄像头
- 文件
- 屏幕内容
- 设备状态

## 输出

AI 可以生成：

- 文本
- 语音
- 图像
- 视频
- 自动化操作
- 控制指令

因此：

> AI 智能体本质上是一种新的交互层。

![Multimodal IO](https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/2026/05/llm-agent-architecture-a-new-kind-of-personal-computer/cn/05_multimodal_io.png)

---

# 电脑整机：一种“类冯诺依曼结构”的 AI 计算机

如果把整个架构放在一起：

| 传统计算机 | AI 智能体 |
|---|---|
| CPU | LLM 引擎 |
| 内存 | Context |
| 硬盘 | Markdown 文件系统 |
| 软件 | Skill |
| 输入设备 | 多模态输入 |
| 输出设备 | 多模态输出 |

你会发现：

它已经越来越像一台真正的计算机。

只是：

这台计算机不是围绕 GUI 构建的。

而是围绕：

> “语言理解与推理”

构建的。

![AI Computer Architecture](https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/2026/05/llm-agent-architecture-a-new-kind-of-personal-computer/cn/06_ai_computer_architecture.png)

---

# 操作系统：个人 AI 操作系统

未来每个人设备中，都可能长期存在一个 AI Agent。

它：

- 理解你
- 记住你
- 帮助你工作
- 管理你的知识
- 调度你的 Skills
- 操作你的设备
- 与你长期共同成长

那时：

我们使用的可能不再只是：

- Windows
- macOS
- Android

而是：

> 一个以 LLM 为核心的新型个人 AI 操作系统。

而今天的聊天框，

可能只是这个新时代最早期的雏形。

![Personal AI OS](https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/2026/05/llm-agent-architecture-a-new-kind-of-personal-computer/cn/07_personal_ai_os.png)

---

# 参考资料

1. Park, Joon Sung et al.  
   **MemGPT: Towards LLMs as Operating Systems**  
   arXiv:2310.08560  
   https://arxiv.org/abs/2310.08560

2. Wang, Lei et al.  
   **LLM as OS, Agents as Apps: Envisioning AIOS, Agents and the AIOS-Agent Ecosystem**  
   arXiv:2312.03815  
   https://arxiv.org/abs/2312.03815