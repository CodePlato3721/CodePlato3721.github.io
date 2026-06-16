# Skill: 发布英文版到个人博客

触发词：用户说"发布英文版:<代号>"或类似表述时，加载并执行本文件。

触发后，从触发短语中提取 `<代号>`，所有文件路径均以 `draft/<代号>/` 为根目录。

前提：已运行 `prepare:<代号>`，英文草稿已生成、图片已上传、`metadata.md` 中已有 `# 图片路径` 段落。

---

## 第一步：读取元数据

读取 `draft/<代号>/metadata.md`，提取：

- `英文标题` → `en-title`
- `英文分类` → `en-category`
- `# 图片路径` → `## 英文版` 表格中的占位符与 URL 对应关系

---

## 第二步：推导路径变量

| 变量 | 说明 |
|------|------|
| `en-slug` | `en-title` 转 kebab-case（非字母字符替换为 `-`，转小写，合并连续 `-`，去首尾 `-`） |
| `date` | 今天的日期，格式 `YYYY-MM-DD` |
| `YYYY/MM` | 从 date 拆出，用于 R2 路径 |

---

## 第三步：读取草稿并回填 URL

读取 `draft/<代号>/en-article.md`，将正文中所有图片占位标签替换为对应 R2 URL：

- 占位标签与 URL 的对应关系来自 `metadata.md` 的 `## 英文版` 表格
- Banner URL 同样来自该表格中的 `en-banner` 行

示例替换：

| 占位标签 | 替换为 |
|---------|--------|
| `<en-image-01>` | `![description](https://…/{en-slug}/en/01.png)` |
| `<en-image-02>` | `![description](https://…/{en-slug}/en/02.png)` |

---

## 第四步：生成文章并写入

组装完整文章，写入 `content/en/post/{en-slug}/index.md`：

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

tags 根据文章内容自行判断，3～5 个英文标签。

---

## 第五步：确认

告知用户：
- 写入的文件路径
- Banner URL
- 所有内联图片 URL
- 下一步建议（commit & push、检查预览）
