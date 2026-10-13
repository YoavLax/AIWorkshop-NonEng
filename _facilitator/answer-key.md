# Facilitator answer key

> **Do not share with participants.** The numbers below are valid for the CSVs in `data/` as committed; if you change the data, recompute them.
> "Today" inside the fictional company is **2026-09-30**.
> Participants verify against Excel - this key is for you to judge whether Copilot's answer is right.

## Metric definitions used by this key
- **Active employee** = row in `employees.csv` with an empty `termination_date`.
- **12-month attrition rate** = leavers with termination dates 2025-10-01 - 2026-09-30 / average of (headcount on 2025-10-01, headcount on 2026-09-30).
- **New hire (last 90 days)** = active employee with `hire_date` within 90 days of 2026-09-30.
- **eNPS** = % scoring 9-10 minus % scoring 0-6 on `enps_0_to_10`.

## Module 1 / 4.1 - Headcount (`employees.csv`)
- Total rows: **240**; active: **213**; leavers (all in the 12-month window): **27**
- Average tenure of active employees: **2.2 years**; new hires in last 90 days: **23**
- Contractors among active: **16**; part-time: **8**

Active headcount by department:

| Department | Active |
|---|---|
| Engineering | 56 |
| Sales | 40 |
| Customer Support | 31 |
| Marketing | 22 |
| Operations | 17 |
| Product | 15 |
| Finance | 13 |
| People & Culture | 11 |
| Legal | 8 |

Active headcount by location: New York 56, Austin 54, London 40, Toronto 37, Berlin 26

Active headcount by work model: Hybrid 135, Remote 49, Onsite 29

> **Common trap:** if Copilot answers "240" for headcount, it forgot to exclude leavers. Great teaching moment.

## Module 4.4A - Attrition & exit reasons (`employees.csv` + `exit_interviews.csv`)
- Leavers: **27**; average headcount: **183.0** -> 12-month attrition: **14.8%**
- Leavers within first year of tenure: **16** of 27 (59.3%)
- Exit interviews on file: **24** of 27 leavers (not everyone has one - data gap to point out)
- Voluntary vs involuntary (interview records): {'Voluntary': 21, 'Involuntary': 3}
- Top reasons: Compensation (5), Better external opportunity (5), Work-life balance (4), Career growth (3), Relocation (3)

Leavers by department:

| Department | Leavers | Attrition vs. dept headcount |
|---|---|---|
| Engineering | 6 | 9.7% |
| Sales | 6 | 13.0% |
| Customer Support | 7 | 18.4% |
| Marketing | 0 | 0.0% |
| Product | 1 | 6.2% |
| Finance | 1 | 7.1% |
| People & Culture | 1 | 8.3% |
| Operations | 5 | 22.7% |
| Legal | 0 | 0.0% |

## Module 4.4B - Engagement survey (`engagement_survey.csv`)
- Responses: **150** (approx. 70.4% participation); eNPS: **-7**
- Responses by department: Engineering 40, Sales 29, Customer Support 22, Marketing 16, Operations 12, Product 11, Finance 9, People & Culture 8, Legal 3
- **Small-group trap:** Legal has only **3** responses - below the minimum group size of 5, so it should be hidden/merged. This is exactly what the privacy rules in Module 5 teach.
- Average score per question (1-5): manager_support 3.97, career_growth 3.74, workload 3.79, recognition 3.75, compensation_fairness 3.95, inclusion 4.00, goal_clarity 3.91
- Planted insights: Customer Support scores lowest on **workload** (2.91) and **recognition** (3.50); Sales is lowest on **career_growth** (3.10); remote employees score lower on recognition/inclusion; employees in the "3-5 years" band score lowest on career growth.
- **Privacy trap:** 5 comments contain names, an email, a phone number, a resignation hint, or a medical remark. A good dashboard must not display raw comments without a warning/redaction.

## Module 4.2 - Recruiting funnel (`recruiting_pipeline.csv`)
- Candidates: **444**; hires: **53**; offers extended (reached Offer stage, not still in progress): **61** -> offer-accept rate **86.9%**
- Average days to hire: **38.6**

Funnel (candidates who reached each stage or beyond):

| Stage | Candidates |
|---|---|
| Applied | 444 |
| Phone Screen | 270 |
| Interview | 162 |
| Final Interview | 93 |
| Offer | 65 |
| Hired | 53 |

Hire rate by source:

| Source | Candidates | Hired | Hire rate |
|---|---|---|---|
| Referral | 52 | 22 | 42.3% |
| LinkedIn | 140 | 15 | 10.7% |
| Careers Site | 103 | 6 | 5.8% |
| Job Board | 79 | 0 | 0.0% |
| Agency | 32 | 5 | 15.6% |
| University | 38 | 5 | 13.2% |

Average days-to-hire by department: Customer Support 21, Engineering 53, Finance 19, Legal 39, Marketing 33, Operations 34, People & Culture 44, Product 54, Sales 33

## Module 4.4C - Compliance training (`training_completion.csv`)
- Records: **1065**; status counts: {'Completed': 852, 'Pending': 150, 'Overdue': 63}; employees with at least one overdue course: **53**
- Overdue by course: {'Anti-Harassment': 20, 'Data Privacy': 17, 'Code of Conduct': 9, 'Workplace Safety': 17}
- Overdue by department: {'Customer Support': 20, 'Engineering': 11, 'Sales': 10, 'Marketing': 6, 'Finance': 5, 'Operations': 5, 'Product': 3, 'Legal': 2, 'People & Culture': 1} (Customer Support is planted as the worst)
- "Security Awareness" is due 2026-11-15 - **Pending is not Overdue** (a good check that Copilot does not mis-flag it).

## Module 4.4D - Pay equity challenge (`employees.csv`, active only)
- Average salary: women **$85,686**, men **$96,224** -> **raw gap 11.0%**
- Raw gap by department: Engineering 10.2%, Sales 17.1%, Customer Support -7.4%
- Gap **after comparing like-for-like levels** (average of per-level ratios): Engineering 2.8%, Sales 3.0%, Customer Support 1.8%
- Planted: women in Engineering and Sales are paid roughly 3-4% less at the same level (the raw gap is larger because fewer women reach senior levels). Teaching point: *raw vs. adjusted gap*, small groups, and why this needs HR/Legal review - not a Copilot verdict.

## Module 3 - Cleaning `new_hires_messy.csv`
- The file has **30** rows for **26** unique people (**4 duplicates**, one with a conflicting start date).
- Intended start dates are all Mondays between 2026-10-19 and 2026-11-16. Ambiguous `dd/mm` vs `mm/dd` values should be resolved or **flagged** - a hire in London may be written day-first.
- Three rows have no email; one email has a typo'd domain (`brightwave.exmaple`); some are upper-cased.

Truth table (for judging the cleaned output):

| Name | Intended start | Department | Location |
|---|---|---|---|
| Imani Okonkwo | 2026-10-19 | Engineering | New York |
| Pedro Almeida | 2026-10-26 | Sales | Austin |
| Hanna Berg | 2026-11-02 | Customer Support | London |
| Yusuf Demir | 2026-11-09 | Engineering | Berlin |
| Clara Whitaker | 2026-11-16 | Marketing | Toronto |
| Mohan Iyer | 2026-10-19 | Finance | New York |
| Sienna Cross | 2026-10-26 | Product | Austin |
| Tomas Havel | 2026-11-02 | Operations | Berlin |
| Aaliyah Brooks | 2026-11-09 | Customer Support | Austin |
| Gabriel Torres | 2026-11-16 | Sales | New York |
| Freya Lund | 2026-10-19 | Engineering | London |
| Nadia Rahman | 2026-10-26 | People & Culture | Toronto |
| Jun Watanabe | 2026-11-02 | Engineering | New York |
| Elise Fontaine | 2026-11-09 | Marketing | London |
| Dominic Pruitt | 2026-11-16 | Sales | Austin |
| Layla Mansour | 2026-10-19 | Legal | London |
| Kai Sorensen | 2026-10-26 | Engineering | Berlin |
| Beatriz Campos | 2026-11-02 | Customer Support | Toronto |
| Owen Gallagher | 2026-11-09 | Operations | New York |
| Ananya Rao | 2026-11-16 | Finance | Austin |
| Theo Marchetti | 2026-10-19 | Product | Berlin |
| Zainab Yusuf | 2026-10-26 | Customer Support | London |
| Callum Reid | 2026-11-02 | Sales | Toronto |
| Mina Kobayashi | 2026-11-09 | Engineering | Toronto |
| Rafael Quintero | 2026-11-16 | Marketing | Austin |
| Esther Boateng | 2026-10-19 | People & Culture | New York |

## Module 2 - Policy Q&A (`docs/`)
| Question | Expected answer | Source |
|---|---|---|
| Weeks of paid leave for a birth parent / secondary caregiver? | 16 weeks / 8 weeks, both at 100% pay | parental-leave-policy.md |
| Who is eligible? | Full-time and part-time employees with 6+ months of service; not contractors | parental-leave-policy.md |
| PTO days for a 5-year employee? | 25 + 2 (one extra day per year of service after year 3) = **27** | pto-and-holidays-policy.md |
| Max work-from-abroad days? | **Conflict:** remote-work-policy says 15; pto-and-holidays-policy says 20 | both |
| Learning stipend? | $1,500 per year after 90 days; $3,000 with manager business case; repayment clause for >$1,000 if leaving within 12 months | learning-and-development-policy.md |
| Do we reimburse gym memberships? | **Not covered** - the correct answer is "I can't find this" | none (trap) |
| Home-office budget? | $600 one-time + $40/month connectivity | remote-work-policy.md |

## Module 2.3 - Job description red flags (`docs/job-description-draft.md`)
"rockstar", "ninja", "young and energetic", "digital native", "recent graduate", "native English speaker", gendered pronoun "he", "clean-cut", "aggressive", "work hard, play hard", "10+ years" for an entry-level role, 50 lb lifting for a desk role, missing salary range.

## Module 2.4 - Performance review notes (`docs/performance-review-notes.md`)
Watch for: gendered/personality language ("bossy", "too emotional"), penalising the 3-month medical leave, vague claims without evidence, and Copilot inventing achievements that are not in the notes.
