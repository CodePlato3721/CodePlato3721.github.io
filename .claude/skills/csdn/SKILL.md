---
name: csdn
description: 为草稿目录中的文章生成 CSDN 发布所需的元数据和草稿（图片占位符回填 R2 URL）。用户输入 "/csdn <代号>"、"发布csdn:<代号>" 或类似表述时使用。
---

## 调用方式

```
/csdn <代号>
```

例：`/csdn 0606tokenmaxxing`

`<代号>` 从 slash 命令参数中获取（也可用 "发布csdn:<代号>" 等自然语言触发），所有文件路径均以 `draft/<代号>/` 为根目录。

## 目标

直接从项目的 `draft/<代号>/` 目录读取文章，生成 CSDN 发布所需的元数据和草稿，输出到 `~/.blog-workspace/<代号>/csdn/` 目录。图片不复制到本地——草稿中直接使用 R2 公共 URL，CSDN 会自动抓取并转存到其图床。

## 步骤

### 1. 读取草稿内容

从项目根目录读取以下文件：

- **`draft/<代号>/metadata.md`**：提取：
  - `中文标题` → `zh-title`
  - `中文分类` → 分类专栏
  - `# 图片路径` → `## 中文版` 表格中的占位符与 R2 URL 对应关系（用于步骤 5 回填）

### 2. 生成文章摘要

阅读文章正文，写一段 200 字以内的中文摘要，概括：
- 文章核心主题
- 主要内容/结构
- 核心观点或结论

### 3. 准备输出目录

确保 `~/.blog-workspace/<代号>/csdn/` 目录存在（不存在则新建）：

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.blog-workspace\<代号>\csdn" | Out-Null
```

### 4. 写出元数据文件

将以下内容写入 `~/.blog-workspace/<代号>/csdn/metadata.md`：

```markdown
# 中文标题
{zh-title}

# 文章摘要
{生成的摘要}

# 分类专栏
{中文分类}
```

### 5. 制作文章

将 `draft/<代号>/cn-article.md` 复制到 `~/.blog-workspace/<代号>/csdn/article.md`：

```powershell
Copy-Item "draft\<代号>\cn-article.md" "$env:USERPROFILE\.blog-workspace\<代号>\csdn\article.md"
```

然后读取 `draft/<代号>/metadata.md` 中 `## 中文版` 表格，将 `article.md` 中的每个占位符（如 `<cn-image-01>`）替换为对应的 R2 图片 URL，格式为标准 Markdown 图片语法：

```markdown
![](https://...)
```

以此类推，将所有 `<cn-image-XX>` 替换为对应 R2 URL。

**追加结尾签名**

在 `article.md` 末尾追加以下固定内容：

```powershell
$dst = "$env:USERPROFILE\.blog-workspace\<代号>\csdn\article.md"
$article = [System.IO.File]::ReadAllText($dst, [System.Text.Encoding]::UTF8)
$footer = "`n`n---`n`n## 关于作者`n`n我是代码Plato。`n`n我相信，人类的创造力才是 AI Coding 的真实之树，而代码与模型不过是投射在洞穴墙上的影子。`n`n微博：@代码Plato`n主页：https://weibo.com/u/1041257881"
$article = $article.TrimEnd() + $footer
[System.IO.File]::WriteAllText($dst, $article, (New-Object System.Text.UTF8Encoding $false))
```

### 6. 复制封面图

将 `draft/<代号>/cn-banner.png` 复制到输出目录并重命名为 `banner.png`：

```powershell
Copy-Item "draft\<代号>\cn-banner.png" "$env:USERPROFILE\.blog-workspace\<代号>\csdn\banner.png"
```

### 7. 确认输出

列出 `~/.blog-workspace/<代号>/csdn/`，确认 `metadata.md`、`article.md`、`banner.png` 均已就绪。
