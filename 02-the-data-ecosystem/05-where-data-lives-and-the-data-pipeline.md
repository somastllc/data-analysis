# Where Data Lives and the Data Pipeline

**Chapter:** 2 — The Data Ecosystem  
**Lesson:** 5 of 6  
**By the end:** You can name the stages a dataset passes through, and where it is stored at each one.

## Overview

The sales figure on a manager's dashboard this morning began as a tap on a card reader three weeks ago. Between those two moments it was moved, stored, cleaned, reshaped, and summarized — usually by systems nobody in that meeting has ever seen. Data does not exist in one single place. It moves through systems and stages before it becomes useful.

### Where data lives

Organizations store data in different systems depending on purpose and scale.

| System | Purpose |
|---|---|
| **Database** | Stores structured business data for daily operations |
| **Data warehouse** | Stores large amounts of historical data for analysis |
| **Data lake** | Stores raw data in many formats, often at large scale |
| **Spreadsheets / files** | Useful for small datasets and quick work |

As a beginner, you will mostly encounter spreadsheets, CSV files, and database tables. Larger organizations also use warehouses and lakes.

### What is a data pipeline?

A **data pipeline** is the path data follows from its source to its final use.

```mermaid
flowchart LR
    collectNode["Collect"] --> storeNode["Store"]
    storeNode --> cleanNode["Clean"]
    cleanNode --> transformNode["Transform"]
    transformNode --> analyzeNode["Analyze"]
    analyzeNode --> shareNode["Share"]
```

Each stage has a purpose:

- **Collect** — gather data from apps, forms, sensors, or systems
- **Store** — save it in a database, warehouse, or file
- **Clean** — fix missing values, duplicates, and errors
- **Transform** — reshape data into a useful format
- **Analyze** — explore patterns and answer questions
- **Share** — present results in reports or dashboards

### Example

A mobile app tracks user activity.

1. The app **collects** click and purchase data
2. The data is **stored** in a cloud database
3. A pipeline **cleans** incomplete records
4. The data is **transformed** into daily usage summaries
5. Analysts **analyze** trends in user behavior
6. Managers view the results in a **dashboard**

This flow connects data engineering, analysis, and business intelligence.

## Key Terms

| Term | Definition |
|---|---|
| **Database** | A structured system for storing and retrieving data |
| **Data pipeline** | A workflow that moves data from its source to its final use |
| **Transform** | Reshaping or preparing data for analysis |
