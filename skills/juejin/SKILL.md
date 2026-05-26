---
name: juejin-publish
description: 为指定的中文博客文章生成掘金发布所需的元数据文件
trigger: "发布到掘金"
---

## 目标

为一篇中文博客文章生成掘金发布所需的元数据，输出到 `~/.blog-workspace/juejin/` 目录。

## 步骤

### 1. 找到文章文件

根据文章标题，定位中文文章文件：
```
content/zh/post/{zh-dir}/index.md
```
`zh-dir` 是文章标题的目录名（把 Windows 禁止字符替换为 `-`，其余保持中文原文）。

### 2. 读取 frontmatter

从文章文件中提取：
- `title`：中文标题
- `categories`：收录至专栏的值

### 3. 生成文章摘要

阅读文章正文，写一段 **100 字以内**的中文摘要，概括核心主题和主要观点。

### 4. 准备输出目录

确保 `~/.blog-workspace/juejin/` 目录存在（不存在则新建）。

### 5. 写出元数据文件

将以下内容写入 `~/.blog-workspace/juejin/元数据.md`：

```markdown
# 中文标题
{title 的值}

# 编辑摘要
{100 字以内的摘要}

# 收录至专栏
{categories 的值}
```

### 6. 复制封面图

将 `~/.blog-workspace/draft/cn-banner.png` 复制到 `~/.blog-workspace/juejin/cn-banner.png`：

```powershell
Copy-Item "$env:USERPROFILE\.blog-workspace\draft\cn-banner.png" `
          "$env:USERPROFILE\.blog-workspace\juejin\cn-banner.png"
```

### 7. 确认输出

列出 `~/.blog-workspace/juejin/`，确认 `元数据.md` 和 `cn-banner.png` 均已就绪。
