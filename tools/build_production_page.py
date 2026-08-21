#!/usr/bin/env python3
"""Render PRODUCTION.md into the on-set HTML page. Single source: the Markdown."""
import re, html, sys, pathlib

SRC = pathlib.Path(sys.argv[1])
OUT = pathlib.Path(sys.argv[2])
md = SRC.read_text(encoding="utf-8")

# --- inline markdown -------------------------------------------------------
def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<!\*)\*(?!\*)([^*\n]+?)(?<!\*)\*(?!\*)', r'<em>\1</em>', s)
    return s

def chip_class(raw):
    """Shot chips encode what kind of shot it is — asset, script section, or boilerplate."""
    if raw.startswith('**'):
        return 'asset'
    if raw.startswith('*'):
        return 'section'
    return 'plain'

def render_shots(body):
    parts = [p.strip() for p in body.split('→')]
    chips = ''.join(
        f'<span class="chip {chip_class(p)}">{inline(p)}</span>' for p in parts if p)
    return f'<div class="shots" role="list"><span class="shots-label">Shots</span>{chips}</div>'

# --- block parse -----------------------------------------------------------
CH_SLUG = {}
out, i = [], 0
lines = md.split('\n')
in_card = False
chapter_n = 0

def close_card():
    global in_card
    if in_card:
        out.append('</article>')
        in_card = False

while i < len(lines):
    ln = lines[i]

    # table
    if ln.startswith('|') and i + 1 < len(lines) and re.match(r'^\|[-: |]+\|$', lines[i+1]):
        head = [c.strip() for c in ln.strip('|').split('|')]
        i += 2
        rows = []
        while i < len(lines) and lines[i].startswith('|'):
            rows.append([c.strip() for c in lines[i].strip('|').split('|')])
            i += 1
        th = ''.join(f'<th>{inline(c)}</th>' for c in head)
        tb = ''.join('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in r) + '</tr>' for r in rows)
        out.append(f'<div class="scroll"><table><thead><tr>{th}</tr></thead><tbody>{tb}</tbody></table></div>')
        continue

    # ordered list
    if re.match(r'^\d+\. ', ln):
        items = []
        while i < len(lines) and re.match(r'^\d+\. ', lines[i]):
            items.append(f'<li>{inline(re.sub(chr(94) + chr(92) + "d+. ", "", lines[i]))}</li>')
            i += 1
        out.append('<ol class="steps">' + ''.join(items) + '</ol>')
        continue

    # blockquote (may run several lines)
    if ln.startswith('> '):
        buf = []
        while i < len(lines) and lines[i].startswith('> '):
            buf.append(lines[i][2:])
            i += 1
        out.append(f'<aside class="callout">{inline(" ".join(buf))}</aside>')
        continue

    # chapter heading
    if ln.startswith('# ') and not ln.startswith('## '):
        title = ln[2:].strip()
        close_card()
        m = re.match(r'Chapter (\d)', title)
        if m:
            chapter_n = int(m.group(1))
            slug = f'ch{chapter_n}'
            CH_SLUG[chapter_n] = (slug, title)
            out.append(f'</section><section class="chapter" data-ch="{chapter_n}" id="{slug}">'
                       f'<h2 class="chapter-title">{inline(title)}</h2>')
        else:
            slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
            chapter_n = 0
            out.append(f'</section><section class="chapter" data-ch="0" id="{slug}">'
                       f'<h2 class="chapter-title">{inline(title)}</h2>')
        i += 1
        continue

    # section heading (## in source = top-level rules blocks)
    if ln.startswith('## '):
        close_card()
        title = ln[3:].strip()
        slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
        out.append(f'<h3 class="block-title" id="{slug}">{inline(title)}</h3>')
        i += 1
        continue

    # lesson card heading:  ### 1.1 · Title — 6.5 min
    if ln.startswith('### '):
        close_card()
        t = ln[4:].strip()
        m = re.match(r'^(\d+\.\d+[a-z]?) · (.+?) — ([\d.]+ min)(.*)$', t)
        if m:
            num, name, run, flag = m.groups()
            warn = ' warn' if '⚠' in flag else ''
            flagtag = ('<span class="flag">split candidate</span>' if '⚠' in flag else '')
            out.append(
                f'<article class="lesson{warn}" id="l{num.replace(".", "-")}">'
                f'<header class="lesson-head">'
                f'<span class="lnum">{num}</span>'
                f'<h4>{inline(name)}</h4>'
                f'<span class="runtime">{run}</span>{flagtag}</header>')
            in_card = True
        else:
            out.append(f'<h3 class="block-title">{inline(t)}</h3>')
        i += 1
        continue

    if ln.strip() == '---':
        i += 1
        continue

    if not ln.strip():
        i += 1
        continue

    # labelled paragraphs
    m = re.match(r'^\*\*Cold open:\*\* \*(.+)\*$', ln)
    if m:
        out.append(f'<div class="cold-open"><span class="co-label">Cold open — verbatim</span>'
                   f'<p>{inline(m.group(1))}</p></div>')
        i += 1
        continue
    m = re.match(r'^\*\*Shots:\*\* (.+)$', ln)
    if m:
        out.append(render_shots(m.group(1)))
        i += 1
        continue
    m = re.match(r'^\*\*(Diagram build|Code slides|Note):\*\*(.*)$', ln)
    if m:
        label, rest = m.group(1), m.group(2)
        kind = 'build' if label != 'Note' else 'plain'
        out.append(f'<p class="note {kind}"><span class="nlabel">{inline(label)}</span>{inline(rest)}</p>')
        i += 1
        continue

    out.append(f'<p>{inline(ln)}</p>')
    i += 1

close_card()
body = '\n'.join(out)
body = body.replace('</section>', '', 1)  # first synthetic close
body += '</section>'

nav = ''.join(
    f'<a class="navchip" data-ch="{n}" href="#{s}">{n}</a>'
    for n, (s, _t) in sorted(CH_SLUG.items()))

CSS = """
:root{
  --ground:#F5F6F8; --surface:#FFFFFF; --surface-2:#EDEFF3;
  --ink:#15181D; --ink-2:#4A515C; --ink-3:#7A828E;
  --line:#DDE1E7; --line-2:#C7CDD6;
  --accent:#1E4E8C; --accent-soft:#E8EEF7;
  --amber:#8A5A0B; --amber-soft:#F6EEDF;
  --warn:#9B3B2E;
  /* film script revision colours: white, blue, pink, yellow, green, goldenrod */
  --c1:#6F7681; --c2:#3D6E9E; --c3:#A85578; --c4:#8A6D18; --c5:#3E7458; --c6:#9A6528;
  --radius:6px;
  --mono:ui-monospace,SFMono-Regular,"SF Mono",Menlo,Consolas,"Liberation Mono",monospace;
  --sans:ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --ground:#0F1216; --surface:#161A20; --surface-2:#1E242C;
    --ink:#E4E7EC; --ink-2:#A2AAB6; --ink-3:#767F8C;
    --line:#272E37; --line-2:#39414C;
    --accent:#79A9E8; --accent-soft:#17273C;
    --amber:#D6A257; --amber-soft:#2A2216;
    --warn:#E08472;
    --c1:#9098A3; --c2:#6E9FCE; --c3:#D083A4; --c4:#C0A047; --c5:#6BA98A; --c6:#C89557;
  }
}
:root[data-theme="dark"]{
  --ground:#0F1216; --surface:#161A20; --surface-2:#1E242C;
  --ink:#E4E7EC; --ink-2:#A2AAB6; --ink-3:#767F8C;
  --line:#272E37; --line-2:#39414C;
  --accent:#79A9E8; --accent-soft:#17273C;
  --amber:#D6A257; --amber-soft:#2A2216;
  --warn:#E08472;
  --c1:#9098A3; --c2:#6E9FCE; --c3:#D083A4; --c4:#C0A047; --c5:#6BA98A; --c6:#C89557;
}
*{box-sizing:border-box}
body{
  margin:0; background:var(--ground); color:var(--ink);
  font-family:var(--sans); font-size:16px; line-height:1.62;
  -webkit-text-size-adjust:100%;
}
.wrap{max-width:860px; margin:0 auto; padding:0 20px 96px}

/* masthead */
.masthead{
  border-bottom:1px solid var(--line); background:var(--surface);
  padding:34px 0 22px; margin-bottom:34px;
}
.masthead .wrap{padding-bottom:0}
.eyebrow{
  font-family:var(--mono); font-size:11px; letter-spacing:.14em;
  text-transform:uppercase; color:var(--ink-3); margin:0 0 10px;
}
h1{
  font-size:clamp(26px,4.4vw,38px); line-height:1.14; letter-spacing:-.022em;
  font-weight:680; margin:0 0 14px; text-wrap:balance;
}
.meta{display:flex; flex-wrap:wrap; gap:8px 22px; margin:0 0 18px; padding:0; list-style:none}
.meta li{font-size:13.5px; color:var(--ink-2)}
.meta b{
  font-family:var(--mono); font-variant-numeric:tabular-nums;
  color:var(--amber); font-weight:600;
}
nav.jump{display:flex; align-items:center; gap:7px; flex-wrap:wrap; padding-bottom:4px}
nav.jump .lbl{
  font-family:var(--mono); font-size:10.5px; letter-spacing:.13em;
  text-transform:uppercase; color:var(--ink-3); margin-right:3px;
}
.navchip{
  font-family:var(--mono); font-size:12.5px; font-weight:600;
  width:28px; height:28px; display:grid; place-items:center;
  border-radius:var(--radius); text-decoration:none;
  color:var(--surface); background:var(--c1); transition:transform .12s ease;
}
.navchip[data-ch="1"]{background:var(--c1)} .navchip[data-ch="2"]{background:var(--c2)}
.navchip[data-ch="3"]{background:var(--c3)} .navchip[data-ch="4"]{background:var(--c4)}
.navchip[data-ch="5"]{background:var(--c5)} .navchip[data-ch="6"]{background:var(--c6)}
.navchip:hover{transform:translateY(-1px)}
.navchip:focus-visible{outline:2px solid var(--ink); outline-offset:2px}

/* structure */
section.chapter{margin:0 0 8px}
.chapter-title{
  font-size:22px; font-weight:670; letter-spacing:-.015em; margin:54px 0 4px;
  padding-left:14px; border-left:4px solid var(--c1); text-wrap:balance;
}
[data-ch="1"] .chapter-title{border-color:var(--c1)}
[data-ch="2"] .chapter-title{border-color:var(--c2)}
[data-ch="3"] .chapter-title{border-color:var(--c3)}
[data-ch="4"] .chapter-title{border-color:var(--c4)}
[data-ch="5"] .chapter-title{border-color:var(--c5)}
[data-ch="6"] .chapter-title{border-color:var(--c6)}
[data-ch="0"] .chapter-title{border-color:var(--line-2)}
.block-title{
  font-size:17px; font-weight:660; letter-spacing:-.008em;
  margin:46px 0 14px; padding-bottom:8px; border-bottom:1px solid var(--line);
}
p{margin:0 0 14px; color:var(--ink-2); max-width:66ch}
p strong{color:var(--ink); font-weight:640}
em{color:var(--ink); font-style:italic}
code{
  font-family:var(--mono); font-size:.87em; background:var(--surface-2);
  padding:.13em .4em; border-radius:3px; color:var(--ink);
}
a{color:var(--accent)}

/* lesson card */
.lesson{
  background:var(--surface); border:1px solid var(--line); border-radius:var(--radius);
  padding:18px 20px 6px; margin:0 0 14px;
}
.lesson.warn{border-color:var(--warn)}
.lesson-head{
  display:flex; align-items:baseline; gap:11px; flex-wrap:wrap;
  padding-bottom:13px; margin-bottom:14px; border-bottom:1px solid var(--line);
}
.lnum{
  font-family:var(--mono); font-size:12px; font-weight:650;
  font-variant-numeric:tabular-nums; color:var(--ink-3);
}
.lesson-head h4{
  font-size:16.5px; font-weight:640; letter-spacing:-.01em; margin:0;
  flex:1 1 auto; min-width:min(100%,14ch); color:var(--ink);
}
.runtime{
  font-family:var(--mono); font-size:12.5px; font-weight:640;
  font-variant-numeric:tabular-nums; color:var(--amber);
  background:var(--amber-soft); padding:2px 8px; border-radius:var(--radius);
  white-space:nowrap;
}
.flag{
  font-family:var(--mono); font-size:10.5px; letter-spacing:.07em;
  text-transform:uppercase; color:var(--warn); border:1px solid var(--warn);
  padding:1px 7px; border-radius:var(--radius); white-space:nowrap;
}

/* cold open — the line read to camera, set in the monospace of a shooting script */
.cold-open{
  background:var(--surface-2); border-left:3px solid var(--accent);
  border-radius:0 var(--radius) var(--radius) 0;
  padding:12px 15px; margin:0 0 15px;
}
.co-label{
  display:block; font-family:var(--mono); font-size:10px; letter-spacing:.13em;
  text-transform:uppercase; color:var(--ink-3); margin-bottom:7px;
}
.cold-open p{
  font-family:var(--mono); font-size:13.5px; line-height:1.66;
  color:var(--ink); margin:0; max-width:none;
}

/* shot sequence */
.shots{display:flex; align-items:center; flex-wrap:wrap; gap:6px; margin:0 0 15px}
.shots-label{
  font-family:var(--mono); font-size:10px; letter-spacing:.13em;
  text-transform:uppercase; color:var(--ink-3); margin-right:3px;
}
.chip{
  font-size:12.5px; line-height:1.35; padding:3px 9px; border-radius:var(--radius);
  border:1px solid var(--line-2); color:var(--ink-2); background:var(--surface);
}
.chip + .chip{position:relative; margin-left:11px}
.chip + .chip::before{
  content:"›"; position:absolute; left:-13px; top:50%; transform:translateY(-50%);
  color:var(--ink-3); font-size:13px;
}
.chip.section{color:var(--ink); border-color:var(--line-2)}
.chip.section em{font-style:normal}
.chip.asset{
  color:var(--accent); border-color:var(--accent); background:var(--accent-soft);
  font-weight:560;
}
.chip.asset strong{font-weight:640}
.chip.plain{color:var(--ink-3); border-style:dashed}

/* notes */
.note{
  font-size:14px; margin:0 0 13px; padding-left:13px;
  border-left:2px solid var(--line-2); color:var(--ink-2); max-width:64ch;
}
.note.build{border-left-color:var(--accent)}
.nlabel{
  display:inline-block; font-family:var(--mono); font-size:10px; letter-spacing:.12em;
  text-transform:uppercase; color:var(--ink-3); margin-right:8px;
}
.note.build .nlabel{color:var(--accent)}

.callout{
  background:var(--accent-soft); border:1px solid var(--line-2);
  border-radius:var(--radius); padding:14px 17px; margin:0 0 20px;
  font-size:14.5px; color:var(--ink-2); max-width:none;
}
.callout strong{color:var(--ink)}

ol.steps{margin:0 0 16px; padding-left:22px; max-width:64ch}
ol.steps li{margin-bottom:7px; color:var(--ink-2); font-size:14.5px}

/* tables */
.scroll{overflow-x:auto; margin:0 0 20px; border:1px solid var(--line); border-radius:var(--radius)}
table{border-collapse:collapse; width:100%; font-size:13.5px; background:var(--surface)}
th,td{padding:9px 13px; text-align:left; vertical-align:top; border-bottom:1px solid var(--line)}
th{
  font-family:var(--mono); font-size:10.5px; letter-spacing:.1em; text-transform:uppercase;
  color:var(--ink-3); font-weight:600; background:var(--surface-2); white-space:nowrap;
}
td{color:var(--ink-2)}
td strong{color:var(--ink)}
tbody tr:last-child td{border-bottom:none}
td:first-child{color:var(--ink); font-weight:520}

@media (max-width:560px){
  body{font-size:15px}
  .lesson{padding:15px 15px 4px}
  .chip{font-size:12px}
}
@media (prefers-reduced-motion:reduce){
  *{transition:none !important; animation:none !important}
}
"""

page = f"""<title>Production Notes — Data Fundamentals for Beginners</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>{CSS}</style>
<header class="masthead"><div class="wrap">
  <p class="eyebrow">Shooting reference · Shared foundation course</p>
  <h1>Production Notes — Recording This Course</h1>
  <ul class="meta">
    <li>39 videos</li>
    <li>Finished runtime <b>≈3h 25m</b></li>
    <li>27 lessons · 6 openers</li>
  </ul>
  <nav class="jump"><span class="lbl">Chapters</span>{nav}</nav>
</div></header>
<main class="wrap">
{body}
</main>"""

OUT.write_text(page, encoding="utf-8")
print(f"wrote {OUT}  ({len(page):,} bytes)")
