# Production Notes — Recording This Course

**Format:** 27 lesson videos, 6 exercise walkthroughs, 6 chapter openers, 1 welcome
**Estimated finished runtime:** ~3h 25m
**Source of truth:** the lesson Markdown files. This document tells you how to shoot them, not what to say — the words are already in the lessons.

---

## Standing rules — every video

**1. Cold open first, no greeting.** The first sentence of each lesson's `## Overview` is the cold open. Say it verbatim over black, before the title card. Never open with "hi, welcome back to the course" — the hook is the retention decision and greeting spends it.

**2. Say the objective at ~0:15.** Every lesson has a `**By the end:**` line. Say it right after the cold open, before the first section. This is the only signpost the video gets — the "This lesson covers…" sentences were removed from all 16 lessons that had them, precisely so this one lands alone.

**3. The metadata block is the title card, not narration.** `**Chapter:** N — Name` / `**Lesson:** N of TOTAL` goes on screen. Never read aloud.

**4. Key Terms tables are end cards. Do not narrate them.** Every lesson closes with a Key Terms table. Put it on screen and hold it. Over it, say two things: one sentence calling back to the lesson's main idea, and one sentence teasing the next lesson. Reading 90 glossary rows aloud across the course would cost 15–20 minutes and would put the flattest possible 45 seconds at the end of all 27 videos — the exact place you need the click to the next one.

**4b. One lesson has no Key Terms table.** `4.2 Why Analysts Write Code` introduces no new vocabulary — it demonstrates. End it on the Python output instead, holding the last code slide while you say the callback and the tease. Every other lesson uses its table.

**5. Every `###` heading is a segment boundary.** Cut, change the slide, or move on camera. The lessons average 3–4 sections, which is your shot count.

**6. Tables go on screen as written.** Read the row, then explain it. Do not paraphrase the cells — the wording is deliberate and the viewer is reading along. Budget 10–14 seconds per row.

**7. Diagrams build, never appear complete.** All 9 mermaid diagrams are sequences. Reveal one node per beat, speaking each as it lands. A completed flowchart dropped on screen is read in one second and then ignored for the remaining 40.

**8. Numbers are spoken exactly as written.** `$2.50 per kg`, `32°C`, `91.4%`. The examples are deliberately non-Western-default and grounded — don't round them off or localize them on the fly.

---

## Build these assets before you shoot

| Asset | Count | Notes |
|---|---|---|
| Animated diagram builds | 9 | One per mermaid block. Build order given per lesson below. |
| Chart pair, truncated vs full axis | 2 | **5.1** — highest-value visual in the course. Currently ASCII in the Markdown. |
| Repayment data table | 1 | **5.1** — must appear *before* either chart. |
| Code slides with line highlighting | 2 | **4.1** — SQL and Python. Only code in the course. |
| Content table slides | 14 | Excludes the 26 Key Terms end cards. |
| Key Terms end card template | 1 | Reusable; table content differs per lesson. |
| Title card template | 1 | Lesson name + chapter/lesson position. |
| Chapter opener bumper | 6 | 60–90s each. **Script lives in each chapter's `00-opener.md`.** |

---

## Chapter openers

Six short bumpers, 60–90 seconds, ~8 minutes total, plus a ~2.5 minute course welcome. **Each chapter's script is `00-opener.md` inside that chapter's folder; the course welcome is `WELCOME.md` at the root.** These seven are the only videos with no lesson file behind them, so those files hold the words themselves rather than shot notes. They supply the orientation a reader gets free from the README table and a viewer gets not at all.

The `00-` prefix puts each opener first in its folder, so a chapter folder now reads top to bottom in shooting order: opener, lessons, exercises.

Each answers three things: what question this chapter settles, why it comes after the last one, and how many lessons it runs.

| Chapter | The question it settles | Lessons |
|---|---|---|
| 1 — What Is Data? | What am I actually working with? | 5 |
| 2 — The Data Ecosystem | Who does what, and what are all these job titles? | 6 |
| 3 — The Data Analysis Process | What are the steps, in order, from question to decision? | 6 |
| 4 — Data in the Real World | What tools and jobs does this turn into? | 4 |
| 5 — Data Ethics and Privacy | When should we *not* do the thing we can do? | 4 |
| 6 — Conclusion | Can I do all of it in one pass? | 2 |

**Chapter 5's opener is mandatory, not optional.** Its four lessons are one continuous case — a mobile money company building automatic small-business loans. A viewer landing on lesson 5.3 without the opener has no idea a loan company has been running for two lessons. State the case up front: the company, the product, and that it will go wrong four different ways.

---

# Chapter 1 — What Is Data?

*5 lessons · 25.5 min*

### 1.1 · What Is Data? — 5.5 min

**Cold open:** *You check your phone and see a mobile money transfer of `$25`, a weather app showing `32°C`, and a message from school about your attendance.*

**Shots:** cold open → title → objective → *Data: raw facts about the world* → **table** Term / Meaning / Example → **diagram build (3)** → *Where you see data every day* → end card

**Diagram build:** `Data` → `Information` → `Insight`. Build it directly out of the table you just showed — same three words, same order. The table is the definition, the diagram is the motion.

**Note:** The cooking analogy (ingredients → meal → knowing what to cook next) lands better spoken than written. Give it a beat.

---

### 1.2 · Types of Data — 5 min

**Cold open:** *A shop owner opens a spreadsheet of last week's sales and sees numbers, product names, and customer comments all mixed together.*

**Shots:** cold open → title → objective → *Structured vs unstructured data* → *Quantitative vs qualitative data* → *Why data types matter* → end card

**Note:** Two independent classifications, not four categories. Say that explicitly — it is the single most common beginner confusion and the text leaves it implicit. Show them as two axes if you can.

---

### 1.3 · Sources and Formats of Data — 5.5 min

**Cold open:** *You receive a file from a colleague and need to decide whether you can trust it and how to open it.*

**Shots:** cold open → title → objective → *Common sources of data* → *Primary vs secondary data* → **table** Format / Common use → *Why source and format matter* → end card

**Note:** The two questions in the last section — "Where did this come from?" and "What format is it in?" — are the takeaway. Put them on screen as a two-line card.

---

### 1.4 · Data Quality Basics — 5 min

**Cold open:** *A manager forwards you a customer list and asks for the average age.*

**Shots:** cold open → title → objective → *Why data quality matters* → *Common data quality problems* → **table** Dimension / Question it answers → *Example* → end card

**Note:** The Example section has a defective table in it. Show it and let the viewer find the problems before you name them — a 5-second hold, then reveal. This is the one lesson in chapter 1 with a built-in pause beat.

---

### 1.5 · Why Data Matters — 4.5 min

**Cold open:** *Two shop owners sell the same products at the same prices.*

**Shots:** cold open → title → objective → *Data helps organizations make better decisions* → *Data creates competitive advantage* → *Data skills are widely valuable* → *Data also comes with responsibility* → end card

**Note:** Four short sections and no diagram — the flattest-shaped lesson in chapter 1. Carry it on delivery, and let the two-shop-owners story run through all four sections rather than dropping it after the cold open. Last section is the setup for chapter 5; point forward.

---

# Chapter 2 — The Data Ecosystem

*6 lessons · 27 min*

> **Watch the monotony here.** Lessons 2.2, 2.3, 2.4 and 2.6 are structurally identical: ~4.5 min, one 3-row Key Terms table, no diagram, same four-section shape. On the page that consistency is a virtue. Four near-identical videos in a row is where attention goes. Vary pacing, framing, or location deliberately across them — and do not shoot all four in one sitting, or the fatigue will show in the delivery.

### 2.1 · Types of Analytics — 4.5 min

**Cold open:** *A manager looks at last month's sales report and asks three questions in one meeting: "What happened? Why did it happen? What should we do next?"*

**Shots:** cold open → title → objective → *What is analytics?* → **diagram build (4)** → *The four types of analytics* → **table** Type / Question / Example → *Simple way to remember them* → *Why this matters* → end card

**Diagram build:** `Descriptive` → `Diagnostic` → `Predictive` → `Prescriptive`. Build one per type as you introduce it, so the diagram completes exactly as the section ends.

**Note:** The manager's three questions in the cold open map onto the first three types. Say so — it turns the hook into the structure.

---

### 2.2 · Data Analysis and Business Intelligence — 4 min

**Cold open:** *A shop owner notices that one product sells out every week while another sits on the shelf.*

**Shots:** cold open → title → objective → *What is data analysis?* → *What is business intelligence?* → *How they relate* → *Example* → end card

**Note:** The shop owner wants two different things — to understand *why*, and to check it monthly without digging. That is the analysis/BI split in one sentence. Hold on it.

---

### 2.3 · Data Science and Machine Learning — 3.5 min

**Cold open:** *Your inbox quietly moved a message to spam this morning.*

**Shots:** cold open → title → objective → *What is data science?* → *What is machine learning?* → *How they relate* → *Example* → end card

**Note:** Shortest lesson in the course and the one with the least visual support, on the subject students are most curious about. Give it the extra asset — a nesting graphic showing ML inside data science would earn its place here more than anywhere else in chapter 2.

---

### 2.4 · Data Engineering — 4 min

**Cold open:** *An analyst opens a report and finds three different versions of the same sales numbers — one outdated, one incomplete, one in the wrong format.*

**Shots:** cold open → title → objective → *What is data engineering?* → *What data engineers do* → *Why data engineering matters* → *Example* → end card

**Note:** Three conflicting numbers is a screen graphic, not a spoken list. Show the three versions side by side during the cold open.

---

### 2.5 · Where Data Lives and the Data Pipeline — 5 min

**Cold open:** *The sales figure on a manager's dashboard this morning began as a tap on a card reader three weeks ago.*

**Shots:** cold open → title → objective → *Where data lives* → **table** System / Purpose → *What is a data pipeline?* → **diagram build (6)** → *Example* → end card

**Diagram build:** `Collect` → `Store` → `Clean` → `Transform` → `Analyze` → `Share`. Six beats — the longest build in chapter 2. Consider running it in reverse first, from the dashboard back to the card reader, matching the cold open, then forward.

---

### 2.6 · How These Fields Work Together — 4 min

**Cold open:** *One customer cancels a subscription.*

**Shots:** cold open → title → objective → *One ecosystem, many roles* → *How they work together* → *Where analytics types fit* → *Key takeaway* → end card

**Note:** Five people touch one cancellation. Name them one at a time on screen as you go — this is the chapter's payoff and the only lesson that puts all five roles in one frame.

---

# Chapter 3 — The Data Analysis Process

*6 lessons · 31 min*

### 3.1 · Defining the Problem and Asking Questions — 5.5 min

**Cold open:** *"Can you look into the sales data?" is one of the most common requests an analyst receives, and it is not yet a question.*

**Shots:** cold open → title → objective → **diagram build (7)** → *Start with the business problem* → *Know your stakeholders* → *How to ask good analytical questions* → *Example* → end card

**Diagram build:** `Define problem` → `Ask questions` → `Collect data` → `Clean data` → `Analyze and visualize` → `Communicate insights` → `Make decisions`. **This is the map for the whole chapter.** Build all seven here, then bring it back as a static locator card at the top of lessons 3.2–3.6 with the current step highlighted. Cheapest continuity device in the course.

---

### 3.2 · Collecting Data — 4.5 min

**Cold open:** *The easiest data to obtain is rarely the data that answers your question.*

**Shots:** cold open → title → **locator: step 3** → objective → *What is data collection?* → **table** Method / Example → *Questions to ask before using data* → *Example* → end card

---

### 3.3 · Cleaning Data — 5 min

**Cold open:** *Ask working analysts what takes up most of their time and the answer is rarely "analysis".*

**Shots:** cold open → title → **locator: step 4** → objective → *Why clean data?* → **table** Task / Example → *Common cleaning tasks* → *How much cleaning is enough?* → *Example* → end card

**Note:** the lesson calls cleaning "a large subject in its own right" and stops there. Deliver it that way — do not promise a later course, here or anywhere else in the shoot.

---

### 3.4 · Analyzing and Visualizing Data — 4.5 min

**Cold open:** *The same table of numbers can hide a trend completely or make it obvious in one second.*

**Shots:** cold open → title → **locator: step 5** → objective → *What happens during analysis?* → *Why visualize data?* → **table** Question type / Chart type → *Common chart types* → *Example* → end card

**Note:** The cold open is a promise of a visual. Deliver it in the first 20 seconds — same numbers as a table, then as a chart, side by side. Do not let this lesson be the one where you *talk about* visualization.

Chart choice is named and dropped on purpose — do not promise where it gets taught.

---

### 3.5 · Communicating Insights — 4 min

**Cold open:** *An analyst spends three weeks on an investigation, presents twelve slides, and nothing changes.*

**Shots:** cold open → title → **locator: step 6** → objective → *Analysis without communication has limited value* → *What to include in a data report* → *Tips for clear communication* → *Know your audience* → end card

**Note:** "It was also the fourth thing mentioned, on slide nine." Land that line, then pause. It is the best-written sentence in chapter 3.

---

### 3.6 · From Analysis to Decisions — 3.5 min

**Cold open:** *Every analysis rests on things you did not check.*

**Shots:** cold open → title → **locator: step 7, completing the map** → objective → *From insight to action* → *Assumptions and limitations* → *Why decisions still need judgment* → *Example* → end card

**Note:** Complete the locator diagram on screen here — the chapter closes as the map fills in.

---

# Chapter 4 — Data in the Real World

*4 lessons · 20.5 min*

### 4.1 · The Modern Data Toolkit — 5.5 min

**Cold open:** *Every new analyst asks which tool to learn first.*

**Shots:** cold open → title → objective → *Why there are many tools* → **table** Tool / What it is / When you reach for it → *Example workflow* → **diagram build (4)** → end card

**Diagram build:** `SQL` → `Python`, then **branch** to `Excel report` and `Power BI dashboard` simultaneously. The branch is the point — one analysis, two audiences. Do not build the two outputs sequentially.

**Note:** ends by handing off to 4.2 — two of the tools in that workflow involve writing code. Say the handoff; it is the reason the next video exists.

---

### 4.2 · Why Analysts Write Code — 5.5 min

**Cold open:** *Spreadsheets work well until three things happen: the data grows too large, the same report is needed every week, or someone asks you to prove how a number was produced.*

**Shots:** cold open → title → objective → *What code solves* → *Asking a database a question* → **code slide: SQL** → *Working through data step by step* → **code slide: Python** → end card

**Code slides:** the only code in the entire course, and a different shooting setup from every other video. Highlight line by line. Say the framing sentence first — *"You are not expected to understand the examples coming up"* — before either slide appears, or beginners will disengage on sight of the SQL.

**Note:** this lesson was split out of 4.1, which ran 10.5 minutes — nearly double the course median. Shoot it in the same session as 4.1 since the setup is shared, but keep it a separate video: the code is a different mode of attention from the tool comparison, and a viewer who only wants the toolkit can stop after 4.1.

---

### 4.3 · Careers in Data — 5.5 min

**Cold open:** *Six job titles, heavily overlapping skills, and no agreement between companies about what any of them actually mean. Here is the map.*

**Shots:** cold open → title → objective → *How people move between roles* → **diagram build (6)** → *Shared skills across data roles* → **table** Role / The question they answer → *How to explore which role fits you* → end card

**Diagram build:** start with `Data Analyst` alone and hold — it is the most common way into the field, and the pause makes the point. Then branch: `Business Analyst`, `Analytics Engineer`, `Data Scientist`, then `Data Engineer` and `ML Engineer` on the outside. Say the caption as the last two land: very few people enter the field at the right-hand end. Do not let the delivery imply the course trains for one specific role — it names no destination.

---

### 4.4 · Data Across Industries — 4 min

**Cold open:** *A hospital, an online store, and a school each hire an analyst with identical skills. Within a month, all three are asking completely different questions.*

**Shots:** cold open → title → objective → *Why industry context matters* → **table** Industry / How data is used → *Examples by industry* → *Short case examples* → *Key takeaway* → end card

**Note:** Three-panel visual for the cold open — hospital, store, school — held through the lesson and returned to at the takeaway. This lesson pairs with exercise 3 in chapter 4's set, which asks the viewer to write the three questions themselves.

---

# Chapter 5 — Data Ethics and Privacy

*4 lessons · 27.5 min*

> **One continuous case.** All four lessons follow a mobile money company building automatic small-business loans. Shoot them in one session so the delivery stays consistent, and shoot them in order — lesson 5.4 resolves a decision set up in 5.1. The chapter opener must establish the case before 5.1 starts.

### 5.1 · Responsible and Ethical Use of Data — 8 min

**Cold open:** *The most damaging data projects are rarely built by bad people. They are built by good teams who never stopped to ask whether they should.*

**Shots:** cold open → title → objective → *Case study: the loan scoring project* → **table** Month / Repayment rate → **chart A (truncated axis)** → **chart B (full axis)** → *Principles of responsible data use* → end card

**The chart pair is the most important asset in the course.** Currently drawn in ASCII hash marks because Markdown has no graphics. Video does.

Sequence it precisely:
1. Show the four repayment numbers as a table. Hold. Let the viewer own them.
2. Reveal Chart A — truncated 90–92% axis. Let it look like a success story. Say nothing about the axis.
3. Ask: is this chart lying?
4. **Animate the axis expanding from 90–92% to 0–100%.** Same bars, same data, morphing into four near-identical columns.
5. Then the line: *"Chart A contains no false numbers."*

Do not cut between two static charts. The morph is what makes it undeniable, and it is the moment students will quote back.

---

### 5.2 · Privacy, Consent, and Security — 5.5 min

**Cold open:** *Everyone clicked "agree". Almost nobody read it.*

**Shots:** cold open → title → objective → *Case study: consent in the loan project* → *The life of a piece of personal data* → **diagram build (5)** → *Why security matters* → end card

**Diagram build:** `Ask consent` → `Collect only what is needed` → `Store securely` → `Use for the stated purpose` → `Delete when no longer needed`. Five beats. The last node is the one organizations skip — hold on it.

**Note:** the "would the customer be surprised?" test is the takeaway. Put it on screen as a single-line card.

---

### 5.3 · Bias and Fairness — 7.5 min

**Cold open:** *A model can sort people by gender using data that contains no gender field anywhere in it.*

**Shots:** cold open → title → objective → *Case study: bias in the loan project* → **table** Source of bias / Example → *How bias repeats itself* → **diagram build (4, looping)** → *What fairness means* → end card

**Diagram build:** `Past decisions` → `Training data` → `Model` → `New decisions` → **and back to `Past decisions`**. This is the only cyclic diagram in the course. Build the four nodes, pause, then draw the closing edge — and let it loop two or three times on screen while you explain that the system is now teaching itself its own history.

**Note:** the proxy-variable passage is the hardest idea in the course. Slow down. The cold open promises it; do not resolve it in under a minute.

---

### 5.4 · Data Governance and Regulations — 6.5 min

**Cold open:** *Every failure in this chapter had someone who could have raised a concern.*

**Shots:** cold open → title → objective → *Case study: governance in the loan project* → **table** Problem from earlier lessons / The rule that catches it → *Regulations* → *How the case ends* → end card

**The 7-row table is the chapter's payoff.** Every row is a callback to something the viewer watched go wrong. Reveal one row at a time and name which lesson it came from as it lands. This is the only place in the course where a table is a narrative rather than a reference — shoot it that way, ~15s per row.

**Note:** end on the case resolution, not the regulations. *"It is usually slower. It is not usually worse."* is the last line of chapter 5 — hold, then end card.

---

# Chapter 6 — Conclusion

*2 lessons · 10 min*

### 6.1 · Course Recap: From Data to Decision — 4 min

**Cold open:** *You have completed the core lessons of this course, and you now have the vocabulary this field runs on.*

**Shots:** cold open → title → objective → *What you learned* → *The full journey* → **diagram build (8)** → end card

**Diagram build:** `Problem` → `Question` → `Data` → `Cleaning` → `Analysis` → `Visualization` → `Insight` → `Decision`. Longest build in the course, eight beats. Speak each stage as it lands and name the chapter it came from — this is the recap doing its job.

**Note:** this lesson deliberately does **not** say what comes next — the course promises no curriculum. End on the closing line about judgment outlasting tools, over the diagram. Do not ad-lib a "next course" tease here or in the end card.

---

### 6.2 · Putting It All Together: End-to-End Scenario — 6 min

**Cold open:** *One business problem. Six steps. Every idea in this course, used once.*

**Shots:** cold open → title → objective → *Scenario* → step 1 → step 2 → step 3 → step 4 → step 5 → step 6 → end card

**Note:** Six explicitly numbered steps — the one lesson where on-screen step numbering is literal rather than decorative. Reuse the chapter 3 locator diagram as a persistent corner element, advancing one step per section. Highest bullet density in the course (38), so resist reading them as a list; each step is a beat in one story.

**This is the capstone.** Shoot it last, after the whole course exists, so the callbacks are accurate.

---

# Exercise walkthroughs

*6 videos · 64 min*

## The pause-beat pattern

`<details>` / "Show answer" has no video equivalent. Without a substitute you either read the answer immediately, which teaches nothing, or leave dead air. Use a fixed pattern for all 24 exercises:

1. Read the prompt verbatim, on screen
2. **Question stays up, 5–10 second countdown, silent**
3. Answer, with the reasoning — never just the correct choice

**Reveal multi-part questions one part at a time.** Nine of the 24 exercises have 4–6 numbered sub-parts. Showing all six then answering all six overloads working memory in a way the written version does not, because a reader can look back and a viewer cannot.

## The trap in each set

Every set has one item designed to be gotten wrong, and its answer is deliberately the longest. Give these the full countdown and the full explanation — they are why the exercise videos are worth watching rather than reading.

| Set | Runtime | Exercises | Spend the time here |
|---|---|---|---|
| Chapter 1 | 10.5 min | 5 | **Ex 3 — Quantitative or qualitative?** ID numbers, postal codes and account numbers look numeric to software but are not quantities. |
| Chapter 2 | 8.5 min | 4 | **Ex 4 — Does this need machine learning?** Longest answer in the set; the temptation is to say yes. |
| Chapter 3 | 13 min | 5 | **Ex 3 — Cleaning decisions.** 178-word answer, the longest in the course outside the capstone. Item 3 is the trap. |
| Chapter 4 | 7.5 min | 3 | **Ex 1, task 2** — reaching for the heavier tool. The right tool is the smallest one that does the job. |
| Chapter 5 | 15.5 min | 5 | **Ex 2 — Find the proxy.** 176 words, and the hardest idea in the course. |
| Chapter 6 | 9 min | 2 | **Ex 1 — Run the process yourself.** 331-word answer; effectively a second capstone. |

---

# Suggested shooting order

Not lesson order. Group by setup and by what has to exist first.

| Session | Shoot | Why |
|---|---|---|
| 1 | **2.4** and **4.1** | Calibration. 2.4 is the shortest lesson, 4.1 the longest and the only one with code. Compare actual runtime against the 4.5 and 10.5 estimates; the ratio you get rescales every number in this document. |
| 2 | Chapter 1 (5 lessons) | Establishes tone. Most-watched chapter — students who quit, quit here. |
| 3 | Chapter 2, split across two sittings | Four structurally identical lessons; fatigue will show if shot in one. |
| 4 | Chapter 3 (6 lessons) | Shoot the 3.1 diagram build first — lessons 3.2–3.6 reuse it as a locator. |
| 5 | Chapter 4 remainder | |
| 6 | **Chapter 5, one session, in order** | Continuous case; consistency of delivery matters more here than anywhere else. |
| 7 | Exercise walkthroughs | After all lessons exist, so callbacks are accurate. |
| 8 | Chapter openers, welcome, **6.2** | Written last because they summarize what now exists. |

---

## Runtime summary

| Component | Count | Runtime |
|---|---|---|
| Lesson videos | 27 | ~135.5 min |
| Exercise walkthroughs | 6 | ~64 min |
| Chapter openers | 6 | ~8 min |
| Welcome | 1 | ~3 min |
| **Total** | **40 videos** | **≈ 3h 30m** |

Estimates come from measured prose words at 130–150 wpm with a 1.4–1.9× spoken expansion, plus dwell time per table row, diagram, and code block. Every per-lesson figure already assumes rule 4 — Key Terms shown on the end card, not read aloud — so the numbers here are what you shoot to, and they sum to the total below. Narrating them adds 15–20 minutes and costs you 27 endings.

Line count is not a proxy for runtime and should not be used as one: lesson 4.1 is 83 lines and 674 words, lesson 6.2 is 122 lines and 558 words.
