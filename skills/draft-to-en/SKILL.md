# Skill: 从草稿制作英文版文章并发布到个人博客

触发词：用户说"发布英文版"或类似表述时，加载并执行本文件。

---

## 第一步：读取草稿内容

从项目根目录读取以下文件：

- **`draft/article.md`**：读取全文作为中文草稿
- **`draft/metadata.md`**：提取：
  - `英文分类` 字段 → 映射为英文分类名
  - `英文标题` 字段 → 作为文章英文标题（`en-title`）
  - `# 首发` 段落（可选）→ 提取 `website` 和 `url`

---

## 第二步：判断发布路线

检查 `metadata.md` 中是否存在 `# 首发` 段落且包含 `website` 和 `url`：

- **有首发信息** → 走**摘要路线**（见下）
- **无首发信息** → 走**全文路线**（现有流程，继续第三步）

---

## 第三步：撰写英文文章正文

### 全文路线

根据中文草稿，撰写完整的英文博客正文：

- 语言地道、流畅，符合英文博客文体
- 忠实传达中文原文的核心观点和结构，允许适当意译
- 图片占位标签（如 `<en-image-01>`）暂时原样保留，不替换

### 摘要路线

根据中文草稿，撰写**较短的英文摘要版**正文：

- 提炼文章的核心观点，保留最重要的论据和结论
- 篇幅控制在全文的 1/3 左右，让读者理解文章在讲什么，但不替代完整阅读
- 语言地道、流畅，符合英文博客文体
- **不包含**图片占位标签（摘要版不上传图片）
- 在正文末尾追加：

```
Read the full article on {website_display_name}: {url}
```

其中 `website_display_name` 根据 `website` 字段映射：
- `hackernoon` → `HackerNoon`
- `infoq` → `InfoQ`

---

## 第四步：上传英文 Banner

**全文路线**和**摘要路线**均需上传 banner。

英文 banner 文件：`draft/en-banner.png`

R2 路径：`{YYYY}/{MM}/{en-slug}/en/banner.png`

```powershell
npx wrangler r2 object put "codeplato-images/{YYYY}/{MM}/{en-slug}/en/banner.png" `
  --file "draft\en-banner.png" `
  --content-type "image/png" `
  --remote
```

Banner URL：`https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/{YYYY}/{MM}/{en-slug}/en/banner.png`

---

## 第五步：上传英文内联图片（仅全文路线）

**摘要路线跳过此步骤。**

草稿目录中的英文图片命名规则为 `draft/en-image-01.png`、`draft/en-image-02.png` 等，对应正文中的 `<en-image-01>`、`<en-image-02>` 占位标签。

对每一张图片：

1. R2 路径：`{YYYY}/{MM}/{en-slug}/en/0N.png`
2. 上传命令：

```powershell
npx wrangler r2 object put "codeplato-images/{YYYY}/{MM}/{en-slug}/en/0N.png" `
  --file "draft\en-image-0N.png" `
  --content-type "image/png" `
  --remote
```

3. URL：`https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/{YYYY}/{MM}/{en-slug}/en/0N.png`

---

## 第六步：回填 URL，组装最终文章

### 全文路线

将正文中所有占位标签替换为对应的 Markdown 图片语法后，组装 frontmatter：

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

### 摘要路线

无需回填图片。直接组装 frontmatter（与全文路线格式相同，banner 照常使用）。

---

## 第七步：写入文件

将最终文章写入：

```
content/en/post/{en-slug}/index.md
```

写入后，告知用户：
- 文件路径
- 发布路线（全文 / 摘要）
- Banner URL
- 全文路线：所有内联图片 URL
- 下一步建议（如：commit & push、检查预览）
