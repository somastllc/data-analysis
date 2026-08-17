#!/usr/bin/env python3
"""Emit a .drawio source file and a matching .svg from one model, per DESIGN.md §6."""
import sys, html, pathlib
import xml.etree.ElementTree as ET

# ── DESIGN.md tokens ────────────────────────────────────────────────────────
INK="#121212"; WHITE="#FFFFFF"; MINT_DEEP="#1F7D3D"; MUTED="#6B7276"
MONO="'Noto Sans Mono', 'Liberation Mono', monospace"   # must match DESIGN.md §2

NODE_W, NODE_H, GAP, MARGIN = 140, 52, 24, 24
ROW_GAP = 44                         # between wrapped rows — a §3 spacing value
SHADOW_DX, SHADOW_DY = 3, 3          # hard offset, no blur — DESIGN.md §6
ARC = 8                              # corner radius in px, both renderers
LINE_H = 17                          # leading for a two-line node label

def layout(nodes, caption_below=None, per_row=None):
    """Positions for every node, as (x, y).

    per_row wraps the chain into rows and reverses every other one — a snake. The
    reversal is what keeps the row-to-row connector a plain vertical drop: the first
    node of row 2 sits directly under the last node of row 1. A left-to-right second
    row would need a connector that runs back across the whole diagram.

    Seven stages in one straight line is 1592px of artwork. On a 1920-wide slide
    that leaves the 13px node labels rendering at 13px — see DESIGN.md §7. Wrapped
    4 + 3 the same seven stages are 680px, which scales up to ~31px labels."""
    n = len(nodes)
    cols = per_row or n
    rows = -(-n // cols)
    w = MARGIN*2 + cols*NODE_W + (cols-1)*GAP
    h = MARGIN*2 + rows*NODE_H + (rows-1)*ROW_GAP + (28 if caption_below else 0)
    pts = []
    for i in range(n):
        row, col = divmod(i, cols)
        if row % 2:
            col = cols - 1 - col
        pts.append((MARGIN + col*(NODE_W+GAP), MARGIN + row*(NODE_H+ROW_GAP)))
    return w, h, pts, cols


def lines(label):
    """A node label is one or two lines; the break is authored with \\n."""
    return label.split("\n")

def svg_vertical(nodes, path, under=None):
    n=len(nodes); VGAP=22
    w = MARGIN*2 + NODE_W
    h = MARGIN*2 + n*NODE_H + (n-1)*VGAP + (26 if under else 0)
    o=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">',
       f'<rect width="{w}" height="{h}" fill="{WHITE}"/>',
       f'<style>.n{{font-family:{MONO};font-size:13px;font-weight:500;fill:{INK}}}'
       f'.u{{font-family:{MONO};font-size:11px;fill:{MUTED};letter-spacing:.08em}}</style>']
    ys=[MARGIN+i*(NODE_H+VGAP) for i in range(n)]
    cx=MARGIN+NODE_W/2
    for i in range(n-1):
        y1=ys[i]+NODE_H; y2=ys[i+1]
        o.append(f'<line x1="{cx}" y1="{y1+2}" x2="{cx}" y2="{y2-7}" stroke="{MINT_DEEP}" stroke-width="2.5"/>')
        o.append(f'<path d="M{cx},{y2-7} L{cx-4.5},{y2-14} L{cx+4.5},{y2-14} Z" fill="{MINT_DEEP}"/>')
    for i,label in enumerate(nodes):
        svg_node(o, MARGIN, ys[i], label)
    if under:
        o.append(f'<text class="u" x="{cx}" y="{ys[-1]+NODE_H+24}" text-anchor="middle">{html.escape(under)}</text>')
    o.append('</svg>')
    pathlib.Path(path).write_text("\n".join(o), encoding="utf-8"); return w,h

def svg_node(o, x, y, label, accent=False):
    stroke = MINT_DEEP if accent else INK
    sw = 2.5 if accent else 2
    o.append(f'<rect x="{x+SHADOW_DX}" y="{y+SHADOW_DY}" width="{NODE_W}" height="{NODE_H}" '   # hard offset shadow
             f'rx="{ARC}" fill="{INK}"/>')
    o.append(f'<rect x="{x}" y="{y}" width="{NODE_W}" height="{NODE_H}" rx="{ARC}" '
             f'fill="{WHITE}" stroke="{stroke}" stroke-width="{sw}"/>')
    ls = lines(label)
    cx = x + NODE_W/2
    first = y + NODE_H/2 + 4.5 - (LINE_H*(len(ls)-1))/2
    for k, ln in enumerate(ls):
        o.append(f'<text class="n" x="{cx}" y="{first + k*LINE_H}" '
                 f'text-anchor="middle">{html.escape(ln)}</text>')


def svg_arrow(o, p, q):
    """Straight connector between two adjacent nodes, in whichever of the three
    directions the layout put them: right, left, or down into the next row."""
    (x1, y1), (x2, y2) = p, q
    if y1 == y2:
        cy = y1 + NODE_H/2
        if x2 > x1:
            a, b = x1+NODE_W+2, x2-8
            head = f'M{b},{cy} L{b-7},{cy-4.5} L{b-7},{cy+4.5} Z'
        else:
            a, b = x1-2, x2+NODE_W+8
            head = f'M{b},{cy} L{b+7},{cy-4.5} L{b+7},{cy+4.5} Z'
        o.append(f'<line x1="{a}" y1="{cy}" x2="{b}" y2="{cy}" stroke="{MINT_DEEP}" stroke-width="2.5"/>')
    else:
        cx = x1 + NODE_W/2
        a, b = y1+NODE_H+2, y2-8
        head = f'M{cx},{b} L{cx-4.5},{b-7} L{cx+4.5},{b-7} Z'
        o.append(f'<line x1="{cx}" y1="{a}" x2="{cx}" y2="{b}" stroke="{MINT_DEEP}" stroke-width="2.5"/>')
    o.append(f'<path d="{head}" fill="{MINT_DEEP}"/>')


def svg(nodes, path, accent_index=None, under=None, background=True, reveal=None, per_row=None):
    """reveal=n paints only the first n nodes on the full-size canvas, for the
    one-node-per-beat slide builds required by PRODUCTION.md standing rule 7.
    Geometry comes from the whole model either way, so nothing shifts between frames."""
    shown = len(nodes) if reveal is None else reveal
    w, h, pts, _ = layout(nodes, under, per_row)
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">',
         *([f'<rect width="{w}" height="{h}" fill="{WHITE}"/>'] if background else []),
         f'<style>.n{{font-family:{MONO};font-size:13px;font-weight:500;fill:{INK}}}'
         f'.u{{font-family:{MONO};font-size:11px;fill:{MUTED};letter-spacing:.08em}}</style>']
    # edges first so nodes sit on top
    for i in range(len(nodes)-1):
        if i+2 > shown: break          # an arrow needs both of its nodes on screen
        svg_arrow(o, pts[i], pts[i+1])
    for i, label in enumerate(nodes[:shown]):
        svg_node(o, pts[i][0], pts[i][1], label, accent=(i == accent_index))
    # the caption names the whole flow, so it waits for the last node
    if under and shown == len(nodes):
        o.append(f'<text class="u" x="{w/2}" y="{pts[-1][1]+NODE_H+26}" text-anchor="middle">'
                 f'{html.escape(under)}</text>')
    o.append('</svg>')
    pathlib.Path(path).write_text("\n".join(o), encoding="utf-8")
    return w, h

def drawio(nodes, path, accent_index=None, under=None, per_row=None):
    w, h, pts, _ = layout(nodes, under, per_row)
    # absoluteArcSize makes arcSize a diameter in px, so the radius is ARC at any
    # node size. Plain arcSize is a percentage of min(w,h) and drifts with height.
    NODE = ("rounded=1;absoluteArcSize=1;arcSize=%d;"
            "fillColor=%s;strokeColor=%s;strokeWidth=%s;"
            "fontFamily=Noto Sans Mono;fontSize=13;fontColor=%s;align=center;verticalAlign=middle;html=1;")
    # draw.io's shadow=1 is a CSS drop-shadow: 2px 3px, 2px blur, 25% black. DESIGN.md
    # calls for a hard opaque offset, so the shadow is its own cell behind the node.
    SHADOW = ("rounded=1;absoluteArcSize=1;arcSize=%d;fillColor=%s;strokeColor=none;"
              "html=1;movable=0;resizable=0;deletable=0;editable=0;connectable=0;" % (ARC*2, INK))
    GROUP = "group;html=1;"
    # Perimeter spacings put the endpoints where the SVG puts them: +2 off the source,
    # 8 short of the target. draw.io pulls a filled marker back by strokeWidth*1.118
    # (2.795 at 2.5), so the target spacing carries that back out. Marker length is
    # endSize+strokeWidth; block markers are as wide as they are long, so 8 splits the
    # difference against the SVG's 7-long, 9-wide head.
    EDGE = ("edgeStyle=orthogonalEdgeStyle;rounded=1;strokeColor=%s;strokeWidth=2.5;"
            "endArrow=block;endFill=1;endSize=5.5;"
            "sourcePerimeterSpacing=2;targetPerimeterSpacing=5.2;html=1;" % MINT_DEEP)
    UND  = ("text;html=1;fillColor=none;strokeColor=none;fontFamily=Noto Sans Mono;fontSize=11;"
            "fontColor=%s;align=center;" % MUTED)
    cells = []
    for i, label in enumerate(nodes):
        st = NODE % (ARC*2, WHITE, MINT_DEEP if i == accent_index else INK,
                     "2.5" if i == accent_index else "2", INK)
        x, y = pts[i]
        # html=1 is already on the node style, so the authored \n becomes a <br>.
        # Escape ONCE, over the joined string: a raw `<` is illegal inside an XML
        # attribute and draw.io refuses the whole file with "Not a diagram file".
        # It un-escapes the attribute first, then parses the result as HTML.
        value = html.escape("<br>".join(lines(label)), quote=True)
        # node and its shadow travel together, so a hand edit cannot separate them
        cells.append(f'<mxCell id="g{i}" value="" style="{GROUP}" vertex="1" connectable="0" '
                     f'parent="1"><mxGeometry x="{x}" y="{y}" width="{NODE_W+SHADOW_DX}" '
                     f'height="{NODE_H+SHADOW_DY}" as="geometry"/></mxCell>')
        cells.append(f'<mxCell id="s{i}" value="" style="{html.escape(SHADOW,quote=True)}" '
                     f'vertex="1" parent="g{i}"><mxGeometry x="{SHADOW_DX}" y="{SHADOW_DY}" '
                     f'width="{NODE_W}" height="{NODE_H}" as="geometry"/></mxCell>')
        cells.append(f'<mxCell id="n{i}" value="{value}" style="{html.escape(st,quote=True)}" '
                     f'vertex="1" parent="g{i}"><mxGeometry x="0" y="0" width="{NODE_W}" '
                     f'height="{NODE_H}" as="geometry"/></mxCell>')
    for i in range(len(nodes)-1):
        cells.append(f'<mxCell id="e{i}" style="{html.escape(EDGE,quote=True)}" edge="1" parent="1" '
                     f'source="n{i}" target="n{i+1}"><mxGeometry relative="1" as="geometry"/></mxCell>')
    if under:
        cells.append(f'<mxCell id="cap" value="{html.escape(under)}" style="{html.escape(UND,quote=True)}" '
                     f'vertex="1" parent="1"><mxGeometry x="{MARGIN}" y="{pts[-1][1]+NODE_H+8}" '
                     f'width="{w-2*MARGIN}" height="20" as="geometry"/></mxCell>')
    xml = (f'<mxfile host="app.diagrams.net">\n'
           f'  <diagram name="Page-1">\n'
           f'    <mxGraphModel dx="{w}" dy="{h}" grid="0" gridSize="8" guides="1" tooltips="1" '
           f'connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{w}" pageHeight="{h}" '
           f'math="0" shadow="0" background="{WHITE}">\n'
           f'      <root>\n        <mxCell id="0"/>\n        <mxCell id="1" parent="0"/>\n        '
           + "\n        ".join(cells) +
           f'\n      </root>\n    </mxGraphModel>\n  </diagram>\n</mxfile>\n')
    # Parse it back before writing. draw.io rejects a malformed file outright with
    # "Not a diagram file", and the first multi-line label shipped a raw `<` inside
    # an attribute — which only surfaced by opening it in the editor. This is the
    # cheap half of that check; the editor is still the other half.
    ET.fromstring(xml)
    pathlib.Path(path).write_text(xml, encoding="utf-8")

# ── the course diagram register ─────────────────────────────────────────────
# Every diagram in the course is declared here. Run with no arguments to
# regenerate all of them in place; pass a directory to write elsewhere.
REGISTER = [
    ("01-what-is-data/diagrams",      "01-01-data-to-insight",
     ["Data", "Information", "Insight"],
     "raw facts become a conclusion you can act on", "raw facts to conclusion", None),
    ("02-the-data-ecosystem/diagrams", "02-05-data-pipeline",
     ["Collect", "Store", "Clean", "Transform", "Analyze", "Share"],
     "the path data follows from source to use", "source to use", None),
    # PRODUCTION.md 3.1: the map for the whole chapter, rebuilt as a locator card at
    # the top of 3.2–3.6 with the current step accented. Wrapped 4 + 3 — seven boxes
    # in one line is unreadable on a slide, see layout().
    ("03-the-data-analysis-process/diagrams", "03-01-analysis-process",
     ["Define\nproblem", "Ask\nquestions", "Collect data", "Clean data",
      "Analyze and\nvisualize", "Communicate\ninsights", "Make\ndecisions"],
     "every stage depends on the question you asked first", "question first", 4),
]

if __name__ == "__main__":
    override = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else None
    root = pathlib.Path(__file__).resolve().parent.parent
    for folder, name, nodes, cap_h, cap_v, per_row in REGISTER:
        out = override or (root / folder)
        out.mkdir(parents=True, exist_ok=True)
        w, h = svg(nodes, out / f"{name}.svg", under=cap_h, per_row=per_row)
        svg(nodes, out / f"{name}-embed.svg", under=cap_h, background=False, per_row=per_row)
        drawio(nodes, out / f"{name}.drawio", under=cap_h, per_row=per_row)
        vw, vh = svg_vertical(nodes, out / f"{name}-vertical.svg", under=cap_v)
        print(f"{name:<26} {w}x{h} horizontal · {vw}x{vh} vertical · +embed +drawio")
