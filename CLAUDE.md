# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

Beginner course "Data Fundamentals for Beginners" — 27 Markdown lessons plus 6 exercise sets across 6 chapters. No code, no build/lint/test tooling. All work is content writing/editing.

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
NN-chapter-slug/99-exercises.md      one exercise set per chapter
```

A chapter folder reads top to bottom in shooting order: opener, lessons, exercises. The numeric prefixes carry that order — `00-` before the lessons, `99-` after them.

**Counting gotcha:** `00-opener.md` matches the same glob as lesson files (`0*/0*.md`). Any script that counts lessons, checks `**By the end:**`, or extracts Key Terms **must exclude both `00-*` and `99-*`**, or it will report 33 lessons instead of 27 and flag six files as missing their Overview and Key Terms sections.

Chapter order, lesson counts, and exercise counts are declared in `README.md`'s Chapters table — update that table whenever any file is added, removed, or renamed. Openers are production material and do not appear in that table.

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

- `## Overview` is mandatory on every lesson. `## Key Terms` is expected but **not mandatory** — include it only where the lesson genuinely introduces vocabulary, and omit it rather than padding the table to a minimum count. A term whose word never appears in the lesson body is a term the lesson did not teach. Demonstration lessons that reuse already-defined vocabulary (e.g. `04/02-why-analysts-write-code.md`) correctly have no table.
- A Key Term may still be a *label* for a concept the lesson teaches without naming — "Misleading visualization" and "Feedback loop" both qualify. The test is whether the concept is taught, not whether the exact phrase appears.
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
- Adding an exercise: update the chapter's count in the README table and the `Exercises:` total in the header.
- Duration in the README is derived from actual length — recheck it after substantial additions rather than leaving a stale claim.
- No build, lint, or test commands exist for this repo. Validate by reading the rendered Markdown, and check that code fences are balanced and every `<details>` has a matching `</details>`.
