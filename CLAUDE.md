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

### Banner images
- Upload to Cloudflare R2 bucket `codeplato-images` via `wrangler r2 object put --remote`
- Key pattern: `{year}/{month}/{en-slug}/banner.png`
- Public URL: `https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/{year}/{month}/{en-slug}/banner.png`
- Do **not** commit banner images to git

### Post structure
- Chinese posts: `content/zh/post/{title}/index.md`
- English posts: `content/en/post/{en-slug}/index.md`
