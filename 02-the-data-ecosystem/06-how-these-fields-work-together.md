# How These Fields Work Together

**Chapter:** 2 — The Data Ecosystem  
**Lesson:** 6 of 6  
**By the end:** You can describe how the data roles depend on each other within a single project.

## Overview

One customer cancels a subscription. Five different people end up touching that single event, and not one of them could have handled it alone. Data analysis, business intelligence, data science, machine learning, and data engineering are separate fields, but they work as one ecosystem.

### One ecosystem, many roles

In a modern organization, data work is rarely done by one person alone. Instead, teams with different specialties collaborate.

Typical roles include:

- **Data engineer** - builds pipelines and storage
- **Data analyst** - explores data and creates reports
- **BI professional** - builds dashboards and KPI tracking
- **Data scientist** - builds models and advanced analysis
- **Business stakeholder** - asks questions and uses insights

### How they work together

One customer stops renewing their monthly data bundle. Follow it:

```mermaid
flowchart LR
    engineerNode["Data engineer"] --> analystNode["Data analyst"]
    analystNode --> dashboardNode["BI dashboard"]
    dashboardNode --> scientistNode["Data scientist"]
    scientistNode --> teamNode["Business team"]
```

1. A **data engineer** collects the top-up and bundle records, and makes them trustworthy
2. A **data analyst** investigates why renewals fell, and finds it started after a price change
3. A **BI dashboard** puts the renewal rate in front of managers every week
4. A **data scientist** builds a model to predict which customers will lapse next
5. The **business team** decides to offer a smaller bundle at the old price

Each step depends on the one before it. The data scientist in step four cannot train anything without the records the engineer built in step one, and the decision in step five is only as good as the investigation in step two.

### Where analytics types fit

- **Descriptive analytics** - dashboards and reports
- **Diagnostic analytics** - analyst investigations
- **Predictive analytics** - data science models
- **Prescriptive analytics** - business decisions based on recommendations

Chapter 2's four types were not four separate jobs after all. They were four stages of one, spread across five people.

### Key takeaway

Nobody in that chain did the whole thing, and nobody needed to. What each of them needed was to know what the person before them had done, and what the person after them was going to do with it.

That is the practical value of knowing the ecosystem: not that you will work in all of it, but that you will be handed something by someone and expected to know what it is.

## Key Terms

| Term | Definition |
|---|---|
| **Data ecosystem** | The connected roles, tools, and processes around data |
