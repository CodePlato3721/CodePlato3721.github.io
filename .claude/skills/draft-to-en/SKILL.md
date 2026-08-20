---
name: draft-to-en
description: 从 draft/<代号>/en-article.md 生成英文文章并发布到个人博客。用户输入 "/draft-to-en <代号>"、"发布英文版:<代号>" 或类似表述时使用。
---

# Skill: 发布英文版到个人博客

## 调用方式

```
/draft-to-en <代号>
```

例：`/draft-to-en 0606tokenmaxxing`

`<代号>` 从 slash 命令参数中获取（也可用 "发布英文版:<代号>" 等自然语言触发），所有文件路径均以 `draft/<代号>/` 为根目录。

前提：已运行 `/prepare <代号>`，英文草稿已生成、图片已上传、`metadata.md` 中已有 `# 图片路径` 段落。

---

## 第一步：读取元数据

读取 `draft/<代号>/metadata.md`，提取：

- **`draft/en-article.md`**：读取全文作为英文正文（已翻译好，直接使用）
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

直接使用 `draft/en-article.md` 的内容作为正文。图片占位标签（如 `<en-image-01>`）暂时原样保留，后续步骤回填。

### 摘要路线

基于 `draft/en-article.md` 的内容，生成**较短的摘要版**正文：

- 提炼文章的核心观点，保留最重要的论据和结论
- 篇幅控制在全文的 1/3 左右，让读者理解文章在讲什么，但不替代完整阅读
- **不包含**图片占位标签（摘要版不上传图片）
- 在正文末尾追加：

```
Read the full article on {website}: {url}
```

`website` 和 `url` 直接使用 `metadata.md` 中 `# 首发` 段落的值，不做映射。

---

## 第四步：生成文章并写入

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

不追加作者签名（签名已手动配置在 dev.to 和 HackerNoon 的个人 profile 中）。

---

## 第五步：确认

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
