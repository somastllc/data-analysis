# Chapter 5 Exercises: Data Ethics and Privacy

**Chapter:** 5 — Data Ethics and Privacy  
**Type:** Practice — no software required

## How to use these

Answer from memory first, then open the answer.

These are the hardest exercises in the course, because most of them have no clean answer. Being able to name the problem and argue a position is the skill.

### Exercise 1 — Would the customer be surprised?

For each use of data, decide whether a reasonable customer would be surprised — and therefore whether consent is meaningful or merely legal.

1. A delivery app uses your past orders to show your reorder history in the app.
2. A delivery app sells your order history to a health insurer.
3. A hospital uses your test results to treat you.
4. A hospital uses anonymized test results from thousands of patients to study a disease.
5. A shop's loyalty program uses your purchase timing to guess you are pregnant, and mails you baby product offers.

<details>
<summary>Show answer</summary>

1. **Not surprising.** This is the service the customer signed up for.
2. **Surprising, and harmful.** Data collected for delivery being used to price someone's insurance is a clear purpose-limitation breach.
3. **Not surprising.**
4. **Probably not surprising**, and generally accepted — but it depends entirely on the anonymization being real. "Anonymized" data that can be re-identified by combining it with other datasets is not anonymized.
5. **Surprising.** The inference itself may be accurate and the data collection legal, yet the customer never agreed to have a pregnancy inferred and disclosed by post, possibly to a household that does not know.

Case 5 is the important one. Nothing was stolen and nothing was inaccurate. The harm came from an **inference** drawn from ordinary data. You are responsible not only for the data you hold, but for what you deduce from it.

</details>

### Exercise 2 — Find the proxy

A company builds a model to shortlist job applicants. To avoid discrimination, the team removes name, gender, age, and photograph from the data.

The following fields remain. Which of them can still act as proxies for the removed attributes, and for what?

1. Postal code of home address
2. Year of graduation
3. Name of secondary school attended
4. Number of years of continuous employment with no gaps
5. Typing speed test score

<details>
<summary>Show answer</summary>

1. **Postal code** → often a strong proxy for ethnicity and income, because neighborhoods are rarely evenly mixed.
2. **Year of graduation** → a direct proxy for age. Removing the age field accomplished nothing.
3. **School name** → a proxy for class, income, religion, and sometimes gender if the school is single-sex.
4. **Continuous employment with no gaps** → a proxy for gender, because career breaks for childcare fall mostly on women. Also a proxy for health and disability.
5. **Typing speed** → the only one with a plausible direct link to the job, and even it can proxy for disability.

Four of the five removed attributes are still fully recoverable from the "safe" fields. This is the central lesson of proxies: **removing a sensitive column does not remove the sensitive information.** It only removes your ability to check whether you are using it.

The fix is not to delete more columns. It is to measure outcomes across groups after the model runs, which requires keeping the sensitive attributes somewhere you can test against.

</details>

### Exercise 3 — Is this chart honest?

For each, say whether the presentation is misleading, and why.

1. A revenue line chart whose vertical axis runs from `$0` to `$500,000`, showing steady growth.
2. A chart titled "Complaints down 40%" whose axis starts at 950 and ends at 1,000, with complaints falling from 1,000 to 960.
3. A bar chart comparing this year's five best-performing branches against last year's company average.
4. A headline reading "Signups up 200% after redesign", where signups went from 3 to 9.

<details>
<summary>Show answer</summary>

1. **Honest.** Full axis, plain reading.
2. **Misleading twice over.** The axis exaggerates a small change, and the title is simply wrong: 1,000 to 960 is a 4% fall, not 40%. Always check whether the headline number matches the data underneath it.
3. **Misleading.** It compares a hand-picked top five against an average — two different kinds of number. The comparison is designed so the current year cannot lose.
4. **Technically true and practically meaningless.** A 200% rise on a base of 3 is noise. Percentages hide the count, which is exactly why they get used when the count is embarrassing.

Only case 1 is clean. Cases 2, 3, and 4 each contain no false numbers whatsoever.

</details>

### Exercise 4 — Which rule would have caught it?

Each situation below is a real failure. Name a governance rule that would have prevented it.

1. An analyst who left the company six months ago can still open the customer database.
2. A marketing team pulls health data from a wellness app to target ads for weight-loss products.
3. A model goes live and is found a year later to reject one ethnic group at twice the rate of others.
4. A stolen laptop contains a spreadsheet of 40,000 customers' full transaction histories.

<details>
<summary>Show answer</summary>

1. **Access control tied to employment status** — access should be revoked automatically when someone leaves, not manually when someone remembers.
2. **Purpose limitation with a documented review** before existing data is used for any new purpose.
3. **A pre-launch fairness review** comparing outcomes across groups, repeated on a schedule after launch. A year is far too long for this to go unnoticed.
4. **Data minimization plus retention limits** — the deeper question is why a full transaction history for 40,000 people was on a laptop at all. Encryption helps, but the strongest protection is not holding the data in that place to begin with.

Notice that none of these four failures were caused by a bad person. Each was caused by a missing rule. That is what governance is for.

</details>

### Exercise 5 — Trace the loop

A school introduces a model that flags students "at risk of dropping out." Flagged students are moved into a smaller class with a less demanding syllabus, so they are not overwhelmed.

Two years later the school reports that the model is highly accurate: flagged students really do go on to leave school early.

What has gone wrong, and how would you test it?

<details>
<summary>Show answer</summary>

**What went wrong:** the model's own output changed the outcome it was predicting. Flagged students were given a less demanding syllabus, which lowered their qualifications, which raised their chance of leaving — and that result then became training data confirming the flag.

The model is not predicting dropout. It is **causing** part of it, then being praised for accuracy.

**How to test it:** compare flagged students against similar students who were *not* flagged — for example because the model was rolled out to some year groups before others, or because a flagged student's family declined the smaller class. If the flag is genuinely predictive, flagged-but-not-moved students should also leave early. If they mostly do not, the intervention is the cause rather than the prediction.

**The general warning sign:** any system whose predictions trigger an action that makes the prediction more likely to come true. High accuracy is not evidence that such a system is working. It may be evidence that it is working *too well* — at producing its own answer.

</details>
