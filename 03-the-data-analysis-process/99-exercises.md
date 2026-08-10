# Chapter 3 Exercises: The Data Analysis Process

**Chapter:** 3 — The Data Analysis Process  
**Type:** Practice — no software required

## How to use these

Answer from memory first, then open the answer. Several of these have no single correct answer — the reasoning matters more than the wording.

### Exercise 1 — Rewrite the request

A manager sends each of these messages. Rewrite each as a **specific, measurable, relevant, clear** analytical question.

1. "Can you look into the sales data?"
2. "I think our customers are unhappy lately."
3. "Marketing wants to know if the campaign worked."

<details>
<summary>Show answer</summary>

Reasonable rewrites:

1. "Which product categories had lower sales this quarter than last quarter, and in which regions?"
2. "Has the average customer satisfaction rating changed over the last six months, and which complaint categories grew fastest?"
3. "Did signups from the campaign channel increase during the campaign period compared with the four weeks before it?"

Each rewrite adds three things the original was missing: a **time range**, a **comparison**, and a **measure**. If your version has all three, it is probably good enough.

There is a fourth question worth asking before any of these: *what will you do differently depending on the answer?* If nobody can answer that, the analysis is not yet worth doing.

</details>

### Exercise 2 — What data would you collect?

Question: **"Are new users cancelling because our support is too slow?"**

Which of these would you collect, and which is a trap?

1. Support ticket response times
2. Cancellation dates
3. Satisfaction survey responses from current subscribers
4. App activity logs for each user
5. Total monthly revenue

<details>
<summary>Show answer</summary>

**Collect:** 1, 2, and 4. You need response times, the cancellations you are explaining, and activity to see whether slow support or simple disengagement came first.

**The trap is 3.** A survey of *current* subscribers systematically excludes everyone who already cancelled — exactly the group the question is about. This is sampling bias, and it is easy to miss because the data looks relevant and is easy to obtain.

**5 is not wrong, just not useful here.** Revenue is an outcome, too far downstream to isolate the cause.

To do 3 properly you would survey cancelled users, which is harder — they have less reason to reply. Convenient data and correct data are often different data.

</details>

### Exercise 3 — Cleaning decisions

You are analyzing average salary by department. You find these four issues. For each, decide what to do and why.

1. Two identical rows for employee `E-204`
2. Fifteen employees have a blank department
3. One salary is recorded as `1` and one as `999999999`
4. Salaries appear as `50000`, `50,000`, and `50000 USD`

<details>
<summary>Show answer</summary>

1. **Remove one.** A duplicated employee is counted twice in both the average and the headcount.
2. **Do not delete these rows silently.** You are grouping *by* department, so they cannot be included — but check first whether the blanks cluster in one department or one hire date, which would point to a broken process rather than random gaps. Then report them as a limitation.
3. **Investigate, do not just delete.** `1` might be a placeholder, an hourly rate in the wrong column, or an intern. `999999999` is almost certainly a data entry error. Averages are extremely sensitive to a single huge value — one bad row here can move the whole department's average.
4. **Standardize to a number.** These are the same value in three formats; left alone, software may treat them as text and silently exclude them from the average.

The pattern across all four: deleting is easy, and understanding *why* the problem exists is what prevents it recurring next month. You will do this work properly in the Data Cleaning and Wrangling course.

</details>

### Exercise 4 — Choose the chart

Match each question to the chart that answers it best.

1. How did monthly revenue change over the past two years?
2. Which of our six branches sold the most?
3. Do customers who visit more often also spend more per visit?
4. What share of total sales came from each product category?

<details>
<summary>Show answer</summary>

1. **Line chart** — change over time.
2. **Bar chart** — comparing categories.
3. **Scatter plot** — relationship between two numeric variables.
4. **Pie chart** — parts of a whole. Only usable because there are few categories; with twenty products a bar chart would be clearer.

A caution on question 3. If the scatter plot shows that frequent visitors do spend more, you have found a **correlation** — the two move together. You have *not* shown that visiting more often causes higher spending. Wealthier customers might simply do both. Correlation is not causation, and confusing them is the most common analytical error there is. You will learn to measure correlation properly in the Statistics course.

</details>

### Exercise 5 — Rewrite for the audience

An analyst writes this in a report to the company's executives:

> "The churn model's coefficient on `support_wait_hours` is positive and significant at p < 0.05, indicating a directional relationship with the cancellation outcome variable."

Rewrite it for an executive who has ten seconds. Then say what you would add if the audience were other analysts.

<details>
<summary>Show answer</summary>

For the executive:

> "Customers who wait longer for support are more likely to cancel. Cutting weekend wait times is the fastest thing we can do about it."

Why this works: it leads with the finding, uses no jargon, and states the action. The executive's next question is "what should we do?" — so answer it before they ask.

For an analyst audience, add back what you removed: sample size and time period, how wait time was measured, the effect size (how *much* more likely, not just "more likely"), what else was controlled for, and the honest caveat that this is an observed relationship rather than a proven cause.

Neither version is dishonest. They are the same finding at two different levels of detail. Choosing the level is part of the job.

</details>
