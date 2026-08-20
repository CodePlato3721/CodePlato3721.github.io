# Blog Conventions

## Categories

All posts must use one of these categories (pick the best fit):

| 中文 | English |
|------|---------|
| AI 的日常使用手册 | Daily AI Usage |
| AI 工程开发手册 | AI Engineering |
| AI Skill 开发手册 | AI Skill Dev |
| AI 哲学 | AI Philosophy |
| AI 方法论 | AI Methodology |
| 软件哲学 | Software Philosophy |
| 随想 | Thoughts |

In frontmatter: use the Chinese name for `zh` posts, English name for `en` posts.

## Publishing Workflow

### Cloudflare R2 — Image Storage

Bucket: `codeplato-images`  
Public base URL: `https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/`  
Account ID: `deaa58408c878ef2c59ace4a70bf0346`  
Auth token: stored in `.Codex/settings.local.json`

**Key (path) conventions:**
- Banner: `{YYYY}/{MM}/{en-slug}/banner.png`
- Inline images: `{YYYY}/{MM}/{en-slug}/{filename}.png` (e.g. `01.png`, `02_diagram.png`)
- Chinese-specific language subdirectory (`cn/`) is **not required** — newer posts omit it and put all images directly under `{en-slug}/`

**Upload command (always add `--remote`):**
```powershell
cd "c:\Users\alexx\Workspace\CodePlato3721.github.io"
npx wrangler r2 object put codeplato-images/{YYYY}/{MM}/{en-slug}/banner.png `
  --file "C:\path\to\banner.png" `
  --content-type "image/png" `
  --remote
```

Do **not** commit images to git.

### Post file structure

**Hugo** static site. Language split:
- Chinese: `content/zh/post/{zh-dir}/index.md`
- English: `content/en/post/{en-slug}/index.md`

**Chinese directory name (`zh-dir`):** use the article title in Chinese as-is, only replacing Windows-forbidden chars (`\ / : * ? " < > |` and full-width equivalents) with `-`. Example: `AI时代如何阅读技术文档-精炼阅读`.

**English title (`en-title`):** natural-language English translation of the Chinese post title. Example: `How to Read Technical Docs in the AI Era: Distilled Reading`.

**English slug (`en-slug`):** `en-title` converted to kebab-case, used for both the `en/post/` directory **and** the R2 image path. Example: `how-to-read-tech-docs-in-the-ai-era`.

### Front matter format

```yaml
---
title: "文章标题"
date: YYYY-MM-DD
draft: false
image: https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/{YYYY}/{MM}/{en-slug}/banner.png
tags: ["Tag1", "Tag2"]
categories: ["分类名"]
---
```

- English posts: same format, English title: `en-title`, English tags/category
- When English banner is not yet generated, use `image: BANNER_PLACEHOLDER` and fill in later
- No `slug` field needed — directory name IS the slug

### Inline images in article body

Reference images with standard Markdown:
```markdown
![描述](https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/{YYYY}/{MM}/{en-slug}/{filename}.png)
```

In draft source files, images appear as placeholder tags like `<图片2>`. Replace each with the full URL after uploading.

## Draft 目录

所有草稿文件位于项目根目录的 `draft/`：

| 文件 | 说明 |
|------|------|
| `draft/article.md` | 文章正文草稿（追踪于 git） |
| `draft/metadata.md` | 元数据：中/英标题、中/英分类（追踪于 git） |
| `draft/cn-banner.png` | 中文版封面图（gitignore） |
| `draft/en-banner.png` | 英文版封面图（gitignore） |
| `draft/cn-image-*.png` | 中文版内联插图（gitignore） |
| `draft/en-image-*.png` | 英文版内联插图（gitignore） |

所有发布平台都直接从 `draft/` 读取，平台之间没有依赖关系。

## Draft 中的 metadata.md 格式

`draft/<代号>/metadata.md` 记录该篇文章的元数据。

| 段落 | 说明 |
|------|------|
| `# 中文分类` | 中文分类名，取值见「分类映射」表 |
| `# 英文分类` | 英文分类名，取值见「分类映射」表 |
| `# 中文标题` | 文章中文标题 |
| `# 英文标题` | 文章英文标题（`en-title`） |
| `# 首发`（可选） | 若该文章此前已在其他平台首发过，记录 `website=` 和 `url=` |
| `# Hackernoon`（可选） | 英文版发布到自己博客和 Dev.to 后，等待 HackerNoon 抓取 RSS 自动发布；过几天 HackerNoon 发布后，手动把文章链接填入 `url=`，供后续生成 LinkedIn 文章时使用 |
| `# 图片路径` | 包含 `## 中文版` 和 `## 英文版` 两个表格，记录占位符与 R2 URL 的对应关系 |

示例：

```markdown
# 中文分类
AI 方法论

# 英文分类
AI Methodology

# 中文标题
Openclaw玩家必学的省钱小技巧

# 英文标题
Money-Saving Tips Every OpenClaw User Should Know

# 首发
website=
url=

# Hackernoon
url=https://hackernoon.com/money-saving-tips-every-openclaw-user-should-know

# 图片路径

## 中文版

| 占位符 | R2 URL |
|--------|--------|
| cn-banner | https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/{YYYY}/{MM}/{en-slug}/cn/banner.png |
| `<cn-image-01>` | https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/{YYYY}/{MM}/{en-slug}/cn/01.png |

## 英文版

| 占位符 | R2 URL |
|--------|--------|
| en-banner | https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/{YYYY}/{MM}/{en-slug}/en/banner.png |
| `<en-image-01>` | https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/{YYYY}/{MM}/{en-slug}/en/01.png |
```

## 分类映射（英文名）：

| 类别 | categories |
|------|-----------|
| AI 的日常使用手册 | Daily AI Usage |
| AI 工程开发手册 | AI Engineering |
| AI Skill 开发手册 | AI Skill Dev |
| AI 哲学 | AI Philosophy |
| AI 方法论 | AI Methodology |
| 软件哲学 | Software Philosophy |
| 随想 | Thoughts |