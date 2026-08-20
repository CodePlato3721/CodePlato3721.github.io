---
title: "如何在Agent之间迁移记忆"
date: 2026-08-19
draft: false
image: https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/2026/08/how-to-migrate-memory-between-agents/cn/banner.png
tags: ["AI", "Agent", "记忆管理", "方法论"]
categories: ["AI 方法论"]
---

## 问题

有的时候我们希望能把正在使用的 agent 的记忆转移到另外一个 agent 上。有可能是以下的情况：

- agent 出问题了，但是不知道问题出在哪里，我们希望通过重装解决问题
    
- 这个 agent 的 token 用完了，想临时用另外一个 agent 顶上
    
- 不想使用这个 agent 了，想换一个 agent 使用
    

我搜索了市面上的解决方案，发现并没有一个统一的 agent 之间导入导出的方案。但是也不是完全没有办法。这是目前已知的方法。

## 解决方案

### 外挂式记忆

使用 agentmemory、ai-memory 等外挂记忆工具，原理是 agent 本身不持有记忆，记忆完全托管在第三方存储（如 Mem0、Zep）里。agent 每次工作时，从这个外部存储里读取相关记忆注入上下文，产生新记忆时再写回存储——agent 只是这份记忆的"读写客户端"，不是"记忆的所有者"。换一个 agent，只要它也接同一个存储，就能读到同一份记忆，不需要导入导出，因为记忆压根没跟着某个 agent 走。

### agent 的 backup 工具

同一个产品重装或者转移，使用各家自己的 backup 工具。比如 OpenClaw 可以用 [Backup](https://docs.openclaw.ai/cli/backup) 工具。如果使用 OpenClaw，你可以先 backup，然后再 restore。

```
# 1. 停止 gateway，备份并验证
openclaw gateway stop
openclaw backup create --output ~/Backups/openclaw --verify

# 2. 卸载/重装
# （原地重装场景通常不需要 openclaw uninstall，直接覆盖装新版即可；
#   如果是"删除重装"，重装完让它先生成一个全新的 ~/.openclaw，反正下一步会覆盖）

# 3. 恢复到一个全新的暂存目录（不是原地！）
openclaw backup restore <archive.tar.gz> --target ~/openclaw-restored

# 4. 手动把 manifest.json 里记录的内容挪到实际生效路径
#    或者直接把 OPENCLAW_STATE_DIR 指向这个恢复出来的目录

# 5. 跑体检 + 重启
openclaw doctor
openclaw gateway restart
openclaw status
```

### agent 的 migrate 工具

如果你想换一个 agent 使用，你可以到**目标** agent 的官网页面上找这个 agent 的 migrate/import from 页面。比如你想从 Hermes Agent 换到 OpenClaw，就可以用 [Migrate from OpenClaw](https://docs.openclaw.ai/install/migrating-hermes) 提供的工具。

```
# 1. 先干跑，看看会导入哪些东西
hermes claw migrate --dry-run

# 2. 确认没问题后正式迁移（默认不带密钥，只导入用户数据/配置）
hermes claw migrate

# 如果要连 API key、TTS 密钥一起带走，必须显式加这个参数
# （--preset full 本身也不会自动带密钥）
hermes claw migrate --preset full --migrate-secrets

# 3. 迁移完，重新拉起消息服务让新配置生效
systemctl --user restart hermes-gateway

# 4. WhatsApp 是二维码配对机制，不在迁移范围内，需要单独重新配对
hermes whatsapp

# 5. 确认没问题后，清理旧目录（重命名为 .pre-migration/，不是删除）
hermes claw cleanup
```

### Agent app 导出工具

如果你的 agent 并不是 OpenClaw、Hermes Agent 这种常驻自主 Agent，也不是 Claude Code 之类的编码 Agent，而是纯聊天类产品（桌面版 Claude、手机端 ChatGPT），这些产品通常没有"agent 状态"可迁移的概念，只能通过账号自带的数据导出功能拿到**对话历史存档**（比如 ChatGPT 的"设置 → 数据控制 → 导出数据"，导出结果会发到注册邮箱）。

虽然这个结果不能直接被另外一个 agent 复用，比如 ChatGPT 会生成 `conversations.json`，但是这个文件很复杂，是一个树状结构。不过信息都在里面。你可以使用另外一个 agent 去写一段脚本来将有用的信息提取出来。

### 指示 agent 导出上下文

如果完全没有官方导出功能，可以直接跟 agent 说："请把你对我的了解——偏好、习惯、背景信息、工作方式——整理成一份结构化 Markdown 文档输出给我"，也可以指定针对某个具体项目。

这份文档是 agent **当场从当前对话窗口里现场总结出来的**，不是从某个持久记忆库里查出来的完整备份——如果对话很长、早期内容已经被压缩掉，或者信息分散在多个不同的历史对话里，这份总结就覆盖不到那些部分。

这个方法的优势是**快**（不用等官方导出的处理时间，比如 ChatGPT 可能要等数天），但是缺点就是不全。

---

## 关于作者

我是代码Plato。

我相信，人类的创造力才是 AI Coding 的真实之树，而代码与模型不过是投射在洞穴墙上的影子。

微博：@代码Plato
主页：https://weibo.com/u/1041257881
