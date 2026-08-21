# Production Notes - Recording This Course

**Format:** 27 lesson videos, 6 chapter openers, 1 welcome
**Estimated finished runtime:** ~2h 40m
**Source of truth:** the lesson Markdown files. This document tells you how to shoot them, not what to say. The words are already in the lessons.

---

## Standing rules - every video

**1. Cold open first, no greeting.** The first sentence of each lesson's `## Overview` is the cold open. Say it verbatim over black, before the title card. Never open with "hi, welcome back to the course". The hook is the retention decision, and a greeting spends it.

**2. Say the objective at ~0:15.** Every lesson has a `**By the end:**` line. Say it right after the cold open, before the first section. This is the only signpost the video gets. The "This lesson covers…" sentences were removed from all 16 lessons that had them, precisely so this one lands alone.

**3. The metadata block is the title card, not narration.** `**Chapter:** N - Name` / `**Lesson:** N of TOTAL` goes on screen. Never read aloud.

**4. Key Terms tables are end cards. Do not narrate them.** Every lesson closes with a Key Terms table. Put it on screen and hold it. Over it, say two things: one sentence calling back to the lesson's main idea, and one sentence teasing the next lesson. Reading 90 glossary rows aloud across the course would cost 15–20 minutes and would put the flattest possible 45 seconds at the end of all 27 videos, which is the exact place you need the click to the next one.

**4b. One lesson has no Key Terms table.** `4.2 Why Data Work Uses Code` introduces no new vocabulary; it demonstrates. End it on the Python output instead, holding the last code slide while you say the callback and the tease. Every other lesson uses its table.

**5. Every `###` heading is a segment boundary.** Cut, change the slide, or move on camera. The lessons average 3–4 sections, which is your shot count.

**6. Tables go on screen as written.** Read the row, then explain it. Do not paraphrase the cells. The wording is deliberate and the viewer is reading along. Budget 10–14 seconds per row.

**7. Diagrams build, never appear complete.** Ten of the 11 mermaid diagrams are sequences. Reveal one node per beat, speaking each as it lands. A completed flowchart dropped on screen is read in one second and then ignored for the remaining 40.

**7b. The exception is 2.3, which is not a sequence.** Machine learning sitting inside data science is a containment picture: no arrows, no order. Build it by drawing the boundary first and dropping the four contents into it, ending on `Machine learning`, the accented one and the reason the diagram exists. Do not imply a flow between the four.

**8. Numbers and places are spoken exactly as written.** `$2.50 per kg`, `32°C`, `91.4%`, Hargeisa, Burco, Muqdisho. The examples are deliberately Somali and grounded, so don't round the numbers off, and don't substitute a city or a name for one you find easier to say.

---

## Build these assets before you shoot

| Asset | Count | Notes |
|---|---|---|
| Animated diagram builds | 11 | One per mermaid block. Build order given per lesson below. |
| Chart pair, truncated vs full axis | 2 | **5.1** - highest-value visual in the course. Currently ASCII in the Markdown. |
| Repayment data table | 1 | **5.1** - must appear *before* either chart. |
| Code slides with line highlighting | 2 | **4.2** - SQL and Python. Only code in the course. |
| Content table slides | 16 | Excludes the 26 Key Terms end cards. |
| Key Terms end card template | 1 | Reusable; table content differs per lesson. |
| Title card template | 1 | Lesson name + chapter/lesson position. |
| Chapter opener bumper | 6 | 60–90s each. **Script lives in each chapter's `00-opener.md`.** |

---

## Chapter openers

Six short bumpers, 60–90 seconds, ~8 minutes total, plus a ~2.5 minute course welcome. **Each chapter's script is `00-opener.md` inside that chapter's folder; the course welcome is `WELCOME.md` at the root.** These seven are the only videos with no lesson file behind them, so those files hold the words themselves rather than shot notes. They supply the orientation a reader gets free from the README table and a viewer gets not at all.

The `00-` prefix puts each opener first in its folder, so a chapter folder reads top to bottom in shooting order: opener, then lessons.

Each answers three things: what question this chapter settles, why it comes after the last one, and how many lessons it runs.

| Chapter | The question it settles | Lessons |
|---|---|---|
| 1 - What Is Data? | What am I actually working with? | 5 |
| 2 - The Data Ecosystem | Who does what, and what are all these job titles? | 6 |
| 3 - The Data Process | What are the steps, in order, from question to decision? | 6 |
| 4 - Data in the Real World | What tools and jobs does this turn into? | 4 |
| 5 - Data Ethics and Privacy | When should we *not* do the thing we can do? | 4 |
| 6 - Conclusion | Can I do all of it in one pass? | 2 |

**Chapter 5's opener is mandatory, not optional.** Its four lessons are one continuous case: a mobile money company building automatic small-business loans. A viewer landing on lesson 5.3 without the opener has no idea a loan company has been running for two lessons. State the case up front: the company, the product, and that it will go wrong four different ways.

---

# Chapter 1 - What Is Data?

*5 lessons · 27 min*

### 1.1 · What Is Data? - 5.5 min

**Cold open:** *You check your phone and see a mobile money transfer of `$25`, a weather app showing `32°C`, and a message from school about your attendance.*

**Shots:** cold open → title → objective → *Data: raw facts about the world* → *Data vs information vs insight* → **table** Term / Meaning / Example → **diagram build (3)** → *Where you see data every day* → end card

**Diagram build:** `Data` → `Information` → `Insight`. Build it directly out of the table you just showed, in the same three words and the same order. The table is the definition, the diagram is the motion.

**Note:** The cooking analogy (ingredients → meal → knowing what to cook next) lands better spoken than written. Give it a beat.

---

### 1.2 · Types of Data - 5 min

**Cold open:** *A shop owner opens a spreadsheet of last week's sales and sees numbers, product names, and customer comments all mixed together.*

**Shots:** cold open → title → objective → *Structured vs unstructured data* → *Quantitative vs qualitative data* → *Why data types matter* → end card

**Note:** Two independent classifications, not four categories. Say that explicitly. It is the single most common beginner confusion and the text leaves it implicit. Show them as two axes if you can.

---

### 1.3 · Sources and Formats of Data - 5.5 min

**Cold open:** *You receive a file from a colleague and need to decide whether you can trust it and how to open it.*

**Shots:** cold open → title → objective → *Common sources of data* → *Primary vs secondary data* → *Common data formats* → **table** Format / Common use → *Why source and format matter* → end card

**Note:** The two questions in the last section - "Where did this come from?" and "What format is it in?" - are the takeaway. Put them on screen as a two-line card.

---

### 1.4 · Data Quality Basics - 6.5 min

**Cold open:** *A manager forwards you a customer list and asks for the average age.*

**Shots:** cold open → title → objective → *Why data quality matters* → *Common data quality problems* → *Key quality dimensions* → **table** Dimension / Question it answers → *Example* → **defective table, held silent** → the three faults, one at a time → the fourth fault → end card

**Note:** The Example section is the customer list from the cold open, with four planted faults. **Put it up and say nothing for five seconds.** The lesson's text tells the viewer to read it before going on, so honour that on screen. This is the one lesson in chapter 1 with a built-in pause beat.

Reveal the three that break the average one at a time: impossible age, blank age, duplicated row. Each sits on its own row on purpose, so each fault can be shown doing its own damage; the duplicated row is deliberately *correct* in every cell, which is the hardest of the three to see and the one to spend longest on.

Then land the two numbers on screen together: **72** as the table stands, **30.5** cleaned. That pays off the cold open's "three separate reasons the answer would be wrong", and it is the number the viewer will remember.

Then the fourth fault, separately, because it is the opposite point: `Hargeisa` / `hargeisa` is a real fault that does not affect this question at all. That last beat is the whole lesson. Do not merge it into the list of three.

---

### 1.5 · Why Data Matters - 4.5 min

**Cold open:** *Two shop owners sell the same products at the same prices.*

**Shots:** cold open → title → objective → *Data helps organizations make better decisions* → *Data creates competitive advantage* → *Data skills are widely valuable* → *Data also comes with responsibility* → end card

**Note:** Four short sections and no diagram, which makes it the flattest-shaped lesson in chapter 1. Carry it on delivery, and let the two-shop-owners story run through all four sections rather than dropping it after the cold open. Last section is the setup for chapter 5; point forward.

---

# Chapter 2 - The Data Ecosystem

*6 lessons · 30 min*

> **Watch the monotony here.** 2.2 and 2.4 are still structurally identical: same length, same four-section shape, no diagram. 2.3 and 2.6 used to be too, and each has since gained a diagram, which is most of what separates them now. Shoot 2.2 and 2.4 in different sittings and vary framing between them.

### 2.1 · Types of Analytics - 4.5 min

**Cold open:** *A manager looks at last month's sales report and asks three questions in one meeting: "What happened? Why did it happen? What should we do next?"*

**Shots:** cold open → title → objective → *What is analytics?* → **diagram build (4)** → *The four types of analytics* → **table** Type / Question / Example → *Simple way to remember them* → *Why this matters* → end card

**Diagram build:** `Descriptive` → `Diagnostic` → `Predictive` → `Prescriptive`. Build one per type as you introduce it, so the diagram completes exactly as the section ends.

**Note:** The manager's three questions in the cold open map onto the first three types. Say so. It turns the hook into the structure.

---

### 2.2 · Data Analysis and Business Intelligence - 4.5 min

**Cold open:** *A shop owner notices that one product sells out every week while another sits on the shelf.*

**Shots:** cold open → title → objective → *What is data analysis?* → *What is business intelligence?* → *How they relate* → *Example* → end card

**Note:** The shop owner wants two different things: to understand *why*, and to check it monthly without digging. That is the analysis/BI split in one sentence. Hold on it.

---

### 2.3 · Data Science and Machine Learning - 6 min

**Cold open:** *Your inbox quietly moved a message to spam this morning.*

**Shots:** cold open → title → objective → *What is data science?* → *What is machine learning?* → *How they relate* → **diagram build (nest)** → *When a project actually needs machine learning* → **table** Question / What it needs → *Example* → end card

**Diagram build:** the containment picture; see standing rule 7b. Boundary labelled `Data science` first, then `Statistics`, `Programming`, `Domain knowledge`, and `Machine learning` last and accented.

**Note:** This was the shortest lesson in the course and the one with the least visual support, on the subject students are most curious about. It now carries the nesting diagram and a three-row table of what does and does not need a model. **The line to land is "no examples, no model".** It is the constraint every beginner meets first, and it reframes machine learning as a data problem rather than a clever-algorithm problem.

---

### 2.4 · Data Engineering - 4.5 min

**Cold open:** *An analyst opens a report and finds three different versions of the same sales numbers - one outdated, one incomplete, one in the wrong format.*

**Shots:** cold open → title → objective → *What is data engineering?* → *What data engineers do* → *Why data engineering matters* → *Example* → end card

**Note:** Three conflicting numbers is a screen graphic, not a spoken list. Show the three versions side by side during the cold open.

---

### 2.5 · Where Data Lives and the Data Pipeline - 5.5 min

**Cold open:** *The sales figure on a manager's dashboard this morning began three weeks ago as a mobile money payment for a sack of rice.*

**Shots:** cold open → title → objective → *Where data lives* → **table** System / Purpose → *What is a data pipeline?* → **diagram build (6)** → *Example* → end card

**Diagram build:** `Collect` → `Store` → `Clean` → `Transform` → `Analyze` → `Share`. Six beats, the longest build in chapter 2. Consider running it in reverse first, from the dashboard back to the mobile money payment, matching the cold open, then forward.

---

### 2.6 · How These Fields Work Together - 5 min

**Cold open:** *One customer cancels a subscription.*

**Shots:** cold open → title → objective → *One ecosystem, many roles* → *How they work together* → **diagram build (5)** → *Where analytics types fit* → *Key takeaway* → end card

**Diagram build:** `Data engineer` → `Data analyst` → `BI dashboard` → `Data scientist` → `Business team`, one per numbered step as you read it. This is the chapter's payoff and the only frame that holds all five roles at once.

**Note:** The lesson now closes on the point that the four analytics types from 2.1 were four stages of one job spread across five people. That callback is the end of the chapter. Land it on the completed diagram.

---

# Chapter 3 - The Data Process

*6 lessons · 32.5 min*

> **The chapter is field-neutral, and the delivery has to be too.** Every lesson carries one short beat naming the same step as a data scientist, or ML, would run it. Those beats are the reason this chapter is not "the analyst chapter". Do not cut them for time, and do not let the analyst examples around them set the tone for the whole chapter.

### 3.1 · Defining the Problem and Asking Questions - 6 min

**Cold open:** *"Can you look into the sales data?" is one of the most common requests an analyst receives, and it is not yet a question.*

**Shots:** cold open → title → objective → **diagram build (7)** → *Start with the business problem* → *Know your stakeholders* → *How to ask good analytical questions* → *The same first step, whatever gets built* → *Example* → end card

**Diagram build:** `Define problem` → `Ask questions` → `Collect data` → `Clean data` → `Analyze and visualize` → `Communicate insights` → `Make decisions`. **This is the map for the whole chapter.** Build all seven here, then bring it back as a static locator card at the top of lessons 3.2–3.6 with the current step highlighted. Cheapest continuity device in the course.

---

### 3.2 · Collecting Data - 5 min

**Cold open:** *The easiest data to obtain is rarely the data that answers your question.*

**Shots:** cold open → title → **locator: step 3** → objective → *What is data collection?* → *Common collection methods* → **table** Method / Example → *How much is enough depends on what gets built* → *Questions to ask before using data* → *Example* → end card

---

### 3.3 · Cleaning Data - 5 min

**Cold open:** *Ask working analysts what takes up most of their time and the answer is rarely "analysis".*

**Shots:** cold open → title → **locator: step 4** → objective → *Why clean data?* → **table** Task / Example → *Common cleaning tasks* → *How much cleaning is enough?* → *Example* → end card

**Note:** the lesson calls cleaning "a large subject in its own right" and stops there. Deliver it that way, and do not promise a later course, here or anywhere else in the shoot.

---

### 3.4 · Analyzing and Visualizing Data - 7.5 min

**Cold open:** *The same table of numbers can hide a trend completely or make it obvious in one second.*

**Shots:** cold open → title → **locator: step 5** → objective → *What happens during analysis?* → *When the output is a model instead of a chart* → *Why visualize data?* → **table** Question type / Chart type → *Common chart types* → *What analysis cannot prove* → **the three explanations, one at a time** → *Example* → end card

**Note:** The cold open is a promise of a visual. Deliver it in the first 20 seconds: same numbers as a table, then as a chart, side by side. Do not let this lesson be the one where you *talk about* visualization.

Chart choice is named and dropped on purpose. Do not promise where it gets taught.

**The correlation section is the most valuable ninety seconds in chapter 3.** The lesson's objective always promised the viewer could "say what analysis can and cannot prove"; until now the lesson never addressed it. Put the three explanations on screen **one at a time, over the same unchanged chart** - longer hours cause the sales, the sales pay for the longer hours, the busy street causes both. The chart never changes, and that is the entire point: three different worlds, one identical picture. Chapter 5's misleading-charts and bias lessons both assume the viewer has this.

---

### 3.5 · Communicating Insights - 4.5 min

**Cold open:** *An analyst spends three weeks on an investigation, presents twelve slides, and nothing changes.*

**Shots:** cold open → title → **locator: step 6** → objective → *Analysis without communication has limited value* → *What to include in a data report* → *Tips for clear communication* → *Know your audience* → end card

**Note:** "It was also the fourth thing mentioned, on slide nine." Land that line, then pause. It is the best-written sentence in chapter 3.

---

### 3.6 · From Analysis to Decisions - 4.5 min

**Cold open:** *Every analysis rests on things you did not check.*

**Shots:** cold open → title → **locator: step 7, completing the map** → objective → *From insight to action* → *Assumptions and limitations* → *Putting a model into use is also a decision* → *Why decisions still need judgment* → *Example* → end card

**Note:** Complete the locator diagram on screen here. The chapter closes as the map fills in.

The model section is the chapter's last field-neutral beat and the setup for chapter 5, because an unexamined assumption running unattended is what chapter 5 spends four lessons on. Say it plainly and move on; do not name what is coming.

---

# Chapter 4 - Data in the Real World

*4 lessons · 21.5 min*

> **This chapter names no destination.** The rule already stated for 4.3 applies to all four lessons: the course trains for no single role, so the delivery must not imply one. The cold opens of 4.1 and 4.4 were rewritten to drop "analyst", and 4.2 was retitled for the same reason: the tooling and the industries belong to the whole field, not to one job title in it.

### 4.1 · The Modern Data Toolkit - 5.5 min

**Cold open:** *Everyone new to data asks which tool to learn first.*

**Shots:** cold open → title → objective → *Why there are many tools* → *Core tools in data work* → **table** Tool / What it is / When you reach for it → *Example workflow* → **diagram build (4)** → end card

**Diagram build:** `SQL` → `Python`, then **branch** to `Excel report` and `Power BI dashboard` simultaneously. The branch is the point: one analysis, two audiences. Do not build the two outputs sequentially.

**Note:** ends by handing off to 4.2, because two of the tools in that workflow involve writing code. Say the handoff; it is the reason the next video exists.

---

### 4.2 · Why Data Work Uses Code - 6 min

**Cold open:** *Spreadsheets work well until three things happen: the data grows too large, the same report is needed every week, or someone asks you to prove how a number was produced.*

**Shots:** cold open → title → objective → *What code solves* → *Asking a database a question* → **code slide: SQL** → *Working through data step by step* → **code slide: Python** → end card

**Code slides:** the only code in the entire course, and a different shooting setup from every other video. Highlight line by line. Say the framing sentence first, *"You are not expected to understand the examples coming up"* - before either slide appears, or beginners will disengage on sight of the SQL.

**Note:** this lesson was split out of 4.1, which ran 10.5 minutes, nearly double the course median. Shoot it in the same session as 4.1 since the setup is shared, but keep it a separate video: the code is a different mode of attention from the tool comparison, and a viewer who only wants the toolkit can stop after 4.1.

---

### 4.3 · Careers in Data - 5.5 min

**Cold open:** *Six job titles, heavily overlapping skills, and no agreement between companies about what any of them actually mean. Here is the map.*

**Shots:** cold open → title → objective → *How people move between roles* → **diagram build (6)** → *Shared skills across data roles* → *Common data careers* → **table** Role / The question they answer → *The title is not the job* → end card

**Diagram build:** start with `Data Analyst` alone and hold. It is the most common way into the field, and the pause makes the point. Then branch: `Business Analyst`, `Analytics Engineer`, `Data Scientist`, then `Data Engineer` and `ML Engineer` on the outside. Say the caption as the last two land: very few people enter the field at the right-hand end. Do not let the delivery imply the course trains for one specific role. It names no destination. **The lesson used to end with a five-branch "which role fits you" quiz, which did exactly that; it has been replaced.** The closing section now delivers the cold open's actual claim, that titles are inconsistent between companies, and sends the viewer to the job description instead.

---

### 4.4 · Data Across Industries - 4.5 min

**Cold open:** *A clinic, a money transfer service, and a school each hire someone with the same data skills. Within a month, all three are asking completely different questions.*

**Shots:** cold open → title → objective → *The methods travel; the questions do not* → *The three from the cold open* → *More of the same* → **table** Where / What they ask data → *Key takeaway* → end card

**Note:** Three-panel visual for the cold open - clinic, money transfer, school - held through the lesson and returned to at the takeaway. The lesson used to name six industries in a table and then narrate the same six again; it now delivers the three the cold open promises, in depth, and lists the rest once.

Each of the three closes on what a *wrong* answer costs: an unfinished treatment, a blocked customer, a missed child. That is the beat, not the industry list.

---

# Chapter 5 - Data Ethics and Privacy

*4 lessons · 29 min*

> **One continuous case.** All four lessons follow a mobile money company building automatic small-business loans. Shoot them in one session so the delivery stays consistent, and shoot them in order, since lesson 5.4 resolves a decision set up in 5.1. The chapter opener must establish the case before 5.1 starts.

### 5.1 · Responsible and Ethical Use of Data - 8 min

**Cold open:** *The most damaging data projects are rarely built by bad people. They are built by good teams who never stopped to ask whether they should.*

**Shots:** cold open → title → objective → *Case study: the loan scoring project* → *When the numbers are true but the chart lies* → **table** Month / Repayment rate → **chart A (truncated axis)** → **chart B (full axis)** → *Principles of responsible data use* → end card

**The chart pair is the most important asset in the course.** Currently drawn in ASCII hash marks because Markdown has no graphics. Video does.

Sequence it precisely:
1. Show the four repayment numbers as a table. Hold. Let the viewer own them.
2. Reveal Chart A - truncated 90–92% axis. Let it look like a success story. Say nothing about the axis.
3. Ask: is this chart lying?
4. **Animate the axis expanding from 90–92% to 0–100%.** Same bars, same data, morphing into four near-identical columns.
5. Then the line: *"Chart A contains no false numbers."*

Do not cut between two static charts. The morph is what makes it undeniable, and it is the moment students will quote back.

---

### 5.2 · Privacy, Consent, and Security - 5.5 min

**Cold open:** *Everyone clicked "agree". Almost nobody read it.*

**Shots:** cold open → title → objective → *Case study: consent in the loan project* → *The life of a piece of personal data* → **diagram build (5)** → *Security in the loan project* → end card

**Diagram build:** `Ask consent` → `Collect only what is needed` → `Store securely` → `Use for the stated purpose` → `Delete when no longer needed`. Five beats. The last node is the one organizations skip. Hold on it.

**Note:** the "would the customer be surprised?" test is the takeaway. Put it on screen as a single-line card.

---

### 5.3 · Bias and Fairness - 7.5 min

**Cold open:** *A model can sort people by gender using data that contains no gender field anywhere in it.*

**Shots:** cold open → title → objective → *Case study: bias in the loan project* → **table** Source of bias / Example → *How bias repeats itself* → **diagram build (4, looping)** → *What fairness means* → end card

**Diagram build:** `Past decisions` → `Training data` → `Model` → `New decisions` → **and back to `Past decisions`**. This is the only cyclic diagram in the course. Build the four nodes, pause, then draw the closing edge, and let it loop two or three times on screen while you explain that the system is now teaching itself its own history.

**Note:** the proxy-variable passage is the hardest idea in the course. Slow down. The cold open promises it; do not resolve it in under a minute.

---

### 5.4 · Data Governance and Regulations - 8 min

**Cold open:** *Every failure in this chapter had someone who could have raised a concern.*

**Shots:** cold open → title → objective → *Case study: governance in the loan project* → **table** Problem from earlier lessons / The rule that catches it → *Regulations* → *How the case ends* → end card

**The 7-row table is the chapter's payoff.** Six of the seven rows are callbacks to something the viewer watched go wrong. Reveal those one at a time and name which lesson each came from. The seventh, retention, never happened in the case, and the lesson says so on purpose: the point is that rules are written from other people's failures, not only your own as it lands. This is the only place in the course where a table is a narrative rather than a reference. Shoot it that way, ~15s per row.

**Note:** end on the case resolution, not the regulations. *"It is usually slower. It is not usually worse."* is the last line of chapter 5. Hold, then end card.

---

# Chapter 6 - Conclusion

*2 lessons · 10.5 min*

### 6.1 · Course Recap: From Data to Decision - 4 min

**Cold open:** *You have completed the core lessons of this course, and you now have the vocabulary this field runs on.*

**Shots:** cold open → title → objective → *What you learned* → *The full journey* → **diagram build (8)** → end card

**Diagram build:** `Problem` → `Question` → `Data` → `Cleaning` → `Analysis` → `Visualization` → `Insight` → `Decision`. Longest build in the course, eight beats. Speak each stage as it lands and name the chapter it came from. This is the recap doing its job.

**Note:** this lesson deliberately does **not** say what comes next, because the course promises no curriculum. End on the closing line about judgment outlasting tools, over the diagram. Do not ad-lib a "next course" tease here or in the end card.

---

### 6.2 · Putting It All Together: End-to-End Scenario - 6.5 min

**Cold open:** *One business problem. Six steps. Every idea in this course, used once.*

**Shots:** cold open → title → objective → *Scenario* → step 1 → step 2 → step 3 → step 4 → step 5 → step 6 → *Final decision* → *What this scenario shows* → end card

**Shot-list note:** this is the one lesson whose shots are numbered rather than named. Its `###` headings *are* `Step 1` … `Step 6`, so the shorthand above is the heading list, not a summary of it.

**Note:** Six explicitly numbered steps, the one lesson where on-screen step numbering is literal rather than decorative. Reuse the chapter 3 locator diagram as a persistent corner element, advancing one step per section. Highest bullet density in the course (38), so resist reading them as a list; each step is a beat in one story.

**This is the capstone.** Shoot it last, after the whole course exists, so the callbacks are accurate.

---

# Suggested shooting order

Not lesson order. Group by setup and by what has to exist first.

| Session | Shoot | Why |
|---|---|---|
| 1 | **2.1** and **3.4** | Calibration. 2.1 is among the shortest and is diagram-led; 3.4 is among the longest and is table-and-prose. Compare actual runtime against the 4.5 and 7.5 estimates; the ratio you get rescales every number in this document. Chapter 5 holds the three longest lessons but cannot supply a calibration subject, because it must be shot in one session and in order. |
| 2 | Chapter 1 (5 lessons) | Establishes tone. Most-watched chapter - students who quit, quit here. |
| 3 | Chapter 2, split across two sittings | Four structurally identical lessons; fatigue will show if shot in one. |
| 4 | Chapter 3 (6 lessons) | Shoot the 3.1 diagram build first - lessons 3.2–3.6 reuse it as a locator. |
| 5 | Chapter 4 remainder | **4.2** needs its own setup for the code slides, and is the only video that does. Shoot it with 4.1, whose handoff sets it up. |
| 6 | **Chapter 5, one session, in order** | Continuous case; consistency of delivery matters more here than anywhere else. |
| 7 | Chapter openers, welcome, **6.2** | Written last because they summarize what now exists. |

---

## Runtime summary

| Component | Count | Runtime |
|---|---|---|
| Lesson videos | 27 | ~150.5 min |
| Chapter openers | 6 | ~8 min |
| Welcome | 1 | ~3 min |
| **Total** | **34 videos** | **≈ 2h 41m** |

Estimates come from measured prose words at 130–150 wpm with a 1.4–1.9× spoken expansion, plus dwell time per table row, diagram, and code block. Every per-lesson figure already assumes rule 4, with Key Terms shown on the end card rather than read aloud, so the numbers here are what you shoot to, and they sum to the total below. Narrating them adds 15–20 minutes and costs you 27 endings.

Line count is not a proxy for runtime and should not be used as one: lesson 4.1 is 83 lines and 674 words, lesson 6.2 is 122 lines and 558 words.
