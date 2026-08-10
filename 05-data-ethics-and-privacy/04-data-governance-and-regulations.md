# Data Governance and Regulations

**Chapter:** 5 — Data Ethics and Privacy  
**Lesson:** 4 of 4  
**By the end:** You can name a governance rule that would have prevented a given data failure.

## Overview

Every failure in this chapter had someone who could have raised a concern. Governance is what makes raising it part of somebody's job.

**Data governance** is the set of rules and roles that help an organization manage data responsibly. It answers: who owns this data, who may access it, how long is it kept, and how is privacy protected?

### Case study: governance in the loan project

Every problem in this chapter was preventable. None would have been caught by one person happening to notice. They are caught by rules that apply before anyone writes code.

| Problem from earlier lessons | The rule that catches it |
|---|---|
| Payment data reused for credit scoring | Purpose limitation: a recorded reason for every dataset, reviewed before reuse |
| Customers surprised by how their data was used | Consent review before a new product uses existing data |
| Model trained on a biased approval history | Fairness review: compare outcomes across groups before launch |
| Proxy variables nobody examined | A documented field list noting what each field may stand in for |
| Repayment chart with a truncated axis | Review of any visual going to leadership |
| Analysts able to read any customer's transactions | Access control: analysts see only what their work requires |
| Loan records kept indefinitely | Retention policy: a stated deletion date for every dataset |

Governance is not paperwork for its own sake. It is the difference between hoping somebody raises a concern and requiring that somebody does.

### Regulations

Many countries have laws protecting personal data. Details vary, but the goals are the same: require consent, give people rights over their own data, set rules for secure storage, and require organizations to report breaches. GDPR in the European Union is the most widely discussed example.

You do not need to memorize these laws as a beginner. You do need to know they exist. In your own work: follow your organization's data policies, ask before sharing sensitive data, respect access permissions, and speak up if data is being misused.

### How the case ends

The loan team pauses the launch.

They test the model against customers the old manual process had rejected, and find that repayment among rejected market traders is close to the overall average — the model was not finding risk, it was finding history. They drop district and business-payment history, and use repayment behavior on small existing advances instead: a direct measure rather than a proxy. Account age they keep — it genuinely predicts repayment — but they now compare approval rates for newer and older accounts every quarter, rather than assuming the split stays fair on its own. Then they tell customers plainly which data affects a loan decision.

The product launches three months later than planned, and reaches more customers than the original version would have.

That is the honest outcome of ethical data work. It is usually slower. It is not usually worse.

## Key Terms

| Term | Definition |
|---|---|
| **Data governance** | Policies and processes for managing data responsibly |
| **Regulation** | A legal rule governing data collection and use |
| **Compliance** | Following laws and organizational policies |
| **Data retention** | How long data is kept before it is deleted |
| **Access control** | Limiting who can see or use specific data |
