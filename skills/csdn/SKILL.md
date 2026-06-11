---
name: csdn-publish
description: 为草稿目录中的文章生成 CSDN 发布所需的元数据、文章草稿和封面图
trigger: "发布到 CSDN"
---

## 目标

直接从项目的 `draft/` 目录读取文章，生成 CSDN 发布所需的全部素材，输出到 `~/.blog-workspace/csdn/` 目录。

## 步骤

### 1. 读取草稿内容

从项目根目录读取以下文件：

- **`draft/metadata.md`**：提取：
  - `中文标题` → `zh-title`
  - `中文分类` → 分类专栏
  - 图片路径表（中文版占位符 → R2 URL）

### 2. 生成文章摘要

阅读文章正文，写一段 200 字以内的中文摘要，概括：
- 文章核心主题
- 主要内容/结构
- 核心观点或结论

### 3. 准备输出目录

确保 `~/.blog-workspace/csdn/` 目录存在（不存在则新建）。

### 4. 写出元数据文件

将以下内容写入 `~/.blog-workspace/csdn/metadata.md`：

```markdown
# 中文标题
{zh-title}

# 文章摘要
{生成的摘要}

# 分类专栏
{中文分类}
```

### 5. 制作文章

将 `draft/cn-article.md` 复制到 `~/.blog-workspace/csdn/article.md`：

```powershell
Copy-Item "draft\cn-article.md" "$env:USERPROFILE\.blog-workspace\csdn\article.md"
```

然后读取 `draft/metadata.md` 中"中文版"图片路径表，将 `csdn/article.md` 中的每个占位符（如 `<cn-image-01>`）替换为对应的 R2 图片 URL，格式为标准 Markdown 图片语法：

```markdown
![](https://...)
```

**重要：必须用 `[System.IO.File]` 显式指定 UTF-8 编码**，否则 PowerShell 5.1 的 `Get-Content` 默认用 ANSI 编码读取，导致中文乱码：

```powershell
$dst = "$env:USERPROFILE\.blog-workspace\csdn\article.md"
$article = [System.IO.File]::ReadAllText($dst, [System.Text.Encoding]::UTF8)
$article = $article -replace [regex]::Escape("<cn-image-01>"), "![](https://...)"
# 以此类推，对每个占位符执行替换
[System.IO.File]::WriteAllText($dst, $article, (New-Object System.Text.UTF8Encoding $false))
```

替换完成后，确认文件中不再存在 `<cn-image-` 开头的占位符。

**添加原文链接**

扫描 `content/zh/post/` 下的子目录，找到 `index.md` 的 `title` 与 `zh-title` 匹配的目录，取其目录名作为 `zh-dir`，构造 URL：

```powershell
$zhTitle = "{zh-title}"
$zhDir = Get-ChildItem "content\zh\post" -Directory | Where-Object {
    $idx = Join-Path $_.FullName "index.md"
    (Test-Path $idx) -and ([System.IO.File]::ReadAllText($idx, [System.Text.Encoding]::UTF8) -match [regex]::Escape($zhTitle))
} | Select-Object -ExpandProperty Name -First 1
$url = "https://CodePlato3721.github.io/zh/post/$zhDir/"
```

在 `article.md` 末尾追加该链接（与正文之间空一行）：

```powershell
$dst = "$env:USERPROFILE\.blog-workspace\csdn\article.md"
$article = [System.IO.File]::ReadAllText($dst, [System.Text.Encoding]::UTF8)
$article = $article.TrimEnd() + "`n`n原文：$url"
[System.IO.File]::WriteAllText($dst, $article, (New-Object System.Text.UTF8Encoding $false))
```

### 6. 复制封面图

将 `draft/cn-banner.png` 复制到 `~/.blog-workspace/csdn/banner.png`：

```powershell
Copy-Item "draft\cn-banner.png" "$env:USERPROFILE\.blog-workspace\csdn\banner.png"
```

### 7. 确认输出

列出 `~/.blog-workspace/csdn/`，确认 `metadata.md`、`article.md`、`banner.png` 均已就绪。
