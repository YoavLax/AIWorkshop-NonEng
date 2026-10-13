---
name: hr-dashboard-builder
description: Builds branded, single-file HTML dashboards (KPI cards and charts) from HR CSV files such as headcount, attrition, recruiting, engagement and training data. Use when the user asks for a dashboard, charts, a visual report, or a "snapshot" from a CSV file.
---

# HR Dashboard Builder (Brightwave house style)

This skill makes every dashboard look the same, work without installs, and respect our privacy rules.

## When to use
Use it whenever someone asks for a dashboard, charts, a visual summary or a "snapshot" of HR data in a CSV file.

## Steps
1. **Inspect the CSV** and list the columns you will use. Mention data problems (blanks, duplicates, odd dates).
2. **Write the definitions** of each KPI in plain words before building (for example "Active = no termination date").
3. **Copy `template.html`** (in this skill's folder) to `output/<topic>-dashboard.html` and replace only the block
   marked `YOUR DASHBOARD`. Do not change the helpers, styles, colours or footer.
4. **Fill the dashboard block** following the layout rules below.
5. **Several CSV files?** If the dashboard needs more than one file (for example employees + exit interviews), use multi: true,\r\n   equiredFiles and dataPaths in the config, exactly as the template comments describe. Join files with IDs, not row order.\r\n6. **Tell the user** the file name, how to open it (double-click, then press "Choose CSV file" and select the CSV (or all the CSVs)),
   and three numbers they can double-check in Excel.

## Layout rules
- Title and subtitle at the top (subtitle shows the "as-of" date and active filters).
- 4 to 5 KPI cards, then 3 to 6 charts, then at most one table.
- Add filters (dropdowns) for the 1 or 2 most useful categories.
- Charts: horizontal bars for rankings, vertical bars for distributions, line for trends over time, doughnut only for
  3 or fewer categories. Every chart has a clear title.
- Use the palette in the template (navy, teal, coral, amber). Never use red/green as the only way to show good/bad.
- Each KPI has a short sub-label that states its definition.

## Data and privacy rules
- The page must load the CSV with the file chooser (the template already does this). **Never paste or retype the data
  into the HTML file.**
- Use `textContent` (the helper functions do this). Never insert CSV text with `innerHTML`.
- Do not show individual salaries, ratings or free-text comments. Hide groups of fewer than 5 people
  (use `HR.suppressSmall`).
- Keep the footer reminder about authorised access.

## Quality checklist (run before you finish)
- [ ] Totals on the page equal the number of qualifying rows in the CSV.
- [ ] "Today" is not hard-coded to the real date when the data has an export date; use an as-of date input.
- [ ] Every KPI definition is visible on the page.
- [ ] The file opens by double-click and works without internet.
- [ ] No files in `data/` were modified.
