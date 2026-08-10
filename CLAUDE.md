# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

Beginner course "Data Fundamentals for Beginners" — 26 Markdown lessons plus 6 exercise sets across 6 chapters. No code, no build/lint/test tooling. All work is content writing/editing.

## Position in the curriculum

This is **course 1 of 11** in the Data Analysis Career Path (`../../data-analyst.md`). That file is the authority on what the later courses cover, and it constrains this one in two directions:

- **Course 1 is the only place** the program ever teaches ethics/privacy/bias/governance, roles and careers, the analytics-type taxonomy, problem framing, and the data landscape. Go deep here — nothing downstream revisits it.
- **Everything else is preview.** Cleaning is owned by course 8, chart choice by course 11, statistics by course 6, tools by courses 3/4/5/10. Name these concepts, then hand off explicitly ("you will learn this in the Statistics course"). Do not grow them.

Learners have **no tools yet** — Python is course 2, Git 3, SQL 4, Excel 5. Nothing in this course may require software.

## Structure

```
NN-chapter-slug/NN-lesson-slug.md    lessons
NN-chapter-slug/99-exercises.md      one exercise set per chapter
```

Chapter order, lesson counts, and exercise counts are declared in `README.md`'s Chapters table — update that table whenever any file is added, removed, or renamed.

## Lesson file convention

Every lesson file follows this exact shape (confirmed across all 26 files):

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

- `## Overview` and `## Key Terms` are mandatory on every lesson — closing table always defines the terms introduced in that lesson.
- `**Chapter:**` / `**Lesson:**` header block must match the lesson's actual position and the README's per-chapter lesson count.
- Some lessons include a `mermaid` `flowchart` block (fenced ` ```mermaid `) to visualize a process (e.g. data → information → insight). Use this sparingly, only where a diagram clarifies a flow better than prose.
- Tables are used heavily for term definitions and comparisons — keep that style rather than switching to bullet lists.
- Examples lean on real-world, non-Western-default scenarios (mobile money transfers, market prices in $/kg, school attendance) — keep new examples in that same grounded, everyday register.

## Exercise file convention

`99-exercises.md` in each chapter folder (`99-` keeps it sorted last regardless of lesson count). Shape:

```markdown
# Chapter N Exercises: Chapter Name

**Chapter:** N — Chapter Name
**Type:** Practice — no software required

### Exercise N — Title

(prompt)

<details>
<summary>Show answer</summary>

(answer, with the reasoning — not just the correct choice)

</details>
```

- Every exercise must be answerable on paper. No CSV to open, no tool to install.
- Answers teach. Explain *why* the wrong answer is tempting, not just which is right.
- Each set should include at least one item designed to be gotten wrong (a plausible trap), and it should be the one the answer spends most words on.
- Chapter 5's exercises extend the loan-scoring case that runs through its four lessons.

## Chapter 5 is a serial case

The four ethics lessons follow one continuous scenario — a mobile money company building automatic small-business loans — under `### Case study: ...` headings, ending with a decision in `04-data-governance-and-regulations.md`. Edits to any one of those lessons must keep the thread consistent with the other three.

## Making changes

- Adding/removing/reordering a lesson: renumber the file prefix, fix the in-file `**Lesson:** N of TOTAL` for every lesson in that chapter, and update `README.md`'s table (lesson count and the total of 26).
- Adding an exercise: update the chapter's count in the README table and the `Exercises:` total in the header.
- Duration in the README is derived from actual length — recheck it after substantial additions rather than leaving a stale claim.
- No build, lint, or test commands exist for this repo. Validate by reading the rendered Markdown, and check that code fences are balanced and every `<details>` has a matching `</details>`.
