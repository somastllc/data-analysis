# Chapter 1 Exercises: What Is Data?

**Chapter:** 1 — What Is Data?  
**Type:** Practice — no software required

## How to use these

Answer from memory first, then open the answer. Getting one wrong and reading why is worth more than getting it right by looking.

### Exercise 1 — Data, information, or insight?

Label each statement as **data**, **information**, or **insight**.

1. `47`
2. Rice sales fell by 12% over the last two weeks.
3. 47 customers visited the shop on Tuesday.
4. Customers stop coming when the rainy season starts, so stock less fresh produce in April.

<details>
<summary>Show answer</summary>

1. **Data** — a raw fact with no context. On its own, `47` means nothing.
2. **Information** — organized to answer a basic question ("what happened to rice sales?").
3. **Information** — the number now has context: who, how many, when.
4. **Insight** — a conclusion that guides an action.

The line between information and insight is the word *so*. Information describes; insight tells you what to do about it.

</details>

### Exercise 2 — Structured, semi-structured, or unstructured?

Classify each.

1. A spreadsheet of student names and exam scores
2. A voice recording of a customer complaint
3. A JSON file of app events with nested fields
4. A folder of scanned receipt photos
5. A database table of mobile money transfers
6. A WhatsApp message thread with a supplier

<details>
<summary>Show answer</summary>

1. **Structured** — fixed rows and columns.
2. **Unstructured** — audio has no fixed fields.
3. **Semi-structured** — labeled fields, but no fixed table layout.
4. **Unstructured** — images. Note that the *receipt* has structure; the *photo of it* does not until someone extracts the values.
5. **Structured**.
6. **Unstructured** — free text.

Item 4 is the useful one. Data can contain structure that a computer cannot reach yet. Most of the world's data is in this state.

</details>

### Exercise 3 — Quantitative or qualitative?

For each, say which type it is, and whether calculating an average would make sense.

1. Temperature readings: `31°C`, `33°C`, `29°C`
2. Satisfaction ratings: `Poor`, `Good`, `Excellent`
3. Phone numbers
4. Number of items sold per day

<details>
<summary>Show answer</summary>

1. **Quantitative.** Average makes sense: `31°C`.
2. **Qualitative (categorical).** An average does not make sense as-is. You could count how many gave each rating, or convert to numbers — but only if you can defend the claim that the gap from Poor to Good equals the gap from Good to Excellent.
3. **Quantitative-looking, but not quantitative.** Phone numbers are digits used as labels. Averaging them produces a number that means nothing. Being made of digits does not make something measurable.
4. **Quantitative.** Average makes sense.

Item 3 is the trap, and it is common in real datasets: ID numbers, postal codes, and account numbers all look numeric to software.

</details>

### Exercise 4 — Quality audit

Find **four** quality problems in this table, and name the quality dimension each one violates.

| Customer ID | Name | City | Age | Signup date |
|---|---|---|---|---|
| 1041 | Amina Yusuf | Mogadishu | 34 | 2024-03-11 |
| 1042 | Hodan Ali | mogadishu | 29 | 11/03/2024 |
| 1043 | Omar Farah | | 205 | 2024-03-12 |
| 1042 | Hodan Ali | mogadishu | 29 | 11/03/2024 |

<details>
<summary>Show answer</summary>

Five problems are present:

| Problem | Dimension |
|---|---|
| Customer `1042` appears twice — an exact duplicate row | Accuracy — duplicates inflate counts and totals |
| `Mogadishu` and `mogadishu` treated as different cities | Consistency |
| Blank city for customer `1043` | Completeness |
| Age of `205` | Accuracy |
| Dates written as `2024-03-11` and `11/03/2024` | Consistency |

The date problem is the most dangerous, because it is the only one that looks fine. `11/03/2024` is ambiguous: 11 March or 3 November, depending on the country of whoever typed it. A duplicate row is obvious once you look. A silently misread date is not.

</details>

### Exercise 5 — Primary or secondary?

A student is researching whether small shops in her neighborhood are raising prices.

Which of these are **primary** data, and which are **secondary**?

1. She visits ten shops and records the price of rice herself.
2. She downloads the national statistics office inflation report.
3. She surveys twenty shoppers about what they paid last month.
4. She uses a price dataset a classmate collected last year for a different project.

<details>
<summary>Show answer</summary>

**Primary:** 1 and 3 — collected firsthand for this specific question.

**Secondary:** 2 and 4 — collected by someone else, for some other purpose.

Item 4 is worth pausing on. It is secondary even though a classmate collected it and even though it is about prices, because it was gathered for a different question, in a different year. Secondary data is not worse data. It is data whose fit you have to check rather than assume.

</details>
