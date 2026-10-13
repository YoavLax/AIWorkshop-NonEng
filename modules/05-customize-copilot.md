# Module 5: Teach Copilot your way of working (40 min)

**Goal:** stop repeating yourself. You will create your team's "house rules" once and reuse them for every task.

In Module 4 every dashboard looked different, and Copilot kept needing reminders about privacy and definitions. Now we fix that.

## 5.1 The four building blocks (5 min)

| Building block | Plain-language analogy | What it is | Used |
|----------------|------------------------|------------|------|
| **Custom instructions** | The **employee handbook** for your AI | A text file with rules that apply to *every* chat | Automatically, always |
| **Prompt files** | **Saved templates** / email templates | A reusable prompt with blanks to fill in | When you type `/` and the name |
| **Custom agents** | A **specialist colleague** with a job description | A persona with its own rules and way of working (e.g. "Inclusive Writing Coach") | When you pick it from the mode list |
| **Skills** | A **training playbook** with templates and checklists | A folder with step-by-step know-how (and files like a dashboard template) | Copilot loads it by itself when your request matches |

**Which one when?**

| I want to... | Use |
|--------------|-----|
| Always follow privacy rules, tone, definitions | **Instructions** |
| Run the same request often, with different input (e.g. a policy question) | **Prompt file** |
| Have a "role" with a distinct approach (e.g. reviewer, analyst) | **Agent** |
| Repeat a *multi-step* job with templates and a quality checklist (e.g. build a branded dashboard) | **Skill** |

Important: **instructions guide the AI, they don't lock it.** They are not a security control. Don't rely on them to protect real confidential data.

All of these are plain text files (Markdown) in a hidden folder called **`.github`** in your workshop folder. You don't have to write them by hand, Copilot will help.

## 5.2 Create your house rules: instructions (10 min)

Switch to **Agent** mode and send:

```
Create a file .github/copilot-instructions.md with house rules for a People & Culture team. Audience: HR colleagues who are not programmers.

Include these sections:
1. How to communicate: plain language, no jargon, short answers, say where the result file is.
2. Privacy: treat everything in data/ as confidential; never show individual salaries, ratings or exit comments unless asked; never show groups of fewer than 5 people; replace names/emails/phones in comments with [redacted]; never send data anywhere else.
3. Accuracy: never invent facts or policy rules; cite the file and section; say "I can't find that" when unsure; state metric definitions; finish analyses with a "how to double-check" line; flag messy or ambiguous data.
4. People decisions: do not recommend hiring/firing/promotion/pay decisions about named individuals; use inclusive language.
5. Dashboards: save in output/ as a single HTML file; never modify data/ or docs/.
Keep it under 40 lines.
```

> Compare with `solutions/customization/copilot-instructions.md` only after you have read yours.

**Test it.** Open a **new** chat in Ask mode and ask:

```
Show me the 10 highest paid employees in #file:data/employees.csv with their names and salaries.
```

Copilot should now push back or ask for your reason (instructions: *never show individual salaries unless explicitly asked*). Try also: *"Show me engagement scores by department"* using `engagement_survey.csv`, and see whether the Legal team (3 responses) is hidden or merged.

## 5.3 Save a template: a prompt file (7 min)

In Agent mode:

```
Create a prompt file .github/prompts/policy-question.prompt.md. It should let me type a policy question, then answer it using ONLY the documents in docs/, quote the exact sentence with file and section, show both versions if two documents conflict, reply exactly "I can't find this in our policies." if it is not covered, and end with a one-line summary I could paste into an email. Use ask mode and an input variable for the question.
```

**Use it:** in the chat box type `/` and pick **policy-question**. Ask: *"Do we reimburse gym memberships?"* Then try the parental-leave question. This is a **one-click Module 2**.

## 5.4 Hire a specialist: a custom agent (8 min)

```
Create a custom agent .github/agents/inclusive-writing-coach.agent.md.
Role: reviews job ads, announcements and policies for inclusive, bias-free language.
How it works: lists problematic phrases with the reason, offers a better wording for each, rewrites the whole text, then lists what is missing (e.g. pay range). It never changes the meaning. It explains, in plain language, why each change matters.
Keep it under 40 lines.
```

Open the mode picker in the chat. You should see **inclusive-writing-coach**. (If it doesn't appear: open the Command Palette and run **Developer: Reload Window**.) Select it and send:

```
Review #file:docs/job-description-draft.md
```

Compare with your result in Module 2.3. Is it faster and more consistent?

## 5.5 Install a skill: the dashboard builder (7 min)

A skill is more than a prompt: a folder with instructions *and* files. We prepared one for you with the Brightwave dashboard look and privacy rules. It sits in `solutions/customization/skills/hr-dashboard-builder`.

Ask the agent to install it:

```
Copy the folder solutions/customization/skills/hr-dashboard-builder to .github/skills/hr-dashboard-builder, keeping its files unchanged. Then summarise in 3 bullets what the skill does, by reading its SKILL.md.
```

Now repeat a dashboard, in a **new Agent chat**:

```
Build a dashboard from #file:data/training_completion.csv showing overdue compliance training by course and department. As-of date 2026-09-30.
```

Don't mention styles, privacy or file locations. Watch the chat: Copilot should mention it is using the **hr-dashboard-builder** skill. The result should have the same navy/teal look as the template and the same footer, with your instructions applied.

> **Before/after:** open your Module 4 dashboard next to this one. Which one would you show your boss?

If the skill is not picked up: check that the folder exists at `.github/skills/hr-dashboard-builder/SKILL.md`, and make sure skills are enabled in VS Code settings (search for "skills" in Settings, or ask your facilitator).

## 5.6 Commit and share (3 min)

Commit `.github` (Source Control > message > Commit). Because these rules are **files in the folder**, any teammate who clones this repository gets the same behaviour. That is how a team shares know-how, rather than each person re-inventing prompts.

## Checkpoint

- [ ] `.github/copilot-instructions.md` exists and Copilot followed a rule from it.
- [ ] `/policy-question` works.
- [ ] You can pick **inclusive-writing-coach** from the mode list.
- [ ] A new dashboard used the **hr-dashboard-builder** skill and looks consistent.

## Discuss

- Which repeated task in your job deserves a prompt file? An agent? A skill?
- What rule would your team want in the "handbook"?

## Stretch

- Ask Copilot to create a prompt file `/weekly-people-snapshot` that builds a one-page summary from a CSV.
- Edit the instructions to add your own company tone ("friendly but concise"), and see the difference.
