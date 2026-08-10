# Chapter 2 Exercises: The Data Ecosystem

**Chapter:** 2 — The Data Ecosystem  
**Type:** Practice — no software required

## How to use these

Answer from memory first, then open the answer.

### Exercise 1 — Which type of analytics?

Label each question as **descriptive**, **diagnostic**, **predictive**, or **prescriptive**.

1. How many new customers signed up last month?
2. Which region should we open the next branch in?
3. Why did returns increase in March?
4. How many orders should we expect during the holiday week?
5. What was our average delivery time last quarter?

<details>
<summary>Show answer</summary>

1. **Descriptive** — reports the past.
2. **Prescriptive** — recommends an action.
3. **Diagnostic** — explains the past.
4. **Predictive** — forecasts the future.
5. **Descriptive**.

A useful test: descriptive and diagnostic look backwards, predictive and prescriptive look forwards. Within each pair, the second one is harder — explaining is harder than reporting, and recommending is harder than forecasting.

</details>

### Exercise 2 — Who does this work?

Match each task to the role most likely to do it: **data engineer**, **data analyst**, **BI professional**, **data scientist**, or **business stakeholder**.

1. Builds an automated job that loads payment records into the warehouse every night
2. Investigates why cancellations spiked in one city
3. Builds a model that predicts which customers will cancel next month
4. Decides to fund a retention discount
5. Creates a dashboard managers check every Monday morning

<details>
<summary>Show answer</summary>

1. **Data engineer**
2. **Data analyst**
3. **Data scientist**
4. **Business stakeholder**
5. **BI professional**

Notice that only one of these five people builds a model, and the person who makes the actual decision writes no code at all. "Working in data" describes five quite different jobs.

</details>

### Exercise 3 — Where did the pipeline break?

A dashboard shows that Tuesday had zero sales. The shop was open and busy on Tuesday.

For each finding below, say which pipeline stage failed: **collect**, **store**, **clean**, **transform**, **analyze**, or **share**.

1. The payment terminal lost its network connection all Tuesday and never sent its records.
2. Tuesday's records arrived, but a cleaning step dropped every row with a blank customer name — and Tuesday's staff skipped that field.
3. All the data is correct, but the dashboard filter is still set to last month.

<details>
<summary>Show answer</summary>

1. **Collect** — the data never entered the pipeline.
2. **Clean** — the data arrived and was then thrown away by a rule that was too aggressive.
3. **Share** — the numbers are right; the presentation is wrong.

All three produce the identical symptom on screen: a zero. This is why knowing the pipeline matters. "The dashboard is wrong" is not a diagnosis, and the fix is different in each case.

</details>

### Exercise 4 — Does this need machine learning?

For each, decide whether machine learning is needed, or whether simpler analysis would do.

1. Find the ten best-selling products last quarter.
2. Flag which of 50,000 daily transactions look fraudulent.
3. Calculate whether the marketing campaign increased signups.
4. Recommend a different song to each of two million listeners.

<details>
<summary>Show answer</summary>

1. **No.** Sorting and summing. A spreadsheet handles this.
2. **Likely yes.** Fraud patterns shift and are too varied to capture in fixed rules, and the volume is far beyond manual review.
3. **No.** This is a comparison, and possibly a statistical test. The tools for it come from statistics.
4. **Likely yes.** Personalizing at that scale cannot be done by hand.

The pattern: machine learning earns its cost when the rules are unknown or constantly changing, *and* the volume is beyond human review. If either half is missing, simpler analysis usually wins. Reaching for a model when a `GROUP BY` would do is one of the most common beginner mistakes.

</details>
