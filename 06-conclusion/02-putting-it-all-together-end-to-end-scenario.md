# Putting It All Together - An End-to-End Scenario

**Chapter:** 6 - Conclusion  
**Lesson:** 2 of 2  
**By the end:** You can walk a real business problem through every stage covered in this course.

## Overview

One business problem. Six steps. Every idea in this course, used once. You will follow that problem from the first question through to a recommended decision.

### Scenario

A subscription-based fitness app notices that many users cancel after the first month. Leadership asks:

**"Why are new users cancelling, and what should we do about it?"**

When customers stop using a product or service, that loss is called **churn**.

Let's walk through the project using this course's framework.

### Step 1: Define the problem and ask questions

**Stakeholders:** product manager, marketing lead, support manager

**Questions:**

- When do most users cancel?
- Do cancelled users share common behavior patterns?
- Are support delays linked to cancellation?
- Did cancellations increase after a recent app update?

### Step 2: Collect data

The team gathers:

- User sign-up and cancellation dates
- App activity logs
- Support ticket response times
- Survey responses from cancelled users

Data comes from the app database, support system, and customer surveys.

### Step 3: Clean the data

Issues found:

- Duplicate user records
- Missing survey responses
- Inconsistent date formats

The analyst removes duplicates, standardizes dates, and documents missing survey data as a limitation.

### Step 4: Analyze and visualize

Findings:

- 40% of cancellations happen within the first 14 days
- Users who complete fewer than 3 workouts are more likely to cancel
- Support response times are slower on weekends
- Survey responses describe **onboarding**, the first experience new users have with the product, as confusing

Visuals include:

- Line chart of cancellations over time
- Bar chart of cancellation reasons
- Table comparing workout counts for retained vs cancelled users

### Step 5: Communicate insights

The analyst presents:

- **Main insight:** New users who do not engage early are much more likely to cancel, and slow weekend support may make the problem worse.
- **Recommendation:** Improve onboarding, encourage early workouts, and increase weekend support coverage.

### Step 6: Consider roles, tools, and ethics

**Roles involved:**

- Data engineer maintained the activity data pipeline
- Data analyst explored the cancellation patterns
- BI dashboard tracked monthly churn
- Product team made the final decision

**Tools used:**

- SQL to extract user data
- Python and a Jupyter Notebook for analysis
- Power BI for a churn dashboard

**Ethical considerations:**

- User data was accessed only with proper permission
- Personal identifiers were removed from the report
- The team checked whether recommendations might affect some user groups unfairly

### Final decision

Leadership approves:

1. A simpler onboarding tutorial
2. Reminder messages encouraging first workouts
3. Extra weekend support staff for the next quarter

They will measure results after 60 days and review the data again.

### What this scenario shows

One business problem touches every part of the course:

- Data types and quality
- The data ecosystem and pipeline
- The process from question to decision
- Tools and careers
- Ethics and responsible use

This scenario was answered with charts and a report. The same six steps, run by a data scientist, would have ended in a model that scores each new user's likelihood of cancelling: different output, same problem, same order, same obligation to name what it assumed.

That is how data work happens in the real world.
