---
name: devto-publish
description: 直接从草稿目录翻译并发布英文文章到 dev.to
trigger: "发布到 dev.to"
---

## 目标

直接从项目的 `draft/` 目录读取文章，翻译为英文，生成可发布的 Markdown 文件，并调用 `scripts/devto.py` 发布到 dev.to。

## 前提

- `skills/.env` 中已设置 `DEVTO_API_KEY`

## 步骤

### 1. 读取草稿内容

从项目根目录读取以下文件：

- **`draft/article.md`**：文章正文（中文）
- **`draft/metadata.md`**：提取：
  - `英文标题` → `en-title`
  - `英文分类` → `en-category`
  - `en-slug` = `en-title` 转 kebab-case（冒号及标点去掉或替换为 `-`）
  - `date` = 今天的日期，格式 `YYYY-MM-DD`
  - `YYYY/MM` = 从 date 拆出，用于 R2 路径

### 2. 上传英文 Banner

将 `draft/en-banner.png` 上传到 R2：

```powershell
npx wrangler r2 object put "codeplato-images/{YYYY}/{MM}/{en-slug}/en/banner.png" `
  --file "draft\en-banner.png" `
  --content-type "image/png" `
  --remote
```

Banner URL：`https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/{YYYY}/{MM}/{en-slug}/en/banner.png`

如果 `draft/en-banner.png` 不存在，跳过此步骤，image 字段留空。

### 3. 上传英文内联图片

扫描 `draft/en-image-*.png`，对每张图片：

```powershell
npx wrangler r2 object put "codeplato-images/{YYYY}/{MM}/{en-slug}/en/0N.png" `
  --file "draft\en-image-0N.png" `
  --content-type "image/png" `
  --remote
```

URL：`https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/{YYYY}/{MM}/{en-slug}/en/0N.png`

如果没有插图，跳过此步骤。

### 4. 翻译并生成英文文章

根据 `draft/article.md` 撰写完整的英文文章正文：
- 语言地道、流畅，符合英文博客文体
- 将正文中所有 `<en-image-XX>` 占位标签替换为对应的 Markdown 图片语法

tags 根据文章内容自行判断，3～4 个英文标签（dev.to 最多 4 个）。

### 5. 准备输出目录

确保 `~/.blog-workspace/devto/` 目录存在：

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.blog-workspace\devto" | Out-Null
```

### 6. 写出草稿文件

将以下完整内容写入 `~/.blog-workspace/devto/draft.md`：

```markdown
---
title: "{en-title}"
date: {date}
draft: false
image: {banner URL 或留空}
tags: ["Tag1", "Tag2", "Tag3"]
categories: ["{en-category}"]
---

{英文正文}
```

### 7. 运行发布脚本

在项目根目录下执行：

```powershell
skills\.venv\Scripts\python.exe skills\devto\scripts\devto.py "$env:USERPROFILE\.blog-workspace\devto\draft.md"
```

### 8. 确认结果

脚本成功后会输出：
```
published: https://dev.to/...
```

如果报错，检查：
- `DEVTO_API_KEY` 是否正确设置
- `~/.blog-workspace/devto/draft.md` 是否存在
- 文章 `draft` 字段是否为 `false`
