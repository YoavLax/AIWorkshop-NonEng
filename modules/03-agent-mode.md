# Module 3: Agent mode, let Copilot do the work (35 min)

**Goal:** hand Copilot a multi-step task, watch it work, review the result, and **undo** what you don't like. Mode: **Agent**.

## 3.1 How an agent differs from Ask (3 min)

| Ask | Agent |
|-----|-------|
| Answers in the chat | Creates and changes files for you |
| One reply per question | Works in several steps, checks its own work |
| You copy and paste results | Results appear as files in your folder |

**You stay in control:**

- The agent **asks permission** before sensitive actions. Read the request before you press **Allow/Continue**.
- Every file change is **visible** and can be **kept or undone** (section 3.4).
- It writes new files to `output/`, so your originals in `data/` stay safe.

## 3.2 The task blueprint: Goal / Inputs / Output / Rules / When unsure

Agents work best with a mini work order. Use this template:

```
GOAL:        what you want done
INPUTS:      which files to use (#file:...)
OUTPUT:      what file(s) to create, where, and what they look like
RULES:       what to follow or avoid
WHEN UNSURE: what to do instead of guessing
```

## 3.3 Exercise: clean a messy spreadsheet (15 min)

`data/new_hires_messy.csv` is what a real HR export often looks like: inconsistent dates, names in two orders, missing emails, "Support" vs. "Customer Support", duplicates. Open it and spend one minute spotting problems.

Switch to **Agent** mode, start a **new chat**, and send:

```
GOAL: Clean the new-hire list so People Ops can use it.
INPUTS: #file:data/new_hires_messy.csv
OUTPUT: A new file output/new_hires_clean.csv (do not change the original) plus output/cleaning_report.md.
RULES:
- One row per person, "First Last" names in normal capitalisation.
- Dates in YYYY-MM-DD format. Today is 2026-09-30; all start dates are in the future.
- Department names must be one of: Engineering, Sales, Customer Support, Marketing, Finance, Product, Operations, People & Culture, Legal.
- Emails in lower case. Locations as full city names (New York, Austin, London, Berlin, Toronto).
- Remove duplicate people, and mention which rows you merged.
WHEN UNSURE: do not guess. Put the row in the report under "Needs a human decision" with the reason (for example a date that could be day/month or month/day, or a missing email).
```

> If Copilot says it needs Python or another program, reply: *"Please don't use any programs. Create the files directly."*

**While it works:** watch the steps. It reads the file, creates files, and may review them.

**Then verify (do not skip!):**

1. Open `output/new_hires_clean.csv` (right-click > **Reveal in File Explorer**, then open in Excel, or simply view it in VS Code).
2. Count rows. Does it match your expectation of unique people? (The original has more rows than unique people.)
3. Pick 5 rows and compare them with the original.
4. Read the report. Did it flag ambiguous dates and missing emails or did it quietly guess?
5. Check some dates: are all start dates **Mondays**? (AI often gets weekdays wrong, so this is a nice sanity check.)

If something is off, reply in the same chat: "Row for X has the wrong department, fix it and update the report." That is **iterating**.

## 3.4 Exercise: batch welcome emails (7 min)

```
GOAL: Write a welcome email for every person in #file:output/new_hires_clean.csv.
INPUTS: the clean CSV and the template #file:docs/onboarding-welcome-template.md
OUTPUT: One file per person in output/welcome-emails/, named like "2026-10-19_imani-okonkwo.md".
RULES: Follow the template exactly. Fill in only the data in the CSV.
WHEN UNSURE: if a value is missing, write [TODO: ask People Ops for <field>]. Never invent a buddy, email or time.
```

Open two or three emails. Are any `[TODO]` markers present where data was missing? A *good* agent leaves gaps and flags them. This is how you make "AI as helper" trustworthy.

> **Privacy reminder:** the emails contain names. In real life you would only do this with HR data on a company-approved Copilot setup (Module 7).

## 3.5 Undo, your safety net (5 min)

You now have a pile of new files. Three levels of undo exist:

1. **In the chat:** each reply has an **Undo** / **Discard** option and the chat shows **Keep** / **Undo** for edits. Use it for the last step.
2. **Source Control panel:** the branch icon in the left bar lists changed files. Click a file to see exactly what changed, or the **Discard** arrow to throw changes away.
3. **Commit:** a **commit** is a named save point ("snapshot") you can always return to. Do this now:
   - Open **Source Control**, type a message such as `Clean new hire list and welcome emails`, and click **Commit**.
   - If VS Code asks to stage changes, choose **Yes / Always**.
   - If Git says it doesn't know who you are, ask Copilot in Ask mode: *"Walk me through telling Git my name and email, step by step"*, or ask your facilitator.

> **Habit:** commit after every task that went well. It costs 10 seconds and means you can't lose good work.

## Checkpoint

- [ ] `output/new_hires_clean.csv` and `output/cleaning_report.md` exist.
- [ ] You checked at least 5 rows against the original and the report flagged uncertain rows.
- [ ] Welcome emails exist with `[TODO]` markers where data was missing.
- [ ] You made a commit.

## Discuss

- What would have happened if we had told the agent "just fix everything" without "When unsure"?
- Which task in your team looks like this one (many similar items, one template)?

## Stretch

- Ask the agent to also produce a one-page onboarding checklist per department.
- Ask: *"Which rows did you change the most? Show me a before/after table for 5 of them."*
