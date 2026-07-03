---
name: juejin-publish
description: 为草稿目录中的文章生成掘金发布所需的元数据和简化版草稿
trigger: "发布juejin:<代号>"
---

## 触发格式

```
发布juejin:<代号>
```

触发后，从触发短语中提取 `<代号>`，所有文件路径均以 `draft/<代号>/` 为根目录。

## 目标

直接从项目的 `draft/<代号>/` 目录读取文章，生成掘金发布所需的全部素材，输出到 `~/.blog-workspace/<代号>/juejin/` 目录。

## 步骤

### 1. 读取草稿内容

从项目根目录读取以下文件：

- **`draft/<代号>/metadata.md`**：提取：
  - `中文标题` → `zh-title`
  - `中文分类` → 收录至专栏

### 2. 生成文章摘要

阅读文章正文，写一段 **100 字以内**的中文摘要，概括核心主题和主要观点。

### 3. 准备输出目录

确保 `~/.blog-workspace/<代号>/juejin/` 目录存在（不存在则新建）：

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.blog-workspace\<代号>\juejin" | Out-Null
```

### 4. 写出元数据文件

将以下内容写入 `~/.blog-workspace/<代号>/juejin/metadata.md`：

```markdown
# 中文标题
{zh-title}

# 编辑摘要
{100 字以内的摘要}

# 收录至专栏
{中文分类}
```

### 5. 制作文章

将 `draft/<代号>/cn-article.md` 复制并改名为 `~/.blog-workspace/<代号>/juejin/article.md`：

```powershell
Copy-Item "draft\<代号>\cn-article.md" "$env:USERPROFILE\.blog-workspace\<代号>\juejin\article.md"
```

然后读取 `draft/<代号>/metadata.md` 中 **`## 中文版`** 表格，将 `article.md` 中的图片占位符替换为对应的 R2 URL。

表格格式为 `| 占位符 | R2 URL |`，例如：

| 占位符 | R2 URL |
|--------|--------|
| `<cn-image-01>` | https://... |

对表格中每一行（跳过标题行和分隔行），提取占位符和 URL，使用 PowerShell 逐一替换。

**重要：必须用 `[System.IO.File]` 显式指定 UTF-8 编码**，否则 PowerShell 5.1 的 `Get-Content` 默认用 ANSI 编码读取，导致中文乱码：

```powershell
$dst = "$env:USERPROFILE\.blog-workspace\<代号>\juejin\article.md"
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

在 `article.md` 末尾追加原文链接和结尾签名：

```powershell
$dst = "$env:USERPROFILE\.blog-workspace\<代号>\juejin\article.md"
$article = [System.IO.File]::ReadAllText($dst, [System.Text.Encoding]::UTF8)
$footer = "`n`n---`n`n## 关于作者`n`n我是代码Plato。`n`n我相信，人类的创造力才是 AI Coding 的真实之树，而代码与模型不过是投射在洞穴墙上的影子。`n`n微博：@代码Plato`n主页：https://weibo.com/u/1041257881"
$article = $article.TrimEnd() + "`n`n原文：$url" + $footer
[System.IO.File]::WriteAllText($dst, $article, (New-Object System.Text.UTF8Encoding $false))
```


### 6. 复制封面图

将 `draft/<代号>/cn-banner.png` 复制到 `~/.blog-workspace/<代号>/juejin/banner.png`：

```powershell
Copy-Item "draft\<代号>\cn-banner.png" "$env:USERPROFILE\.blog-workspace\<代号>\juejin\banner.png"
```

### 7. 确认输出

列出 `~/.blog-workspace/<代号>/juejin/`，确认 `metadata.md`、`article.md`、`banner.png` 均已就绪。
