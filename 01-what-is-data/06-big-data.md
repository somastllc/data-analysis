# Big Data

**By the end:** You can say what makes data "big", and judge whether a dataset actually is.

## Overview

A market trader's sales book holds four hundred rows and answers every question the trader has. A digital wallet serving millions of customers records four hundred payments while you read this sentence. Both are data, collected the same way, describing the same kind of event. Only one of them breaks an ordinary spreadsheet, and the difference is not what the data means. It is how much of it arrives, how fast, and in how many shapes.

### What makes data big

**Big data** is data at a scale that ordinary tools and methods can no longer handle. There is no row count that makes the label true. What matters is whether the usual approach has stopped working.

Three things push a dataset past that point, and they are usually named together.

| The three Vs | The question it answers | The market trader | The digital wallet |
|---|---|---|---|
| **Volume** | How much is there? | 400 rows in a book | Billions of payment records |
| **Velocity** | How fast does it arrive? | A few sales an hour | Thousands of payments a second |
| **Variety** | How many shapes does it come in? | One table | Payments, app logs, support chats, photos of receipts |

Variety you have already met. It is the structured, semi-structured, and unstructured split from the types lesson, seen from a distance.

### Big is a relationship, not a number

The same dataset can be big for one organization and ordinary for another. A hospital that has always worked in spreadsheets meets big data at a few million rows. A payment company meets it much later, because it already owns the systems.

This is why the honest test is a question about the tools rather than the data: has the usual way of working broken? If a file still opens, a query still returns, and one machine still holds it, the dataset is not big, whatever its subject.

Most data work is not big data work. A shop, a school, and a clinic each run on data that fits comfortably in ordinary tools, and the questions that matter to them are answered there. Calling a small dataset "big data" is how organizations end up buying systems they never needed, to solve a problem they did not have.

### What changes when data really is big

Once one machine is not enough, the work changes shape rather than just getting slower.

- **Storage spreads out.** The data sits across many machines instead of one, which is what a data lake is for.
- **Errors hide.** In four hundred rows you can see a bad value. In four billion you have to detect it, and anything you cannot detect you inherit.
- **Deletion gets hard.** Finding every copy of one person's records across many systems is real work, which is why retention rules are written before the data piles up rather than after.
- **Someone has to build the plumbing.** Moving data at this scale is a full-time job, and a field exists around it.

That last point is the reason this lesson sits here. Most of what the next chapter describes, the systems, the specialists, and the pipelines between them, exists because data outgrew the spreadsheet.

### Big is not the same as useful

A large dataset is not automatically a better one. Everything from the quality lesson still applies, and applies harder: billions of rows collected carelessly are billions of rows of careless data, and the scale makes the flaw more convincing rather than less.

The trader with four hundred honest rows can answer the trader's question. That is worth more than four billion rows nobody checked.
