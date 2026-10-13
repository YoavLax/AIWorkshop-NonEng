# Module 6: The GitHub Copilot app (25 min)

**Goal:** go from "one chat at a time in an editor" to **several tasks running side by side**, each safely separated, with a visual way to review the results.

> The app is updated often. Button names in this guide may differ slightly from what you see; look for the closest match, and ask your facilitator if you're stuck.

## 6.1 Why a separate app? (3 min)

VS Code is an editor with Copilot inside. The **GitHub Copilot app** is built around **work sessions**:

| Concept | Plain meaning |
|---------|---------------|
| **Project** | Your workshop folder / repository, added to the app |
| **Session** | One task with its own chat. Think of it as one "assignment" handed to a colleague |
| **Isolated copy** | Each session works on its **own copy** of the files (a Git "worktree"/branch). Two sessions can't overwrite each other, and your main folder is untouched until you accept the result |
| **Modes** | **Plan** (think and ask first), **Interactive** (works with you, asks before key steps), **Autopilot** (works through the whole task by itself) |
| **Review** | A change viewer that shows exactly what files were added or changed, so you can accept or reject |
| **Automations** | Tasks that run on a schedule (e.g. every Monday) |

Everything you learned already applies: prompts (Goal / Context / Format / Rules), verification, privacy.

## 6.2 Open your project (3 min)

1. Open the **GitHub Copilot app** and sign in with GitHub.
2. **Add a project** and pick the workshop repository (the folder you cloned). The app remembers it.
3. Look around: project list, sessions list, chat area, and the changes/review area.

## 6.3 Two tasks at the same time (10 min)

Create **two new sessions** in your project. Give them clear names.

> Each session starts from your **committed** files. That's why we committed `.github` (your rules and skill) in Module 5. If a session doesn't seem to know your house rules, go back to VS Code and commit first.

**Session 1, "Attrition dashboard"** (mode: **Plan**, then approve and let it run)

```
Plan and build an attrition dashboard from data/employees.csv and data/exit_interviews.csv: attrition rate for the last 12 months (as-of date 2026-09-30), leavers by department, exit reasons, tenure at exit. Save it as output/attrition-dashboard.html. Use the hr-dashboard-builder skill and follow the house rules.
```

Read the plan. Approve it when it makes sense.

**Session 2, "New joiner FAQ"** (mode: **Autopilot**)

```
Read all policies in docs/ and create output/new-joiner-faq.md: 15 questions and answers for new joiners, each with the file and section it comes from. If something isn't covered by the policies, list it at the end under "Not covered yet". Do not invent anything.
```

Watch both sessions work at the same time. While waiting, notice how the app tells you when a session needs your input.

### Review and accept

When a session finishes:

1. Open its **changes / review** view. You will see the new files. Read the FAQ: pick 3 answers and check them against the policy.
2. Open the dashboard HTML in your browser, load the CSVs (**both** files together), and compare the attrition rate with your Excel check (expected: roughly 14.8%).
3. Happy? **Keep / merge** the result into your main folder. Not happy? Tell the session what to fix or discard it. Nothing was lost.

> **Autopilot** is great for well-defined tasks with clear rules. **Plan** or **Interactive** is better when the task is new or the stakes are higher. You decide how much autonomy to give.

## 6.4 Automations: your recurring tasks (4 min)

An **automation** runs a prompt on a schedule, such as every Monday morning.

Create one (**Automations** area of the app):

- **Name:** Weekly people snapshot
- **Schedule:** weekly, Monday 8:00 (for the workshop, you can set "manual" and press **Run now**)
- **Prompt:**

```
Create output/weekly-people-snapshot.md: a one-page summary of headcount, new hires in the last 30 days and leavers in the last 30 days (as-of date 2026-09-30) from data/employees.csv. Define each number. End with a "How to double-check" line. Do not show individual salaries.
```

Run it once and check the result. In real life, the automation would run on your latest export.

## 6.5 Optional: hand work to the cloud (2 min, demo)

If your organisation allows it, the app can send a task described in a GitHub **issue** to a **cloud agent**: it works on GitHub without using your laptop, and comes back with a **pull request** (a "proposed change" to review and approve). Your facilitator may demo this. You do not need it today.

## Checkpoint

- [ ] You ran two sessions at the same time.
- [ ] You reviewed the changes before accepting them.
- [ ] You know the difference between Plan, Interactive and Autopilot.
- [ ] You created or saw an automation.

## Discuss

- Which tasks in your role could safely run in Autopilot? Which should always be Plan/Interactive first?
- What would you want to review before sending anything created by Copilot to your team?
