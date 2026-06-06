# Skill: 从草稿制作英文版文章并发布到个人博客

触发词：用户说"发布英文版"或类似表述时，加载并执行本文件。

---

## 第一步：读取草稿内容

从项目根目录读取以下文件：

- **`draft/article.md`**：读取全文作为中文草稿
- **`draft/metadata.md`**：提取：
  - `英文分类` 字段 → 映射为英文分类名
  - `英文标题` 字段 → 作为文章英文标题（`en-title`）

---

## 第二步：确定元数据

| 字段 | 说明 |
|------|------|
| `en-title` | 直接使用 `metadata.md` 中的 `英文标题` |
| `en-slug` | `en-title` 转 kebab-case，冒号及标点去掉或替换为 `-` |
| `date` | 今天的日期，格式 `YYYY-MM-DD` |
| `YYYY/MM` | 从 date 拆出，用于 R2 路径 |
| `categories` | 直接使用 `metadata.md` 中的 `英文分类` |

---

## 第三步：撰写英文文章

根据中文草稿，撰写完整的英文博客正文：

- 语言地道、流畅，符合英文博客文体
- 忠实传达中文原文的核心观点和结构，允许适当意译
- 图片占位标签（如 `<en-image-01>`）暂时原样保留，不替换

---

## 第四步：上传英文 Banner

英文 banner 文件：`draft/en-banner.png`

R2 路径：`{YYYY}/{MM}/{en-slug}/en/banner.png`

上传命令：

```powershell
npx wrangler r2 object put "codeplato-images/{YYYY}/{MM}/{en-slug}/en/banner.png" `
  --file "draft\en-banner.png" `
  --content-type "image/png" `
  --remote
```

上传成功后，Banner URL 为：
`https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/{YYYY}/{MM}/{en-slug}/en/banner.png`

---

## 第五步：上传英文内联图片

草稿目录中的英文图片命名规则为 `draft/en-image-01.png`、`draft/en-image-02.png` 等，对应正文中的 `<en-image-01>`、`<en-image-02>` 占位标签。

对每一张图片：

1. R2 路径：`{YYYY}/{MM}/{en-slug}/en/0N.png`（如 `en/01.png`、`en/02.png`）
2. 上传命令：

```powershell
npx wrangler r2 object put "codeplato-images/{YYYY}/{MM}/{en-slug}/en/0N.png" `
  --file "draft\en-image-0N.png" `
  --content-type "image/png" `
  --remote
```

3. URL：`https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/{YYYY}/{MM}/{en-slug}/en/0N.png`

如果草稿中没有英文图片文件，跳过此步骤。

---

## 第六步：回填 URL，生成最终文章

将正文中所有占位标签替换为对应的 Markdown 图片语法：

```markdown
![description](https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/{YYYY}/{MM}/{en-slug}/en/0N.png)
```

组装完整的 frontmatter：

```yaml
---
title: "{en-title}"
date: {date}
draft: false
image: https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/{YYYY}/{MM}/{en-slug}/en/banner.png
tags: ["Tag1", "Tag2"]
categories: ["{en-category}"]
---
```

tags 根据文章内容自行判断，3~5 个英文标签。

---

## 第七步：写入文件

将最终文章写入：

```
content/en/post/{en-slug}/index.md
```

写入后，告知用户：
- 文件路径
- Banner URL
- 所有内联图片 URL
- 下一步建议（如：commit & push、检查预览）
