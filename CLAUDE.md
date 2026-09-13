# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

Beginner course "Data Fundamentals for Beginners": 27 Markdown lessons across 6 chapters. The Markdown files remain the curriculum source. Visual lesson exports are now being added as self-contained HTML presentations with SVG assets and print-ready PDFs. There is no conventional application build, lint, or test suite.

## Position in the curriculum

This course is a **self-contained foundation**. It is used ahead of several different directions in data work, so it must not describe, name, or imply any particular curriculum that follows it.

**The no-promise rule.** The course states facts about the *field*, never about a *curriculum*. It has no "what comes next" section, names no downstream course, names no specialization or career track, and never says "you will learn this later". Where a topic is deliberately shallow, say why in terms of the subject - "cleaning is a large subject in its own right" - not in terms of a course that will cover it. A student may arrive here from any direction, and a promise this repo cannot keep is worse than no promise.

That self-contained position still constrains the content in two ways:

- **This course is the only place** the material it owns gets taught: ethics/privacy/bias/governance, roles and careers, the analytics-type taxonomy, problem framing, and the data landscape. Go deep here.
- **Everything else is preview.** Cleaning, chart choice, statistics, and the tools get named and handed off as subjects, then dropped. Do not grow them.

One track that uses this course is `../../data-analyst.md`, where it appears as "Introduction to Data and Data Science". That file is useful background for judging what is preview versus owned material, but nothing in this repo may reference it, or any other track, in learner-facing text.

Learners have **no tools yet**. Python, Git, and SQL all come later. Nothing in this course may require software.

## Structure

```
NN-chapter-slug/00-opener.md         video opener script (production only, not a lesson)
NN-chapter-slug/NN-lesson-slug.md    lessons
exports/html/                        self-contained visual lesson HTML packages
exports/pdf/                         final print-ready lesson PDFs
references/                          user-supplied visual references
```

A chapter folder reads top to bottom in shooting order: opener, then lessons. The numeric prefix carries that order, with `00-` before the lessons.

**Counting gotcha:** `00-opener.md` matches the same glob as lesson files (`0*/0*.md`). Any script that counts lessons or checks `**By the end:**` **must exclude `00-*`**, or it will report 33 files instead of 27 lessons. A Key Terms audit must also account for all 27 lessons, which intentionally have no closing tables.

Chapter order and lesson counts are declared in `README.md`'s Chapters table. Update that table whenever any file is added, removed, or renamed. Openers are production material and do not appear in that table.

**Renaming a chapter means renaming three things, not one.** Change the folder slug, the `Ch N - Name` column in `GLOSSARY.md`, and the chapter link in `README.md`. If the opener names the chapter, update that wording too. Chapter 3 was renamed this way in full; use it as the worked example.

## Lesson file convention

Every lesson file begins with this shape:

```markdown
# Lesson Title

## Overview

(intro paragraph)

### Subsection headings...
```

- `## Overview` is mandatory on every lesson. All learner-facing `## Key Terms` tables have been removed: vocabulary is defined at the point of teaching and collected once in `GLOSSARY.md`. Lesson 4.2 already followed this pattern because it demonstrates previously defined vocabulary.
- Vocabulary must still be taught before it appears in the glossary. Removing a table is not permission to leave a term defined only in `GLOSSARY.md`.
- A Key Term may still be a *label* for a concept the lesson teaches without naming - "Misleading visualization" and "Feedback loop" both qualify. The test is whether the concept is taught, not whether the exact phrase appears.
- Lesson files do not include `**Chapter:**` or `**Lesson:**` metadata. The folder name and numeric file prefix carry that structure.
- Some lessons include a `mermaid` `flowchart` block (fenced ` ```mermaid `) to visualize a process (e.g. data → information → insight). Use this sparingly, only where a diagram clarifies a flow better than prose.
- Tables are used heavily for term definitions and comparisons - keep that style rather than switching to bullet lists.
- **There are no em dashes in this repo, anywhere.** Not in prose, not in the `Ch N - Name` column of `GLOSSARY.md`, and not in `- **Term** - definition rows. Use a **comma** where the aside is light, a **full stop** where it is a separate thought, a **colon** where the second half specifies the first, and a plain **hyphen** where a template needs a separator. A pair of em dashes around a phrase is rewritten, not swapped: "differ in what they produce - a report, a dashboard - not in how they start" is worse than the dashes were, so recast the sentence instead. `grep -r "\u2014" .` must return nothing.
- **Other tells to stay clear of**, all currently at zero: the adverb tricolon ("accurately, responsibly, and fairly"), `Note that` / `It is worth noting` / `It is important to`, and the vocabulary set *delve, leverage, robust, seamless, ever-growing, in today's world*. A closing sentence that only restates the paragraph above it is the same failure in a different costume.
- **Examples are grounded and everyday.** Use familiar scenarios such as digital wallet activity, market prices in $/kg, school attendance, shop sales, and customer records. Most lessons name nobody at all - "a shop owner", "a market trader", "a manager" - so prefer an unnamed actor and reach for a name only when the example genuinely needs one, as a table of customer records does.

## Visual lesson exports

The retired visual system is no longer the reference. A new reference has been supplied at `references/Data Fundamentals Lesson.pdf`, and Lesson 1.1 is the first completed export using the new workflow.

Current structure:

```text
exports/
├── html/
│   ├── Lesson 01 - What Is Data.html
│   ├── Lesson 02 - Types of Data.html
│   ├── Lesson 03 - Sources and Formats of Data.html
│   ├── Lesson 04 - Data Quality.html
│   ├── Lesson 05 - Why Data Matters.html
│   ├── assets/lesson-01/
│   │   ├── patterns-emerge.svg
│   │   └── facebook-post-likes.svg
│   ├── assets/lesson-02/
│   │   ├── structured-table.svg
│   │   ├── unstructured-media.svg
│   │   ├── semi-structured-json.svg
│   │   ├── quantitative-measures.svg
│   │   └── qualitative-categories.svg
│   ├── assets/lesson-03/
│   │   ├── primary-firsthand.svg
│   │   ├── secondary-reused.svg
│   │   └── source-format-checks.svg
│   ├── assets/lesson-04/
│   │   ├── garbage-in-garbage-out.svg
│   │   └── same-data-different-average.svg
│   └── assets/lesson-05/
│       ├── evidence-vs-memory.svg
│       └── data-responsibility.svg
├── pdf/
│   ├── Lesson 01 - What Is Data.pdf
│   ├── Lesson 02 - Types of Data.pdf
│   ├── Lesson 03 - Sources and Formats of Data.pdf
│   ├── Lesson 04 - Data Quality.pdf
│   └── Lesson 05 - Why Data Matters.pdf
references/
└── Data Fundamentals Lesson.pdf
```

Keep each HTML lesson self-contained inside `exports/html/`. Its editable visual sources and rendered SVGs belong under a lesson-specific assets folder. Final PDFs belong in `exports/pdf/`. User-supplied examples belong in `references/` and should not be overwritten when regenerating an export.

`PRODUCTION.md` remains the recording plan. It describes shot order and required teaching visuals. The supplied PDF and completed Lesson 1.1 export now provide the practical visual baseline.

**Page and asset counts are content-driven.** Lesson 1.1 having eight slides and five SVGs is a reference result, not a fixed template or quota. Plan every lesson from its exact Markdown content and give each idea enough room to remain clear and readable. A lesson may use eight pages, fewer than eight, or more than eight. The SVG count may also be lower, equal, or higher depending on which concepts genuinely benefit from a custom visual. Do not add filler pages or unnecessary SVGs to match Lesson 1.1, and do not compress content merely to stay at eight pages. Eight pages is fully acceptable when it naturally fits the lesson.

### Current visual production progress

- Lesson 1.1, "What Is Data?", is complete as an eight-slide HTML presentation and an eight-page PDF with two standalone SVG illustrations.
- Lesson 1.2, "Types of Data", is complete as a seven-slide HTML presentation and a seven-page PDF with five standalone SVG illustrations.
- Lesson 1.3, "Sources and Formats of Data", is complete as a seven-slide HTML presentation and a seven-page PDF with three standalone SVG illustrations.
- Lesson 1.4, "Data Quality", is complete as a nine-slide HTML presentation and a nine-page PDF with two standalone SVG illustrations.
- Lesson 1.5, "Why Data Matters", is complete as a seven-slide HTML presentation and a seven-page PDF with two standalone SVG illustrations.
- Chapter 2 lessons 2.1 through 2.6 are complete as HTML presentations and PDFs: 7, 8, 8, 9, 9, and 7 pages respectively, with 11 standalone SVG illustrations across the six lessons.
- All eleven PDFs use a 16:9 page size of 720 x 404.88 points, equivalent to a 10 x 5.625 inch page.
- The visual language is off-white paper, dark ink, restrained green accents, rough hand-drawn lines, short annotations, and generous whitespace.
- Lesson 1.1 uses a focused pattern chart and one combined Facebook likes comparison rather than separate assets for every stage of data, information, and insight.
- All 25 SVG exports across the eleven completed lessons pass the SVG validator and XML parsing.
- All five Chapter 1 lessons and the first six Chapter 2 lessons are converted. Chapter 2 lesson 2.7 has not been converted yet. Do not mark later lessons complete merely because their Markdown content exists.

### HTML and PDF conventions

- Each English slide is a direct `section` child of `x-import` and is designed at 1920 x 1080.
- Print CSS sets `@page` to `10in 5.625in`, scales each slide with `zoom: .5`, and forces one section per page.
- The normal browser deck and printed PDF share the same HTML. Do not maintain a second hand-edited PDF-only document.
- HTML asset paths are relative to their HTML package. English Lesson 1.1 uses `assets/lesson-01/...`.
- Keep informative `alt` text on every SVG image.
- Excalidraw SVG backgrounds should be transparent unless the illustration genuinely needs a filled panel.
- Avoid fixed tall wrappers around wide diagrams. They create large empty blocks when a shallow SVG uses `object-fit: contain`.
- A normal browser `load` listener initializes Lucide icons for PDF export. The custom deck lifecycle alone does not run when Chrome prints the raw HTML.

### Re-exporting a lesson PDF

Run headless Chrome against the HTML package and write the result to `exports/pdf/`. For Lesson 1.1:

```bash
google-chrome-stable \
  --headless=new \
  --no-sandbox \
  --disable-gpu \
  --allow-file-access-from-files \
  --run-all-compositor-stages-before-draw \
  --virtual-time-budget=10000 \
  --no-pdf-header-footer \
  --print-to-pdf-no-header \
  --print-to-pdf="$(pwd)/exports/pdf/Lesson 01 - What Is Data.pdf" \
  "file://$(pwd)/exports/html/Lesson%2001%20-%20What%20Is%20Data.html"
```

After export, verify the page count and dimensions:

```bash
pdfinfo "exports/pdf/Lesson 01 - What Is Data.pdf"
```

Expected result for Lesson 1.1: 8 pages at 720 x 404.88 points.

Validate SVG assets with:

```bash
bash /home/sharafdin/.agents/skills/svg-skill/scripts/validate.sh exports/html/assets/lesson-01
xmllint --noout exports/html/assets/lesson-01/*.svg
```

## Opener and welcome convention

Seven videos have no lesson file behind them, so these files hold the spoken script itself rather than shot notes: six `NN-chapter-slug/00-opener.md` plus `WELCOME.md` at the root. Shape:

```markdown
# Chapter N Opener - Chapter Name

**Chapter:** N - Chapter Name
**Type:** Video opener - ~NNs, no lesson file behind it

(standing-rules line, link to PRODUCTION.md)

---

*On screen: ...*

(the script, as speakable prose)
```

- They obey the standing rules in `PRODUCTION.md`, including **no greeting** - open cold, same as every lesson.
- Each opener states how many lessons its chapter runs. **Adding or removing a lesson means editing that chapter's `00-opener.md` too** - this is exactly the drift the per-chapter layout exists to prevent, so it is one folder away rather than in a separate root file.
- Chapter 5's opener is load-bearing: its four lessons are one continuous case, and a viewer arriving mid-chapter needs the setup.

## Chapter 5 is a serial case

The four ethics lessons follow one continuous scenario - a digital wallet company building automatic small-business loans - under `### Case study: ...` headings, ending with a decision in `04-data-governance-and-regulations.md`. Edits to any one of those lessons must keep the thread consistent with the other three.

## Making changes

- Adding/removing/reordering a lesson: renumber the file prefix and update `README.md`'s table (lesson count and the total of 27).
- Duration in the README is derived from actual length - recheck it after substantial additions rather than leaving a stale claim.
- Markdown has no build, lint, or test command. Validate it by reading the rendered files and checking that code fences are balanced.
- For visual exports, inspect the rendered PDF pages in addition to running the SVG and PDF checks documented above. A successful command is not enough if text is clipped, icons are missing, arrows cross labels, or a diagram leaves excessive empty space.
