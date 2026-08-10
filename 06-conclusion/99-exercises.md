# Chapter 6 Exercises: Putting It Together

**Chapter:** 6 — Conclusion  
**Type:** Practice — no software required

## How to use these

These two exercises cover the whole course. Work through the first one on paper before opening the answer — it is the closest thing to real analytical work that this course can give you without software.

### Exercise 1 — Run the process yourself

**The situation.** A bus company operating twelve routes in a growing city has a problem. Passenger numbers are flat overall, but drivers on three routes complain that buses are overcrowded, while managers see reports showing plenty of spare capacity.

Work through all six steps of the analysis process. For each step, write two or three lines.

1. Define the problem and ask questions
2. Collect data
3. Clean the data
4. Analyze and visualize
5. Communicate insights
6. Decide and consider ethics

<details>
<summary>Show answer</summary>

A reasonable version. Yours will differ — check that each step does its own job rather than matching this wording.

**1. Define and ask.** Stakeholders: operations manager, drivers, finance. The complaint and the report disagree, so the real question is not "are buses full?" but "why do two sources disagree?" Questions: is crowding concentrated at particular hours? Are the reports averaging across the whole day? Which three routes, and what do they have in common?

**2. Collect.** Ticket sales by route, stop, and timestamp; bus capacity per vehicle; the schedule; driver complaint records. Ticket data is the key source because it carries time — the daily totals in the manager's report do not.

**3. Clean.** Expect duplicate scans when passengers tap twice, missing data from terminals that lost connection, routes renamed mid-year, and timestamps in different time zones or formats. Document anything you drop.

**4. Analyze and visualize.** Compare passengers against capacity *per hour*, not per day. Likely finding: the three routes run at 130% capacity between 07:00 and 09:00 and near-empty at midday, and averaging across the day hides both. A line chart of hourly load per route would make this visible immediately.

**5. Communicate.** Lead with the finding: "Three routes are over capacity at rush hour. The daily average hides it, because the same buses are nearly empty by 11am." Show one chart. Recommend the action.

**6. Decide and consider ethics.** Options: add buses at peak, shift departure times, or reprice. Ethical considerations: ticket data can reveal where individuals travel and when, so analysis should use aggregated counts rather than individual journeys, and any published version should not allow a single rider to be identified from a thin route at an odd hour.

**The point of this exercise:** the error was not in the data. It was in the *averaging*. A correct number computed at the wrong level of detail is one of the most common ways analysis misleads people, and no tool protects you from it.

</details>

### Exercise 2 — Map the path ahead

For each task below, name which upcoming course in the Data Analysis path would teach you to do it.

1. Pull rush-hour ticket records for three routes out of a database with 200 million rows
2. Decide whether the difference between two routes is real or just random variation
3. Repeat the whole cleaning process automatically each week
4. Build the hourly-load chart as a dashboard managers can filter themselves
5. Handle the duplicate taps and inconsistent timestamps properly
6. Let a colleague review your work before it ships

<details>
<summary>Show answer</summary>

1. **SQL for Data Analysis** (course 4)
2. **Statistics for Data Analysis** (course 6)
3. **Python Fundamentals** (course 2), then **Data Analysis with Pandas** (course 7)
4. **Power BI** (course 10), with **Data Visualization and Storytelling** (course 11) for making it readable
5. **Data Cleaning and Data Wrangling** (course 8)
6. **Git and GitHub** (course 3)

Every one of the six steps you just worked through has a course behind it. You have now done the whole process once, on paper, with none of the tools.

That was the point. The tools are the easy part to learn and the fastest part to become outdated. Knowing which question to ask, noticing that an average was hiding the answer, and recognizing when data should not be used at all — those do not expire, and no course later in this path will teach them again.

</details>
