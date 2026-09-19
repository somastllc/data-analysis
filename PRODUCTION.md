# Production Notes - Recording This Course

**Format:** 23 lesson videos, 5 chapter openers, 1 welcome
**Estimated finished runtime:** ~2h 16m
**Source of truth:** the lesson Markdown files. This document tells you how to shoot them, not what to say. The words are already in the lessons.

---

## Standing rules - every video

**1. Cold open first, no greeting.** The first sentence of each lesson's `## Overview` is the cold open. Say it verbatim over black, before the title card. Never open with "hi, welcome back to the course". The hook is the retention decision, and a greeting spends it.

**2. Say the objective at ~0:15.** Every lesson has a `**By the end:**` line. Say it right after the cold open, before the first section. This is the only signpost the video gets. The "This lesson covers…" sentences were removed from all 16 lessons that had them, precisely so this one lands alone.

**3. The title card is production text, not lesson narration.** Show the lesson title and its course position on screen when needed, but do not add chapter or lesson metadata lines to the lesson Markdown.

**4. Close on lesson content, not repeated vocabulary.** No lesson has a Key Terms end card. Hold the final meaningful teaching slide while you close: one sentence calling back to the lesson's main idea and, where the script provides it, one sentence teasing the next lesson. On the final lesson, land the written closing line and stop.

**4b. Lesson 3.2 ends on the Python output.** `3.2 Why Data Work Uses Code` introduces no new vocabulary; it demonstrates. Hold the last code slide while you say the callback and the tease.

**5. Every `###` heading is a segment boundary.** Cut, change the slide, or move on camera. The lessons average 3–4 sections, which is your shot count.

**6. Tables go on screen as written.** Read the row, then explain it. Do not paraphrase the cells. The wording is deliberate and the viewer is reading along. Budget 10–14 seconds per row.

**7. Diagrams build, never appear complete.** All 10 mermaid diagrams are sequences. Reveal one node per beat, speaking each as it lands. A completed flowchart dropped on screen is read in one second and then ignored for the remaining 40.

**8. Numbers and places are spoken exactly as written.** `$2.50 per kg`, `32°C`, `91.4%`, and any named cities or locations. The examples are deliberately grounded, so don't round the numbers off, and don't substitute a city or a name for one you find easier to say.

---

## Visuals required for recording

This is a production checklist only. The repository contains no generated visual files or build tooling. Create these visuals after the new visual reference is supplied.

| Visual | Count | Notes |
|---|---|---|
| Animated diagram builds | 10 | One per mermaid block. Build order given per lesson below. |
| Chart pair, truncated vs full axis | 2 | **4.1** - highest-value visual in the course. Currently ASCII in the Markdown. |
| Repayment data table | 1 | **4.1** - must appear *before* either chart. |
| Code slides with line highlighting | 2 | **3.2** - SQL and Python. Only code in the course. |
| Content table slides | 15 | Teaching tables only; Key Terms cards have been removed from every lesson. |
| Title card template | 1 | Lesson name + chapter/lesson position. |
| Chapter opener bumper | 5 | 60–90s each. **Script lives in each chapter's `00-opener.md`.** |

---

## Chapter openers

Five short bumpers, 60–90 seconds, ~6.5 minutes total, plus a ~2.5 minute course welcome. **Each chapter's script is `00-opener.md` inside that chapter's folder; the course welcome is `WELCOME.md` at the root.** These six are the only videos with no lesson file behind them, so those files hold the words themselves rather than shot notes. They supply the orientation a reader gets free from the README table and a viewer gets not at all.

The `00-` prefix puts each opener first in its folder, so a chapter folder reads top to bottom in shooting order: opener, then lessons.

Each answers three things: what question this chapter settles, why it comes after the last one, and how many lessons it runs.

| Chapter | The question it settles | Lessons |
|---|---|---|
| 1 - What Is Data? | What am I actually working with, and what happens to it? | 7 |
| 2 - The Data Ecosystem | Who does what, and what are all these job titles? | 7 |
| 3 - Data in the Real World | What tools and jobs does this turn into? | 3 |
| 4 - Data Ethics and Privacy | When should we *not* do the thing we can do? | 4 |
| 5 - Conclusion | Can I do all of it in one pass? | 2 |

**Chapter 4's opener is mandatory, not optional.** Its four lessons are one continuous case: a digital wallet company building automatic small-business loans. A viewer landing on lesson 4.3 without the opener has no idea a loan company has been running for two lessons. State the case up front: the company, the product, and that it will go wrong four different ways.

---

# Chapter 1 - What Is Data?

*7 lessons · 37.5 min*

### 1.1 · What Is Data? - 5.5 min

**Cold open:** *You check your phone and see a digital wallet transfer of `$25`, a weather app showing `32°C`, and a message from school about your attendance.*

**Shots:** cold open → title → objective → *Data: raw facts about the world* → *Data vs information vs insight* → **table** Term / Meaning / Example → **diagram build (3)** → *Where you see data every day*

**Diagram build:** `Data` → `Information` → `Insight`. Build it directly out of the table you just showed, in the same three words and the same order. The table is the definition, the diagram is the motion.

**Note:** The cooking analogy (ingredients → meal → knowing what to cook next) lands better spoken than written. Give it a beat.

---

### 1.2 · Types of Data - 5 min

**Cold open:** *A shop owner opens a spreadsheet of last week's sales and sees numbers, product names, and customer comments all mixed together.*

**Shots:** cold open → title → objective → *Structured vs unstructured data* → *Quantitative vs qualitative data* → *Why data types matter*

**Note:** Two independent classifications, not four categories. Say that explicitly. It is the single most common beginner confusion and the text leaves it implicit. Show them as two axes if you can.

---

### 1.3 · Sources and Formats of Data - 5.5 min

**Cold open:** *You receive a file from a colleague and need to decide whether you can trust it and how to open it.*

**Shots:** cold open → title → objective → *Common sources of data* → *Primary vs secondary data* → *Common data formats* → **table** Format / Common use → *Why source and format matter*

**Note:** The two questions in the last section - "Where did this come from?" and "What format is it in?" - are the takeaway. Put them on screen as a two-line card.

---

### 1.4 · Data Quality - 6.5 min

**Cold open:** *A manager forwards you a customer list and asks for the average age.*

**Shots:** cold open → title → objective → *Why data quality matters* → *Common data quality problems* → *Key quality dimensions* → **table** Dimension / Question it answers → *Example* → **defective table, held silent** → the three faults, one at a time → the fourth fault

**Note:** The Example section is the customer list from the cold open, with four planted faults. **Put it up and say nothing for five seconds.** The lesson's text tells the viewer to read it before going on, so honour that on screen. This is the one lesson in chapter 1 with a built-in pause beat.

Reveal the three that break the average one at a time: impossible age, blank age, duplicated row. Each sits on its own row on purpose, so each fault can be shown doing its own damage; the duplicated row is deliberately *correct* in every cell, which is the hardest of the three to see and the one to spend longest on.

Then land the two numbers on screen together: **72** as the table stands, **30.5** cleaned. That pays off the cold open's "three separate reasons the answer would be wrong", and it is the number the viewer will remember.

Then the fourth fault, separately, because it is the opposite point: `Mogadishu` / `mogadishu` is a real fault that does not affect this question at all. That last beat is the whole lesson. Do not merge it into the list of three.

---

### 1.5 · The Data Lifecycle - 5 min

**Cold open:** *A shop records a sale of rice at `$2.50 per kg` on a Tuesday morning.*

**Shots:** cold open → title → objective → *What is the data lifecycle?* → **diagram build (7)** → **table** Stage / What happens / The rice sale → *Creating is not the same as collecting* → *Processing is where the time goes* → *Data does not live forever* → *Where data sits in its life changes what it can tell you*

**Diagram build:** `Create` → `Collect` → `Store` → `Process` → `Analyze` → `Visualize` → `Delete`. Seven beats, one per stage, then hold the complete chain while the table walks the same seven with the rice sale in the third column. Diagram first, table second: the diagram gives the shape, the table gives the content.

**Note:** The cold open and the final section are the same sentence pair, four minutes apart. Open on the Tuesday morning sale; close on the four-year-old archive. Let the viewer notice that the lesson ended where it started.

*Creating is not the same as collecting* is the beat that earns the lesson. The line to land is that data you never collected leaves no gap to notice, unlike a blank cell. Put a blank cell on screen, then put nothing on screen, and say which of the two is more dangerous.

The next lesson asks what happens to all of this at enormous scale. Do not name the pipeline here; 2.5 owns it.

---

### 1.6 · Big Data - 5.5 min

**Cold open:** *A market trader's sales book holds four hundred rows and answers every question the trader has.*

**Shots:** cold open → title → objective → *The trader and the wallet* → *What makes data big* → **table** The three Vs / The question it answers / The market trader / The digital wallet → *Big is a relationship, not a number* → *What changes when data really is big* → *Big is not the same as useful*

**Note:** The cold open is half a comparison. Deliver the trader's sales book and the digital wallet in one breath, over the two-panel sketch, and let the viewer see the four hundred rows next to the six machines before any definition arrives.

The four-column table is the widest in the course. Read it **down the columns, not across the rows**: volume, velocity, variety for the trader, then the same three for the wallet. Reading it across turns three ideas into six.

**The beat that earns the lesson** is *Big is a relationship, not a number*. Put the question on screen on its own: **has the usual way of working broken?** This is the one lesson where the course pushes back on a term the viewer has already heard used loosely, so land the line about buying systems nobody needed and pause on it.

*What changes when data really is big* is four cards, and the fourth is the handoff: a field exists to move data at this scale. Chapter 2 is about to spend seven lessons on the people in it, so say that transition out loud.

Close on the trader. Four hundred honest rows against four billion unchecked ones is the chapter's argument about quality, restated at scale.

---

### 1.7 · Why Data Matters - 4.5 min

**Cold open:** *Two shop owners sell the same products at the same prices.*

**Shots:** cold open → title → objective → *Data helps companies make better decisions* → *Data creates competitive advantage* → *Data skills are widely valuable* → *Data also comes with responsibility*

**Note:** Four short sections and no diagram, which makes it the flattest-shaped lesson in chapter 1, and it now closes the chapter. Carry it on delivery, and let the two-shop-owners story run through all four sections rather than dropping it after the cold open. In *Data creates competitive advantage*, land "What separates them is that somebody looked" first, then give the quote a beat: "Without data, you are just another person with an opinion." Last section is the setup for chapter 4; point forward.

---

# Chapter 2 - The Data Ecosystem

*7 lessons · 29 min*

> **Watch the density here.** This is the course's most vocabulary-heavy chapter. Lessons 2.3 and 2.4 deliberately separate data science from machine learning; keep their examples connected, but do not let either lesson borrow the other's definition. Shoot 2.2 and 2.6 in different sittings because both are prose-led field explanations with similar pacing.

### 2.1 · Types of Analytics - 4 min

**Cold open:** *A manager looks at last month's sales report and asks four questions: "What happened? Why did it happen? What might happen next? What should we do?"*

**Shots:** cold open → title → objective → *What is analytics?* → **diagram build (4)** → *The four types of analytics* → **table** Type / Question / Example → *Why this matters*

**Diagram build:** `Descriptive` → `Diagnostic` → `Predictive` → `Prescriptive`. Build one per type as you introduce it, so the diagram completes exactly as the section ends.

**Note:** The manager's four questions in the cold open map directly onto the four types. Use that connection as the lesson's structure.

---

### 2.2 · Data Analysis - 4 min

**Cold open:** *A wholesaler supplies shops in Mogadishu, Hargeisa, and Kismayo. Some shops keep ordering products, while other shops send many products back unsold.*

**Shots:** cold open → title → objective → *What is data analysis?* → *Questions data analysis answers* → *What data analysis can produce* → *Example*

**Note:** Keep the lesson centered on the activity, not job titles. The wholesaler story should carry the overview, question examples, and final example.

---

### 2.3 · Data Science - 4.5 min

**Cold open:** *A mobile company notices that thousands of customers have stopped buying their monthly bundles.*

**Shots:** cold open → title → objective → *What is data science?* → **table** Part / What it contributes → *What data scientists do* → *Example*

**Note:** Mention once that data science may use statistical analysis, experiments, simulations, careful exploration, or machine learning. Keep the falling-renewals example focused on framing, investigation, hypothesis testing, and evidence. Land the final change of question as the handoff to 2.4: *why did customers leave?* becomes *which customers may leave next?*

---

### 2.4 · Machine Learning - 3.5 min

**Cold open:** *Your inbox quietly moved a message to spam this morning.*

**Shots:** cold open → title → objective → *What is machine learning?* with **diagram build (5)** → *When a project actually needs machine learning* with **table** Question / What it needs → *Example*

**Diagram build:** `Past examples` → `Training` → `Trained model` → `Apply to new data` → `Prediction`. The transition from the training side to the use side is the conceptual hinge; pause on the trained model before introducing new data.

**Note:** **The line to land is "no examples, no model".** It is the constraint every beginner meets first, and it reframes machine learning as a data problem rather than a clever-algorithm problem.

---

### 2.5 · Where Data Lives and the Data Pipeline - 4 min

**Cold open:** *The sales number on a manager's dashboard this morning began three weeks ago as a digital wallet payment for a sack of rice.*

**Shots:** cold open → title → objective → *Where data lives* → **table** System / Purpose → *What is a data pipeline?* → **diagram build (6)** → *Example*

**Diagram build:** `Collect` → `Store` → `Clean` → `Transform` → `Analyze` → `Share`. Six beats, the longest build in chapter 2. Consider running it in reverse first, from the dashboard back to the digital wallet payment, matching the cold open, then forward.

**Note:** The viewer met this chain as the lifecycle in **1.5**, and the two builds share three words exactly: `Collect`, `Store`, `Analyze`. Say that out loud on the diagram rather than pretending it is new.

Then spend the time on the differences, which are the lesson. `Clean` and `Transform` are 1.5's single `Process` stage pulled apart, because a pipeline has to do them as separate jobs. `Share` is narrower than 1.5's `Visualize`. And a pipeline has no `Create` or `Delete` at all, because it only ever handles data that already exists and is still wanted.

The other thing 1.5 does not have is the storage table, and the fact that a pipeline runs on a schedule with nobody deciding each morning that today the data gets cleaned.

---

### 2.6 · Data Engineering - 3.5 min

**Cold open:** *An analyst opens a report and finds three different versions of the same sales numbers - one outdated, one incomplete, one in the wrong format.*

**Shots:** cold open → title → objective → *What is data engineering?* → *What data engineers do* → *Example*

**Note:** Three conflicting numbers is a screen graphic, not a spoken list. Show the three versions side by side during the cold open.

---

### 2.7 · How These Fields Work Together - 5.5 min

**Cold open:** *A telecom company sees that customers are not renewing their monthly data bundles.*

**Shots:** cold open → title → objective → *How they work together* → **diagram build (6)** → *Where analytics types fit* → *Key takeaway*

**Diagram build:** `Data engineer` → `Data analyst` → `BI professional` → `Data scientist` → `ML engineer` → `Business team`, one per numbered step as you read it. This is the chapter's payoff and the only frame that holds all six contributors at once.

**Note:** The fifth step is conditional: a model enters only if individual prediction helps the decision. The callback to the four analytics types from 2.1 presents them as kinds of questions shared across the ecosystem, not four rigid stages or four job descriptions. Land the close on the completed diagram.

---

# Chapter 3 - Data in the Real World

*3 lessons · 16 min*

> **This chapter names no destination.** The course trains for no single role, so the delivery must not imply one. The cold opens of 3.1 and 3.3 avoid "analyst", and 3.2 was retitled for the same reason: the tooling and the industries belong to the whole field, not to one job title in it. Career titles and movement between roles are covered in 2.7.

### 3.1 · Modern Data Tools - 5.5 min

**Cold open:** *Everyone new to data asks which tool they should learn first.*

**Shots:** cold open → title → objective → *Why there are many tools* → *Core tools in data work* → **table** Tool / What it is / When you reach for it → *Example workflow* → **diagram build (4)**

**Diagram build:** `SQL` → `Python`, then **branch** to `Excel report` and `Power BI dashboard` simultaneously. The branch is the point: one analysis, two audiences. Do not build the two outputs sequentially.

**Note:** ends by handing off to 3.2, because two of the tools in that workflow involve writing code. Say the handoff; it is the reason the next video exists.

---

### 3.2 · Why Data Work Uses Code - 6 min

**Cold open:** *Spreadsheets work well until three things happen: the data grows too large, the same report is needed every week, or someone asks you to prove how a number was produced.*

**Shots:** cold open → title → objective → *What code solves* → *Asking a database a question* → **code slide: SQL** → *Working through data step by step* → **code slide: Python**

**Code slides:** the only code in the entire course, and a different shooting setup from every other video. Highlight line by line. Say the framing sentence first, *"You are not expected to understand the examples coming up"* - before either slide appears, or beginners will disengage on sight of the SQL.

**Note:** this lesson was split out of 3.1, which ran 10.5 minutes, nearly double the course median. Shoot it in the same session as 3.1 since the setup is shared, but keep it a separate video: the code is a different mode of attention from the tool comparison, and a viewer who only wants the toolkit can stop after 3.1.

---

### 3.3 · Data Across Industries - 4.5 min

**Cold open:** *A clinic, a money transfer service, and a school can use the same data skills. The tools may be similar, but each place has different questions and different data.*

**Shots:** cold open → title → objective → *Same skills, different questions* → *Why domain knowledge matters* → *Examples from different industries* → **table** Industry / Example question / Domain knowledge needed → *Key point*

**Note:** Use the three-panel clinic, money transfer, and school visual for the overview and return to it at the key point. The main idea is that data skills transfer between industries, but domain knowledge helps an analyst ask useful questions and understand the answers.

Keep the examples simple. The table shows how the questions and domain knowledge change across eight industries.

---

# Chapter 4 - Data Ethics and Privacy

*4 lessons · 29 min*

> **One continuous case.** All four lessons follow a digital wallet company building automatic small-business loans. Shoot them in one session so the delivery stays consistent, and shoot them in order, since lesson 4.4 resolves a decision set up in 4.1. The chapter opener must establish the case before 4.1 starts.

### 4.1 · Responsible and Ethical Use of Data - 8 min

**Cold open:** *The most damaging data projects are rarely built by bad people. They are built by good teams who never stopped to ask whether they should.*

**Shots:** cold open → title → objective → **definition:** Data ethics → *Case study: the loan scoring project* → *When the numbers are true but the chart lies* → **table** Month / Repayment rate → **chart A (truncated axis)** → **chart B (full axis)** → *Principles of responsible data use*

**The chart pair is the most important visual in the course.** Currently drawn in ASCII hash marks because Markdown has no graphics. Video does.

Sequence it precisely:
1. Show the four repayment numbers as a table. Hold. Let the viewer own them.
2. Reveal Chart A - truncated 90–92% axis. Let it look like a success story. Say nothing about the axis.
3. Ask: is this chart lying?
4. **Animate the axis expanding from 90–92% to 0–100%.** Same bars, same data, morphing into four near-identical columns.
5. Then the line: *"Chart A contains no false numbers."*

Do not cut between two static charts. The morph is what makes it undeniable, and it is the moment students will quote back.

---

### 4.2 · Privacy, Consent, and Security - 5.5 min

**Cold open:** *Everyone clicked "agree". Almost nobody read it.*

**Shots:** cold open → title → objective → **definitions:** Privacy / Consent → *Case study: consent in the loan project* → *The life of a piece of personal data* → **diagram build (5)** → *Security in the loan project*

**Diagram build:** `Ask consent` → `Collect only what is needed` → `Store securely` → `Use for the stated purpose` → `Delete when no longer needed`. Five beats. The last node is the one organizations skip. Hold on it.

**Note:** the "would the customer be surprised?" test is the takeaway. Put it on screen as a single-line card.

---

### 4.3 · Bias and Fairness - 7.5 min

**Cold open:** *A model can sort people by gender using data that contains no gender field anywhere in it.*

**Shots:** cold open → title → objective → **definition:** Bias → **table** Source of bias / Example → *Case study: bias in the loan project* → *How bias repeats itself* → **diagram build (4, looping)** → *What fairness means*

**Diagram build:** `Past decisions` → `Training data` → `Model` → `New decisions` → **and back to `Past decisions`**. This is the only cyclic diagram in the course. Build the four nodes, pause, then draw the closing edge, and let it loop two or three times on screen while you explain that the system is now teaching itself its own history.

**Note:** the proxy-variable passage is the hardest idea in the course. Slow down. The cold open promises it; do not resolve it in under a minute.

---

### 4.4 · Data Governance and Regulations - 8 min

**Cold open:** *Every failure in this chapter had someone who could have raised a concern.*

**Shots:** cold open → title → objective → **definition:** Data governance → *Case study: governance in the loan project* → **table** Problem from earlier lessons / The rule that catches it → *Regulations* → *How the case ends*

**The 7-row table is the chapter's payoff.** Six of the seven rows are callbacks to something the viewer watched go wrong. Reveal those one at a time and name which lesson each came from. The seventh, retention, never happened in the case, and the lesson says so on purpose: the point is that rules are written from other people's failures, not only your own as it lands. This is the only place in the course where a table is a narrative rather than a reference. Shoot it that way, ~15s per row.

**Note:** end on the case resolution, not the regulations. *"It is usually slower. It is not usually worse."* is the last line of chapter 4. Hold on that final line while you close the chapter.

---

# Chapter 5 - Conclusion

*2 lessons · 11 min*

### 5.1 · Course Recap: The Life of One Record - 4.5 min

**Cold open:** *You have completed the core lessons of this course, and you now have the vocabulary this field runs on.*

**Shots:** cold open → title → objective → *What you learned* → *One record, start to finish* → **diagram build (7)** → **table** Stage / What happens to the record / Where you met it → *What the record cannot tell you*

**Diagram build:** the same seven-stage lifecycle from **1.5**, rebuilt here. Speak each stage as it lands and name the chapter it came from, then hold the complete chain while the table walks the same seven stages against the rice sale. The viewer has seen this diagram before; that is the point of a recap.

**Note:** this lesson deliberately does **not** say what comes next, because the course promises no curriculum. End on the closing line about judgment outlasting tools, over the diagram. Do not ad-lib a "next course" tease.

---

### 5.2 · Putting It All Together: End-to-End Scenario - 6.5 min

**Cold open:** *One business problem. One dataset. Every idea in this course, used once.*

**Shots:** cold open → title → objective → *Scenario* → *Create and collect* → *Store and process* → *Analyze and visualize* → **table** Role / What they contributed → *What ethics asked at each stage* → *The decision* → *Archive and delete* → *What this scenario shows*

**Note:** The lesson walks one dataset through the lifecycle. Reuse the 1.5 lifecycle diagram as a persistent corner element, advancing one stage per section. Highest bullet density in the course, so resist reading them as a list; each stage is a beat in one story.

The beat to protect is in *Create and collect*: the users who never answered the survey created no record, so their reasons were never collected. It pays off 1.5 directly, and it is the only place the capstone says something the charts cannot.

*Archive and delete* is the last teaching section in the course. Three different retention answers for three kinds of data, and the point that deciding what to destroy is a governance call rather than an analysis one.

**This is the capstone.** Shoot it last, after the whole course exists, so the callbacks are accurate.

---

# Suggested shooting order

Not lesson order. Group by setup and by what has to exist first.

| Session | Shoot | Why |
|---|---|---|
| 1 | **2.1** and **4.1** | Calibration. 2.1 is among the shortest and is diagram-led; 4.1 is the longest and is table-and-prose. Compare actual runtime against the 4 and 8 minute estimates; the ratio you get rescales every number in this document. Shoot 4.1 on its own here, then reshoot it in session 5 with the rest of its chapter if the delivery drifts. |
| 2 | Chapter 1 (7 lessons) | Establishes tone. Most-watched chapter - students who quit, quit here. Shoot the 1.5 lifecycle build early; chapter 5 reuses it. |
| 3 | Chapter 2, split across two sittings | Seven concept-heavy lessons; fatigue will show if shot in one. Keep 2.3 and 2.4 in the same sitting so their distinction and handoff remain clear. |
| 4 | Chapter 3 (3 lessons) | **3.2** needs its own setup for the code slides, and is the only video that does. Shoot it with 3.1, whose handoff sets it up. |
| 5 | **Chapter 4, one session, in order** | Continuous case; consistency of delivery matters more here than anywhere else. |
| 6 | Chapter openers, welcome, **5.2** | Written last because they summarize what now exists. |

---

## Runtime summary

| Component | Count | Runtime |
|---|---|---|
| Lesson videos | 23 | ~129 min |
| Chapter openers | 5 | ~6.5 min |
| Welcome | 1 | ~3 min |
| **Total** | **29 videos** | **≈ 2h 19m** |

Estimates come from measured prose words at 130–150 wpm with a 1.4–1.9× spoken expansion, plus dwell time per table row, diagram, and code block. Every lesson holds its final teaching slide during the close; no Key Terms cards remain. The closing narration is unchanged, so this does not materially change the estimates.

Line count is not a proxy for runtime and should not be used as one: lesson 3.1 is 83 lines and 674 words, lesson 5.2 is shorter in lines and longer in words.
