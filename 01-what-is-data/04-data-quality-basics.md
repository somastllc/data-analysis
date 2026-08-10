# Data Quality Basics

**Chapter:** 1 — What Is Data?  
**Lesson:** 4 of 5  
**By the end:** You can inspect a table and name the quality problems in it.

## Overview

A manager forwards you a customer list and asks for the average age. Two minutes in, you have found three separate reasons the answer would be wrong. Almost every analysis you will ever run begins with a moment like this. Bad data leads to bad decisions. Even simple analysis can fail if the data is incomplete, incorrect, or inconsistent.

### Why data quality matters

Imagine making a business decision based on sales numbers that are missing, duplicated, or entered incorrectly. The decision might look logical, but it would be built on a weak foundation.

Good analysis depends on **good data**. That is why data professionals spend significant time checking and cleaning data before analyzing it.

### Common data quality problems

Some of the most common issues include:

- **Missing values** — blank cells or empty fields
- **Duplicates** — the same record appearing more than once
- **Incorrect values** — typos, wrong units, or impossible numbers
- **Inconsistent formatting** — dates written as `01/05/2024` and `2024-05-01` in the same dataset
- **Outdated data** — information that no longer reflects the current situation

These problems are normal. Real-world data is rarely perfect.

### Key quality dimensions

| Dimension | Question it answers |
|---|---|
| **Accuracy** | Is the data correct? |
| **Completeness** | Is anything missing? |
| **Consistency** | Is the data formatted the same way throughout? |
| **Timeliness** | Is the data up to date? |
| **Relevance** | Does the data actually help answer the question? |

You do not need advanced tools to start checking quality. Sometimes a simple review of a table can reveal missing values, strange entries, or duplicate rows.

### Example

A customer dataset contains:

- Age: `200`
- Email: blank
- City: `New York` and `new york`
- Two identical rows for the same customer

Each issue affects quality:

- `200` is inaccurate
- Blank email means incomplete data
- Different city formatting shows inconsistency
- Duplicate rows can inflate results

## Key Terms

| Term | Definition |
|---|---|
| **Data quality** | How fit data is for its intended use |
| **Accuracy** | Whether data values are correct |
| **Completeness** | Whether required data is present |
| **Consistency** | Whether data follows the same format and rules |
