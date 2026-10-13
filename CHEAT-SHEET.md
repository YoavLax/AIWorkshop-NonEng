# Cheat sheet

## The prompt formula

| | |
|-|-|
| **Goal** | What do I want? |
| **Context** | Who is it for? Which files? (`#file:docs/...`) |
| **Format** | Bullets? Table? Word limit? File name? |
| **Rules** | Use only these documents. Don't invent. Say "I can't find that" when unsure. |

For agents add: **INPUTS / OUTPUT / WHEN UNSURE** (what to do instead of guessing).

## Three modes

| Mode | Use it to | Touches files? |
|------|-----------|----------------|
| **Ask** | Question, explain, draft, review | No |
| **Plan** | Think first; Copilot asks you questions and proposes steps | No |
| **Agent** | Create and edit files, multi-step jobs | Yes |

## Shortcuts

| Do this | How |
|---------|-----|
| Open chat | `Ctrl+Alt+I` (Mac `Ctrl+Cmd+I`) |
| Command Palette | `Ctrl+Shift+P` (Mac `Cmd+Shift+P`) |
| Attach a file / folder | type `#file:` / `#folder:` and pick, or drag it into the chat |
| Run a saved prompt | type `/` then the name (e.g. `/policy-question`) |
| Pick a specialist agent | mode picker at the bottom of the chat |
| New topic? | **New chat** (the `+` icon) |

## Three levels of undo

1. **In chat**: Undo / Discard the last change.
2. **Source Control panel**: view each file's changes, discard any.
3. **Commit** after good work. A commit is a save point you can return to.

## Verify checklist (before you share anything)

- [ ] Numbers checked in Excel: at least 3.
- [ ] Definitions written down (what counts as "active", "overdue", "attrition").
- [ ] Quotes and names checked against the source.
- [ ] Dates and weekdays spot-checked.
- [ ] No groups under 5 people, no personal data, no comments with names.
- [ ] A human made the decision.

## Fix-it phrases

| Situation | Say |
|-----------|-----|
| Answer sounds too sure | "What did you assume? What is not in the documents?" |
| Wrong number | "I expected X, you show Y. Explain the difference and fix it." |
| Too long | "Shorter, 5 bullets." |
| Invented something | "Use only #file:... If it is not there, say so." |
| Agent wants to install things | "Don't install or run anything. Create the files directly." |
| Page is blank | "It shows nothing after I choose the CSV. Debug it and tell me what you changed." |

## Which customisation?

| Need | Use |
|------|-----|
| Rules for everything | **Instructions** (`.github/copilot-instructions.md`) |
| Reusable prompt with blanks | **Prompt file** (`.github/prompts/*.prompt.md`) |
| A role / specialist | **Agent** (`.github/agents/*.agent.md`) |
| Multi-step playbook with files | **Skill** (`.github/skills/<name>/SKILL.md`) |

## Data traffic light

🟢 public / fictional / templates · 🟡 anonymised or aggregated, approved tools only · 🔴 health, individual pay or ratings, investigations, IDs, passwords.

**When in doubt: don't paste it. Ask first.**
