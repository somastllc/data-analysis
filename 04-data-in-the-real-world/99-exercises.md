# Chapter 4 Exercises: Data in the Real World

**Chapter:** 4 — Data in the Real World  
**Type:** Practice — no software required

## How to use these

Answer from memory first, then open the answer.

### Exercise 1 — Pick the tool

Choose the most suitable tool for each task: **Excel / Google Sheets**, **SQL**, **Python**, **Power BI**, or **Git & GitHub**.

1. Pull last year's orders for one region out of a company database with 40 million rows
2. Summarize a 300-row budget and chart it for a meeting tomorrow
3. Give twelve regional managers a report they can filter themselves, refreshed daily
4. Run the same cleaning steps on a new file every morning without repeating the work by hand
5. Keep a record of what changed in an analysis, and let a colleague review it before it ships

<details>
<summary>Show answer</summary>

1. **SQL** — the data is in a database, and 40 million rows will not open in a spreadsheet.
2. **Excel / Google Sheets** — small, one-off, needed fast. Reaching for Python here would be slower, not more professional.
3. **Power BI** — self-service filtering and scheduled refresh are exactly what BI tools are for.
4. **Python** — repeatable automation.
5. **Git & GitHub** — version history and review.

The judgment being tested is task 2. Choosing the heavier tool is a real and common mistake. The right tool is the smallest one that does the job.

</details>

### Exercise 2 — Which role fits?

Read each description and name the role: **data analyst**, **data engineer**, **data scientist**, **analytics engineer**, **business analyst**, or **machine learning engineer**.

1. "I like finding out why a number moved and explaining it to the people who can act on it."
2. "I like building the plumbing that makes sure everyone's numbers arrive on time and match."
3. "I like experiments, statistics, and testing whether a prediction actually holds up."
4. "I like sitting between the business and the data team, working out what is actually being asked."
5. "I like taking a working model and making it run reliably in production."

<details>
<summary>Show answer</summary>

1. **Data analyst**
2. **Data engineer**
3. **Data scientist**
4. **Business analyst**
5. **Machine learning engineer**

This learning path trains you for **1**. That is deliberate: it is the most common entry point into data work, and the other five are easier to move into from there than from outside the field.

</details>

### Exercise 3 — Same skill, different question

A hospital, an online store, and a school all hire someone with identical skills: they can ask a clear question, clean a dataset, analyze it, and explain the result.

For each organization, write one realistic question that person would be asked in their first month.

<details>
<summary>Show answer</summary>

Reasonable answers:

- **Hospital:** "Which patients are most likely to be readmitted within 30 days, and what do they have in common?"
- **Online store:** "At which step of checkout do most customers abandon their cart, and does it differ on mobile?"
- **School:** "Which students had attendance drop this term, and did it start before or after their grades fell?"

The method is the same in all three: define, collect, clean, analyze, communicate. What changes is the vocabulary and what counts as a good outcome — a readmission is not a cart abandonment.

This is what makes data skills portable. It is also why domain knowledge matters: you cannot ask a good hospital question without knowing what a readmission costs a patient.

</details>
