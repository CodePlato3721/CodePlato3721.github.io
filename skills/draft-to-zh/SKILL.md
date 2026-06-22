# Skill: 发布中文版到个人博客

触发词：用户说"发布中文版:<代号>"或类似表述时，加载并执行本文件。

触发后，从触发短语中提取 `<代号>`，所有文件路径均以 `draft/<代号>/` 为根目录。

前提：已运行 `prepare:<代号>`，图片已上传、`metadata.md` 中已有 `# 图片路径` 段落。

---

## 第一步：读取元数据

读取 `draft/<代号>/metadata.md`，提取：

- `中文标题` → `zh-title`
- `中文分类` → 对应 PROJECT.md 中的中文分类名
- `英文标题` → 用于推导 `en-slug`
- `# 图片路径` → `## 中文版` 表格中的占位符与 URL 对应关系

---

## 第二步：推导路径变量

| 变量 | 说明 |
|------|------|
| `zh-dir` | `zh-title`，将 Windows 禁用字符（`\ / : * ? " < > |` 及全角等价字符）替换为 `-` |
| `en-slug` | `英文标题` 转 kebab-case（非字母字符替换为 `-`，转小写，合并连续 `-`，去首尾 `-`） |
| `date` | 今天的日期，格式 `YYYY-MM-DD` |
| `YYYY/MM` | 从 date 拆出，用于 R2 路径 |

---

## 第三步：读取草稿并回填 URL

读取 `draft/<代号>/cn-article.md`，将正文中所有图片占位标签替换为对应 R2 URL：

- 占位标签与 URL 的对应关系来自 `metadata.md` 的 `## 中文版` 表格
- Banner URL 同样来自该表格中的 `cn-banner` 行

示例替换：

| 占位标签 | 替换为 |
|---------|--------|
| `<cn-image-01>` | `![描述](https://…/{en-slug}/cn/01.png)` |
| `<cn-image-02>` | `![描述](https://…/{en-slug}/cn/02.png)` |

---

## 第四步：生成文章并写入

组装完整文章，写入 `content/zh/post/{zh-dir}/index.md`：

```yaml
---
title: "{zh-title}"
date: {date}
draft: false
image: https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/{YYYY}/{MM}/{en-slug}/cn/banner.png
tags: ["Tag1", "Tag2"]
categories: ["{中文分类}"]
---
```

tags 根据文章内容判断，3～5 个为宜。

在文章正文末尾追加以下固定内容（注意保留前面的空行）：

```
---

## 关于作者

我是代码Plato。

我相信，人类的创造力才是 AI Coding 的真实之树，而代码与模型不过是投射在洞穴墙上的影子。

微博：@代码Plato
主页：https://weibo.com/u/1041257881
```

---

## 第五步：确认

告知用户：
- 写入的文件路径
- Banner URL
- 所有内联图片 URL
- 下一步建议（发布英文版、提交 git）
