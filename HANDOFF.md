# Handoff — state after the draw.io verification

Written 2026-08-10. Read this plus `CLAUDE.md` and `DESIGN.md` and you have the whole picture.

---

## Resolved: `.drawio` now verified against the SVG

Both `.drawio` files have been opened in the real draw.io editor and their rendered geometry
read back out of the canvas DOM. The prediction held — all three suspect areas were wrong,
and all three are fixed in `tools/gen_diagram.py` and re-locked in `DESIGN.md` §6:

| What | Was | Now |
|---|---|---|
| Corner radius | `arcSize=12` → **6.24px**, because plain `arcSize` is a percentage of the shorter side | `absoluteArcSize=1;arcSize=16` → 8px, matching the SVG at any node size |
| Shadow | `shadow=1` → CSS `drop-shadow(… 2px 3px 2px)` at 25% black. Offset wrong, **blurred**, translucent — the exact CSS card `DESIGN.md` says not to make | Its own `--ink` rect at +3/+3, no stroke, grouped with the node so a hand edit cannot separate them |
| Edge endpoints | Arrow touched the source and stopped 2.8px short of the target | `sourcePerimeterSpacing=2;targetPerimeterSpacing=5.2` → starts at +2, tip at −8, exactly where the SVG puts them |

Verified numerically, not by eye: node rects at `rx=8`, shadow rects at +3/+3 filled `#121212`,
and every arrow starting at 166 with its tip at 180 in the 3-node diagram, on all five edges of
the 6-node one. Edge routing itself was never wrong — a straight horizontal run either way.

**The method matters more than the fix**, because six diagrams are still to come.
`open_drawio_xml` returns nothing about what was drawn; it just opens a URL. Open that URL in a
tab with `&dark=0&ui=min` — dark mode inverts the canvas and hides a black shadow on white —
and read the `rect`/`path` attributes out of the canvas SVG. `DESIGN.md` §9 records this.

---

## Where everything is

| Path | What |
|---|---|
| `DESIGN.md` | **Locked design system.** Palette, type, spacing, page geometry, components, `.drawio` styles, verified toolchain (§9), test procedure (§10) |
| `SLIDES.md` | **How to build a deck.** The rules with their reasons, the step order, the pre-ship checklist, the traps already paid for. Read before writing deck 3 |
| `PRODUCTION.md` | Shot notes for all 40 videos — cold opens, shot sequences, diagram build order, runtimes |
| `WELCOME.md`, `NN-*/00-opener.md` | The 7 spoken scripts with no lesson file behind them |
| `tools/gen_diagram.py` | Emits `.drawio` + 3 SVG variants from one model. `python3 tools/gen_diagram.py` regenerates every diagram in place |
| `tools/lesson.css` | `DESIGN.md` implemented as CSS. The lesson page stylesheet |
| `tools/build_production_page.py` | `PRODUCTION.md` → the shooting-reference HTML page |
| `NN-*/diagrams/` | Generated diagram assets, beside their chapter |
| `samples/` | The worked examples — see below |

### Samples to look at before changing anything

- `samples/01-01-what-is-data.pdf` — **the reference for what a lesson page looks like.** Lesson 1.1, 3 A4 pages, full design system
- `samples/01-01-what-is-data-preview.html` — the same thing as three on-screen sheets
- `samples/01-01-what-is-data-slides.pdf` — **the reference for what a deck looks like.** The same lesson as 12 slides at 1920 × 1080, following its `**Shots:**` line, diagram revealed one node per beat. **Every word is the lesson's own** — the build prints `verbatim: 44/44` and names anything that drifted. Every frame carries `NN / 12` bottom-right so it can be called during the shoot
- `samples/03-01-defining-the-problem-slides.pdf` — **the second deck**, lesson 3.1, 16 slides. Proves the parts 1.1 could not: a 7-node diagram built one stage per beat, two-column slides, and the snake-wrapped process diagram. `verbatim: 41/41`
- `samples/01-01-what-is-data-slides.html` — **the same deck as the thing you actually record.** Scales to fit any window with no JS (1rem = one slide pixel, see `DESIGN.md` §7), one slide per screenful, arrow keys page it. Open it rather than the PDF when shooting
- `samples/05-01-axis-lie-interactive.html` — the truncated-axis chart with the animated morph, step-controlled for narration

### Rebuild the PDF toolchain if the venv is gone

```bash
python3 -m venv .venv && .venv/bin/pip install weasyprint   # WeasyPrint 69.0
.venv/bin/weasyprint samples/01-01-what-is-data.html out.pdf   # A4 handout
PYTHONPATH=tools python3 tools/build_slides.py                  # every 16:9 deck
PYTHONPATH=tools python3 tools/build_slides.py 03-01            # just one
```

`DESIGN.md` §9 lists every verified tool. **Do not use `soffice --headless` for designed pages** — it drops SVG, backgrounds, and layout. That was tested and rejected.

---

## What is settled

- **Course content is finished and audited.** 27 lessons, 85 glossary terms, 7 scripts. Two full audits; the last one found four defects, all fixed. The 24 exercises that used to sit in `NN-*/99-exercises.md` were removed — recover them from git history if that decision is ever revisited
- The course is **track-neutral** — it names no specialization, promises no downstream curriculum, and `CLAUDE.md` carries the no-promise rule
- **Design system is locked** in `DESIGN.md` and proven on a real lesson in both output forms — the A4 handout and the 16:9 deck, from the same tokens
- **`.venv` is rebuilt.** WeasyPrint 69.0. It is still not committed and never should be
- Fonts are **deterministic** — Noto Serif / Noto Sans / Noto Sans Mono, all installed and verified, all embedded and subset into the PDF. An earlier draft named Charter, Segoe UI and Menlo, **none of which exist on this machine**; the pages rendered anyway via generic fallback, so the typefaces were being chosen by fontconfig rather than by design

## What is open

| Item | Note |
|---|---|
| **~3 pages per lesson** | Measured, not guessed: lesson 1.1 is 2.46 pages of content. Spacing, type size, and keep-together rules were each tested and none change it. ~75 pages for the set. A decision, not a defect — the lever is page geometry, not typography |
| **Heading/table split** | On sample page 1 an H2 sits near the foot with only its lead paragraph; the table it introduces lands overleaf. Bind heading + intro + table as one block |
| **6 diagrams still to build** | Three of nine exist, all verified in the editor. `tools/gen_diagram.py` has a `REGISTER` — add the rest there. It now draws straight chains and snake-wrapped ones with two-line labels; **hubs, group boundaries and the 5.3 feedback loop are in `DESIGN.md` §6 but still not in code** |
| **Locator cards for 3.2–3.6** | `PRODUCTION.md` 3.1 asks for the process diagram to reappear at the top of each later lesson in the chapter with the current step accented. `svg(..., accent_index=N, under='step N of 7', per_row=4)` already produces it — verified by rendering step 3 — but the five files are not in the `REGISTER` yet |
| **Calibration shoot** | Not started. Record `2.3` (3.5 min, shortest) and `5.1` (8 min, longest) and compare to the estimates. Every runtime in `PRODUCTION.md` rescales off that ratio |
| **Stress test** | `DESIGN.md` §10 names the 7 files that cover 100% of the course's structural features. Not yet run |
| **25 decks still to build** | `tools/build_slides.py` has two hand-written deck functions, `deck_01_01` and `deck_03_01`, declared in a `DECKS` table; `python3 tools/build_slides.py 03-01` builds just one. The stylesheet and the build-frame machinery are general; what stays per-lesson is only *which lesson sentence lands on which slide* — the sentences themselves are copied, never rewritten (`DESIGN.md` §7). Point `verbatim_report` at each new lesson and keep it at N/N. The 4.1 code slides and the 5.1 chart pair have no component yet |

## Not mine to touch

Three PDFs sit in the repo root. `MCP-field-guide.pdf` is the **design reference** for `DESIGN.md` — do not delete it. `internet message.pdf` and `packet.pdf` are unidentified; they were flagged once as strays and that was wrong about the field guide, so leave all three alone unless told otherwise.

## Repo notes

- Git repo on `master`, three commits, last is `58dd6fd`. **Everything from the design-system session is still untracked** — `DESIGN.md`, `HANDOFF.md`, `tools/`, `samples/`, and all three `diagrams/` folders. Until they are committed there is no undo for them, so check before overwriting or deleting
- Was Markdown-only until this session; `tools/`, `samples/` and `NN-*/diagrams/` are new
- **Counting gotcha:** any script counting lessons must exclude `00-*` and `99-*`, or it reports 33 instead of 27. See `CLAUDE.md`
