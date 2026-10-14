# 如是有为博客

Hugo 静态博客，现有 290 篇文章（2025-09-22 ~ 2026-10-13，含手写稿）。
线上地址：https://sensor.fans/

## 正文排版与发布前检查

文章标题只在页头显示一次，页头不显示关键词；正文使用统一字体和两级小节。
表格必须保持真实行列，窄屏在表格内部横向滚动。

使用 Hugo 0.147.6 或更新版本。公式由 Hugo 自带的 `transform.ToMath` 在构建时转成原生 MathML；
不需要 LaTeX 安装、客户端插件、CDN 脚本或外部公式字体。
行内公式使用 `\( ... \)`，独立公式使用 `\[ ... \]`。
旧稿 MathJax SVG 可从保留的数学节点转成 MathML，原 SVG 文件仍保留在静态资源中。

修复文章：`python3.11 tools/readability.py --fix`。
只检查是否还有待修格式：`python3.11 tools/readability.py`。
导入脚本已接入同一套规范化流程，手写稿也须维护 `posts_extra/` 中的源文件。
逐篇修订规则在 `tools/readability_fixes.py`，可核对修复过的公式、变量和采集缺口。

先用 Hugo 构建到独立目录，再运行 `python3.11 tools/check_readability.py <构建目录绝对路径>`。
检查器需要 `beautifulsoup4`，只用于校验，不是网站运行依赖；检查全部正文的标题、
表格列数与空单元格、数学节点、图片、内部链接以及未渲染标记。

## 日常操作

### 数学公式视觉回归（2026-10-14）

不要对 MathML 根元素设置普通 `display:block`：这会覆盖浏览器的 `block math`，使变量逐个拆行、分数线撑满正文。块公式用 `<math display="block">`，保留浏览器原生数学布局；不需要新增 LaTeX 插件。

`check_readability.py` 现在会拒绝这种 CSS 覆盖，但结构检查仍不等于视觉验收。用本地 HTTP 服务打开 `tools/math-layout-regression.html`（引用实际 `static/css/site.css`），在桌面及 360px 窄屏确认 `passed: true`，目视检查短等式、行内上下标、分数、矩阵与长公式。发布前后还需检查实际文章 `_7ifyuhvjfspoqpfkbsqoq` 中的三组公式；记录浏览器引擎、视口和前后对照。

- 本地预览：`hugo server`，打开 http://localhost:1313/
- 重新导入文章：`python tools/import_wechat.py`
  - 来源：`D:\VerySync\VerySync_notes\2-Resources\2K-公众号-如是有为`
  - 会清空并重建 `content/posts/`；新出现的微信配图自动下载到 `static/images/wx/`，已下载的不重复下
- 压缩新下载的大图：`python tools/optimize_images.py`，然后再跑一次导入改好链接
- 发布：`bash tools/deploy.sh`（`main` 分支放构建产物给 GitHub Pages，`source` 分支放源码）

## 标签

`tools/tag_vocab.txt` 是词表，分三段：`[型号]` `[公司]` `[主题]`，每行「显示名|别名|别名」。
导入时在标题和正文里匹配。型号和公司出现 1 次就打标签，主题词要出现 2 次（标题里出现算 2 次）。
加标签就往词表里加一行，再重跑导入。

## 手写稿（不是公众号存档来的）

`posts_extra/*.md` 是手工写/从公众号精排 HTML 转来的文章，格式与 `content/posts/*.md` 一样
（frontmatter：title / date / slug / description / tags，不要写 `original`）。
`python tools/import_wechat.py` 在重建 `content/posts` 之后会把它们原样复制进去，
所以重导不会冲掉——**新增这类文章只要往 `posts_extra/` 放一个 md，再跑导入 + 发布即可**。

## 发布时的坑（2026-10-09 实测，本机 t14p）

`bash tools/deploy.sh` 在这台机器的 Hermes bash（MSYS）下有几处会咬人的地方，报错都不好认：

1. **`TMPDIR` 要给一个双方都认的 Windows 路径。** MSYS 的 `mktemp -d` 返回 `/tmp/...`，而 bash 的 `/tmp` 与原生 git 认的 `/tmp`（＝`D:\tmp`）不是同一个目录：脚本在子 shell 里 `cd` 进了一个非仓库目录，`git checkout --orphan` 静默失败（stderr 被脚本重定向掉了），**只剩一个 exit 128、什么错误都不打印**。写成
   `TMPDIR="C:/Users/wangc/AppData/Local/hermes/cache/scratch/tmpd" bash tools/deploy.sh` 即可。
2. **上一次死在 push 的残留会毒死下一次。** `deploy-tmp` 分支或 `D:/tmp/tmp.*` worktree 还在时，下一次一定在脚本开头 `git checkout --orphan` 撞名失败。跑之前先 `git worktree list` 与 `git branch -D deploy-tmp` 清一遍。
3. **GitHub 的 HTTPS 凭据会失效**，报 `remote: Invalid username or token. Password authentication is not supported`。本机 SSH 通的是 `neurusuv`、对该仓库有写权限，所以发布用
   `REMOTE=git@github.com:rushiuv/rushiuv.github.io.git bash tools/deploy.sh`；也可以重新登录一次 HTTPS 凭据，两种都行。
4. 发布后**核一遍线上**：文章地址里的 slug 是**小写**的（Hugo 会把网址转小写），
   `https://rushiuv.github.io/posts/<小写slug>/`；Actions 那次运行记录在仓库 Actions 页，
   推送 main 之后才会出现。
5. **IndexNow 会报「密钥文件还没上线」**（2026-10-13 实测）：GitHub Pages（Fastly）对
   `Python-urllib/x.y` 这个默认 UA 直接回 **403**，脚本的前置校验于是永远不通过、五个 5 分钟重试跑完就退出
   ——文件其实早就在线了。`tools/indexnow.py` 已给校验和提交都带上浏览器 UA；**以后新写这类外部校验脚本，
   只要目标在 GitHub Pages 上，就要带 UA**。

## 主题

`layouts/` 和 `static/css/site.css` 是自带的模板，只做亮色，没有外部依赖。
主图、头像、二维码在 `static/images/site/`；《金刚经》引句写在 `hugo.toml` 的 `params` 里。
