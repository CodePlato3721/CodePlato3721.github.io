---
name: juejin-publish-metadata
description: 为指定的中文博客文章生成掘金发布所需的元数据文件
trigger: "发布到掘金" 或 "生成掘金元数据"
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
- `image`：封面图 URL
- `categories`：收录至专栏的值

### 3. 生成文章摘要

阅读文章正文，写一段 **100 字以内**的中文摘要，概括核心主题和主要观点。

### 4. 准备输出目录

确保 `~/.blog-workspace/juejin/` 目录存在（不存在则新建）。

### 5. 写出元数据文件

将以下内容写入 `~/.blog-workspace/juejin/元数据.md`：

```markdown
# 编辑摘要
{100 字以内的摘要}

# 收录至专栏
{categories 的值}
```

### 6. 准备封面图

检查 `~/.blog-workspace/cn-banner.png` 是否已存在：

- **已存在**：直接使用，无需下载。
- **不存在**：从文章 `image` 字段的 URL 下载，保存为 `~/.blog-workspace/cn-banner.png`。

使用 PowerShell：
```powershell
$bannerPath = "$env:USERPROFILE\.blog-workspace\cn-banner.png"
if (-not (Test-Path $bannerPath)) {
    Invoke-WebRequest -Uri "{image_url}" -OutFile $bannerPath
}
```

### 7. 确认输出

列出 `~/.blog-workspace/` 的内容，确认 `元数据.md`（在 `juejin/` 下）和 `cn-banner.png` 均已就绪。
