# Skill: 准备草稿（翻译 + 上传图片）

触发词：用户说"prepare"、"准备草稿"或类似表述时，加载并执行本文件。

---

## 概述

本 skill 做两件事：

1. 将 `draft/cn-article.md` 翻译为英文，输出到 `draft/en-article.md`
2. 将所有草稿图片上传到 Cloudflare R2，并将占位符与 URL 的对应关系写入 `draft/metadata.md` 中的 **图片路径** 段落

两步完成后，所有发布 skill 可直接使用，无需任何额外准备。

---

## 前提

- `draft/cn-article.md`：中文文章正文（图片用 `<cn-image-01>` 等占位）
- `draft/metadata.md`：含 `英文标题` 字段
- `draft/cn-banner.png`、`draft/en-banner.png`、`draft/cn-image-*.png`、`draft/en-image-*.png`：本地图片文件（gitignore）
- wrangler 已通过 `npx wrangler login` 登录

---

## 第一步：读取元数据，推导路径变量

读取 `draft/metadata.md`，提取：

- `英文标题` → `en-title`

推导：

| 变量 | 规则 |
|------|------|
| `en-slug` | `en-title` 中所有非字母字符（空格、标点、冒号等）替换为 `-`，转小写，连续 `-` 合并为一个，首尾 `-` 去掉 |
| `date` | 今天日期，格式 `YYYY-MM-DD` |
| `YYYY` | 从 date 拆出年份 |
| `MM` | 从 date 拆出月份（两位，如 `06`） |

R2 base 路径：`codeplato-images/{YYYY}/{MM}/{en-slug}`  
公开 URL base：`https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/{YYYY}/{MM}/{en-slug}`

---

## 第二步：翻译 cn-article.md → en-article.md

读取 `draft/cn-article.md`，翻译为英文，写入 `draft/en-article.md`：

- 语言地道、流畅，符合英文博客文体
- 忠实传达原文的核心观点和结构，允许适当意译
- 将正文中所有 `<cn-image-XX>` 占位标签替换为 `<en-image-XX>`（例：`<cn-image-01>` → `<en-image-01>`）
- 不做其他格式变动

---

## 第三步：上传中文版图片

扫描 `draft/` 下的中文版图片，按顺序上传：

### cn-banner

```powershell
npx wrangler r2 object put "codeplato-images/{YYYY}/{MM}/{en-slug}/cn/banner.png" `
  --file "draft\cn-banner.png" `
  --content-type "image/png" `
  --remote
```

URL：`https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/{YYYY}/{MM}/{en-slug}/cn/banner.png`

如果 `draft/cn-banner.png` 不存在，跳过。

### cn-image-*.png

对每一张 `draft/cn-image-0N.png`：

```powershell
npx wrangler r2 object put "codeplato-images/{YYYY}/{MM}/{en-slug}/cn/0N.png" `
  --file "draft\cn-image-0N.png" `
  --content-type "image/png" `
  --remote
```

URL：`https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/{YYYY}/{MM}/{en-slug}/cn/0N.png`

如果没有 `cn-image-*.png`，跳过。

---

## 第四步：上传英文版图片

### en-banner

```powershell
npx wrangler r2 object put "codeplato-images/{YYYY}/{MM}/{en-slug}/en/banner.png" `
  --file "draft\en-banner.png" `
  --content-type "image/png" `
  --remote
```

URL：`https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/{YYYY}/{MM}/{en-slug}/en/banner.png`

如果 `draft/en-banner.png` 不存在，跳过。

### en-image-*.png

对每一张 `draft/en-image-0N.png`：

```powershell
npx wrangler r2 object put "codeplato-images/{YYYY}/{MM}/{en-slug}/en/0N.png" `
  --file "draft\en-image-0N.png" `
  --content-type "image/png" `
  --remote
```

URL：`https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/{YYYY}/{MM}/{en-slug}/en/0N.png`

如果没有 `en-image-*.png`，跳过。

---

## 第五步：更新 draft/metadata.md

在 `draft/metadata.md` 末尾写入（或覆盖已有的）`# 图片路径` 段落：

```markdown
# 图片路径

## 中文版

| 占位符 | R2 URL |
|--------|--------|
| cn-banner | https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/{YYYY}/{MM}/{en-slug}/cn/banner.png |
| `<cn-image-01>` | https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/{YYYY}/{MM}/{en-slug}/cn/01.png |
| `<cn-image-02>` | https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/{YYYY}/{MM}/{en-slug}/cn/02.png |

## 英文版

| 占位符 | R2 URL |
|--------|--------|
| en-banner | https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/{YYYY}/{MM}/{en-slug}/en/banner.png |
| `<en-image-01>` | https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/{YYYY}/{MM}/{en-slug}/en/01.png |
| `<en-image-02>` | https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/{YYYY}/{MM}/{en-slug}/en/02.png |
```

只列出实际存在的图片文件。

---

## 第六步：确认

告知用户：

- `draft/en-article.md` 已生成
- 所有已上传的图片及其 R2 URL
- `draft/metadata.md` 已更新
- 下一步建议（发布中文版、英文版或各平台）
