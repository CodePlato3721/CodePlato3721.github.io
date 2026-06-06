# Skill: 发布中文版到个人博客

触发词：用户说"发布中文版"时，加载并执行本文件。

---

## 草稿目录约定

所有文件固定放在项目根目录的 `draft/`：

| 文件 | 说明 |
|------|------|
| `draft/article.md` | 文章正文草稿，图片用 `<cn-image-01>` 等占位 |
| `draft/metadata.md` | 包含中文标题、中文分类等字段 |
| `draft/cn-banner.png` | 中文版 banner（gitignore，不提交） |
| `draft/en-banner.png` | 英文版 banner（本 skill 不使用） |
| `draft/cn-image-01.png` … | 中文版内联插图（按序编号，可选，gitignore） |
| `draft/en-image-01.png` … | 英文版插图（本 skill 不使用） |

---

## 第一步：读取元数据

读取 `draft/metadata.md`，提取：

- `中文标题`：文章的中文标题
- `中文分类`：对应 PROJECT.md 中的中文分类名

---

## 第二步：推导路径变量

| 变量 | 说明 |
|------|------|
| `zh-title` | 从元数据读取的中文标题 |
| `zh-dir` | `zh-title`，将 Windows 禁用字符（`: / \ * ? " < > |` 及全角等价字符）替换为 `-` |
| `en-slug` | 根据 `zh-title` 推导的 kebab-case 英文摘要，用于 R2 路径和英文目录 |
| `date` | 今天的日期，格式 `YYYY-MM-DD` |
| `YYYY/MM` | 从 date 拆出，用于 R2 路径 |

---

## 第三步：上传 cn-banner

将 `draft/cn-banner.png` 上传到 R2：

```powershell
cd "c:\Users\alexx\Workspace\CodePlato3721.github.io"
npx wrangler r2 object put codeplato-images/{YYYY}/{MM}/{en-slug}/banner.png `
  --file "draft\cn-banner.png" `
  --content-type "image/png" `
  --remote
```

Banner URL：`https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/{YYYY}/{MM}/{en-slug}/banner.png`

---

## 第四步：上传内联插图

扫描 `draft/` 下所有 `cn-image-*.png`，按编号顺序上传：

- 本地文件：`draft/cn-image-01.png`、`draft/cn-image-02.png`……
- R2 路径：`{YYYY}/{MM}/{en-slug}/01.png`、`02.png`……

```powershell
npx wrangler r2 object put codeplato-images/{YYYY}/{MM}/{en-slug}/01.png `
  --file "draft\cn-image-01.png" `
  --content-type "image/png" `
  --remote
```

URL 格式：`https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/{YYYY}/{MM}/{en-slug}/01.png`

如果没有 `cn-image-*.png`，跳过此步骤。

---

## 第五步：读取草稿并回填 URL

读取 `draft/article.md`，将图片占位标签替换为对应 R2 URL：

| 占位标签 | 替换为 |
|---------|--------|
| `<cn-image-01>` | `![描述](https://…/{en-slug}/01.png)` |
| `<cn-image-02>` | `![描述](https://…/{en-slug}/02.png)` |
| … | … |

---

## 第六步：生成文章并写入

组装完整文章，写入 `content/zh/post/{zh-dir}/index.md`：

```yaml
---
title: "{zh-title}"
date: {date}
draft: false
image: https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/{YYYY}/{MM}/{en-slug}/banner.png
tags: ["Tag1", "Tag2"]
categories: ["{分类}"]
---
```

tags 根据文章内容判断，3～5 个为宜。

---

## 第七步：确认

告知用户：
- 写入的文件路径
- Banner URL
- 所有内联图片 URL
- 下一步建议（发布英文版、提交 git）
