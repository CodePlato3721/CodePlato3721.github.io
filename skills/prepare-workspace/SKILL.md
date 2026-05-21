---
name: prepare-workspace
description: 检查并清理上次发布后残留在 .blog-workspace 的文件
trigger: "准备工作区"
---

## 目标

在开始新一轮发布前，检查 `~/.blog-workspace/` 是否有上次遗留的文件，并在用户确认后清空。

## 步骤

### 1. 列出工作区内容

用 PowerShell 列出 `~/.blog-workspace/` 下所有文件（递归）：

```powershell
Get-ChildItem "$env:USERPROFILE\.blog-workspace" -Recurse -File | Select-Object FullName, Length, LastWriteTime
```

### 2. 判断是否有残留

- **没有文件**：告知用户"工作区是干净的"，流程结束。
- **有文件**：列出所有文件，询问用户："发现以上残留文件，是否清空工作区？"

### 3. 根据回答处理

- 用户回答**清空**：删除 `~/.blog-workspace/` 下所有文件和子目录内容，但保留 `~/.blog-workspace/` 目录本身。

```powershell
Get-ChildItem "$env:USERPROFILE\.blog-workspace" | Remove-Item -Recurse -Force
```

  完成后告知用户"工作区已清空"。

- 用户回答**不清空** / 其他：保持现状，流程结束。
