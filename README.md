# GitHub Copilot for People & Culture (and other non-technical teams)

A hands-on workshop for people who **do not write code**: HR, Recruiting, Finance, Ops, Legal, Marketing, and anyone else who works with documents, spreadsheets and reports.

You will use GitHub Copilot as a **work assistant**: ask questions about policies, clean up messy spreadsheets, draft documents, and build interactive dashboards from CSV files, without writing a line of code yourself.

> **Time:** about 4.5 hours (with a break) | **Level:** beginner | **Coding experience needed:** none

## What you will be able to do afterwards

- Explain in plain words what AI can and cannot do, and why it sometimes gets things wrong.
- Write prompts that get good results the first time (the **Goal / Context / Format / Rules** formula).
- Use **Ask**, **Plan** and **Agent** modes, and know when to use which.
- Turn a messy spreadsheet into a clean one, and an HR CSV into a working HTML dashboard.
- Teach Copilot your team's rules once, using **instructions**, **prompt files**, **agents** and **skills**, so you never repeat yourself.
- Run several tasks in parallel in the **GitHub Copilot app**.
- Use AI responsibly with employee data (what to share, what to never share, how to double-check).

## Agenda

| # | Module | What you do | Time |
|---|--------|-------------|------|
| 0 | [Setup and tour](modules/00-setup.md) | Open the workshop folder, find your way around Copilot | 20 min |
| 1 | [AI foundations](modules/01-ai-foundations.md) | Understand how AI works, and how to prompt it | 30 min |
| 2 | [Ask mode: documents and policies](modules/02-ask-mode.md) | Policy Q&A, summaries, inclusive job ads, review notes | 30 min |
| 3 | [Agent mode: let Copilot do the work](modules/03-agent-mode.md) | Clean a messy spreadsheet, write 26 welcome emails, undo mistakes | 35 min |
| | **Break** | | 10 min |
| 4 | [Dashboards](modules/04-dashboards.md) | Plan first, then build HR dashboards from CSV files | 60 min |
| 5 | [Teach Copilot your way of working](modules/05-customize-copilot.md) | Instructions, prompt files, agents, skills | 40 min |
| 6 | [The GitHub Copilot app](modules/06-copilot-app.md) | Parallel sessions, Plan / Autopilot, automations | 25 min |
| 7 | [Responsible AI and wrap-up](modules/07-responsible-ai-and-wrap-up.md) | Privacy, bias, habits, your Monday list | 20 min |

Keep [CHEAT-SHEET.md](CHEAT-SHEET.md) open all day. Unknown word? Check [GLOSSARY.md](GLOSSARY.md).

## What to install (prerequisites)

| Required | Why |
|----------|-----|
| A **GitHub account** with a **Copilot** licence | Copilot needs it to sign in |
| **[Visual Studio Code](https://code.visualstudio.com/)** | The editor where Copilot lives (think of it as "Word for files") |
| **GitHub Copilot** extension for VS Code | Installs together with Chat; sign in with your GitHub account |
| **[Git](https://git-scm.com/downloads)** | Gives you an "undo history" for everything Copilot changes |
| **GitHub Copilot app** (download link from your facilitator) | Used in Module 6 |
| Excel, Google Sheets or similar | To double-check Copilot's numbers |
| A web browser (Edge, Chrome, ...) | To open the dashboards you build |

Optional, nice to have: the **Live Preview** extension (Microsoft) in VS Code, which lets dashboards load the CSV automatically.

**You do NOT need:** Node.js, Python, Docker, a terminal, or any programming knowledge.

## Getting the workshop files

Your facilitator will give you a repository link (a template copy of this folder).

1. In VS Code press `Ctrl+Shift+P` (Mac: `Cmd+Shift+P`), type **Git: Clone**, paste the link and choose a folder.
2. Click **Open** when VS Code offers to open the cloned folder.

> **Important:** the folder you open in VS Code must be the workshop folder itself (the one that contains `data`, `docs` and `modules`). Copilot only reads your team's rules if that is the top-level folder.

## What is in the folder

| Folder / file | Purpose |
|---------------|---------|
| `modules/` | The step-by-step guides. Follow them in order. |
| `data/` | Practice data. **Fictional**: 240 employees of the made-up company "Brightwave Co." |
| `docs/` | Practice documents: policies, a job ad, review notes, a welcome-email template. All fictional. |
| `assets/` | A wireframe image and the chart library used by the dashboards |
| `output/` | **Everything Copilot creates for you goes here.** Starts empty. |
| `solutions/` | Reference answers. Peek only if you are stuck ([details](solutions/README.md)). |
| `_facilitator/` | For the person running the workshop. Participants: please don't open it, it contains the answers. |

## Four golden rules

1. **You are the author, Copilot is the assistant.** You are responsible for everything that goes out under your name.
2. **Never trust numbers you have not checked.** Always double-check in Excel. Every module shows you how.
3. **Be specific.** Say what you want, what it is for, what the result should look like, and what the rules are.
4. **Real employee data stays out unless your company allows it.** In this workshop everything is fictional, so you are safe. Module 7 explains the real-world rules.
