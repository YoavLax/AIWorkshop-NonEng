# Module 4: Dashboards, from CSV to a working web page (60 min)

**Goal:** plan a dashboard with Copilot, build it with Agent mode, **verify the numbers**, then iterate. You will end up with real, interactive HTML pages you can double-click, no coding needed.

**Why a dashboard instead of "ask the AI for the numbers"?** The dashboard page **calculates** the numbers from the CSV every time (the calculator). Copilot only writes the page (the builder). That is more reliable, repeatable (load next month's file and it updates) and keeps data on your computer.

## How these dashboards work (read once)

- A dashboard is **one `.html` file** in the `output/` folder. Double-click it and it opens in your browser.
- It does **not contain the data**. You open it, press **Choose CSV file**, and pick the CSV. (If you installed the Live Preview extension and open the file with it, it can load the CSV automatically.)
- Charts use a chart library already in the workshop: `assets/vendor/chart.umd.js`. No internet needed.

> **Use this "as-of date":** the sample data was exported on **2026-09-30**. Tell Copilot to treat that as "today", otherwise tenure and "last 90 days" numbers will differ from ours.

## 4.1 Plan first (10 min) | mode: **Plan**

Never start building straight away. Switch the mode to **Plan** and send:

```
I want an interactive HTML dashboard for our headcount, built from #file:data/employees.csv.
Audience: the People & Culture leadership team. As-of date: 2026-09-30.
Before proposing anything, look at the file, then ask me the questions you need to answer to build it well.
Then propose: the KPI cards, the charts (with the chart type for each), the filters, and the exact definition of every KPI.
```

Copilot will ask you questions (for example "what counts as an active employee?"). **Answer them.** Good answers: *"Active = no termination date."* *"Show department filter and work model filter."*

Review the plan. Edit it ("remove the table", "add average tenure"). When it fits on one page and you agree with the **definitions**, move on. Planning costs two minutes and saves twenty.

## 4.2 Build the headcount dashboard (15 min) | mode: **Agent**

Switch to **Agent** (same chat, so it remembers the plan) and send:

```
Build the dashboard we planned.
OUTPUT: one self-contained file output/headcount-dashboard.html (no internet needed). Use the local chart library via <script src="../assets/vendor/chart.umd.js"></script>.
RULES:
- The page does NOT contain data. It has a "Choose CSV file" button and also accepts drag and drop of the CSV, and reads it in the browser.
- Active employee = empty termination_date. As-of date 2026-09-30.
- Show a clear title, 4-5 KPI cards with a short definition under each, 3-5 charts, and filters.
- Clean, professional look; do not show salaries of individuals.
WHEN UNSURE: tell me your assumption instead of guessing silently.
```

When it finishes, open `output/headcount-dashboard.html`, **double-click it** (or right-click > **Reveal in File Explorer**), press **Choose CSV file** and select `data/employees.csv`.

### Verify like a pro (5 min)

Open `employees.csv` in Excel (or Sheets) and check **three numbers** from the dashboard:

1. **Active employees** → filter `termination_date` empty, count rows.
2. **Headcount by department**, e.g. Engineering → filter department + empty termination date.
3. **Average tenure** or **new hires in last 90 days** → trickier. Does the dashboard's definition match yours?

> **Common mistake to look for:** if the dashboard says **240**, it counted people who have already left. Ask Copilot: *"The headcount should exclude people with a termination date. Fix it and explain what was wrong."*

## 4.3 Vision: build from a sketch (10 min) | mode: **Agent**

Open `assets/wireframe-recruiting-dashboard.png`. This is a **wireframe**, a rough sketch of a dashboard. In the chat, **attach the image** (drag it into the chat box or use the paperclip / **Add Context > Image**) and send:

```
Build this recruiting dashboard from the attached wireframe, using #file:data/recruiting_pipeline.csv.
OUTPUT: output/recruiting-dashboard.html, one self-contained file, using ../assets/vendor/chart.umd.js, with a "Choose CSV file" button and no embedded data.
RULES: follow the wireframe's layout. Define every metric in a short sub-label. Do not invent metrics that are not possible with the columns in the file.
WHEN UNSURE: list your assumptions at the end.
```

> **If your Copilot version does not support images**, ask in Plan mode: *"What would a good recruiting funnel dashboard look like for this CSV?"* and build from that plan.

Verify:

- **Hires** = rows with `final_status` = Hired. How many in Excel?
- **Average days to hire** → average of `days_to_hire` for hired candidates.
- Is the funnel **in the right order** (Applied → Phone Screen → Interview → Final Interview → Offer → Hired)?
- Which **source** has the best hire rate? (Hint: check candidates *and* hires, not just hires.)

## 4.4 Choose your own adventure (20 min)

Pick **one**. Always Plan, then Build, then Verify. (If your dashboard needs **two** files (A, and C if you want departments), tell Copilot "the user selects both files at once and the page joins them by `employee_id`".)

| | Dashboard | Files | Challenge |
|-|-----------|-------|-----------|
| **A** | **Attrition and exit reasons** | `employees.csv` + `exit_interviews.csv` | Attrition rate for the last 12 months; reasons for leaving; leavers by department and tenure |
| **B** | **Engagement survey** | `engagement_survey.csv` | Score per question, by department; eNPS; where are the lowest scores? |
| **C** | **Compliance training** | `training_completion.csv` (+ `employees.csv` for department) | Who is overdue, per course and per department |
| **D** | **Pay equity check** (advanced, sensitive) | `employees.csv` | Compare average pay by gender and level; discuss raw vs. like-for-like gaps |

Prompt starter (adapt it!):

```
Plan, then build, a [topic] dashboard from [files]. Audience: [who]. As-of date 2026-09-30.
Think about what decisions this dashboard should help with. Ask me questions first.
```

### Traps to look for (this is where you earn your badge 🏅)

- **A:** Attrition = leavers in last 12 months ÷ *average* headcount, not ÷ current headcount. Did the definition appear on the page? Not everyone who left has an exit interview, did the dashboard say so?
- **B:** One department has **fewer than 5 responses**. Showing it identifies individuals. Does your dashboard hide or merge it? The comments column contains **personal details**: should the dashboard show comments at all?
- **C:** A course due in the future is **Pending, not Overdue**. Does your dashboard keep them apart?
- **D:** The raw gap is bigger than the gap at the *same level*. Which would you publish, and who should review before anything is shared? (This is a conversation for HR + Legal, not an AI verdict.)

## 4.5 Iterate and polish (5 min)

Try plain-English follow-ups on any dashboard:

- "Make the KPI cards bigger and use our colours: navy, teal and coral."
- "Add a filter for work model."
- "Add a 'how to read this dashboard' note at the top."
- "Add a print button / make it print nicely on one page."

**Commit your work** (Source Control > message > Commit).

Compare your dashboards: **do they all look different?** Different fonts, colours, layouts, KPI styles? In Module 5 you will fix that.

## Checkpoint

- [ ] `output/headcount-dashboard.html` opens and numbers match Excel.
- [ ] You built a recruiting dashboard from the wireframe.
- [ ] You built one more dashboard of your choice and checked at least one "trap".
- [ ] You can explain why the CSV is not embedded in the page.

## If it goes wrong

| Problem | Fix |
|---------|-----|
| Page is blank / "Choose CSV" does nothing | Tell Copilot: *"The page doesn't show anything after I choose the CSV. Please debug it and tell me what you changed."* |
| Charts are missing | Check the script line points to `../assets/vendor/chart.umd.js` (the page must be in `output/`) |
| Copilot pasted the data into the HTML | Say: *"Don't embed the data. Read it from the CSV the user selects."* |
| Numbers are off | Ask for **definitions**; compare with Excel; tell Copilot exactly which number is wrong and what you expected |
| Agent wants to run Python / install something | Say: *"Please don't install or run anything. Just create the HTML file."* |
