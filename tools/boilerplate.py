"""采集文尾部清理：去掉公众号文末的「统一注释 / 广告信息 / 联系信息」套路块。

统一规律（2026-10-14 王超定）：采集来的文章，文末的固定套路（公司简介+联系方式+扫码关注+
往期回顾+免责声明+推广）一律不属于文章内容，导入时统一去掉。

用法：
    python3 tools/boilerplate.py            # 只检查，列出每篇会删掉什么（不改文件）
    python3 tools/boilerplate.py --fix      # 真删（同时写 content/posts 与 posts_extra 源稿）
    python3 tools/boilerplate.py --json out.json
"""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WX_DST = ROOT / "static" / "images" / "wx"

# 强标记：命中即认定为套路块（不受长度限制）
STRONG = [
    r"销售服务\s*/?\s*SALES",
    r"SALES\s*&\s*SERVICES",
    r"TECHNICAL\s*SUPPORT",
    r"HEAD\s*QUARTER",
    r"全球服务中心\s*/",
    r"扫码关注",
    r"长按.{0,8}识别",
    r"往期回顾",
    r"推荐阅读",
    r"相关阅读",
    r"免责声明",
    r"版权声明",
    r"版权归.{0,16}所有",
    r"未经授权.{0,12}转载",
    r"商务合作",
    r"线索爆料",
    r"投稿邮箱",
    r"support@",
    r"sales@",
    r"^\s*END\s*$",
    # 账号固定附在文末的「公司简介」段（各家公众号的通用套路）
    r"成立于.{0,40}(使命|愿景|高新技术企业)",
    r"产品线包括",
    r"公司具备.{0,12}(完备|领先|自主)",
    r"^[^\n]{0,20}-\s*专注于",
    # 「关于 XX」「公司简介」「ABOUT」这类栏目页（2026-10-14 王超：末尾的广告/注释信息一律去掉）
    r"^\s*\*{0,2}[·\s]*关于[^\n]{0,26}\*{0,2}\s*$",
    r"^\s*\*{0,2}公司简介\*{0,2}\s*$",
    r"^\s*\*{0,2}(ABOUT|About)\b[^\n]{0,28}$",
    r"欢迎扫描",
    r"扫描.{0,8}二维码",
    r"长按.{0,8}(二维码|识别)",
    r"^\s*<end>\s*$",
    r"^\s*欢迎(咨询|联系|合作|垂询)[！!。]?\s*$",
    r"^\s*(如果|若)(你|您|贵司)?(也|想|需要)?.{0,12}(合作|咨询|联系我们)",
    # 厂商样片/扫码留资/邮件获客（2026-10-30 cleanup）
    r"扫描上方二维码",
    r"开放样片申请",
    r"申请样片",
    r"获取产品样片",
    r"样片申请",
    r"设为.{0,4}星标",
    r"请点击.{0,20}关注",
    r"欢迎发送邮件至\s*sales@",
]

# 正文中段的获客块：申请样片标题 + 可选二维码图 + 扫码/邮件说明；或独立获客句；或开头关注星标
LEADGEN_PATTERNS = [
    # 「**申请样片**」小节：标题 + 可选二维码图 + 说明段
    re.compile(
        r"(?ms)^\s*\*{0,2}申请样片\*{0,2}\s*\n+"
        r"(?:!\[[^\]]*\]\([^\)]+\)\s*\n+)*"
        r"[^\n]*(?:开放样片申请|扫描上方二维码|获取产品样片|sales@)[^\n]*\n*"
    ),
    # 独立获客段（无「申请样片」标题）
    re.compile(
        r"(?m)^[^\n]*(?:扫描上方二维码填写申请|欢迎发送邮件至\s*sales@|"
        r"进一步咨询[^\n]{0,60}申请样片[^\n]{0,80}sales@|"
        r"可邮件\s*sales@[^\n]{0,80}www\.novosns)[^\n]*\n*"
    ),
    # 文首关注/星标引流（紧贴 front matter 后）
    re.compile(
        r"(?m)^\*{0,2}请点击\*{0,2}[^\n]{0,40}(?:关注|星标)[^\n]*\n+"
    ),
    # 斜体「注：…开放样片申请…」获客备注（非技术口径）
    re.compile(
        r"(?m)^\s*\*注：[^\n]*开放样片申请[^\n]*\*\s*\n*"
    ),
    # 厂商文末公司简介（股票代码 + 使命口号）
    re.compile(
        r"(?ms)^[^\n]*（简称[^\n]{0,40}科创板股票代码[^\n]*\n+"
        r"(?:[^\n]+\n+)*?"
        r"[^\n]*以[『「].{0,80}为使命[^\n]*\n*"
    ),
]


def strip_leadgen(body: str):
    """去掉正文里的样片二维码/邮件获客/关注星标等引流块。返回 (新正文, 删除片段列表)。"""
    removed = []
    out = body
    for rx in LEADGEN_PATTERNS:
        while True:
            m = rx.search(out)
            if not m:
                break
            snippet = m.group(0)
            removed.append(snippet.strip())
            out = out[: m.start()] + out[m.end() :]
    if removed:
        out = re.sub(r"\n{3,}", "\n\n", out)
        # front matter 后若直接贴正文，补一个空行
        if out.startswith("**") or (out and not out.startswith("\n")):
            pass
        out = out.lstrip("\n")
        if not out.endswith("\n"):
            out += "\n"
        else:
            out = out.rstrip("\n") + "\n"
    return out, removed


# 弱标记：只在**短块**（默认 ≤80 字）里才算套路，避免正文里提到"官网/电话"被误删
# ⚠️ 不放「在看/留言/分享」：作者的收尾提问（「欢迎在评论区分享」「留言说说」）是正文语气，不是套路
WEAK = [
    r"总部\s*/",
    r"研发中心\s*/",
    r"运营中心\s*/",
    r"关注我们",
    r"关注.{0,8}公众号",
    r"点击.{0,6}关注",
    r"阅读原文",
    r"点赞",
    r"打赏",
    r"订阅",
    r"转发",
    r"官网",
    r"联系电话",
    r"电话[:：]",
    r"座机",
    r"邮箱[:：]",
    r"[a-z0-9\-_.]+@[a-z0-9\-]+\.(com|cn|net)",
    r"www\.",
    r"^[\u4e00-\u9fa5]{2,10}(公司|中心|研究所)\s*[:：]",
    r"^地址\s*[:：]",
    r"[\u4e00-\u9fa5]{2,8}(省|市)[\u4e00-\u9fa5]{0,4}(区|县)[^\n]{0,40}(号|室|楼|园|大厦|广场)",
]

# 块本身可能只是装饰（图片可带列表符号、分隔线、栏目标签），跟在套路块前后一起带走
DECOR = re.compile(r"^\s*(?:[-*+]\s+)?!\[[^\]]*\]\([^)]*\)\s*$|^\s*(?:[-*+]\s+)?(<hr\s*/?>|[-—*_>\s]+)\s*$")
LABEL = re.compile(r"^[\u4e00-\u9fa5A-Za-z &/·]{2,28}[:：]\s*‍?$")  # 如「总部/HEAD QUARTERS:」
# 作者自己的方法学/口径备注（如「注：本文为简化模型计算…」）属于正文，切套路段时要留下
KEEP_LINE = re.compile(r"^\s*(注|说明|备注)\s*[:：]")
# 纯 ASCII 的短块（英文地址、公司英文名、门牌号）在套路段里算同一块
CJK = re.compile(r"[\u4e00-\u9fa5]")
# 这些词一出现就说明是正文内容，立即停止往上切
CONTENT_STOP = re.compile(r"知识卡片|本文作者|图\s*\d|表\s*\d")
# 「关于 XX / 公司简介 / ABOUT」栏目页标题
AD_HEAD = re.compile(r"^\s*\*{0,2}[·\s]*(关于[^\n]{0,26}|公司简介|(ABOUT|About)\b[^\n]{0,28})\*{0,2}\s*$", re.M)
# 推广句（直播预告、扫码领资料、点关注这一类），贴着套路块时一起切
PROMO = re.compile(r"欢迎扫描|扫描.{0,10}二维码|二维码|长按.{0,6}(二维码|识别)|直播|扫码|点(击|我).{0,4}(关注|查看|领取)|领取|报名|限时|优惠")
AD_SIGNAL = re.compile(r"!\[|扫码|关注|微信|有限公司|股份有限公司|股票代码|电话|邮箱|官网|www\.|产品线")


# 地址行：城市/路街词 + 号室楼栋，且不带句末标点
ADDRESS = re.compile(r"(省|市|区|县|路|街|大道|园区|镇|村)[^\n]{0,24}(号|室|楼|栋|大厦|广场|科技园|产业园)")


def is_boiler(block, weak_max=80):
    b = block.strip()
    for p in STRONG:
        if re.search(p, b, re.M):
            return True, "strong:" + p
    first = b.split("\n", 1)[0].strip()
    if first.endswith("有限公司") or first.endswith("股份有限公司"):
        return True, "strong:公司名抬头"
    if len(re.findall(r"mp\.weixin\.qq\.com/s", b)) >= 3:
        return True, "strong:往期推荐链接"
    if len(b) <= weak_max:
        if ADDRESS.search(b) and not re.search(r"[。！？；]", b):
            return True, "address"
        for p in WEAK:
            if re.search(p, b, re.M):
                return True, "weak:" + p
    return False, ""


def find_tail_cut(body, weak_max=80):
    """返回（cut_index 字符位置, 命中的第一条标记）——从文末往上找连续的套路块。

    允许跳过夹在套路块之间的装饰块、栏目标签块，以及 ≤30 字的碎句（如「了解更多信息」）。
    """
    parts = re.split(r"(\n\s*\n)", body)          # 交替：块、分隔符、块、分隔符…
    blocks = parts[0::2]
    seps = parts[1::2]
    hits = []
    for i in range(len(blocks) - 1, -1, -1):
        b = blocks[i].strip()
        if not b:
            continue
        ok, why = is_boiler(b, weak_max)
        if ok:
            hits.append((i, why))
            continue
        if CONTENT_STOP.search(b):
            break             # 命中正文特征词（知识卡片/图N 等）立即停
        if hits and (DECOR.match(b) or LABEL.match(b) or len(b) <= 34 or KEEP_LINE.match(b)
                     or PROMO.search(b)
                     or (not CJK.search(b) and len(b) <= 60)):
            continue          # 紧邻套路块的装饰/栏目标签/碎句/推广句/作者备注/英文地址，算同一块
        if not hits and (DECOR.match(b) or len(b) <= 34 or PROMO.search(b)):
            continue          # 文末先出现推广句/碎句也允许继续往上找套路块
        break
    if not hits:
        # 文末的「关于 XX / 公司简介 / ABOUT」栏目页：标题本身是套路，但它上面常有一段公司介绍
        # （长于 weak_max，按块判定会先停下），所以这里直接按位置找：限文末 40%，且尾部有广告信号。
        # 取「最早出现」的那一个（「关于 X」通常在公司简介之前），整段到文末一起切。
        for i in range(len(blocks)):
            b = blocks[i].strip()
            if not b or CONTENT_STOP.search(b):
                continue
            if AD_HEAD.search(b):
                pos = sum(len(blocks[j]) + (len(seps[j]) if j < len(seps) else 0) for j in range(i))
                if pos >= len(body) * 0.6 and AD_SIGNAL.search(body[pos:]):
                    # 从该栏目页向上扩展：装饰图、推广句、碎句、紧邻的套路块一起带走
                    start = i
                    while start > 0:
                        j = start - 1
                        bj = blocks[j].strip()
                        if not bj:
                            start = j
                            continue
                        ok, _ = is_boiler(bj, weak_max)
                        if ok or DECOR.match(bj) or LABEL.match(bj) or PROMO.search(bj):
                            start = j
                            continue
                        break
                    pos = sum(len(blocks[j]) + (len(seps[j]) if j < len(seps) else 0) for j in range(start))
                    first_block = blocks[start]
                    m2 = PROMO.search(first_block)
                    if m2:
                        head = first_block[:m2.start()]
                        cut_at = max((head.rfind(c) for c in "。！？；"), default=-1)
                        if cut_at >= 0:
                            pos += cut_at + 1
                    return pos, "ad-section:关于/公司简介"
    if not hits:
        return None, ""
    start = min(i for i, _ in hits)
    pos = sum(len(blocks[j]) + (len(seps[j]) if j < len(seps) else 0) for j in range(start))
    # 若切口所在那一段是「正文 + 推广句」混在同一段里，只从推广句起切，保留前面的正文
    first_block = blocks[start]
    m = PROMO.search(first_block)
    if m:
        head = first_block[:m.start()]
        cut_at = max((head.rfind(c) for c in "。！？；"), default=-1)
        if cut_at >= 0:
            pos += cut_at + 1
    return pos, hits[0][1]


def find_small_images(body, max_kb=10):
    """找出正文里引用的「小图」——公众号正文里的表情包、装饰符号、栏目小图标多为 ≤10KB。
    2026-10-14 王超：文章里的（红）表情包、品牌装饰小图一律去掉。"""
    import re as _re
    keys = set(_re.findall(r"/images/wx/([^)\s\"']+)", body))
    out = []
    for k in sorted(keys):
        p = WX_DST / k
        if p.exists() and p.stat().st_size <= max_kb * 1024:
            out.append(k)
    return out


def drop_images(body, keys):
    """把指定配图的引用从正文里去掉（整行/整段一起清，避免留空行）。"""
    for k in keys:
        body = body.replace(f"![](/images/wx/{k})", "")
        body = re.sub(r"^\s*!\[\]\(/images/wx/" + re.escape(k) + r"\)\s*$", "", body, flags=re.M)
    body = re.sub(r"\n{3,}", "\n\n", body)
    return re.sub(r"\n\s*\n\s*(?=\n)", "\n\n", body).strip() + "\n"


def collect_files():
    out = []
    for d in ("content/posts", "posts_extra"):
        root = ROOT / d
        out += sorted(root.glob("*.md"))
        out += sorted(root.glob("*/index.md"))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fix", action="store_true")
    ap.add_argument("--json")
    ap.add_argument("--weak-max", type=int, default=80)
    ap.add_argument("--max-kb", type=int, default=10,
                    help="正文里 ≤ 这个大小的配图按表情包/装饰小图去掉（默认 10KB）")
    args = ap.parse_args()

    report, changed = [], 0
    for f in collect_files():
        text = f.read_text(encoding="utf-8")
        if not text.startswith("---"):
            continue
        _, fm, body = text.split("---", 2)
        body, leadgen = strip_leadgen(body)
        pos, why = find_tail_cut(body, args.weak_max)
        small = find_small_images(body, args.max_kb)
        if pos is None and not small and not leadgen:
            continue
        if pos is None:
            kept = body
            cut = ""
            why = "only-small-images"
        else:
            cut = body[pos:].strip()
            # 切掉的区域里若有作者自己的「注：/说明：」行，保留回正文（那是内容不是套路）
            keep = [ln.strip() for ln in cut.splitlines() if KEEP_LINE.match(ln.strip())]
            kept = body[:pos].rstrip()
            if keep:
                kept += "\n\n" + "\n\n".join(keep)
            kept += "\n"
        if small:
            kept = drop_images(kept, small)
        if leadgen and pos is None and not small:
            kept = body
            cut = "\n\n".join(leadgen)
            why = "leadgen"
            keep = []
        elif leadgen:
            # leadgen already applied to body; append note
            why = (why + "+leadgen") if why else "leadgen"
            cut = (cut + "\n\n" if cut else "") + "\n\n".join(leadgen)
        report.append({"file": str(f.relative_to(ROOT)), "why": why, "cut_chars": len(cut),
                       "kept_lines": keep if pos is not None else [],
                       "small_images": small,
                       "leadgen": leadgen,
                       "cut_preview": re.sub(r"\s+", " ", cut)[:70]})
        if args.fix:
            f.write_text("---" + fm + "---" + kept, encoding="utf-8", newline="\n")
            changed += 1

    print(f"扫描 {len(collect_files())} 个文件；命中 {len(report)} 篇；"
          + (f"已清理 {changed} 篇" if args.fix else "（检查模式，未改动）"))
    for r in sorted(report, key=lambda r: -r["cut_chars"]):
        extra = f" | 小图 {len(r.get('small_images', []))} 张" if r.get("small_images") else ""
        print(f"  {r['cut_chars']:>6} 字  {r['file'][:40]:<40} [{r['why'][:26]}]{extra} {r['cut_preview'][:40]}")
    if args.json:
        Path(args.json).write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
        print("报告 ->", args.json)


if __name__ == "__main__":
    main()
