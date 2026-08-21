# Building a Lesson Deck

How to turn a lesson into the 16:9 deck that gets screen-recorded. Two decks exist —
`samples/01-01-what-is-data-slides.pdf` (12 slides) and
`samples/03-01-defining-the-problem-slides.pdf` (16) — and 25 remain.

**Precedence.** `DESIGN.md` owns how it looks, `PRODUCTION.md` owns what gets shot and in
what order, the lesson Markdown owns every word. This file owns the procedure that joins
them, and records *why* each rule exists so it does not get re-litigated.

**The deck is the video.** There is no separate camera to cut to: the recording is this HTML
scrolling past while the lesson is narrated. Every rule below follows from that one fact.

---

## The rules

### 1. Every word on a slide is the lesson's own

Copied from the lesson Markdown, or from the handout where one exists and already added a
line. Not paraphrased, not compressed into a headline.

**Why.** The lesson Markdown *is* the script. A paraphrased slide puts one set of words on
screen and a different set in the presenter's mouth, and the viewer reads the mismatch.

**Enforced.** Every build prints `verbatim: N/N text elements are the lesson's own words` and
names anything that drifted. Both decks are at N/N. Treat a stray as a defect, not a warning.

**Exempt as furniture** — they name the frame rather than say anything, like a figure number:
the eyebrow, the plate title, a `.k` column label, the slide number.

> This retired an earlier "under 25 words per slide" rule. That rule is right for a deck
> backing a live talk where the speaker improvises around it. Here it forced invention, and
> cost the first cold open its actual content.

### 2. No shot names on screen

"Cold open" is a term from `PRODUCTION.md`. Labelling the first frame `COLD OPEN` is the
on-screen equivalent of the greeting that standing rule 1 forbids. The first slide is the
opening paragraph and nothing else.

Eyebrows that *are* the lesson's own labels stay: `By the end`, `Key terms`, the
chapter/lesson metadata block, and the numbered section running heads.

### 3. Nothing is stacked on the cold open

Carry the whole `## Overview` paragraph, to its last clause. Lesson 1.1's ends on
*"what is data?"* — which is the question the title card answers, so a heading above it asks
the same question twice.

### 4. A slide break must be a beat in the lesson

Split only where the narration actually stops.

- A heading, its lead sentence, and the table or list it introduces are **one slide**. A
  heading alone is a frame the presenter has nothing to say over.
- A list and the sentence that draws the conclusion from it are **one slide**.
- **The diagram build is the exception** — standing rule 7 says one node per beat, so a
  7-stage diagram is 7 slides. That is a real beat each time.

> Lesson 1.1 first ran 14 slides by giving each heading its own frame. It is 12 now, and the
> two it lost were the two nobody would have spoken over.

### 5. One ground: white

Every slide in a lesson deck. `.slide.ink` and its colour overrides stay in the stylesheet
for the six chapter-opener bumpers, which are separate videos.

**Why.** Opening and closing on ink made a single screen recording flash dark, light, dark —
it reads as three videos cut together.

### 6. The deck must fit the window

1rem = one slide pixel; the root font size is the only thing that differs between screen and
print. See `DESIGN.md` §7. Verify `heightGap=0` and ratio 1.778 in a browser, not by eye.

### 7. Diagrams are the generator's, never hand-drawn

Add to the `REGISTER` in `tools/gen_diagram.py`, regenerate, **open the `.drawio` in the real
draw.io editor**, and read the geometry back out of the canvas DOM. Valid XML and *renders as
intended* are different claims. Three defects were found this way that all produced valid
files; a fourth made draw.io refuse the file outright.

---

## The procedure

1. **Read the lesson's `**Shots:**` line** in `PRODUCTION.md`. That is the slide order. Note
   any `**Diagram build:**` line — it gives the node list and often says what the diagram is
   for later in the chapter.

2. **Add the diagram to `REGISTER`** in `tools/gen_diagram.py` if it does not exist:
   `(folder, name, nodes, caption_horizontal, caption_vertical, per_row)`.
   - More than 4 stages → set `per_row=4`. Seven in a straight line renders its labels at
     13px on a 1920 slide; wrapped 4 + 3 they land at ~31px.
   - Labels wider than ~14 characters → break with `\n`. Two lines is the limit at 140 × 52.

3. **`python3 tools/gen_diagram.py`** — regenerates every diagram in place, byte-identical for
   unchanged ones. It parses each `.drawio` back before writing, so malformed XML fails here.

4. **Verify the new `.drawio` in the editor.** `open_drawio_xml` with the file's
   `<mxGraphModel>` block, open the returned URL with `&dark=0&ui=min`, then read the canvas
   SVG's `rect`/`path` attributes from the DOM and compare to the `.svg`. Checklist:
   `rx=8`, shadow rects at +3/+3 filled `#121212`, arrow tips 8px short of their target.

5. **Write the deck function** in `tools/build_slides.py`, one slide per shot chip, and add an
   entry to the `DECKS` table naming its sources for the verbatim check.

6. **`PYTHONPATH=tools python3 tools/build_slides.py <key>`**. Read the two printed lines.
   Fix every `paraphrased <tag>:` before looking at anything else.

7. **Render and look at all of it.** `pdftoppm -png -r 55 <pdf> s` then
   `magick montage s-*.png -tile 4x -geometry 400x225+5+5 -background '#888' contact.png`.
   A contact sheet catches overflow and empty frames that per-slide checks miss.

8. **Check the HTML in a browser**, since it is what gets recorded — not the PDF.

---

## Before a deck ships

- [ ] `verbatim: N/N` — no strays
- [ ] No shot name anywhere on screen
- [ ] Cold open is the whole opening paragraph, nothing stacked on it
- [ ] No slide is a heading with nothing under it
- [ ] Every slide on white
- [ ] `pdfinfo` reports **1440 × 810 pts**, one page per slide
- [ ] Diagram `.drawio` opened in the editor and its geometry read back
- [ ] Contact sheet reviewed — nothing overflows the safe area, nothing is a near-empty frame
- [ ] `pdffonts` shows every face embedded and subset, all Noto

---

## What stays hand-written, and why

The stylesheet, the build-frame machinery, and the verbatim check are general. **Which lesson
sentence lands on which slide is not, and should not be.** That is an editorial judgement per
lesson, taken from its `**Shots:**` line — a generator that guessed it would produce 25 decks
nobody would want to shoot. The sentences themselves are copied, never rewritten.

Two components do not exist yet: the **4.1 code slides** with line highlighting, and the
**5.1 chart pair** (truncated vs full axis). Both are named in `PRODUCTION.md`'s asset table.

---

## Traps already paid for

Each of these shipped once and was caught by rendering, not by reading.

| Trap | Symptom | Fix |
|---|---|---|
| `font-weight:640` | WeasyPrint logs `Ignored`, falls back to normal — bold-in-body silently was not bold | Multiples of 100 only |
| `<br>` in a draw.io `value` | *"Not a diagram file"* — the whole file refused, not one label | `&lt;br&gt;`; escape once over the joined string |
| `arcSize=12` | 6.24px radius, not 8 — it is a percentage of the shorter side | `absoluteArcSize=1;arcSize=16` |
| `shadow=1` | A blurred 25%-black CSS card, the exact thing `DESIGN.md` §6 forbids | Shadow is its own cell, grouped with the node |
| `.plate-title` without `max-width:none` | Inherits the `p` reading measure, wraps a four-word title | `max-width:none`, as `.plate-cap` already needed |
| `--ink` term column on `.slide.ink` | Invisible — the whole first column of the end card | Restate every colour on the ink ground |
| Visible scrollbar | Sits inside `100vw` but outside usable width; slide ~15px too wide when width binds | `scrollbar-width:none` |
| Elbow turned mid-gap | SVG and draw.io drew two different pictures from one model; the SVG's 10px corner did not fit the 4px of run left before the arrowhead and the path doubled back | Turn over the target's centre line — `orthogonalEdgeStyle`'s own route. `DESIGN.md` §6 |
| Editor showed the old diagram | Two `open_drawio_xml` URLs differ only after `#`, so the browser does not reload and the readback is of the *previous* file. Cost one wrong conclusion | `location.reload()` after navigating, and confirm a changed value before reading geometry |

---

## Left open on purpose

- **Content does not fill the frame.** Most slides have empty space below the text. That is
  `DESIGN.md` §3 — pages are top-aligned and never filled — and it applies to slides too. If
  frames should look fuller the lever is geometry (safe area, type multiplier), not padding.
- **~50 words per slide** means a viewer can read ahead of the narration. One idea per slide
  is what keeps that bounded. Split a section rather than let one slide grow.
