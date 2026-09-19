# Data Governance and Regulations

**By the end:** You can name a governance rule that would have prevented a given data failure.

## Overview

Every failure in this chapter had someone who could have raised a concern. Governance is what makes raising it part of somebody's job.

**Data governance** is the set of rules and roles that help an organization manage data responsibly. It answers: who owns this data, who may access it, how long is it kept, and how is privacy protected?

### Case study: governance in the loan project

Every problem in this chapter was preventable. None would have been caught by one person happening to notice. They are caught by rules that apply before anyone writes code.

| Problem | The rule that catches it |
|---|---|
| Payment data reused for credit scoring | Purpose limitation: a recorded reason for every dataset, reviewed before reuse |
| Customers surprised by how their data was used | Consent review before a new product uses existing data |
| Model trained on a biased approval history | Fairness review: compare outcomes across groups before launch |
| Proxy variables nobody examined | A documented field list noting what each field may stand in for |
| Repayment chart with a truncated axis | Review of any visual going to leadership |
| Analysts able to read any customer's transactions | Access control: analysts see only what their work requires |
| Loan records kept indefinitely | **Data retention**: a rule stating how long each dataset is kept and when it must be deleted |

Six of those seven went wrong in front of you over the last three lessons. The last one did not: nobody in this case ever asked how long the loan records would be kept, and nothing in the story forced them to.

That is the argument for governance in one line. The rules are not written from the failures you have had. They are written from the failures other people have had, which is the only way to be protected from the one you have not thought of yet.

### Regulations

A **regulation** is a legal rule governing how data is collected and used.

Many countries have laws protecting personal data. Details vary, but the goals are the same: require consent, give people rights over their own data, set rules for secure storage, and require organizations to report breaches. GDPR in the European Union is the most widely discussed example, and for most people reading this it is also the one that does not apply. The law that governs your work is the one where your organization operates and where your customers live. Find out which that is before you need it, not during the week you need it.

You do not need to memorize these laws as a beginner. You do need to know they exist. In your own work: follow your organization's data policies, ask before sharing sensitive data, respect access permissions, and speak up if data is being misused.

### How the case ends

The loan team pauses the launch.

They test the model against customers the old manual process had rejected, and find that repayment among rejected market traders is close to the overall average. The model was not finding risk, it was finding history. They go back to the four fields they started with. District and business-payment history are dropped: both were proxies, and both were the ones sorting by gender. Monthly transaction volume stays, because it was never a proxy for anything - it measures the business the loan is for. Account age they keep too, since it genuinely predicts repayment, but they now compare approval rates for newer and older accounts every quarter rather than assuming the split stays fair on its own. In place of the two dropped fields they add repayment behaviour on small existing advances: another direct measure. Then they tell customers plainly which data affects a loan decision.

The product launches three months later than planned, and reaches more customers than the original version would have.

That is the honest outcome of ethical data work. It is usually slower. It is not usually worse.
