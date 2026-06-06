---
name: csdn-publish
description: 为草稿目录中的文章生成 CSDN 发布所需的元数据、简化版草稿和封面图
trigger: "发布到 CSDN"
---

## 目标

直接从项目的 `draft/` 目录读取文章，生成 CSDN 发布所需的全部素材，输出到 `~/.blog-workspace/csdn/` 目录。

## 步骤

### 1. 读取草稿内容

从项目根目录读取以下文件：

- **`draft/article.md`**：文章正文
- **`draft/metadata.md`**：提取：
  - `中文标题` → `zh-title`
  - `中文分类` → 分类专栏

### 2. 生成文章摘要

阅读文章正文，写一段 200 字以内的中文摘要，概括：
- 文章核心主题
- 主要内容/结构
- 核心观点或结论

### 3. 准备输出目录

确保 `~/.blog-workspace/csdn/` 目录存在（不存在则新建）。

### 4. 写出元数据文件

将以下内容写入 `~/.blog-workspace/csdn/元数据.md`：

```markdown
# 中文标题
{zh-title}

# 文章摘要
{生成的摘要}

# 分类专栏
{中文分类}
```

### 5. 生成简化版草稿

读取 `draft/article.md` 正文，生成简化版文章，写入 `~/.blog-workspace/csdn/草稿.md`。

简化规则：
- **适度简化文字**：对篇幅较长的说明段落，精简表述，去掉冗余；但保留核心观点，不改变含义
- **保留不简化的内容**：代码块、示例、表格、列表条目——这类内容结构固定，原样保留
- **图片占位符**：将 `<cn-image-XX>` 占位标签原样保留（CSDN 编辑器上传图片后再替换）

### 6. 复制封面图

将 `draft/cn-banner.png` 复制到 `~/.blog-workspace/csdn/cn-banner.png`：

```powershell
Copy-Item "draft\cn-banner.png" "$env:USERPROFILE\.blog-workspace\csdn\cn-banner.png"
```

### 7. 复制插图

将 `draft/` 下所有 `cn-image-*.png` 复制到 `~/.blog-workspace/csdn/`：

```powershell
Copy-Item "draft\cn-image-*.png" "$env:USERPROFILE\.blog-workspace\csdn\"
```

如果没有 `cn-image-*.png`，跳过此步骤。

### 8. 确认输出

列出 `~/.blog-workspace/csdn/`，确认 `元数据.md`、`草稿.md`、`cn-banner.png`、所有插图均已就绪。
