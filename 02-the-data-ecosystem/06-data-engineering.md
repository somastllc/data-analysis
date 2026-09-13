# Data Engineering

**By the end:** You can describe what data engineers build and how they prepare data for others to use.

## Overview

An analyst opens a report and finds three different versions of the same sales numbers: one outdated, one incomplete, one in the wrong format. The data exists, but nobody can trust it yet. Before analysts and data scientists can work with data, it must be collected, stored, and prepared reliably. That is the role of **data engineering**.

### What is data engineering?

**Data engineering** focuses on building and maintaining the systems that move, store, and organize data so it is reliable and ready to use.

### What data engineers do

Common responsibilities include:

- Building **data pipelines** that collect data from different sources
- Storing data in databases, data lakes, or a **data warehouse** - a centralized system designed for analysis and reporting
- Cleaning and transforming data at scale
- Ensuring data is available, secure, and efficient to access
- Working with cloud platforms and automation tools

If data analysis is about finding insights, data engineering is about making those insights possible.

### Example

The wholesaler from lesson 2 has data arriving from four places at once:

- A till in each shop, recording sales as they happen
- Delivery drivers logging what was dropped off, and where
- Supplier invoices, arriving as PDFs by email
- Phone orders, written into a notebook and typed up at the end of the day

None of these agree on how a product is named, and two of them arrive late. A data engineer builds the pipelines that pull all four together, reconcile the product names, and deliver one clean table that an analyst can actually use, every morning, without anyone being asked.
