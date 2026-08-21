# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

Beginner course "Data Fundamentals for Beginners" — 27 Markdown lessons across 6 chapters. No code, no build/lint/test tooling. All work is content writing/editing.

## Position in the curriculum

This course is a **self-contained foundation**. It is used ahead of several different directions in data work, so it must not describe, name, or imply any particular curriculum that follows it.

**The no-promise rule.** The course states facts about the *field*, never about a *curriculum*. It has no "what comes next" section, names no downstream course, names no specialization or career track, and never says "you will learn this later". Where a topic is deliberately shallow, say why in terms of the subject — "cleaning is a large subject in its own right" — not in terms of a course that will cover it. A student may arrive here from any direction, and a promise this repo cannot keep is worse than no promise.

That self-contained position still constrains the content in two ways:

- **This course is the only place** the material it owns gets taught: ethics/privacy/bias/governance, roles and careers, the analytics-type taxonomy, problem framing, and the data landscape. Go deep here.
- **Everything else is preview.** Cleaning, chart choice, statistics, and the tools get named and handed off as subjects, then dropped. Do not grow them.

One track that uses this course is `../../data-analyst.md`, where it appears as "Introduction to Data and Data Science". That file is useful background for judging what is preview versus owned material — but nothing in this repo may reference it, or any other track, in learner-facing text.

Learners have **no tools yet** — Python, Git, and SQL all come later. Nothing in this course may require software.

## Structure

```
NN-chapter-slug/00-opener.md         video opener script (production only, not a lesson)
NN-chapter-slug/NN-lesson-slug.md    lessons
```

A chapter folder reads top to bottom in shooting order: opener, then lessons. The numeric prefix carries that order — `00-` before the lessons.

**Counting gotcha:** `00-opener.md` matches the same glob as lesson files (`0*/0*.md`). Any script that counts lessons, checks `**By the end:**`, or extracts Key Terms **must exclude `00-*`**, or it will report 33 lessons instead of 27 and flag six files as missing their Overview and Key Terms sections.

Chapter order and lesson counts are declared in `README.md`'s Chapters table — update that table whenever any file is added, removed, or renamed. Openers are production material and do not appear in that table.

**Renaming a chapter means renaming four things, not one.** The folder slug, the `**Chapter:**` line in every lesson plus the opener, the `Ch N — Name` column in `GLOSSARY.md`, and any generated-asset name under `diagrams/` that carried the old wording. Code holds paths in two places — the `REGISTER` in `tools/gen_diagram.py` and `DECKS` in `tools/build_slides.py` — and both must move with the folder. Chapter 3 was renamed this way in full; use it as the worked example.

## Lesson file convention

Every lesson file follows this exact shape (confirmed across all 27 files):

```markdown
# Lesson Title

**Chapter:** N — Chapter Name
**Lesson:** N of TOTAL

## Overview

(intro paragraph)

### Subsection headings...

## Key Terms

| Term | Definition |
|---|---|
```

- `## Overview` is mandatory on every lesson. `## Key Terms` is expected but **not mandatory** — include it only where the lesson genuinely introduces vocabulary, and omit it rather than padding the table to a minimum count. A term whose word never appears in the lesson body is a term the lesson did not teach. Demonstration lessons that reuse already-defined vocabulary (e.g. `04/02-why-data-work-uses-code.md`) correctly have no table.
- A Key Term may still be a *label* for a concept the lesson teaches without naming — "Misleading visualization" and "Feedback loop" both qualify. The test is whether the concept is taught, not whether the exact phrase appears.
- `**Chapter:**` / `**Lesson:**` header block must match the lesson's actual position and the README's per-chapter lesson count.
- Some lessons include a `mermaid` `flowchart` block (fenced ` ```mermaid `) to visualize a process (e.g. data → information → insight). Use this sparingly, only where a diagram clarifies a flow better than prose.
- Tables are used heavily for term definitions and comparisons — keep that style rather than switching to bullet lists.
- **Em dashes are rationed.** The course once ran one every 88 words, which is the single loudest signal that prose was machine-written. In running prose the budget is roughly **one per 600 words**. Reach for the alternative first: a colon where the second half specifies the first, a full stop where it is a separate thought, a comma where it is a light aside. A dash survives only as a *paired* parenthetical whose interior already contains commas, where brackets would be too quiet and commas would be ambiguous. Two structural uses are exempt and unlimited: the `**Chapter:** N — Name` metadata block, and `- **Term** — definition` rows in lists and tables.
- **Other tells to stay clear of**, all currently at zero: the adverb tricolon ("accurately, responsibly, and fairly"), `Note that` / `It is worth noting` / `It is important to`, and the vocabulary set *delve, leverage, robust, seamless, ever-growing, in today's world*. A closing sentence that only restates the paragraph above it is the same failure in a different costume.
- **Examples are Somali.** Scenarios are grounded and everyday — mobile money transfers, market prices in $/kg, school attendance. Where a person is named, the name is Somali (Hodan Warsame, Farah Guled, Sagal Ibrahim); where a place is named, it is Somali (Hargeisa, Muqdisho). This is a Somali course and a generically "international" example is still the wrong example. Note that most lessons name nobody at all — "a shop owner", "a market trader", "a manager" — so prefer an unnamed actor and reach for a name only when the example genuinely needs one, as a table of customer records does.

## Start here after a restart

`HANDOFF.md` carries the current state and the open questions. Read it before touching visual assets.

**Building a slide deck for a lesson? Read `SLIDES.md` first.** It is the procedure — the rules with their reasons, the step order, the pre-ship checklist, and a table of traps that have already cost a rebuild each. Two decks exist as worked examples; 25 remain.

## Repo layout beyond the lessons

```
tools/        gen_diagram.py, lesson.css, slides.css, build_slides.py, build_production_page.py
samples/      worked examples — the reference for what a lesson page and deck look like
NN-*/diagrams/  generated .drawio + .svg per chapter
```

The repo was Markdown-only until the design system landed. `tools/` is generation code, not application code: `python3 tools/gen_diagram.py` regenerates every diagram in place from the `REGISTER` at the bottom of that file, and reproduces byte-identical output. `PYTHONPATH=tools python3 tools/build_slides.py [key]` builds the 16:9 decks declared in its `DECKS` table (`--no-pdf` skips WeasyPrint).

The PDF toolchain lives in a `.venv` that is **not** committed — recreate with `python3 -m venv .venv && .venv/bin/pip install weasyprint`.

## Visual assets

`DESIGN.md` is the locked design system for every PDF, slide, and `.drawio` diagram — palette, type scale, spacing scale, page geometry, component set, and diagram styles. **Read it before generating any visual asset, and change it before deviating from it.**

Two constraints from it are load-bearing and easy to get wrong:

- **Mint `#3ACC69` measures 1.97:1 on paper — it may never carry text on a light ground.** Mint-colored text uses `--mint-deep` `#1F7D3D`. Mint is for shapes, fills, rules, and bars.
- **Pages are top-aligned and never filled.** Empty page bottoms are the intended look; do not pad to reach the margin.

Reference documents for that system: `MCP-field-guide.pdf` (layout and spacing only) and the three brand swatches recorded in `DESIGN.md` §1.

## Opener and welcome convention

Seven videos have no lesson file behind them, so these files hold the spoken script itself rather than shot notes: six `NN-chapter-slug/00-opener.md` plus `WELCOME.md` at the root. Shape:

```markdown
# Chapter N Opener — Chapter Name

**Chapter:** N — Chapter Name
**Type:** Video opener — ~NNs, no lesson file behind it

(standing-rules line, link to PRODUCTION.md)

---

*On screen: ...*

(the script, as speakable prose)
```

- They obey the standing rules in `PRODUCTION.md`, including **no greeting** — open cold, same as every lesson.
- Each opener states how many lessons its chapter runs. **Adding or removing a lesson means editing that chapter's `00-opener.md` too** — this is exactly the drift the per-chapter layout exists to prevent, so it is one folder away rather than in a separate root file.
- Chapter 5's opener is load-bearing: its four lessons are one continuous case, and a viewer arriving mid-chapter needs the setup.

## Chapter 5 is a serial case

The four ethics lessons follow one continuous scenario — a mobile money company building automatic small-business loans — under `### Case study: ...` headings, ending with a decision in `04-data-governance-and-regulations.md`. Edits to any one of those lessons must keep the thread consistent with the other three.

## Making changes

- Adding/removing/reordering a lesson: renumber the file prefix, fix the in-file `**Lesson:** N of TOTAL` for every lesson in that chapter, and update `README.md`'s table (lesson count and the total of 27).
- Duration in the README is derived from actual length — recheck it after substantial additions rather than leaving a stale claim.
- No build, lint, or test commands exist for this repo. Validate by reading the rendered Markdown, and check that code fences are balanced.
