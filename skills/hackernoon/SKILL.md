---
name: hackernoon-prepare
description: 将英文博客文章的 banner 和插图下载到 ~/.blog-workspace，并生成 HackerNoon 发布所需的元数据文件
trigger: "发布文章 <文章名> 到 hackernoon"
---

## 目标

将指定英文文章的 banner 和正文插图从 R2 下载到 `~/.blog-workspace/`，文件名使用 `en-` 前缀；并在 `~/.blog-workspace/hackernoon/` 下生成包含发布元数据的 `metadata.md`。

## 步骤

### 1. 找到文章文件

根据触发短语中的文章名，定位英文文章文件：

```
content/en/post/{en-slug}/index.md
```

`en-slug` 由文章标题转 kebab-case 得到。

### 2. 读取图片 URL

从文章文件中提取：

- **banner URL**：frontmatter 中 `image` 字段的值
- **插图 URL**：正文中所有 `![...](url)` 的 URL（排除与 banner 相同的 URL）

### 3. 下载 banner

将 banner 下载到：

```
~/.blog-workspace/en-banner.png
```

```powershell
Invoke-WebRequest -Uri "{banner_url}" -OutFile "$env:USERPROFILE\.blog-workspace\en-banner.png"
```

### 4. 下载插图

对正文中每张插图，提取 URL 最后一段文件名（如 `01.png`），去掉扩展名后加前缀 `en-image-`，得到目标文件名（如 `en-image-01.png`）。

下载到 `~/.blog-workspace/`：

```powershell
$ws = "$env:USERPROFILE\.blog-workspace"
Invoke-WebRequest -Uri "{img_url}" -OutFile "$ws\en-image-{原始文件名去扩展名}.{扩展名}"
```

### 5. 生成元数据文件

阅读文章正文，生成以下内容：

- **Metadescription**：160 字符以内的英文描述，概括文章核心主题，适合作为 SEO meta description
- **TL;DR**：3~5 句话的英文摘要，让读者快速了解文章的核心观点和结论

确保 `~/.blog-workspace/hackernoon/` 目录存在：

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.blog-workspace\hackernoon" | Out-Null
```

将元数据写入 `~/.blog-workspace/hackernoon/metadata.md`：

```markdown
## Metadescription

{生成的 metadescription，160 字符以内}

## TL;DR

{生成的 TL;DR}
```

### 6. 确认输出

列出 `~/.blog-workspace/` 中所有 `en-*` 文件，确认下载完整：

```powershell
Get-ChildItem "$env:USERPROFILE\.blog-workspace" -File | Where-Object { $_.Name -like "en-*" } | Select-Object Name, @{N='Size(KB)';E={[math]::Round($_.Length/1KB,1)}}
```

告知用户：
- 已下载的文件列表及大小
- metadata.md 路径
- 下一步建议（如：打开 HackerNoon 编辑器，手动上传图片后替换正文中的图片链接）
