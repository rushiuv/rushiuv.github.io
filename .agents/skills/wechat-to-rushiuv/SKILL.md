---
name: wechat-to-rushiuv
description: 在 ChatGPT 聊天模式中，通过 GitHub Actions 读取用户提供的公开微信公众号文章，保存图文，按需发布到「如是有为」Hugo 博客。
---

# WeChat → 如是有为（Chat-mode Skill）

## 触发
用户发送 `https://mp.weixin.qq.com/s/...`，并要求读取、转发、转载、归档、同步或发布到「如是有为」。不要求用户安装程序，不默认要求切换 Work/Codex。

## 既有成功路径
- 博客仓库：`rushiuv/rushiuv.github.io`
- 已验证导入分支：`import/wechat-ezLZtznHzE3`
- 已运行的 Actions 脚本：`.github/workflows/import-one-wechat.yml`
- 已成功导入文章：`https://mp.weixin.qq.com/s/ezLZtznHzE3-08Xvy1JR5Q`
- 结果目录：`.wechat-import/ezLZtznHzE3-08Xvy1JR5Q/`，包含 `article.md`、`article.html`、`metadata.json`、`images/`（15 张图）。

## 工作方法
1. 使用连接的 GitHub 工具读取此 SKILL.md、既有 Actions 脚本、博客实际目录和 Hugo 配置；不要假定工作流已安装为全局工具。
2. 对新微信链接，优先创建隔离分支，将脚本参数化或创建一次性 GitHub Actions 工作流，在 GitHub 云端 Ubuntu runner 执行；用 GitHub API 检查运行状态和日志。
3. 脚本优先使用 `curl_cffi` 的 Chrome/Safari impersonation 请求公开文章，BeautifulSoup 提取 `#js_content`、`#activity-name`、`#js_name`，再用 markdownify 转 Markdown。失败时尝试 Jina Reader 等公开解析入口。仅在确认正文有效、不是验证码/拦截页时标记成功。
4. 对正文图片优先读取 `data-src`，下载微信图片到相对路径，记录元数据和失败项，避免站外图片防盗链；过滤 script、iframe 等内容。
5. 保存完整文章、元数据和图片至隔离分支。通过 GitHub fetch_file 读取结果并检查标题、正文长度、图片数量、原文 URL 和发布时间。
6. 只有在用户要求发布时，依照当前 Hugo 结构生成文章 Page Bundle / Front Matter，并检查列表页、首页展示规则。发布前避免重复 slug 或覆盖已有文章。
7. 用户明确要求转载他人文章时，优先保留作者与来源信息，必要时用摘要+原文链接而非未经授权复制完整受版权保护的第三方文章。对用户自有文章可按其要求全文迁移。
8. 最后验证 GitHub commit、构建状态和实际文章 URL；若失败，明确区分读取成功、保存成功、发布成功三种状态。

## 关键限制
- 微信风控会变化，单篇成功不保证所有文章成功。
- 不要把 GitHub Actions 方案说成聊天环境直接运行了 Python；实际执行发生在 GitHub runner。
- 不要声称后台永久监控或跨会话自动加载本 Skill。未来会话应通过仓库路径重新读取本文件。
- 不要修改或查询 `neurusuv/VerySync_Work_BK`。
