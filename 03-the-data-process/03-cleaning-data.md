# Cleaning Data

**Chapter:** 3 - The Data Process  
**Lesson:** 3 of 6  
**By the end:** You can decide what to do about duplicates, blanks, and impossible values, not just spot them.

## Overview

Ask working analysts what takes up most of their time and the answer is rarely "analysis". It is getting the data into a state where analysis is possible at all. Real-world data is rarely perfect. Before analyzing it, you usually need to **clean** it. Data cleaning improves quality by fixing errors, handling missing values, and making formats consistent.

### Why clean data?

If you analyze messy data, your results may be misleading.

Chapter 1 covered *what* poor quality looks like: missing values, duplicates, wrong entries, inconsistent formats. Cleaning is what you do about it.

That difference matters more than it sounds. Spotting a problem takes a few minutes. Deciding what to do about it is where the judgment lives, and two analysts looking at the same flawed column can reasonably make different choices.

### Common cleaning tasks

| Task | Example |
|---|---|
| **Removing duplicates** | Same customer listed twice |
| **Handling missing values** | Blank age or email fields |
| **Fixing formats** | Dates written in different styles |
| **Standardizing categories** | `HG`, `Hargeisa`, and `hargeisa` |
| **Correcting invalid values** | Age = `-3` or `999` |

### How much cleaning is enough?

Not every issue needs the same treatment.

Examples:

- A few missing survey answers may be acceptable
- Duplicate financial records must usually be removed
- A typo in a category name should be corrected through **standardization**, so every spelling of a city or product becomes one

The right treatment depends on what the data will be asked to answer, which is why this step comes after the question and not before it.

### Example

A staff list from a wholesaler contains:

- Two rows for the same employee ID
- Missing branch values
- Salaries entered as `$500`, `500`, and `500 USD`

Before comparing pay across branches, you would:

1. Remove duplicate rows
2. Decide how to handle the missing branches
3. Standardize salary format

Skipping these steps could produce incorrect averages and rankings.

Cleaning is a large subject in its own right. What matters now is recognizing that the step exists, and that skipping it invalidates everything after it.

## Key Terms

| Term | Definition |
|---|---|
| **Data cleaning** | The process of fixing errors and improving data quality |
| **Missing value** | A blank or unavailable data entry |
| **Standardization** | Making data follow a consistent format |
