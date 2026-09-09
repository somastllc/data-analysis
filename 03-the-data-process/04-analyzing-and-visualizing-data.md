# Analyzing and Visualizing Data

**By the end:** You can choose a chart that matches your question, and say what analysis can and cannot prove.

## Overview

The same table of numbers can hide a trend completely or make it obvious in one second. The numbers do not change. The picture does. After cleaning, you explore the data to find patterns, comparisons, and trends. **Analysis** uncovers what the data shows; **visualization** helps you see and communicate it clearly.

### What happens during analysis?

Analysis means examining data to answer your questions.

Common activities include:

- Calculating totals and averages
- Comparing groups
- Finding a **trend**, or general direction of change over time
- Identifying top or bottom performers
- Looking for relationships between variables

Example questions:

- Which city had the highest sales?
- Did orders rise after the price change?
- Do customers who buy in bulk return more often than those who do not?

### When the output is a model instead of a chart

An analyst asks what the data shows. A data scientist asks what the data predicts, and builds a model to answer it. Both start from the same cleaned data, both answer a question set in step one, and both fail the same way, by producing something correct that nobody asked for.

The rest of this lesson uses charts, because charts are the version you can read without software.

### Why visualize data?

**Data visualization** turns numbers into charts and graphs that are easier to understand.

Visuals help you:

- Spot patterns quickly
- Compare categories
- Show change over time
- Explain results to non-technical audiences

### Common chart types

| Question type | Chart type |
|---|---|
| Compare categories | Bar chart |
| Show change over time | Line chart |
| Show parts of a whole | Pie chart |
| Compare two numeric variables | Scatter plot |

Choose the chart that best matches your question. For example, use a line chart for monthly trends and a bar chart to compare product categories.

### What analysis cannot prove

Analysis finds patterns. On its own, it does not explain them.

Suppose the shops that stay open latest also sell the most rice. Three explanations fit that pattern equally well:

- The longer hours cause the extra sales
- Selling well is what lets a shop afford the staff to stay open longer
- Shops on the busiest streets do both, and the street is the real cause

The data cannot tell you which. All three produce exactly the same table and exactly the same chart.

Two things moving together like this is called **correlation**. It is a real finding and worth reporting, but it is not the same as one thing causing the other, and acting on the wrong one is expensive. A shop that extends its hours because of this chart, when the real cause was its location, has added a wage bill and gained nothing.

So when you find a pattern, call it a pattern. Whether it is a cause is a separate question, and it is usually answered by deliberately changing one thing and measuring what happens.

### Example

A wholesaler looks at the orders coming in from its shops.

Analysis findings:

- Orders rose 25% in March
- Rice and oil account for most of the increase
- The Lakeview shops order later in the week than the others

Visualizations:

- Line chart of orders by month
- Bar chart of orders by product
- Table of average order day by city

The chart shows Lakeview ordering late. It does not show why, and the lesson above is the reason you should not guess.
