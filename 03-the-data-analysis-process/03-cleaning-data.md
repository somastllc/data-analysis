# Cleaning Data

**Chapter:** 3 — The Data Analysis Process  
**Lesson:** 3 of 6  
**By the end:** You can decide what to do about duplicates, blanks, and impossible values — not just spot them.

## Overview

Ask working analysts what takes up most of their time and the answer is rarely "analysis". It is getting the data into a state where analysis is possible at all. Real-world data is rarely perfect. Before analyzing it, you usually need to **clean** it. Data cleaning improves quality by fixing errors, handling missing values, and making formats consistent.

### Why clean data?

If you analyze messy data, your results may be misleading.

Chapter 1 covered *what* poor quality looks like — missing values, duplicates, wrong entries, inconsistent formats. Cleaning is what you do about it.

That difference matters more than it sounds. Spotting a problem takes a few minutes. Deciding what to do about it is where the judgment lives, and two analysts looking at the same flawed column can reasonably make different choices.

### Common cleaning tasks

| Task | Example |
|---|---|
| **Removing duplicates** | Same customer listed twice |
| **Handling missing values** | Blank age or email fields |
| **Fixing formats** | Dates written in different styles |
| **Standardizing categories** | `NY`, `New York`, and `new york` |
| **Correcting invalid values** | Age = `-3` or `999` |

Cleaning can be simple or complex depending on the dataset.

### How much cleaning is enough?

Not every issue needs the same treatment.

Examples:

- A few missing survey answers may be acceptable
- Duplicate financial records must usually be removed
- A typo in a category name should be standardized

The right approach depends on the dataset and the question.

### Example

An employee dataset contains:

- Two rows for the same employee ID
- Missing department values
- Salaries entered as `$50000`, `50,000`, and `50000 USD`

Before analyzing salary by department, you would:

1. Remove duplicate rows
2. Decide how to handle missing departments
3. Standardize salary format

Skipping these steps could produce incorrect averages and rankings.

Cleaning is a large subject in its own right. What matters now is recognizing that the step exists, and that skipping it invalidates everything after it.

## Key Terms

| Term | Definition |
|---|---|
| **Data cleaning** | The process of fixing errors and improving data quality |
| **Missing value** | A blank or unavailable data entry |
| **Standardization** | Making data follow a consistent format |
