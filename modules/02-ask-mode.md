# Module 2: Ask mode, documents and policies (30 min)

**Goal:** use Copilot as a reading and writing assistant on documents, and learn to make it **cite its sources** and **admit when it doesn't know**. Mode: **Ask**.

You will work with the fictional policies in `docs/`.

## 2.1 Policy Q&A with sources (10 min)

Open a new chat (Ask mode). The context tip: attach files with `#`, or attach a whole folder.

```
Using ONLY the files in #folder:docs, answer: how many weeks of paid parental leave do employees get, and who is eligible?

Rules:
- Quote the exact sentence you rely on and name the file and section.
- If two documents disagree, show both and tell me they conflict.
- If the answer is not in the documents, say "I can't find this in our policies."
```

Now compare with Module 1 test A. Same question, much better answer, because it now has **context** and **rules**.

Try these one at a time and check each answer against the source document (open the file and find the sentence):

1. How many PTO days does an employee with 5 years of service get?
2. How many days per year can someone work from abroad?
3. What is the learning budget, and what happens if I leave the company shortly after using it?
4. Do we reimburse gym memberships?

> **Spot the traps.** Question 2 touches a deliberate conflict between two policies. Question 4 is not covered by any document. A good answer says so. If Copilot invents a gym policy, you have just seen a hallucination in the wild.

**Discuss:** which behaviour from the prompt rules (quote, flag conflicts, admit unknowns) made the biggest difference?

## 2.2 Summaries for different audiences (5 min)

```
Summarise #file:docs/remote-work-policy.md twice:
1) For employees: 5 bullets, friendly tone, with the three things they must do.
2) For managers: 5 bullets, focused on what they must approve and what to watch for.
Do not add anything that is not in the policy.
```

Notice how the same source becomes two different messages.

## 2.3 Make a job ad more inclusive (8 min)

Open `docs/job-description-draft.md` (it is a deliberately bad job ad). Then:

```
Review #file:docs/job-description-draft.md for inclusive language.
1) List every phrase that could discourage qualified candidates (gendered, age-related, culture-fit, unnecessary requirements), and say why.
2) Then rewrite the ad: same role, welcoming tone, skills-based requirements, under 300 words.
3) List the information that is missing and should be added (for example pay range).
```

Did it find the "rockstar", the age hints, the unrealistic experience requirement? Did it miss any? **You are the final reviewer.**

## 2.4 Performance review notes: a careful use case (7 min)

Open `docs/performance-review-notes.md` (fictional manager notes about "Jamie Rivera"). Try:

```
Turn #file:docs/performance-review-notes.md into a balanced, fact-based performance review summary.
Rules:
- Use only facts and examples that appear in the notes. Do not invent achievements.
- Flag any wording that sounds biased, vague, or personal rather than about work.
- Flag anything that should NOT be part of a performance review (for example health or leave).
- Do not recommend a rating, promotion or pay decision.
```

This is a good example of **AI as an editor and a second pair of eyes**, not as a decision-maker.

## Tips that came out of this module

- Attach **files and folders** with `#file:` / `#folder:` instead of pasting text.
- Ask for **citations** and a **"say so if you can't find it"** rule whenever you rely on documents.
- Have it **list its assumptions**: "What did you assume?"
- Use it to **review for bias**, but a human decides.

## Checkpoint

- [ ] You got cited answers to 4 policy questions and found the conflict.
- [ ] The gym question was answered with "I can't find this" (or you noticed it was invented).
- [ ] You produced an inclusive rewrite of the job ad.

## Stretch ideas

- Draft an FAQ for new joiners from all the policies (with source references).
- Ask for a table comparing PTO, remote and learning rules for managers.
- Ask it to write 5 quiz questions with answers from the parental leave policy.
