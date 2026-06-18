---
name: csdn-publish
description: 为草稿目录中的文章生成 CSDN 发布所需的元数据和草稿（图片占位符回填 R2 URL）
trigger: "发布csdn:<代号>"
---

## 触发格式

```
发布csdn:<代号>
```

触发后，从触发短语中提取 `<代号>`，所有文件路径均以 `draft/<代号>/` 为根目录。

## 目标

直接从项目的 `draft/<代号>/` 目录读取文章，生成 CSDN 发布所需的元数据和草稿，输出到 `~/.blog-workspace/<代号>/csdn/` 目录。图片不复制到本地——草稿中直接使用 R2 公共 URL，CSDN 会自动抓取并转存到其图床。

## 步骤

### 1. 读取草稿内容

从项目根目录读取以下文件：

- **`draft/<代号>/cn-article.md`**：文章正文
- **`draft/<代号>/metadata.md`**：提取：
  - `中文标题` → `zh-title`
  - `中文分类` → 分类专栏
  - `# 图片路径` → `## 中文版` 表格中的占位符与 R2 URL 对应关系（用于步骤 5 回填）

### 2. 生成文章摘要

阅读文章正文，写一段 200 字以内的中文摘要，概括：
- 文章核心主题
- 主要内容/结构
- 核心观点或结论

### 3. 准备输出目录

确保 `~/.blog-workspace/<代号>/csdn/` 目录存在（不存在则新建）：

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.blog-workspace\<代号>\csdn" | Out-Null
```

### 4. 写出元数据文件

将以下内容写入 `~/.blog-workspace/<代号>/csdn/metadata.md`：

```markdown
# 中文标题
{zh-title}

# 文章摘要
{生成的摘要}

# 分类专栏
{中文分类}
```

### 5. 生成草稿（回填 R2 图片 URL）

读取 `draft/<代号>/cn-article.md` 正文，将图片占位标签替换为对应 R2 URL，原样写入 `~/.blog-workspace/<代号>/csdn/article.md`。

**图片回填规则**：
- 占位标签与 URL 的对应关系来自 `metadata.md` 的 `## 中文版` 表格
- `<cn-image-01>` → `![](https://…/cn/01.png)`（标准 Markdown 图片语法，描述留空即可）
- 以此类推，将所有 `<cn-image-XX>` 替换为对应 R2 URL

### 6. 复制封面图

将 `draft/<代号>/cn-banner.png` 复制到输出目录并重命名为 `banner.png`：

```powershell
Copy-Item "draft\<代号>\cn-banner.png" "$env:USERPROFILE\.blog-workspace\<代号>\csdn\banner.png"
```

### 7. 确认输出

列出 `~/.blog-workspace/<代号>/csdn/`，确认 `metadata.md`、`article.md`、`banner.png` 均已就绪。
