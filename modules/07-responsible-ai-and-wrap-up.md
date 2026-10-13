# Module 7: Responsible AI and wrap-up (20 min)

**Goal:** leave with safe habits, a clear picture of what to share and what to never share, and a concrete plan for Monday morning.

## 7.1 The data traffic light (5 min)

Before you paste or attach anything, ask: *"What is in it, and where does it go?"*

| 🟢 Green: OK | 🟡 Amber: only with approved setup | 🔴 Red: don't |
|--------------|-----------------------------------|---------------|
| Public text (job ads, public policies) | Employee lists without sensitive fields | Health, medical or disability information |
| Templates, drafts without names | Anonymous or aggregated survey results | Individual salary or performance ratings in an unapproved tool |
| Fictional or sample data (like today) | Internal policies (follow company rules) | Passwords, API keys, ID numbers, bank details |
| Your own questions about how to do things | Documents with names but no sensitive content | Disciplinary / investigation / legal case details outside approved systems |

Rules of thumb:

- **Ask your IT/security/legal team which Copilot setup is approved** for employee data. Business and Enterprise plans typically have different data terms than personal accounts.
- **Minimise**: remove names and IDs when you don't need them. Ask for patterns, not people.
- **Aggregate**: share counts and averages, not rows. Suppress groups under 5.
- **Local where possible**: the dashboards in Module 4 read the CSV in your browser; the data never gets embedded in the page. But if you **attach** the CSV to a chat, the content goes to the AI service. Know which you are doing.

## 7.2 Five habits of a responsible AI user

1. **Verify**: check numbers in Excel, quotes in the source, names and dates against the original.
2. **Cite**: ask for the source file and section, and keep it.
3. **Disclose**: where your company expects it, say AI helped draft.
4. **Keep a human decision-maker**: AI drafts and analyses; people decide about people.
5. **Check for bias**: ask "is there anything in this that could disadvantage a group?" *and* read it yourself.

## 7.3 Spot the risk (8 min, in pairs)

Discuss each scenario: what is the risk, and what would you do instead?

1. A recruiter pastes 50 CVs into a chat and asks "rank these candidates".
2. A manager asks Copilot: "Given Jamie's last year, should we promote or let them go?"
3. An analyst shares an engagement dashboard with every department, including one with 3 respondents.
4. Someone sends 26 AI-written welcome emails without opening them; two have the wrong start date.
5. A colleague asks Copilot to "summarise this investigation file" with all names in it.
6. A dashboard shows verbatim survey comments, one of which includes a person's phone number.

<details>
<summary>Suggested answers (try first!)</summary>

1. Ranking people with AI risks bias and may be unlawful in some places; it also exposes personal data. Use AI to *structure* criteria or summarise against clear job requirements, with a human review and approved tools.
2. A decision about a named individual must be human-made. Ask Copilot to organise the *facts* and the policy process instead.
3. Groups under 5 can identify individuals. Merge or hide; check the dashboard's minimum group size.
4. Always check AI output before sending. Verify dates, names and the `[TODO]` markers.
5. Highly sensitive; use only approved systems with proper access control. Not a general chat.
6. Redact personal details before sharing, or don't show comments. The privacy rules in `copilot-instructions.md` exist for exactly this, but remember they are guidance, not a lock.
</details>

## 7.4 Build your Monday list (5 min)

Write down (a sheet of paper or a note is fine):

| My task | Which Copilot feature? (Ask / Agent / prompt file / agent / skill / automation) | First prompt I will try |
|---------|--------------------------------------------------------------|-------------------------|
| | | |
| | | |
| | | |

Tip: choose tasks that are **repetitive, text- or table-heavy, and low risk**. Use the CHEAT-SHEET to get started.

## 7.5 Bring your own task (optional, 5 min)

Take one item from your Monday list (with fictional or anonymised data) and try it right now. Share one lesson with the group: *what worked, and what did you need to check?*

## 7.6 What we covered

| Concept | One-liner |
|---------|-----------|
| AI is a prediction engine | Brilliant at language, confident when wrong, knows nothing about your company unless you provide it |
| Prompt formula | Goal / Context / Format / Rules |
| Ask / Plan / Agent | Answers / plans / does |
| Build the calculator | Let AI build the tool, verify the numbers |
| Instructions, prompt files, agents, skills | Handbook, templates, specialists, playbooks |
| Copilot app | Parallel, isolated sessions; Plan / Autopilot; automations |
| Responsible AI | Traffic light, verify, human decides |

## Feedback

Please answer these three questions for your facilitator:

1. What is the one thing you'll use next week?
2. What was confusing or too fast?
3. What should we add for your team?

Thank you! 🎉
