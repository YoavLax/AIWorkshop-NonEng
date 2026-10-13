# Module 1: AI foundations (30 min)

**Goal:** understand just enough about how AI works to use it well and to spot when it is wrong. Mode: **Ask**.

## 1.1 The 5-minute mental model

Copilot is powered by a **large language model (LLM)**. Think of it as a very well-read colleague who:

- has read a huge amount of text and is excellent at **writing, summarising, rephrasing, structuring, and spotting patterns**,
- **predicts the most likely helpful answer**. It does not "look things up" or "know" things the way a database does,
- is **confident even when it is wrong**. Wrong answers sound just as polished as right ones,
- knows **nothing about your company** unless you give it your files (this is called **context**),
- **forgets** everything between chats, unless you save instructions (Module 5).

| AI is great at | AI is risky at |
|----------------|----------------|
| Drafting and rewriting text | Facts about *your* company that you did not provide |
| Summarising long documents | Exact arithmetic on big tables (it may "eyeball" it) |
| Cleaning and reformatting data | Anything legal, medical, or a decision about a person |
| Explaining and brainstorming | Dates, weekdays, names and numbers (always verify) |
| Building tools that do the maths (formulas, dashboards) | Knowing what is confidential |

**Hallucination** = the AI invents something plausible that is not true (a policy that does not exist, a made-up statistic). It is the number one thing to watch for.

**Key idea for today:** *Have AI build the calculator. Don't make AI be the calculator.* We let Copilot create a spreadsheet formula or a dashboard that computes numbers reliably, and we check the result.

## 1.2 Where Copilot is smarter: agents and tools

A plain chatbot only talks. Copilot in VS Code can also **act**:

| Term | Plain meaning |
|------|---------------|
| **Chat / Ask** | Conversation. You get text back. |
| **Agent** | An AI that can *do* steps: read your files, create files, fix its own mistakes, and tell you what it did. |
| **Tools** | The things an agent is allowed to use (read a file, create a file, search the workspace...). You approve sensitive ones. |
| **Context** | What the AI can see right now: your message, the files you attached, your saved instructions. |
| **Instructions / skills / prompt files** | Saved know-how you give the AI once (Module 5). |
| **MCP** | A "plug" that connects Copilot to other systems like Jira or an HR system. We only mention it; you don't need it today. |

## 1.3 Exercise: see the weaknesses with your own eyes (10 min)

Open a **new chat** each time (the **+** icon at the top of the chat panel). Mode: **Ask**.

**A. Hallucination test.** Type:

```
How many weeks of paid parental leave does Brightwave Co. give?
```

Copilot has never seen your documents in this chat. Does it say "I don't know", or does it invent a number? Whatever it says, **notice how confident it sounds.** (In Module 2 you will give it the real policy.)

**B. The calculator test.** Type:

```
Look at #file:data/employees.csv. How many active employees do we have, and what is their average salary?
```

(Typing `#` lets you attach a file. Pick `employees.csv`.) The answer may or may not be right. Check it: open the CSV in Excel, filter where `termination_date` is empty, and count. Does it match? Remember: some AI answers about big tables are guesses.

**C. Vague vs. specific.** In a new chat type:

```
Write a job ad.
```

Then in another new chat:

```
Write a job ad for a Customer Support Specialist at Brightwave Co., a 240-person software company. Audience: career changers with 1-2 years of customer-facing experience. Format: short intro paragraph, 5 bullet responsibilities, 5 bullet requirements, one inclusive closing sentence. Rules: friendly tone, no jargon, under 250 words, no gendered words.
```

Compare. Same AI, very different result. The difference is **you**.

## 1.4 The prompt formula: Goal / Context / Format / Rules

| Part | Question it answers | Example |
|------|---------------------|---------|
| **Goal** | What do I want done? | "Summarise the attached policy" |
| **Context** | Who is it for? What is it based on? | "for new managers; use only `#file:docs/remote-work-policy.md`" |
| **Format** | What should the result look like? | "5 bullets and a one-line takeaway" |
| **Rules** | What must it do or avoid? | "Don't invent anything; say 'not in the policy' if unsure" |

Tips:

- **Talk to it like a smart new colleague** who has never worked here.
- **Iterate.** Your first message does not have to be perfect. Follow up with "shorter", "more formal", "use a table", "what did you assume?".
- **Ask it to ask you.** Add "If anything is unclear, ask me up to 3 questions first."
- **Start a new chat for a new topic.** Long, mixed chats confuse it.

## 1.5 Exercise: your own prompt (10 min)

Think of a real writing task from your week (a policy explanation, a candidate rejection email, an announcement). Use **no real names or confidential data**. Write it with Goal / Context / Format / Rules and run it. Then improve it with **two** follow-up messages. Share the best result with your neighbour.

## Checkpoint

- [ ] You can name two things AI is good at and two it is risky at.
- [ ] You saw it answer confidently without any source (test A).
- [ ] You can write a prompt with Goal / Context / Format / Rules.

## Discussion

- Where in your job would a confident-but-wrong answer be most expensive?
- What is the "calculator" equivalent in your daily work (the thing you would not trust AI to do in its head)?
