---
name: hackernoon-prepare
description: 从 draft/<代号>/en-article.md 生成 HackerNoon 发布素材，替换图片占位符为 R2 URL
trigger: "发布hackernoon:<draft代号>"
---

## 触发格式

```
发布hackernoon:<代号>
```

例：`发布hackernoon:0606tokenmaxxing`

触发后，从触发短语中提取 `<代号>`，所有文件路径均以 `draft/<代号>/` 为根目录。

## 目标

从 `draft/<代号>/en-article.md` 读取已翻译好的英文文章，替换图片占位符为 R2 URL，生成 HackerNoon 发布所需的素材，输出到 `~/.blog-workspace/hackernoon/`。

## 步骤

### 1. 读取草稿内容

从项目根目录读取以下文件：

- **`draft/<代号>/en-article.md`**：英文文章正文（含 `<en-image-XX>` 占位标签）
- **`draft/<代号>/metadata.md`**：提取：
  - `英文标题` → `en-title`
  - `# 图片路径` → `## 英文版` 表格中的所有占位符与 URL 对应关系

### 2. 替换图片占位符

将正文中所有 `<en-image-XX>` 占位标签替换为对应的 Markdown 图片语法，URL 来自 `metadata.md` 的 **英文版** 图片路径表格：

```markdown
![](https://pub-deacd49348914a49b1254b01f351ef0d.r2.dev/{YYYY}/{MM}/{en-slug}/en/0N.png)
```

### 3. 生成元数据

根据替换后的英文正文，生成：

- **Metadescription**：160 字符以内的英文描述，概括文章核心主题，适合作为 SEO meta description
- **TL;DR**：2~3 句话的英文摘要，写成一个 paragraph，不分项，让读者快速了解文章的核心观点和结论

### 4. 准备输出目录

确保 `~/.blog-workspace/<代号>/hackernoon/` 目录存在：

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.blog-workspace\<代号>\hackernoon" | Out-Null
```

### 5. 写出文章文件

将替换好图片 URL 的完整正文写入 `~/.blog-workspace/<代号>/hackernoon/article.md`。

### 6. 写出元数据文件

将元数据写入 `~/.blog-workspace/<代号>/hackernoon/metadata.md`：

```markdown
## Title

{en-title}

## Metadescription

{生成的 metadescription，160 字符以内}

## TL;DR

{生成的 TL;DR}
```

### 7. 复制 en-banner

将 `draft/<代号>/en-banner.png` 复制到 `~/.blog-workspace/<代号>/hackernoon/en-banner.png`：

```powershell
Copy-Item "draft\<代号>\en-banner.png" "$env:USERPROFILE\.blog-workspace\<代号>\hackernoon\en-banner.png"
```

如果 `draft/<代号>/en-banner.png` 不存在，跳过。

### 8. 确认输出

告知用户：
- `article.md` 路径（正文已替换图片 URL，可直接粘贴到 HackerNoon 编辑器）
- `metadata.md` 路径
- 下一步建议（打开 HackerNoon 编辑器，粘贴正文，填写 metadescription 和 TL;DR，手动上传 en-banner）
