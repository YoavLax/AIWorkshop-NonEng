# Module 0: Setup and tour (20 min)

**Goal:** get everything working and learn where things are. No AI skills needed yet.

## 0.1 Check your tools (5 min)

You should have installed VS Code, Git, and your GitHub Copilot licence is active. Quick check:

- Open **VS Code**. In the left bar, click the **Extensions** icon (four squares) and confirm **GitHub Copilot** and **GitHub Copilot Chat** appear as installed (recent VS Code versions bundle them).
- Click the **account icon** at the bottom of the left bar. It should say you are signed in with GitHub. If not, choose **Sign in to use Copilot**.

## 0.2 Open the workshop folder (5 min)

1. `Ctrl+Shift+P` (Mac: `Cmd+Shift+P`) opens the **Command Palette**, the search box for everything in VS Code.
2. Type **Git: Clone**, paste the link your facilitator gave you, pick a location, then **Open**.
3. If VS Code asks "Do you trust the authors?", choose **Yes, I trust the authors** (it is your own copy).
4. In the left panel (**Explorer**) you should see `data`, `docs`, `modules`, `output`, ...

> **Check:** the Explorer's top line shows the workshop folder name, and `data` is directly under it. If you see a bigger folder containing `non-eng-workshop`, use **File > Open Folder** and pick the inner one.

## 0.3 Take the tour (10 min)

Find each of these. Tick them off.

- [ ] **Explorer** (left): your files. Click `data\employees.csv` to open it. It looks like a table. Don't change anything.
- [ ] **Chat panel**: open it with `Ctrl+Alt+I` (Mac: `Ctrl+Cmd+I`), or click the Copilot icon next to the search bar at the top. Copilot Chat is where you will spend most of today.
- [ ] **The mode picker** at the bottom of the chat box. Click it: you will see **Ask**, **Plan**, **Agent** (names can vary slightly by version). We use all three today:

| Mode | In one sentence | Changes your files? |
|------|-----------------|---------------------|
| **Ask** | Answers questions, explains, drafts text in the chat | No |
| **Plan** | Thinks through the steps and asks you questions before anything is done | No |
| **Agent** | Does multi-step work: creates and edits files, checks its own work | **Yes** (always visible and undoable) |

- [ ] **The model picker** (next to the mode). Different AI models have different strengths. Leave it on the default, unless your facilitator says otherwise.
- [ ] **Source Control** icon (left bar, a branching line). This is where Git shows what changed. You will use it in Module 3.

## 0.4 Say hello (warm-up)

Make sure the mode is **Ask**. Type:

```
In 3 bullets, explain what you can help me with as an HR professional, and one thing I should never ask you to do.
```

Read the answer. Is it sensible? Keep that critical eye on all day.

## Checkpoint

- [ ] Chat answers you.
- [ ] You can see the `data`, `docs` and `output` folders.
- [ ] You can switch between Ask, Plan and Agent.

## If something is stuck

| Problem | Fix |
|---------|-----|
| No chat icon | Update VS Code (Help > Check for Updates) and sign in with GitHub |
| "No access to Copilot" | Your licence is not assigned yet; tell the facilitator |
| Can't find Agent mode | Update VS Code; ask your facilitator whether your organisation has switched it off |
| Clone fails | Check you are signed in to GitHub in VS Code and have access to the repository |
