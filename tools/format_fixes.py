"""正文格式修复（固定工序，2026-10-14 王超：表格错误、大量格式乱码）。

处理三类转换器留下的机械毛病，都是渲染层问题、不动一个字：
1. 中英/标点混排处的 `**加粗**` 不满足 CommonMark 的 flanking 规则 → 改用 <strong>（站点开 unsafe）
2. 孤立列表符号行（一整行只有 `-` / `*` / `•`，下一段才是内容）→ 合并成正常的 `- 内容`
3. 孤立竖线行（一整行只有 `|` / `｜`，表格转换残留）→ 删除

用法：
    python3 tools/format_fixes.py          # 只检查
    python3 tools/format_fixes.py --fix    # 修改 content/posts 与 posts_extra
"""
import argparse
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BULLET_ONLY = re.compile(r"^\s*([-*•])\s*$")
PIPE_ONLY = re.compile(r"^\s*[|｜]\s*$")


def is_punct(ch):
    return bool(ch) and unicodedata.category(ch).startswith("P")


def is_space(ch):
    return ch == "" or ch.isspace()


def fix_bold(p):
    """把不符合 flanking 规则的 **粗体** 换成 <strong>（内容一字不改）。"""
    out, i = [], 0
    while True:
        o = p.find("**", i)
        if o < 0:
            out.append(p[i:])
            break
        c = p.find("**", o + 2)
        if c < 0:
            out.append(p[i:])
            break
        before_open = p[o - 1] if o > 0 else ""
        after_open = p[o + 2] if o + 2 < len(p) else ""
        before_close = p[c - 1]
        after_close = p[c + 2] if c + 2 < len(p) else ""
        left_ok = (not is_space(after_open)) and (not is_punct(after_open) or is_space(before_open) or is_punct(before_open))
        right_ok = (not is_space(before_close)) and (not is_punct(before_close) or is_space(after_close) or is_punct(after_close))
        inner = p[o + 2:c]
        out.append(p[i:o])
        out.append(("**" + inner + "**") if (left_ok and right_ok) else ("<strong>" + inner + "</strong>"))
        i = c + 2
    return "".join(out)


def fix_body(body):
    changed = []
    # 1) 逐段修加粗锚点（段落按空行切）
    paras = body.split("\n\n")
    new = []
    for p in paras:
        q = fix_bold(p)
        if q != p:
            changed.append("bold")
        new.append(q)
    body = "\n\n".join(new)

    lines = body.splitlines()
    # 2) 孤立竖线行删除；3) 孤立列表符号行与下一段内容合并
    out = []
    for i, l in enumerate(lines):
        if PIPE_ONLY.match(l):
            continue
        if BULLET_ONLY.match(l):
            mark = l.strip()
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines) and lines[j].strip() and not BULLET_ONLY.match(lines[j]):
                out.append(f"{mark} {lines[j].strip()}")
                changed.append("bullet")
                lines[j] = "\x00SKIP\x00"      # 标记已合并
                continue
        out.append(l)
    body = "\n".join(x for x in out if x != "\x00SKIP\x00")
    body = re.sub(r"\n{3,}", "\n\n", body).strip() + "\n"
    return body, sorted(set(changed))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fix", action="store_true")
    args = ap.parse_args()
    files = sorted((ROOT / "content" / "posts").glob("*.md")) + sorted((ROOT / "posts_extra").glob("*.md"))
    hits = []
    for f in files:
        text = f.read_text(encoding="utf-8")
        if not text.startswith("---"):
            continue
        _, fm, body = text.split("---", 2)
        fixed, kinds = fix_body(body)
        if kinds:
            hits.append((f.name, kinds))
            if args.fix:
                f.write_text("---" + fm + "---" + fixed, encoding="utf-8", newline="\n")
    print(f"扫描 {len(files)} 个文件；命中 {len(hits)} 篇"
          + ("（已修改）" if args.fix else "（检查模式）"))
    for name, kinds in hits[:30]:
        print(f"  {name[:56]:<56} {kinds}")


if __name__ == "__main__":
    main()
