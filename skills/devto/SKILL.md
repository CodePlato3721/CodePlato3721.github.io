---
name: devto-publish
description: 从 draft/<代号>/en-article.md 生成并发布英文文章到 dev.to
trigger: "发布devto:<draft代号>"
---

## 触发格式

```
发布devto:<代号>
```

例：`发布devto:0606tokenmaxxing`

触发后，从触发短语中提取 `<代号>`，所有文件路径均以 `draft/<代号>/` 为根目录。

## 前提

- `skills/.env` 中已设置 `DEVTO_API_KEY`

## 步骤

### 1. 读取草稿内容

从项目根目录读取以下文件：

- **`draft/<代号>/en-article.md`**：英文文章正文（含 `<en-image-XX>` 占位标签）
- **`draft/<代号>/metadata.md`**：提取：
  - `英文标题` → `en-title`
  - `英文分类` → `en-category`
  - `en-slug` = `en-title` 转 kebab-case（冒号及标点去掉或替换为 `-`）
  - `date` = 今天的日期，格式 `YYYY-MM-DD`
  - `YYYY/MM` = 从 date 拆出，用于 R2 路径
  - `# 图片路径` → `## 英文版` 表格中的所有占位符与 URL 对应关系

### 2. 替换图片占位符

将 `en-article.md` 正文中所有 `<en-image-XX>` 占位标签替换为对应的 Markdown 图片语法，URL 来自 `metadata.md` 的 **英文版** 图片路径表格：

```markdown
![](https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/{YYYY}/{MM}/{en-slug}/en/0N.png)
```

tags 根据文章内容自行判断，3～4 个英文标签（dev.to 最多 4 个）。

### 3. 准备输出目录

确保 `~/.blog-workspace/<代号>/devto/` 目录存在：

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.blog-workspace\<代号>\devto" | Out-Null
```

### 4. 写出草稿文件

将以下完整内容写入 `~/.blog-workspace/<代号>/devto/draft.md`：

```markdown
---
title: "{en-title}"
date: {date}
draft: false
image: {banner URL 或留空}
tags: ["Tag1", "Tag2", "Tag3"]
categories: ["{en-category}"]
---

{替换好图片 URL 的英文正文}
```

### 5. 运行发布脚本

在项目根目录下执行：

```powershell
skills\.venv\Scripts\python.exe skills\devto\scripts\devto.py "$env:USERPROFILE\.blog-workspace\<代号>\devto\draft.md"
```

### 6. 确认结果

脚本成功后会输出：
```
published: https://dev.to/...
```

如果报错，检查：
- `DEVTO_API_KEY` 是否正确设置
- `~/.blog-workspace/<代号>/devto/draft.md` 是否存在
- 文章 `draft` 字段是否为 `false`
