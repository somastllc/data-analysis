# Defining the Problem and Asking Questions

**Chapter:** 3 — The Data Analysis Process  
**Lesson:** 1 of 6  
**By the end:** You can turn a vague request into a specific analytical question.

## Overview

"Can you look into the sales data?" is one of the most common requests an analyst receives, and it is not yet a question. Answering it exactly as written is how a week disappears. Good analysis starts before any data is collected. You must understand the problem and ask clear questions. Without this step, even advanced tools can produce useless results.

```mermaid
flowchart LR
    problemNode["Define problem"] --> questionNode["Ask questions"]
    questionNode --> collectNode["Collect data"]
    collectNode --> cleanNode["Clean data"]
    cleanNode --> analyzeNode["Analyze and visualize"]
    analyzeNode --> shareNode["Communicate insights"]
    shareNode --> decideNode["Make decisions"]
```

### Start with the business problem

A common mistake is jumping straight into data without knowing what you are trying to solve.

Always begin by asking:

- What problem are we trying to solve?
- Who cares about the answer?
- What decision will this analysis support?

Example:

- Weak question: "Let's analyze the sales data."
- Strong question: "Why did sales drop in the North region last quarter?"

For a local shop, the same idea applies:

- Weak question: "Let's look at the sales spreadsheet."
- Strong question: "Why did rice sales drop in the last two weeks compared to the month before?"

The stronger questions give analysis a clear direction.

### Know your stakeholders

A **stakeholder** is anyone who needs the results of your analysis.

Examples:

- A manager deciding on marketing spend
- A product team improving an app feature
- A finance team reviewing budget performance

Understanding stakeholders helps you:

- Ask the right questions
- Choose relevant metrics
- Present results in a useful way

### How to ask good analytical questions

Good questions are:

- **Specific** — focused on one issue
- **Measurable** — answerable with data
- **Relevant** — connected to a real decision
- **Clear** — easy for others to understand

Examples:

- Which product category had the highest return rate last month?
- Are new customers more likely to cancel within 30 days?
- Which marketing channel brings the most qualified leads?

### Example

An online course platform notices fewer enrollments.

Stakeholders: marketing team and product manager  
Problem: enrollment decline  
Questions:

- When did enrollments start dropping?
- Did the drop affect all courses or only some?
- Did traffic decrease, or did fewer visitors convert?

These questions guide the rest of the analysis process.

## Key Terms

| Term | Definition |
|---|---|
| **Business problem** | The issue or decision the analysis is meant to support |
| **Stakeholder** | A person or group affected by, or interested in, the results of the analysis |
| **Analytical question** | A clear question that data can help answer |
