---
name: hackernoon-prepare
description: 直接从草稿目录生成 HackerNoon 发布所需的元数据文件，并复制图片到工作区
trigger: "发布文章 <文章名> 到 hackernoon"
---

## 目标

直接从项目的 `draft/` 目录读取文章，生成 HackerNoon 发布所需的素材，输出到 `~/.blog-workspace/hackernoon/`。

## 步骤

### 1. 读取草稿内容

从项目根目录读取以下文件：

- **`draft/article.md`**：文章正文（中文）
- **`draft/metadata.md`**：提取：
  - `英文标题` → `en-title`
  - `en-slug` = `en-title` 转 kebab-case

### 2. 生成元数据

阅读文章正文（若为中文，翻译理解后生成英文），生成：

- **Metadescription**：160 字符以内的英文描述，概括文章核心主题，适合作为 SEO meta description
- **TL;DR**：2~3 句话的英文摘要，写成一个 paragraph，不分项，让读者快速了解文章的核心观点和结论

### 3. 准备输出目录

确保 `~/.blog-workspace/hackernoon/` 目录存在：

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.blog-workspace\hackernoon" | Out-Null
```

### 4. 写出元数据文件

将元数据写入 `~/.blog-workspace/hackernoon/metadata.md`：

```markdown
## Metadescription

{生成的 metadescription，160 字符以内}

## TL;DR

{生成的 TL;DR}
```

### 5. 复制 Banner

将 `draft/en-banner.png` 复制到 `~/.blog-workspace/hackernoon/en-banner.png`：

```powershell
Copy-Item "draft\en-banner.png" "$env:USERPROFILE\.blog-workspace\hackernoon\en-banner.png"
```

### 6. 复制插图

将 `draft/` 下所有 `en-image-*.png` 复制到 `~/.blog-workspace/hackernoon/`：

```powershell
Copy-Item "draft\en-image-*.png" "$env:USERPROFILE\.blog-workspace\hackernoon\"
```

如果没有 `en-image-*.png`，跳过此步骤。

### 7. 确认输出

列出 `~/.blog-workspace/hackernoon/` 中的文件，告知用户：
- metadata.md 路径
- 已复制的图片列表
- 下一步建议（打开 HackerNoon 编辑器，手动上传图片后替换正文中的图片链接）
