# Skill: 从草稿制作中文初稿

触发词：用户说"发布中文初稿"或类似表述时，加载并执行本文件。

---

## 第一步：扫描草稿目录

读取 `~/.blog-workspace/draft/` 目录下的文件：

- 找到唯一的非 `metadata.md` 的 `.md` 文件，文件名（去掉 `.md`）即为文章标题（中文）
- 读取该草稿文件的全文内容
- 读取 `metadata.md`，提取 `类别` 字段

草稿中的图片以占位标签形式出现，例如 `<cn-image-01>`、`<cn-image-02>`，后续步骤会替换。

---

## 第二步：确定元数据

根据标题和今天的日期推导以下字段：

| 字段 | 说明 |
|------|------|
| `zh-title` | 草稿文件名，即中文标题 |
| `zh-dir` | 中文标题，将冒号（`:`、`：`）等 Windows 禁用字符替换为 `-` |
| `en-slug` | 根据中文标题推导的 kebab-case 英文摘要，用于 R2 路径和英文目录 |
| `date` | 今天的日期，格式 `YYYY-MM-DD` |
| `YYYY/MM` | 从 date 拆出，用于 R2 路径 |
| `categories` | 从 metadata.md 读取，映射到 CLAUDE.md 中的中文分类名 |

分类映射（使用中文名）：

| metadata.md 中的值 | frontmatter 中写 |
|-------------------|----------------|
| AI 的日常使用手册 | AI 的日常使用手册 |
| AI 工程开发手册 | AI 工程开发手册 |
| AI Skill 开发手册 | AI Skill 开发手册 |
| AI 哲学 | AI 哲学 |
| AI 方法论 | AI 方法论 |
| 软件哲学 | 软件哲学 |

---

## 第三步：撰写中文文章

根据草稿内容，撰写完整的中文博客正文：

- 语言流畅、口语化，符合博客文体
- 保留草稿中的核心观点和结构
- 图片占位标签（如 `<cn-image-01>`）暂时原样保留，不替换

---

## 第四步：上传 Banner 图片

Banner 图片来源：询问用户 banner 图片的本地路径，或者用户已经在对话中提供了路径。

R2 路径：`{YYYY}/{MM}/{en-slug}/banner.png`

上传命令：

```powershell
cd "c:\Users\lotus\Workspace\CodePlato3721.github.io"
npx wrangler r2 object put codeplato-images/{YYYY}/{MM}/{en-slug}/banner.png `
  --file "用户提供的本地路径" `
  --content-type "image/png" `
  --remote
```

上传成功后，Banner URL 为：
`https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/{YYYY}/{MM}/{en-slug}/banner.png`

---

## 第五步：上传正文内联图片

对草稿中每一个图片占位标签（`<cn-image-N>`）：

1. 询问用户该图片的本地路径（或用户已在对话中提供）
2. 确定文件名：使用 `0N.png` 格式（如 `01.png`、`02.png`），或用户指定的名称
3. R2 路径：`{YYYY}/{MM}/{en-slug}/{filename}.png`
4. 上传命令同上，替换路径和文件名
5. 得到 URL：`https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/{YYYY}/{MM}/{en-slug}/{filename}.png`

如果草稿中没有图片占位标签，跳过此步骤。

---

## 第六步：回填 URL，生成最终文章

将文章中所有占位标签替换为对应的图片 URL：

```markdown
![描述](https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/{YYYY}/{MM}/{en-slug}/{filename}.png)
```

组装完整的 frontmatter：

```yaml
---
title: "{zh-title}"
date: {date}
draft: false
image: https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/{YYYY}/{MM}/{en-slug}/banner.png
tags: ["Tag1", "Tag2"]
categories: ["{category}"]
---
```

tags 根据文章内容自行判断，3~5 个为宜。

---

## 第七步：写入文件

将最终文章写入：

```
content/zh/post/{zh-dir}/index.md
```

写入后，告知用户：
- 文件路径
- Banner URL
- 所有内联图片 URL
- 下一步建议（如：发布英文版、检查预览）
