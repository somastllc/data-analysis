# Putting It All Together - An End-to-End Scenario

**By the end:** You can follow one real dataset through its whole life, and name the ideas from this course that apply at each stage.

## Overview

One business problem. One dataset. Every idea in this course, used once. You will follow that data from the moment it is created to the moment it is deleted.

### Scenario

A subscription-based fitness app notices that many users cancel after the first month. Leadership asks:

**"Why are new users cancelling, and what should we do about it?"**

When customers stop using a product or service, that loss is called **churn**.

### Create and collect

The data already exists before anyone decides to study it. Every sign-up, workout, support ticket, and cancellation created a record at the moment it happened.

What the team gathers:

- User sign-up and cancellation dates
- App activity logs
- Support ticket response times
- Survey responses from cancelled users

Those four sources are different types of data. Dates and workout counts are quantitative and structured. Survey answers are qualitative and unstructured. The activity logs sit somewhere in between.

Notice what is not here. Users who never answered the survey created no record, so their reasons for leaving were never collected at all. That gap leaves no blank cell to notice.

### Store and process

The records live in three different places: the app database, the support system, and a survey tool. A pipeline built by a data engineer moves them into one warehouse where they can be compared.

Quality problems found on arrival:

- Duplicate user records
- Missing survey responses
- Inconsistent date formats

The duplicates are removed, the dates are put in one format, and the missing survey responses are counted and reported rather than filled in. A missing answer and a neutral answer are different things.

### Analyze and visualize

Findings:

- 40% of cancellations happen within the first 14 days
- Users who complete fewer than 3 workouts are more likely to cancel
- Support response times are slower on weekends
- Survey responses describe **onboarding**, the first experience new users have with the product, as confusing

Visuals:

- Line chart of cancellations over time
- Bar chart of cancellation reasons
- Table comparing workout counts for retained and cancelled users

The charts show that early inactivity and cancellation happen together. They do not show that one causes the other.

### Who did the work, with what

| Role | What they contributed |
|---|---|
| **Data engineer** | Built and maintained the pipeline feeding the warehouse |
| **Data analyst** | Explored the cancellation patterns and built the charts |
| **BI professional** | Kept a monthly churn dashboard visible to leadership |
| **Product team** | Made the final decision |

Tools used: SQL to pull the user data, Python in a notebook for the analysis, and a dashboard tool for the churn view. The smallest tool that answered each question, which is the rule from the toolkit lesson.

### What ethics asked at each stage

- **Collect:** only data the question needed, gathered with permission
- **Store:** access limited to the people working on the problem
- **Analyze:** the team checked whether the recommended changes would affect some user groups unfairly
- **Share:** personal identifiers removed before the report left the team

### The decision

Leadership approves:

1. A simpler onboarding tutorial
2. Reminder messages encouraging first workouts
3. Extra weekend support staff for the next quarter

They will measure results after 60 days and look at the data again.

### Archive and delete

The analysis ends; the data does not. The survey responses are kept for one year and then deleted, because they contain free text about individual people and serve no purpose afterwards. The activity logs move to slower storage after two years. The cancellation dates stay, because next year's churn question will need them.

Deciding what to keep and what to destroy is the last stage of the lifecycle, and it is a governance decision rather than an analysis one.

### What this scenario shows

One business problem touched every part of this course:

- Data types, formats, and quality
- The full lifecycle, from creation to deletion
- The data ecosystem, the roles in it, and the pipeline underneath
- Tools and careers
- Ethics and responsible use

The same data, handed to a data scientist, would have ended in a model that scores each new user's likelihood of cancelling. Different output, same records, same life, and the same obligation to the person behind each one.

That is how data work happens in the real world.
