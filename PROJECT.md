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

## Skills

当用户说"发布中文初稿"或类似表述时，读取 `skills/draft-to-zh/SKILL.md` 并按其中步骤执行。
