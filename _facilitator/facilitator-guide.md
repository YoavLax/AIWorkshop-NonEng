# Facilitator guide

Do not share this folder (`_facilitator/`) with participants. It contains the answer key.

## 1. Before the workshop (checklist)

**Licences and policies**
- [ ] Every participant has a GitHub account and a **Copilot** seat (Business/Enterprise or individual).
- [ ] Org policies allow: **Copilot Chat**, **agent mode**, and (if used) **custom agents / skills**. Ask an admin to check the org's Copilot policies, plus the VS Code settings for agent mode and skills. Setting names change between releases: search "agent" and "skills" in VS Code Settings.
- [ ] The **GitHub Copilot app**: get the current download link and sign-in steps from your organisation, and put it in the README's prerequisites. Check it runs on participants' OS. If you cannot provide it, run Module 6 as a facilitator demo.
- [ ] Optional: share the Microsoft **Live Preview** VS Code extension.

**Create the participant repository (recommended)**
This folder is its own repository. Participants should open it as the workspace root (so the `.github` files they create apply).

Option A, template repo (best): push this repo to GitHub, mark it as a **Template repository** (Settings), and make sure the published copy does not include `_facilitator/` (for example keep a private facilitator repo, or delete the folder from the template). Participants click **Use this template**, then clone it in VS Code.

Option B: zip the folder and share it; participants unzip and **File > Open Folder**. (Participants then need to run **Git: Initialize Repository** for Module 3's commit step, and the Copilot app needs a Git repository.)

**Dry-run it yourself** the day before, as a participant (a clean machine/user if possible). Time each module. Check:
- [ ] Module 3: does the agent try to run Python? (Python is not required, tell it to create files directly.)
- [ ] Module 4: dashboards open by double-click, "Choose CSV file" works.
- [ ] Module 5: `/policy-question` and the custom agent appear; the skill is used.
- [ ] Module 6: sessions open and a worktree session sees committed `.github` files.

**Room**
- Pairs work well. One participant types, the other checks the output against the source.
- Put the traffic-light table on a slide for the end.

## 2. Run of show

| Time | Module | Facilitator focus |
|------|--------|-------------------|
| 0:00 | **0 Setup** | Get everyone to a working chat. Have 1 helper handle stuck installs. Don't wait more than 5 minutes per person; pair them up. |
| 0:10 | **1 Foundations** | Stress: *confident is not correct*. Keep it short; the hands-on starts in Module 2. |
| 0:30 | **2 Ask** | The hallucination (Module 1 question without docs vs. with docs), the 15 vs. 20 day conflict and the gym question are the aha moments. Ask: "who noticed the conflict?" |
| 0:55 | **3 Agent** | Live-demo the first 3 minutes. The messy CSV is relatable. Emphasise permission prompts and undo. Make sure everyone commits. |
| 1:30 | Break | Helpers: collect common problems. |
| 1:40 | **4 Dashboards** | Plan mode first. After each build, force the verification step; ask "who found a wrong number?" Celebrate. |
| 2:40 | **5 Customize** | The before/after on dashboards sells skills. Keep the analogies (handbook, templates, specialist, playbook). |
| 3:20 | **6 Copilot app** | Demo, then hands-on. If the app isn't available, demo only. |
| 3:45 | **7 Responsible AI** | Do the scenarios in pairs. Close with Monday lists. |
Total about 4 h with a 10-minute break. For a **3-hour version**: do 0, 1, 2, 3, 4.1-4.3, 7 (skip 4.4, 5, 6). For a **half-day plus**: add the optional demos below.

## 3. Wow moments to plan for

1. Confident parental-leave answer with no documents (Module 1) vs. cited answer (Module 2).
2. 26 welcome emails created in a minute (Module 3), with `[TODO]` where data is missing.
3. Wireframe image becomes a working dashboard (Module 4.3).
4. Same prompt, before and after the skill: consistent branded dashboards (Module 5.5).
5. Two sessions working in parallel (Module 6).

## 4. Known behaviours and fixes

| Symptom | Likely cause / fix |
|---------|--------------------|
| Agent says it needs Python/Node | Tell it: "Don't use programs, create the files directly." |
| Headcount shows 240 | It counted leavers. Teaching moment, then fix. |
| Weekday mistakes in clean list | Copilot is poor at weekdays. Ask it to verify, or flag in the report. |
| Dashboard embeds data | Say "Don't embed the data; read it from the CSV the user selects." |
| Blank dashboard | Participant must press Choose CSV file. Make sure the file is in `output/` (chart library path), then ask Copilot to debug it. |
| Skill not used | Folder must be `.github/skills/hr-dashboard-builder/SKILL.md`; check skills setting; reload window. Fallback: attach `SKILL.md` and `template.html` explicitly. |
| Custom agent not in picker | Reload window. File must end with `.agent.md` in `.github/agents/`. |
| Git commit fails ("who are you?") | `git config --global user.name`/`user.email`, or have Copilot walk them through. |
| Copilot app session doesn't see `.github` | Changes weren't committed. Commit in VS Code first. |
| "Live Preview" absent | Fine, file chooser works everywhere. |
| Output differs from the answer key | Non-determinism is normal. Judge by definitions and Excel checks, not identical text. |

## 5. The planted traps (teaching points)

- **Conflicting policies:** remote-work-policy says 15 days work-from-abroad; PTO policy says 20.
- **Unanswerable question:** gym reimbursement is in no document.
- **Biased inputs:** the job description (rockstar, young, native speaker...), the review notes (medical leave, gendered adjectives).
- **Small groups:** Legal has 3 survey responses.
- **PII in comments:** 5 survey comments contain names, an email, phone, or medical remark.
- **Pending vs. overdue** in training data.
- **Raw vs. adjusted pay gap** in employees.csv.
- **Duplicates / ambiguous dates** in new_hires_messy.csv.

See `answer-key.md` for the expected numbers. The key matches the committed CSVs; if the data changes, recompute it.

## 6. Data and adapting the workshop

All data is fictional ("Brightwave Co.", as-of date 2026-09-30) and fixed: the CSVs in `data/` and `answer-key.md` match each other, so don't edit either without recomputing the other (the original generator script is in the git history). To adapt the workshop for another function:
- **Finance/Ops:** reuse the structure with invoices, expenses or tickets, and adapt the policies.
- **Legal/Compliance:** use the policy Q&A and conflicts, and the training dataset.
- **Marketing:** swap in campaign metrics for the dashboard module.

Dashboards use the `HR.*` helpers in `solutions/customization/skills/hr-dashboard-builder/template.html`. The skill's rules there (minimum group 5, text via `textContent`, no embedded data) are the same ones the workshop teaches.

## 7. Optional demos (facilitator-led)

- **MCP:** show a connector (for example to Jira or a calendar) and explain "Copilot gets plugs to other systems" and why permissions matter. Skip if the audience is new.
- **Cloud agent:** create a GitHub issue "Add FAQ about parental leave to docs", assign it to Copilot, show the resulting pull request.
- **Excel formula assistant:** have Copilot write a spreadsheet formula to calculate attrition, then compare to the dashboard.

## 8. After the workshop

Send participants: the repo link, CHEAT-SHEET.md, your org's data guidance, and a feedback form:

1. How confident are you using Copilot for work (1-5)? Before / after.
2. Which module was most useful? Which was too hard or too easy?
3. What's the first task you will use it for?
4. Do you know what you should never share with an AI tool?

Suggested follow-ups: a 30-minute "show your skill" session after two weeks, and a shared `.github` folder for the team.
