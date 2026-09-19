# Why Data Work Uses Code

**By the end:** You can explain why data work moves to code instead of staying in spreadsheets.

## Overview

Spreadsheets work well until three things happen: the data grows too large, the same report is needed every week, or someone asks you to prove how a number was produced.

### What code solves

Code solves all three. It handles large datasets, it can be re-run on demand, and it leaves a written record of every step you took.

That last one matters more than beginners expect. A spreadsheet shows you a number. Code shows you how the number was made, which is the difference between a result someone trusts and one they merely accept.

This gets less optional the further you go. An analyst can do useful work with no code at all. Training a model, or building the pipeline that feeds one, cannot be done any other way.

You are not expected to understand the examples coming up. The goal is to see what the work looks like.

### Asking a database a question

**SQL** asks a database a question:

```sql
SELECT city, SUM(sales) AS total_sales
FROM orders
WHERE order_date >= '2024-01-01'
GROUP BY city;
```

That is one question, "how much did each city sell this year?", answered in four lines.

### Working through data step by step

**Python** loads data and works with it step by step:

```python
import pandas as pd

orders = pd.read_csv("orders.csv")
average_by_city = orders.groupby("city")["sales"].mean()
print(average_by_city)
```

This code loads the `orders.csv` file, groups the orders by city, calculates the average sales for each city, and prints the result.

Both examples do something you could also do by hand in a spreadsheet. The difference is that they run in seconds on a million rows, and they run the same way every time.
