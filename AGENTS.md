# 工程区目录与临时文件规则

2026-10-30 王超明确要求，适用于本目录及全部子项目。

- 禁止在 VerySync_works 或项目内随意新建以点号开头的临时目录，也禁止改用普通名称堆积验收副本、临时克隆和构建结果。
- 临时脚本、预览、构建验收、临时克隆与 Git worktree 统一使用系统临时目录下的任务专用目录；PowerShell 用 Join-Path $env:TEMP，跨平台脚本用系统临时目录接口。长期外部临时区须经王超明确指定。
- .git、.github、.vitepress、.vscode、同步元数据等必要目录按实际用途保留；.vitepress 内源码配置与生成缓存分开判断。不能仅按点号或体积删除目录。
- 清理前核对 Git 状态、分支、引用、worktree 指针、源码引用和运行进程。保护源码、配置、未提交修改、独有分支、Git 对象和仍在使用的依赖。
- 确认废弃的材料优先放可恢复隔离区。用途不明的临时材料按王超本次要求保全至 D:\VerySync\DOCS for AI\_works4ai，记录原路径和 SHA-256；归档不等于已学习、已合并或已进入全文索引。
- 不使用同步软件的 .verysync/Archive 当回收站，不自动清空同步历史。禁止无清单的递归删除、git clean -fdx、清理工作树时顺带丢弃未提交内容。
- 本地 Gitea http://localhost:3002/ 与公开 GitHub/Pages 分开。只同步用户授权的相关分支，核对远端祖先并正常快进，不强推、不重写历史。

本文件随博客仓库同步；构建时通过 Hugo --destination 指向系统临时目录，缓存用 --cacheDir 指向系统临时目录。不得再创建 .build-check*、.local-preview、.release-* 等临时目录。
