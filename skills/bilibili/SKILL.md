---
name: bilibili-prepare
description: 将中文博客文章的正文（去除 frontmatter）复制到 ~/.blog-workspace/bilibili/文章.md
trigger: "发布文章 <文章名> 到 bilibili"
---

## 目标

将指定中文文章的正文内容（去除 frontmatter 头部）输出到 `~/.blog-workspace/bilibili/文章.md`，供后续在 Bilibili 发布时使用。

## 步骤

### 1. 找到文章文件

根据触发短语中的文章名，定位中文文章文件：

```
content/zh/post/{zh-dir}/index.md
```

`zh-dir` 是文章标题的目录名（把 Windows 禁止字符替换为 `-`，其余保持中文原文）。

### 2. 读取文章，剥离 frontmatter

读取文件内容，去掉头部的 frontmatter 块。

frontmatter 是文件开头由两行 `---` 包裹的部分，例如：

```
---
title: "AI时代应该怎么写代码：督导和编排"
date: 2026-05-20
draft: false
image: https://...
tags: [...]
categories: [...]
---
```

取第二个 `---` 之后的所有内容作为正文，并去掉开头多余的空行。

### 3. 准备输出目录

确保 `~/.blog-workspace/bilibili/` 目录存在（不存在则新建）：

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.blog-workspace\bilibili"
```

### 4. 写出正文文件

将正文内容写入：

```
~/.blog-workspace/bilibili/文章.md
```

```powershell
$content = {正文内容}
Set-Content -Path "$env:USERPROFILE\.blog-workspace\bilibili\文章.md" -Value $content -Encoding utf8
```

### 5. 确认输出

告知用户：
- 输出文件路径
- 正文字数（大致）
- 下一步建议（如：打开文件、手动复制到 Bilibili 编辑器）
