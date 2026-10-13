---
description: Answer a policy question using ONLY the policy documents in the docs folder, with citations.
agent: ask
---
Answer this question using ONLY the policy documents in the `docs/` folder:

${input:question:Type your policy question, for example "How long is parental leave?"}

Rules:
1. Quote the exact sentence you rely on and name the file and section.
2. If two documents disagree, show both and tell me they conflict. Do not pick one silently.
3. If the answer is not in the documents, reply exactly: "I can't find this in our policies." and suggest who to ask.
4. Finish with a one-line plain-language summary I could paste into an email.
