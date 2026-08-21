# Responsible and Ethical Use of Data

**Chapter:** 5 — Data Ethics and Privacy  
**Lesson:** 1 of 4  
**By the end:** You can name the principles of responsible data use, and spot a chart that misleads without stating anything false.

## Overview

The most damaging data projects are rarely built by bad people. They are built by good teams who never stopped to ask whether they should.

This chapter follows one project — a mobile money company building an automatic loan product — through four lessons: responsible use, privacy, bias, and governance.

### Case study: the loan scoring project

A mobile money company has millions of customers who send and store money on their phones. It decides to launch **small business loans**, approved automatically in minutes.

To decide who gets a loan, the team scores each customer using data the company already holds:

- How much money flows through the account each month
- How long the account has existed
- Which district the phone number is registered in
- Whether the customer has ever received a business payment

On paper this is an excellent project. The data exists, and the business case is strong. Almost every ethical problem in this chapter is hiding inside it.

### When the numbers are true but the chart lies

Before the full launch, the team runs a pilot and reports its repayment rates:

| Month | Repayment rate |
|---|---|
| January | 91.0% |
| February | 91.4% |
| March | 91.2% |
| April | 92.0% |

An analyst who wants the project to look successful can draw this:

```
Chart A — vertical axis runs from 90% to 92%

Jan  ##########
Feb  ##############
Mar  ############
Apr  ####################
```

The same four numbers, with a full axis:

```
Chart B — vertical axis runs from 0% to 100%

Jan  ####################################
Feb  ####################################
Mar  ####################################
Apr  ####################################
```

Chart A contains no false numbers. It is still misleading, because the axis turns a one-point change into what looks like a doubling.

This is the most common dishonesty in data work, and it rarely feels like lying. Nobody edited a number. Someone chose the axis that told the story they wanted.

Two warning signs in your own charts: an axis that does not start at zero without a reason, and a percentage shown without the count behind it, like "50% growth" from 2 customers to 3.

### Principles of responsible data use

- **Transparency** — be clear about what data is collected and why
- **Purpose limitation** — use data only for the purpose it was collected for
- **Accuracy** — do not base decisions on flawed or misleading data
- **Fairness** — avoid harm to individuals or groups
- **Accountability** — take responsibility for how data is used

Before starting any data project, ask the question the loan team skipped: could this harm someone, and would we be comfortable explaining it publicly?

## Key Terms

| Term | Definition |
|---|---|
| **Data ethics** | Principles for using data responsibly and fairly |
| **Transparency** | Openness about data collection and use |
| **Accountability** | Responsibility for the outcomes of data use |
| **Purpose limitation** | Using data only for the purpose it was collected for |
| **Misleading visualization** | A chart that is factually correct but creates a false impression |
