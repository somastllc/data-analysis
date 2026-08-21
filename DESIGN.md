# Visual Design Lock-in

The single source of truth for every visual asset in this course: PDF handouts, lesson slides, and `.drawio` diagrams. Nothing gets generated until it conforms to this file, and nothing here changes without changing this file first.

**Reference for layout and spacing:** `MCP-field-guide.pdf` in this folder — its restraint, its generous margins, and its habit of leaving the bottom of a page empty rather than filling it.
**Reference for color:** the three brand swatches below. Nothing else.
**Deliberately simpler than the reference:** one accent instead of two, no illustration, no emoji, fewer component types.

---

## 1. Color

Three brand colors. Everything else is a neutral derived from them.

| Token | Hex | Role |
|---|---|---|
| `--mint` | `#3ACC69` | The accent. Shapes, fills, rules, bars, borders. |
| `--ink` | `#121212` | Headings, strong text, diagram strokes. |
| `--paper` | `#F6F8F8` | Panel and plate fill. **Not** the page ground. |

### The rule that governs everything

**Mint on paper measures 1.97:1. It fails WCAG for text at any size, and it will disappear in print and on a projector.**

> **Mint is a shape color, never a text color on a light ground.**
> For mint-colored *text* on white or paper, use **`--mint-deep` `#1F7D3D`** (5.17:1 on white, 4.85:1 on paper).
> On an ink ground, mint text is fine — `#3ACC69` on `#121212` is 8.94:1.

### Full ramp

The page ground is **white**, and `--paper` is the panel fill sitting on it. This is how the reference works: white page, tinted plates.

| Token | Hex | On white | On paper | Permitted use |
|---|---|---|---|---|
| `--ink` | `#121212` | 18.73:1 | 17.57:1 | Headings, strong text, diagram strokes |
| `--body` | `#43494C` | 9.15:1 | 8.58:1 | Body copy |
| `--muted` | `#6B7276` | 4.89:1 | 4.59:1 | Eyebrows, captions, axis labels |
| `--faint` | `#9AA1A5` | 2.62:1 | — | Non-text only: tick marks, dividers |
| `--hairline` | `#DDE2E2` | 1.31:1 | — | Rules, panel borders, gridlines |
| `--panel` | `#F6F8F8` | 1.07:1 | — | Plate and card fill |
| `--panel-2` | `#EDF1F1` | 1.14:1 | — | Caption strip under a plate |
| `--mint` | `#3ACC69` | 2.10:1 | 1.97:1 | **Shapes only.** Fills, bars, rules, borders |
| `--mint-deep` | `#1F7D3D` | 5.17:1 | 4.85:1 | **Mint-colored text**, small mint marks |
| `--white` | `#FFFFFF` | — | — | Page ground, node fill in diagrams |

### Semantic color

Semantic states are separate from the accent and never borrow it.

| Token | Hex | Meaning |
|---|---|---|
| `--warn` | `#A8452F` | A dishonest or broken thing — the truncated axis, a bias source |
| `--good` | `#1F7D3D` | The corrected version. Same value as `--mint-deep`; that is intentional |

Chapter 5 is the only place `--warn` appears. Everywhere else the palette is mint, ink, paper.

### Dark ground (chapter openers only)

The inverted ground is `#121212`, text `#F6F8F8`, accent `#3ACC69` at full strength. It belongs to the six chapter-opener bumpers, which are their own videos.

**A lesson deck never uses it** — not even for its first and last slide. Inverting the ends makes one screen recording flash dark, light, dark, which reads as three videos cut together. See §7.

Never invert PDF or `.drawio` — they get printed.

---

## 2. Typography

Three roles, matching the reference's structure.

| Role | Family | Where |
|---|---|---|
| **Display** | **Noto Serif**, Liberation Serif, serif | Page and section headings only |
| **Body** | **Noto Sans**, Liberation Sans, sans-serif | All running text, node labels in diagrams |
| **Data** | **Noto Sans Mono**, Liberation Mono, monospace | Eyebrows, plate titles, numbers, code, axis ticks, diagram labels |

> **These three are named because they are installed and verified**, each with 6 weight variants. An earlier draft specified Charter, Segoe UI, and Menlo — **none of which exist on this machine.** The pages still rendered, because CSS fell through to the generic `serif` / `sans-serif` keyword, so the document's actual typefaces were chosen by fontconfig rather than by design, and would change on any other machine.
>
> **The same stack must be used in HTML/CSS and inside every generated SVG.** They were different in the first test — the page set in Liberation Mono while the embedded diagram set in Noto Sans Mono, putting two monospace faces on one page.
>
> WeasyPrint embeds and subsets every face into the PDF (verified with `pdffonts`), so output is portable once the stack is deterministic.

The serif display against a sans body is the reference's defining move and the reason its pages read as a document rather than a webpage. Keep it.

### Scale

| Step | Size / line-height | Weight | Tracking | Use |
|---|---|---|---|---|
| Eyebrow | 11 / 1.4 | 600 | `.15em` | Mono, uppercase, `--muted` |
| H1 | 32 / 1.15 | 700 | `-.015em` | Serif, `--ink` |
| H2 | 22 / 1.25 | 700 | `-.01em` | Serif, `--ink` |
| Lead | 16 / 1.65 | 400 | 0 | Sans, `--body` |
| Body | 15.5 / 1.62 | 400 | 0 | Sans, `--body` |
| Plate title | 13 / 1.3 | 600 | `.12em` | Mono, uppercase, `--ink` |
| Caption | 13.5 / 1.55 | 400 | 0 | Sans, `--muted` |
| Data / node label | 13 / 1.4 | 500 | 0 | Mono, `--ink` |
| Micro | 11 / 1.4 | 500 | `.08em` | Mono, `--muted` — under-node labels |

Numerals in any table, axis, or step marker use `font-variant-numeric: tabular-nums`. Running text stays at or under **68 characters** per line.

---

## 3. Spacing

One scale. Every gap is a member of it — no arbitrary values.

```
4  ·  8  ·  12  ·  16  ·  24  ·  32  ·  48  ·  64  ·  96
```

| Gap | Value |
|---|---|
| Eyebrow → H1 | 24 |
| H1 → lead | 24 |
| Lead → first plate or rule | 48 |
| Between plates | 48 |
| Plate inner padding | 24 |
| Plate → its caption strip | hairline, then 16 padding |
| Between body paragraphs | 16 |
| Section → next section | 64 |

### The rule that carries the reference's feel

**Pages are top-aligned and never filled.** Content ends where it ends; the bottom of the page stays empty. Do not pad, stretch, or add filler to reach the bottom margin. Half-empty pages are the intended look — that emptiness is what makes the pages feel considered rather than crammed.

---

## 4. Page geometry — PDF

| Property | Value |
|---|---|
| Size | A4 portrait, 210 × 297 mm |
| Margins | 12 mm left/right, 18 mm top, 20 mm bottom |
| Content width | 186 mm (≈ 700 px at 96 dpi) |
| Columns | One. Card grids may split it into two. |
| Ground | White. `--paper` appears only inside panels. |

**Footer** on every page except the first: hairline rule, then descriptive text left in sans `--muted` 11px, page marker right in mono `--muted`.

**Build path:** HTML + CSS → **WeasyPrint**. See §9 — this was tested against the alternatives and is the only path that renders this design faithfully.

> **Do not use `soffice --headless --convert-to pdf` for designed pages.** It produces a valid PDF, but it drops embedded SVG to bare text, discards panel background fills, ignores flex layout, and inflates line-height. It is fine for plain prose, useless for this system. This was found by testing, after the path had already been written into an earlier draft of this file.

---

## 5. Components

Six. The reference has more; we are deliberately simpler.

### 5.1 Page header
Eyebrow (mono, uppercase, `--muted`) → H1 (serif, `--ink`, one word may take `--mint-deep`) → lead paragraph (sans, `--body`, max 68ch). Nothing else above the first plate.

### 5.2 Plate
The workhorse. A figure with its explanation attached.

```
┌─────────────────────────────────────────┐
│ PLATE TITLE            (mono, uppercase) │  fill --panel
│                                          │  padding 24
│            [ the diagram ]               │
│                                          │
├──────────────────────────────────────────┤  hairline
│ Caption. One or two sentences saying     │  fill --panel-2
│ what the reader should take from it.     │  padding 16, sans --muted
└──────────────────────────────────────────┘
```

No border on the outer panel — the fill alone separates it from the white page.

### 5.3 Callout
For a single sentence that must not be missed. Left bar 4px `--mint`, fill `--panel`, mono uppercase label in a 96px left gutter, body right.

One per page maximum.

### 5.4 Numbered step
Large mono numeral (`--mint-deep`, 26px) · bold sans title · body · optional inset mono strip on `--panel-2` separated by a hairline. Used only where the content is a genuine sequence.

### 5.5 Card grid
Two columns. Serif H2, optional outlined pill label (mono uppercase, 1px `--mint-deep` border, transparent fill), body, optional mono list with `›` markers in `--faint`.

### 5.6 Term table
Two columns — term in mono `--ink`, definition in sans `--body`. Rows separated by hairlines, no outer border, no zebra striping. This is how `GLOSSARY.md` and every `## Key Terms` table renders.

**Not carried over from the reference:** illustration/robot art, emoji, dual accent colors, roman-numeral index grids, the colored top-bar card variant.

---

## 6. Diagrams — `.drawio`

All 9 course diagrams become `.drawio` files so they stay editable, and export to SVG for slides and PDF for print. `.drawio` is XML and is written directly — no tooling needed.

### Canvas
Page background white. Grid off. No page shadow. Export with a 12px margin.

### Node — standard

The reference's defining diagram move is a **hard offset shadow, no blur** — it reads as a sticker rather than a CSS card, and it survives being printed in black and white.

```
style="rounded=1;absoluteArcSize=1;arcSize=16;
       fillColor=#FFFFFF;strokeColor=#121212;strokeWidth=2;
       fontFamily=Noto Sans Mono;fontSize=13;fontColor=#121212;
       align=left;spacingLeft=12;
       verticalAlign=middle;html=1;"
```
Default size **200 × 52**, or **140 × 52** for single-word stages. Snap to an 8px grid.

**`absoluteArcSize=1` is required, and `arcSize` is then a diameter.** Plain `arcSize` is a
percentage of the shape's shorter side, so `arcSize=12` gives a 6.24px radius on a 52px-tall
node and a different radius on every other node size. `absoluteArcSize=1;arcSize=16` gives 8px
everywhere, which is what the SVG draws.

**The shadow is its own cell, not `shadow=1`.** Verified in the draw.io editor: `shadow=1`
renders as CSS `drop-shadow(… 2px 3px 2px)` at 25% black — offset by 2/3, blurred by 2, and
translucent. That is the CSS card this section exists to avoid. The hard shadow is a second
rounded rect behind the node, same size, offset **+3/+3**, filled `--ink`, no stroke:

```
style="rounded=1;absoluteArcSize=1;arcSize=16;fillColor=#121212;strokeColor=none;html=1;
       movable=0;resizable=0;deletable=0;editable=0;connectable=0;"
```

Node and shadow go in a `group` cell sized 143 × 55, shadow first so the node paints over it.
Grouping is not cosmetic: without it a hand edit in the editor moves the node and leaves the
shadow behind. Edges still attach to the node cell inside the group.

**A line break in a node label is `&lt;br&gt;`, not `<br>`.** A raw `<` inside an XML attribute
is illegal, and draw.io refuses the entire file with *"Not a diagram file (Unescaped '<' not
allowed in attributes values)"* — not the one label, the whole diagram. Escape once over the
joined string; draw.io un-escapes the attribute and then parses the result as HTML, which is
why `html=1` on the node style is required for the break to take. `gen_diagram.py` now parses
each `.drawio` back with ElementTree before writing it, which catches this class of defect
without opening a browser.

`align=left;spacingLeft=12` is for nodes carrying a label *and* a value. **Single-word nodes are centered** (`align=center`) — left-aligning one word in a 140px box looks like a mistake.

### Node — accent
The node the diagram is *about*. Same as standard, plus `strokeColor=#1F7D3D;strokeWidth=2.5`. Never fill a node with `#3ACC69` and put text on it unless the text is `--ink`.

### Node — hub
Where several paths converge: `shape=hexagon`, `strokeColor=#1F7D3D`, fill `#FFFFFF`.

### Group boundary
```
style="rounded=1;absoluteArcSize=1;arcSize=12;fillColor=none;
       strokeColor=#1F7D3D;strokeWidth=1.5;dashed=1;dashPattern=6 4;
       verticalAlign=top;align=left;spacingLeft=10;spacingTop=6;
       fontFamily=Noto Sans Mono;fontSize=11;fontColor=#6B7276;html=1;"
```

### Edges

**Flow arrows carry the accent.** Nodes are ink on white; the movement between them is mint-deep. Without this, a plain process diagram — which is most of this course — contains no brand color at all. Found by rendering the first one and seeing a monochrome picture.

| Meaning | Style |
|---|---|
| Normal flow | `strokeColor=#1F7D3D;strokeWidth=2.5;endArrow=block;endFill=1;rounded=1` |
| Protocol / good path | add `dashed=1;dashPattern=8 4;strokeColor=#1F7D3D` |
| Problem / bespoke path | add `dashed=1;dashPattern=3 3;strokeColor=#A8452F` |
| Feedback loop (5.3) | normal flow plus `curved=1`, label `repeats` in mono `--muted` |

Edge labels: mono 11px, `--muted`, `labelBackgroundColor=#FFFFFF`.

**Endpoints.** An arrow starts 2px clear of its source and its tip stops 8px short of its
target — the gap is what keeps a row of boxes from reading as one welded bar. In `.drawio`
that is `sourcePerimeterSpacing=2;targetPerimeterSpacing=5.2`: draw.io pulls a filled marker
back by `strokeWidth × 1.118` (2.795 at 2.5), and the target spacing carries that back out.
`endSize=5.5` gives an 8px head — draw.io's block marker is always as wide as it is long, so
8 is the closest single number to the SVG's 7-long, 9-wide head.

### Under-node caption
A borderless text cell below the node — mono 11px `--muted`, e.g. `the model`, `one protocol`. Used sparingly, to name a thing the node itself cannot.

### Long chains wrap into a snake

**Four stages is the most that fits one row.** Seven boxes in a straight line is 1592px of
artwork; displayed in a 1632px slide plate that is a scale of 1.02, so the 13px node labels
render at 13px on a 1920-wide slide — unreadable. Wrapped 4 + 3 the same seven stages are
680px, which scales up to ~31px.

`gen_diagram.py`'s `per_row` wraps the chain and **reverses every other row**. The reversal is
what keeps the row-to-row connector a plain vertical drop: the first node of row 2 sits
directly under the last node of row 1. A left-to-right second row would need a connector
running back across the whole diagram, which is the thing that makes wrapped flowcharts hard
to read.

Node labels break onto a second line with `\n` in the model. Two lines is the limit at
140 × 52.

### Locator card

A wrapped process diagram doubles as a locator: same artwork, `accent_index` set to the
current stage, caption replaced with `step N of M`. `PRODUCTION.md` uses this at the top of
lessons 3.2–3.6 to place each one inside the chapter's process.

### Orientation
Every diagram is generated in **two layouts from one model**:

- **Horizontal** — for 16:9 slides. A 6-node flow lands near 1008px wide.
- **Vertical** — for A4 portrait pages. The same 6 nodes come to 188 × 496, which drops into a plate at **full size with no scaling**, so node text stays at its specified 13px. Scaling a horizontal diagram down to the 700px content width would render that text at ~9px, which is unreadable in print.

### Background
Diagram SVGs ship in two variants:

- **Standalone** (`*.svg`) — paints its own white background. For opening on its own or handing to someone.
- **Embedded** (`*-embed.svg`) — **no background rect.** Required inside a plate; a self-painted white box on a `--panel` fill shows as an obvious lighter rectangle.

### Naming
`NN-chapter-slug/diagrams/NN-slug.drawio`, plus `.svg`, `-embed.svg`, `-vertical.svg` and `.pdf` alongside. The `.drawio` is the editable source; every export is generated from the same model and never hand-edited.

---

## 7. Slides

HTML, built from the shot sequences already in `PRODUCTION.md`.

> This section is the **look**. `SLIDES.md` is the **procedure** — how to turn a given lesson
> into a deck, in what order, and what to check before it ships. Read that one when building.

| Property | Value |
|---|---|
| Aspect | 16:9, 1920 × 1080 |
| Safe area | 96px all sides |
| Ground | **White, for every slide of a lesson deck.** Ink `#121212` is reserved for the six chapter-opener bumpers |
| Type scale | Multiply the PDF scale by **2.2** — slide body ≈ 34px |
| Words per slide | **One idea per slide, in the lesson's own words** — see below. ~45 in practice. |
| Reading measure | 44ch, not the page's 68ch. Slide prose is read at a distance in one pass. |
| Accent | Mint, on shapes and rules. One accent moment per slide. |

**Build order per lesson** comes from that lesson's `**Shots:**` line in `PRODUCTION.md` — one slide per chip. Diagram slides reveal one node per beat, per standing rule 7. Key Terms is an end card and is **never narrated** (rule 4).

### A slide break must be a beat in the lesson

Split a chip across slides **only where the narration actually stops** — the diagram build is three slides because rule 7 says one node per beat. Everything else stays whole:

- A heading, its lead sentence, and the table or list it introduces are **one slide**. The heading is how you introduce the thing; on its own it is a slide the presenter has nothing to say over.
- A list and the sentence that draws the conclusion from it are **one slide**.
- Nothing is stacked on top of the cold open. It ends on *"what is data?"*, which is the question the title card answers; a heading above it asks the same question twice.

A first draft ran 14 slides for lesson 1.1 by giving each heading its own frame. It is 12 now, and the two it lost were the two nobody would have spoken over.

### One ground

**Every slide in a lesson deck is on white.** An earlier draft opened and closed on ink for drama; the deck then flashed dark, light, dark across a single screen recording, which reads as three different videos cut together. The inverted ground is a real part of the system (§1) but it belongs to the chapter-opener bumpers, which are separate videos. `.slide.ink` and its color overrides stay in `tools/slides.css` for them.

### No shot names on screen

The deck carries the lesson, not the production notes. **"Cold open" is a shot name and never appears on a slide** — the video opens cold, and labelling the frame "cold open" is the on-screen equivalent of the greeting standing rule 1 exists to forbid. The first slide is the opening paragraph and nothing else.

Eyebrows that *are* the lesson's own labels stay: `By the end`, `Key terms`, the chapter/lesson metadata block, and the numbered section running heads.

### Slide text is the lesson's text

**Every text element on a slide is copied from the lesson Markdown, or from the handout where the handout already added a line.** Not paraphrased, not compressed into a headline. The only words that are ours are the eyebrows, which are running heads rather than content.

An earlier draft of the deck did the conventional thing — invented short headlines and put three data chips where the cold open should be — and it was wrong for this format. These decks are *screen-recorded while the lesson is narrated*, and the lesson Markdown **is** the script. A paraphrased slide therefore puts one set of words on screen and a different set in the presenter's mouth, and the viewer reads the mismatch.

That is what retires the old "under 25 words" rule. It is the right rule for a slide backing a live talk, where the speaker improvises around the deck. It is the wrong rule here, and following it cost the cold open its actual content.

`tools/build_slides.py` enforces this: every build prints
`verbatim: N/N text elements are the lesson's own words` and names any element that drifted. Lesson 1.1 is 44/44.

The cost is real and accepted: slides run ~50 words, so a viewer can read ahead of the narration. One idea per slide is what keeps that bounded — split a section across slides rather than letting one slide grow.

### Build path

Same as the PDF — HTML + CSS → WeasyPrint — with the page redeclared:

```css
@page { size: 20in 11.25in; margin: 0; }   /* exactly 1920 × 1080 at 96dpi */
```

WeasyPrint sizes in physical units, so declaring inches rather than pixels is what pins the
page. Verify with `pdfinfo`: it must report **1440 × 810 pts**. One slide per page,
`break-after:page`.

### One slide pixel = 1rem

**Every length in `tools/slides.css` is in `rem`, and the root font size is the only thing
that differs between the two media:**

```css
html            { font-size: 1px }                              /* print: 1rem = 1px */
@media screen   { html { font-size: min(100vw / 1920, 100vh / 1080) } }
```

On screen that makes the whole slide scale to fit whichever edge of the window runs out
first, at any size, **with no JavaScript** — `min()` of two lengths, and `ch`-based measures
come along for free because `ch` is font-relative. In print the same stylesheet reproduces
the design at exactly 1920 × 1080. The two renderings were diffed pixel by pixel across all
12 slides after the conversion: identical.

The HTML matters because it, not the PDF, is what gets screen-recorded — a browser gives you
a chrome-free 16:9 surface and arrow-key paging. Before this it laid out a fixed 1920px box
and overflowed every window narrower than that.

Two things stay in `px` on purpose:

- **Hairlines and borders.** A 1px rule scaled to 0.6px is a rule that disappears on half the screens it lands on.
- **Nothing else.** Inline styles in `build_slides.py` are slide pixels too, so they are `rem` as well.

Screen mode also makes the deck a viewer: `scroll-snap-type:y mandatory` on `html`, `scroll-snap-align:center` on the slide, so one scroll or arrow key advances exactly one frame — verified as `scrollHeight == slides × viewportHeight`. The scroll container is declared on `html`, not left to propagate up from `body`. The surround is `#1A1C1C`; recording a 16:9 window fills it edge to edge and the surround never appears.

**The scrollbar is hidden** (`scrollbar-width:none`). This is not cosmetic: a visible scrollbar sits inside `100vw` but outside the usable width, so on any window narrower than 16:9 — where width is the binding edge — the slide came out ~15px wider than the space it had. Measured before and after at 1360px: usable width 1345 → 1360.

**What "fits" means here.** The slide *box* fits the viewport exactly on the binding edge — measured `heightGap=0`, ratio 1.778, and the letterboxing appears on the other axis. What does *not* fill the frame is the **content**, and that is deliberate: §3's rule that pages are top-aligned and never filled applies to slides too. If a slide should look fuller, the lever is page geometry — a smaller safe area or a larger type scale — not padding the content out.

Reference implementation: `tools/slides.css` + `tools/build_slides.py`, proven on lesson 1.1
in `samples/01-01-what-is-data-slides.pdf` (12 slides).

### Diagram builds

`gen_diagram.py`'s `svg(..., reveal=n)` paints the first *n* nodes on the **full-size canvas**,
so a node lands in its final position the moment it appears and nothing reflows between beats.
Frames are inlined into the HTML, not written beside the deck — they are intermediate.

Diagrams are scaled **up** on slides (516px artwork to 1400px, node labels 13px → ~35px).
That is the opposite of the print case and it is fine: §6 rejects scaling *down*, which is
what drops node text to ~9px.

### On an ink ground, restate every color

`.slide.ink` inverts the ground but not the tokens, and three of them are wrong by default:

| Element | Light-ground value | On ink |
|---|---|---|
| Term column | `--ink` — **invisible on `--ink`** | `--mint` (8.94:1; the only ground where mint may carry text) |
| Table rules | `--hairline` — reads as bright white | `#2E3232` |
| Column heads | `--muted` — 3.4:1 | `--faint` |

Found by rendering the Key Terms end card and seeing a table with an empty first column.

### The `max-width` trap, again

`.plate-title` needs `max-width:none` for the same reason `.plate-cap` does (§9) — otherwise it
inherits the `p` reading measure and wraps a four-word title onto two lines. Any new block-level
`<p>` that is a label rather than prose needs the same override.

---

## 8. Conformance

Before any asset ships:

- [ ] Every color is a token from §1 — no one-off hex values
- [ ] `#3ACC69` carries no text on a light ground anywhere
- [ ] Every gap is a member of the §3 scale
- [ ] Serif for headings, sans for body, mono for data — no substitutions
- [ ] Running text at or under 68 characters
- [ ] Numerals in tables and axes are tabular
- [ ] Page bottoms left empty rather than padded
- [ ] Diagrams legible in pure black and white — color never the only signal
- [ ] `.drawio` source committed alongside every exported `.svg`/`.pdf`

### Precedence

This file, then `PRODUCTION.md` for shot and timing decisions, then the lesson Markdown for content. Where they disagree, the lesson content wins on *what* is said and this file wins on *how* it looks.

---

## 9. Verified toolchain

Everything below was run on this machine and its output inspected. Nothing here is assumed.

| Need | Tool | Status |
|---|---|---|
| HTML/CSS → PDF | **WeasyPrint 69.0** in `scratchpad/.venv` | ✅ Renders panels, flex, embedded SVG, hairlines, letter-spacing correctly |
| HTML → PDF | `soffice --headless` | ❌ **Rejected.** Drops SVG, backgrounds, and layout |
| SVG → PDF / PNG | `rsvg-convert` | ✅ Vector-faithful; used for standalone diagram export |
| Merge page PDFs | `pdfunite` | ✅ Available |
| Raster / inspection | ImageMagick `magick` | ✅ Available |
| Diagram preview + shape search | `@drawio/mcp`, user scope | ✅ **Used.** `open_drawio_xml`, `open_drawio_mermaid`, `search_shapes`, `list_pages`, `get_page`, `set_page` |
| Reading what draw.io actually drew | draw.io in Chrome + `claude-in-chrome` | ✅ Open with `&dark=0&ui=min`, then read the canvas SVG's `rect`/`path` attributes from the DOM |

```bash
# one-time
python3 -m venv .venv && .venv/bin/pip install weasyprint

# page → PDF
.venv/bin/weasyprint page.html page.pdf

# standalone diagram → PDF
rsvg-convert -f pdf -o diagram.pdf diagram.svg
```

**On the MCP server.** It *opens* diagrams in the draw.io editor and searches its shape libraries — it does **not** generate the course's files. `.drawio` files are authored directly as XML from the same generator that emits the SVG, which is what keeps the two from diverging. The MCP is for previewing the result and for finding shapes.

**Previewing is not verifying.** `open_drawio_xml` hands the diagram to the browser; nothing
comes back. To actually check what draw.io drew, open the returned URL in a tab with
`&dark=0` (dark mode inverts the canvas and hides a black shadow on white) and `&ui=min`, then
read the rendered `rect` and `path` attributes out of the canvas SVG. That is how the three
defects in §6 were found — every one of them produced valid XML and a wrong picture.

### Two CSS rules that are easy to get wrong

- `.plate-cap` needs `max-width:none`. It inherits the `p { max-width:68ch }` reading measure otherwise and stops short of the plate edge — visible as a caption strip that does not reach the right side. `.plate-title` has the same problem on slides — see §7.
- Embedded diagram SVGs need `style="width:100%;height:auto"` and a `viewBox`, or they render at intrinsic size and overflow the plate.
- **`font-weight` must be a multiple of 100.** An earlier draft used `640` for `strong` in `lesson.css`; WeasyPrint logs `Ignored font-weight:640, invalid value` and falls back to normal, so bold-in-body was silently not bold in the first sample PDF. It is `600` now in both stylesheets.

---

## 10. How to test before generating the real assets

Generating 27 lessons × (page + slides + diagram) is ~40 assets. A defect in the system multiplies by 40. So the system gets proven on a deliberately hostile sample first.

### The mistake to avoid

The first test used lesson 2.5 — short prose, one table, one diagram. It proved almost nothing, because it is an easy page. **Test the worst cases, not the average one.**

### Stage 0 — determinism (do this first, it invalidates everything else)

- [x] Every font family in §2 is actually installed — verified with an exact-name `fc-list` check, not `fc-match`, which always returns a best guess and never reports "missing"
- [x] The HTML/CSS stack and the SVG generator stack are the **same** — otherwise one page carries two different monospace faces
- [x] `pdffonts` shows every face embedded and subset, so output is portable

### Stage 1 — the stress set

Seven files. **26% of the course, 100% of its structural features.** Derived by inventorying every lesson, not chosen by feel.

| File | What it is the only test of |
|---|---|
| `04/02-why-data-work-uses-code` | The only code blocks in the course — SQL and Python |
| `05/01-responsible-and-ethical-use` | The ASCII chart pair, which must become a real custom visual |
| `05/04-data-governance-and-regulations` | A 12-row narrative table |
| `06/02-putting-it-all-together` | 6+ sections, 38 bullets — the densest page in the course |
| `03/01-defining-the-problem` | The 7-node diagram, largest in the course and reused as a locator |
| `01/01-what-is-data` | 3-column table, inline code spans, 3-node diagram |
| `05/99-exercises` | `<details>` answers — **no print equivalent exists yet; this is an open format question** |

If all seven render correctly, the remaining 20 lessons contain nothing structurally new.

### Stage 2 — what each render must be checked for

Things a single easy page never exercises:

- [ ] **No plate splits across a page break** — needs `break-inside: avoid`
- [ ] **No heading orphaned** at the foot of a page — needs `break-after: avoid`
- [ ] **No table splits** mid-row, and a header repeats if one must
- [ ] **Long titles wrap without a one-word last line**
- [ ] **Greyscale**: convert the PDF to grey and confirm mint arrows still read. Color is never the only signal
- [ ] **Page count per lesson is deliberate** — a 3-page lesson means the page model is wrong, not that the lesson is long
- [ ] Bottom margins are empty, per §3, and were not padded to look full

### Stage 3 — print one page

Screen tests cannot tell you whether an 11px mono eyebrow is legible on paper, whether `--hairline #DDE2E2` survives a laser printer, or whether the plate fill turns into a grey smear. **Print one page of the stress set at actual size on the actual printer** before committing to 40 assets.

### Stage 4 — only then, generate

Run the full set. Re-run Stage 2's checklist on a random three lessons as a regression check.

