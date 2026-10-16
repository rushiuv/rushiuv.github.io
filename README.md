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

## 手写稿与转载稿（不是公众号存档来的）

`posts_extra/*.md` 是手工写、从公众号精排 HTML 转来、或从别的号转载来的文章，格式与
`content/posts/*.md` 一样，frontmatter：title / date / slug / description / original /（companies / tags）。
`python tools/import_wechat.py` 在重建 `content/posts` 之后会把它们复制进去，所以重导不会冲掉
——**新增这类文章只要往 `posts_extra/` 放一个 md，再跑导入 + 发布即可**。

三条硬规矩（2026-10-14 王超定）：

1. **日期用原文发布时间**（2026-10-14 王超定，改自当天早些时候的「用入库当刻」）：frontmatter 的 `date`
   与文件名前缀都取公众号原文的发布时间，和 291 篇存档稿同一口径；链接与排序都按文章自己的时点走。
2. **原文链接要列出来**，写在 frontmatter 的 `original`；页头会渲染成「… · 查看原文」。
   本号首发用默认文案；**别人的号要把来源写清楚**：加 `original_from: "转载自公众号「昆泰芯微电子」"`
   （模板 `layouts/_default/single.html` 支持这个字段，不写则回落到「首发于公众号「如是有为」」）。
3. **文末的固定套路一律去掉**（联系信息、公司简介、扫码关注、往期推荐、免责/版权声明、推广）——
   见下一节，导入管道会自动处理，源稿也应保持干净。

## 采集文的尾部套路清理（统一规律，2026-10-14 定）

公众号文末固定挂的那几块——公司简介、销售/技术支持联系方式、总部与研发中心地址、扫码关注、
往期推荐、免责与版权声明、推广榜单——**不属于文章内容，一律不入稿**。

`tools/boilerplate.py` 从文末往上找连续的套路块并整段切掉：装饰图（含带列表符号的图片）、
栏目标签（`总部/HEAD QUARTERS:` 这类）、碎句、纯 ASCII 的英文地址都算同一块；
**作者自己的 `注：/说明：/备注：` 行会保留回正文**（那是内容，不是套路）；
命中「知识卡片」「图 N」「表 N」立即停止（不误切正文）。

```sh
python3.11 tools/boilerplate.py           # 只检查，列出每篇会切掉多少字、切口在哪
python3.11 tools/boilerplate.py --fix     # 真切（content/posts 与 posts_extra 源稿一起）
```

`import_wechat.py` 已把这一步接在 `clean_body` 之前（**先切套路再本地化图片**，于是套路块里的
横幅图会自然落成"未被引用"、被导入时的孤儿图清理删掉），导入结束会打印「文末套路块已去除 N 篇」。
手写稿复制进 `content/posts` 时也会过一遍，源稿漏了会提示跑 `--fix`。

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


## 芯片与公司词条（2026-10-15）

`/wiki/` 为词条入口，型号与公司仍沿用 `/models/<term>/`、`/companies/<term>/`。词条写在相应目录的 `_index.md`，不复制成独立文章、不改旧文章标签。`layouts/_default/term.html` 在第一页显示正文和官方资料，后面自动列相关文章；分页页只显示文章并提供返回词条链接。

首批从311篇文章中按现有型号／公司标签关联篇数合并取前20条，每篇只计一次；同篇数按名称 `casefold()` 排序，因此第20条为KTH7111，MT6835同为10篇、排第21条。运行 `python3.11 tools/wiki_inventory.py` 可复算，初始快照在 `data/wiki-seed.json`。后续新增文章不会由导入器删除这些词条。

型号采用基本介绍、工作原理与功能、关键规格、应用与使用条件、官方资料模块；公司采用公司与品牌、相关业务与技术路线、产品系列与代表方向、与编码器应用的关系、如何查找资料、官方资料模块。约2000字按资料量调整，参数保留条件。型号专用手册优先于系列汇总表，KTH78按系列管理。

本次7个型号／系列均提供已取回并核对的官方PDF地址，KTH78链接KTH7812代表型号手册；图片为官方功能框图局部或产品示意，附来源，WebP仅压缩与裁取原图，不重画电气关系。图片与文档来源保存在 `data/wiki-sources.json`。AS5047P使用英飞凌当前产品与手册地址，注明2026年7月业务迁移。

构建：`hugo --minify --destination <独立输出目录>`。结构检查沿用 `tools/check_readability.py`，词条还需检查目录、下载按钮、关联词条、文章分页与窄屏表格。发布时正常推送源码到source；静态部署以远端main为父提交生成新提交，保留 `.github/workflows/pages.yml` 与 `.nojekyll`，禁止使用旧部署脚本的强推路径。


### 2026-10-16 全部型号与公司标签词条

- 311篇文章现有models 78个、companies 91个，共169条；在首批20条基础上补齐149条。
- 完整排名与统计口径在data/wiki-inventory.json；首批选择记录data/wiki-seed.json保留。
- 新增来源、文档摘要、资料核对日期与正文路径在data/wiki-expansion-sources.json。
- 非芯片产品保留实际类别；学校、金融和软件机构保留真实身份。不得将一般机理解释当成型号实测。
- 更新范围使用tools/wiki_inventory.py --limit 10000重新盘点，再按对应taxonomy的_index.md维护，不自动修改文章标签。
- 官网资料缺失时保留正式入口和明确边界，不使用邻近型号参数填空；参考文档或相关后缀需明确标注。
