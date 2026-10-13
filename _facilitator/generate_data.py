"""
Generates the SYNTHETIC "Brightwave Co." HR data used in the workshop, plus the
facilitator answer key (_facilitator/answer-key.md).

Everything here is fictional. The script is seeded, so re-running it always
produces identical files and an answer key that matches them.

Usage (facilitators only - participants never need Python):
    python _facilitator/generate_data.py
"""
import csv
import datetime as dt
import pathlib
import random
import statistics
from collections import Counter, defaultdict

SEED = 2026
rng = random.Random(SEED)
ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
AS_OF = dt.date(2026, 9, 30)  # "today" inside the fictional company
WINDOW_START = dt.date(2025, 10, 1)  # 12-month attrition window
DOMAIN = "brightwave.example"

FEMALE = ["Olivia", "Priya", "Maria", "Aisha", "Chen", "Sofia", "Emily", "Hannah", "Fatima", "Yuki",
          "Grace", "Lena", "Amara", "Isabella", "Nora", "Zoe", "Mei", "Camila", "Ruth", "Elena",
          "Samira", "Julia", "Tessa", "Ingrid", "Leila", "Naomi", "Rosa", "Anika", "Bianca", "Claire"]
MALE = ["Liam", "Arjun", "Carlos", "Omar", "Wei", "Lucas", "Daniel", "Noah", "Ibrahim", "Kenji",
        "Samuel", "Felix", "Kwame", "Mateo", "Ethan", "Marco", "Tariq", "Oscar", "Raj", "Viktor",
        "Andre", "Ben", "Diego", "Hugo", "Jonas", "Kofi", "Leo", "Nikolai", "Paul", "Ravi"]
NONBINARY = ["Alex", "Jordan", "Taylor", "Riley", "Casey", "Morgan"]
LAST = ["Nguyen", "Patel", "Garcia", "Kim", "Johnson", "Okafor", "Silva", "Rossi", "Mueller", "Haddad",
        "Brown", "Tanaka", "Lopez", "Singh", "Cohen", "Murphy", "Ivanov", "Santos", "Wright", "Adeyemi",
        "Chen", "Khan", "Dubois", "Novak", "Larsen", "Costa", "Fischer", "Reyes", "Bennett", "Sato",
        "Hughes", "Moreau", "Kowalski", "Mehta", "Ortiz", "Walker", "Yilmaz", "Andersson", "Romero", "Park",
        "Cooper", "Zhang", "Bianchi", "Okoye", "Hassan", "Foster", "Lindqvist", "Vargas", "Shah", "Turner"]

DEPTS = {
    # name: (rows, base L1 salary, attrition prob, IC titles, manager title, director title)
    "Engineering": (62, 85000, 0.09, ["Software Engineer", "QA Engineer", "DevOps Engineer", "Data Engineer"],
                    "Engineering Manager", "Director of Engineering"),
    "Sales": (46, 62000, 0.18, ["Account Executive", "Sales Development Rep", "Solutions Consultant"],
              "Sales Manager", "Director of Sales"),
    "Customer Support": (38, 48000, 0.22, ["Support Specialist", "Customer Success Manager"],
                         "Support Team Lead", "Director of Customer Support"),
    "Marketing": (22, 60000, 0.12, ["Marketing Specialist", "Content Strategist", "Designer"],
                  "Marketing Manager", "Director of Marketing"),
    "Product": (16, 85000, 0.08, ["Product Manager", "Product Designer", "UX Researcher"],
                "Group Product Manager", "Director of Product"),
    "Finance": (14, 65000, 0.05, ["Accountant", "Financial Analyst", "Payroll Specialist"],
                "Finance Manager", "Director of Finance"),
    "People & Culture": (12, 60000, 0.08, ["HR Business Partner", "Recruiter", "People Operations Specialist",
                                           "Compensation Analyst", "Learning Specialist"],
                         "People Manager", "Director of People & Culture"),
    "Operations": (22, 52000, 0.12, ["Operations Analyst", "Facilities Coordinator", "Procurement Specialist",
                                     "IT Support Specialist"],
                   "Operations Manager", "Director of Operations"),
    "Legal": (8, 80000, 0.0, ["Counsel", "Paralegal", "Compliance Specialist"],
              "Legal Manager", "General Counsel"),
}
LEVELS = ["L1", "L2", "L3", "L4", "L5", "M1", "M2"]
LEVEL_MULT = {"L1": 1.0, "L2": 1.18, "L3": 1.4, "L4": 1.68, "L5": 2.0, "M1": 1.75, "M2": 2.4}
LEVEL_PREFIX = {"L3": "Senior ", "L4": "Lead ", "L5": "Principal "}
LOCATIONS = ["New York", "Austin", "London", "Toronto", "Berlin"]
LOC_W = [30, 22, 20, 15, 13]


def wchoice(items, weights):
    return rng.choices(items, weights=weights, k=1)[0]


def d_iso(d):
    return d.isoformat() if d else ""


def write_csv(name, header, rows):
    # utf-8-sig so Excel opens the files correctly
    with open(DATA / name, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


# --------------------------------------------------------------------------- employees
used_names = set()


def new_person():
    g = wchoice(["Female", "Male", "Non-binary"], [47, 50, 3])
    pool = {"Female": FEMALE, "Male": MALE, "Non-binary": NONBINARY}[g]
    while True:
        first, last = rng.choice(pool), rng.choice(LAST)
        if (first, last) not in used_names:
            used_names.add((first, last))
            return g, first, last


employees = []
for dept, (n, base, attr_p, ic_titles, mgr_title, dir_title) in DEPTS.items():
    for i in range(n):
        g, first, last = new_person()
        # level mix; women are a little under-represented at the top in Engineering and Sales
        w = [26, 30, 24, 10, 2, 6, 2]
        if dept in ("Engineering", "Sales") and g == "Female":
            w = [30, 34, 22, 7, 1, 5, 1]
        if dept == "Legal":
            w = [20, 30, 25, 10, 0, 10, 5]
        level = wchoice(LEVELS, w)
        if i == 0:
            level = "M2"  # guarantee a leader per department
        elif i == 1:
            level = "M1"
        if level == "M2":
            title = dir_title
        elif level == "M1":
            title = mgr_title
        else:
            title = LEVEL_PREFIX.get(level, "") + rng.choice(ic_titles)
        tenure_days = min(int(rng.expovariate(1 / 900)) + 5, 4000)
        hire = AS_OF - dt.timedelta(days=tenure_days)
        salary = base * LEVEL_MULT[level] * rng.uniform(0.94, 1.06)
        if dept in ("Engineering", "Sales") and g == "Female":
            salary *= 0.96  # small unexplained gap, discoverable in the pay-equity challenge
        loc = wchoice(LOCATIONS, LOC_W)
        model = wchoice(["Onsite", "Hybrid", "Remote"], [15, 60, 25])
        etype = wchoice(["Full-time", "Part-time", "Contractor"], [90, 4, 6])
        rating = ""
        if hire < dt.date(2026, 1, 1):
            rating = wchoice([1, 2, 3, 4, 5], [4, 14, 46, 26, 10])
        employees.append(dict(
            first=first, last=last, gender=g, dept=dept, title=title, level=level, location=loc,
            model=model, etype=etype, hire=hire, salary=int(round(salary / 500.0) * 500), rating=rating,
            term=None, attr_p=attr_p))

# terminations (12-month window)
for e in employees:
    p = e["attr_p"] * (1.6 if (AS_OF - e["hire"]).days < 365 else 1.0)
    if e["level"] in ("M2",):
        p = 0
    if rng.random() < p and (AS_OF - e["hire"]).days > 75:
        earliest = max(WINDOW_START, e["hire"] + dt.timedelta(days=45))
        span = (AS_OF - earliest).days
        if span > 0:
            e["term"] = earliest + dt.timedelta(days=rng.randint(0, span))

employees.sort(key=lambda e: (e["hire"], e["last"]))
for i, e in enumerate(employees):
    e["id"] = f"E{1001 + i}"
    e["email"] = f"{e['first']}.{e['last']}@{DOMAIN}".lower()

# managers (always active people from the same department)
active_by_dept = defaultdict(list)
for e in employees:
    if not e["term"]:
        active_by_dept[e["dept"]].append(e)
for e in employees:
    pool_m1 = [m for m in active_by_dept[e["dept"]] if m["level"] == "M1" and m["id"] != e["id"]]
    pool_m2 = [m for m in active_by_dept[e["dept"]] if m["level"] == "M2" and m["id"] != e["id"]]
    if e["level"] == "M2":
        e["manager"] = ""
    elif e["level"] == "M1":
        e["manager"] = rng.choice(pool_m2)["id"] if pool_m2 else ""
    else:
        pool = pool_m1 or pool_m2
        e["manager"] = rng.choice(pool)["id"] if pool else ""

emp_header = ["employee_id", "first_name", "last_name", "email", "department", "job_title", "level",
              "manager_id", "location", "work_model", "employment_type", "hire_date", "termination_date",
              "gender", "salary_usd", "last_performance_rating"]
write_csv("employees.csv", emp_header, [
    [e["id"], e["first"], e["last"], e["email"], e["dept"], e["title"], e["level"], e["manager"],
     e["location"], e["model"], e["etype"], d_iso(e["hire"]), d_iso(e["term"]), e["gender"], e["salary"],
     e["rating"]] for e in employees])
active = [e for e in employees if not e["term"]]
leavers = [e for e in employees if e["term"]]

# --------------------------------------------------------------------------- exit interviews
VOL_REASONS = {
    "Customer Support": (["Compensation", "Work-life balance", "Career growth", "Manager relationship", "Better external opportunity", "Relocation"], [28, 26, 16, 14, 10, 6]),
    "Sales": (["Compensation", "Career growth", "Better external opportunity", "Manager relationship", "Work-life balance", "Relocation"], [26, 24, 22, 12, 10, 6]),
    "default": (["Career growth", "Better external opportunity", "Compensation", "Work-life balance", "Relocation", "Manager relationship", "Return to school", "Retirement"], [26, 24, 16, 12, 8, 8, 3, 3]),
}
INVOL_REASONS = (["Performance", "Role eliminated", "Conduct"], [55, 30, 15])
EXIT_COMMENTS = {
    "Compensation": ["Offered a significantly higher salary elsewhere.", "Pay did not keep up with the market or my responsibilities.", "Compensation review kept getting postponed."],
    "Career growth": ["No clear path to the next level.", "I wanted more responsibility than my role allowed.", "Promotion criteria were never explained."],
    "Work-life balance": ["Workload was unsustainable for too long.", "Constant after-hours requests wore me down.", "I need a more predictable schedule."],
    "Manager relationship": ["Did not feel supported by my manager.", "Feedback was rare and unclear.", "Priorities changed weekly without explanation."],
    "Better external opportunity": ["Received an opportunity I could not turn down.", "Another company offered a bigger scope.", "Moving to a role in a different industry."],
    "Relocation": ["Relocating for family reasons.", "Moving to a city where we have no office."],
    "Return to school": ["Going back to complete a degree."],
    "Retirement": ["Retiring after a great run."],
    "Performance": ["Mutual decision after a performance plan."],
    "Role eliminated": ["Position was eliminated in a reorganisation."],
    "Conduct": ["Separation following an HR investigation."],
}
exit_rows = []
for e in leavers:
    if rng.random() > 0.87:
        continue  # not everyone completes an exit interview (a realistic data gap)
    voluntary = rng.random() < 0.78
    if voluntary:
        reasons, w = VOL_REASONS.get(e["dept"], VOL_REASONS["default"])
        reason = wchoice(reasons, w)
    else:
        reason = wchoice(*INVOL_REASONS)
    rating = e["rating"] if e["rating"] != "" else 3
    regrettable = "Yes" if (voluntary and rating >= 4 and rng.random() < 0.85) else "No"
    if voluntary and rating < 4 and rng.random() < 0.1:
        regrettable = "Yes"
    recommend = wchoice(["Yes", "Maybe", "No"], [50, 30, 20] if voluntary else [20, 30, 50])
    exit_rows.append([e["id"], d_iso(e["term"]), "Voluntary" if voluntary else "Involuntary", reason,
                      recommend, regrettable, rng.choice(EXIT_COMMENTS[reason])])
exit_rows.sort(key=lambda r: r[1])
write_csv("exit_interviews.csv", ["employee_id", "exit_date", "exit_type", "primary_reason",
                                  "would_recommend_company", "regrettable_loss", "comment"], exit_rows)

# --------------------------------------------------------------------------- engagement survey
QUESTIONS = ["manager_support", "career_growth", "workload", "recognition", "compensation_fairness",
             "inclusion", "goal_clarity"]
DEPT_MOD = {
    "Customer Support": {"workload": -0.9, "recognition": -0.6, "career_growth": -0.2},
    "Sales": {"career_growth": -0.7, "compensation_fairness": -0.3},
    "Engineering": {"workload": -0.2, "compensation_fairness": 0.2, "goal_clarity": 0.2},
    "Product": {"goal_clarity": -0.4},
    "Finance": {"workload": -0.3},
    "Legal": {"workload": -0.5},
}
POS = {
    "manager_support": ["My manager genuinely has my back.", "Regular 1:1s with actionable feedback - thank you."],
    "career_growth": ["I can see a clear path to my next role.", "The mentoring program has been great for me."],
    "workload": ["Workload is demanding but manageable.", "Good balance, and the team covers for each other."],
    "recognition": ["Shout-outs from leadership make a real difference.", "I feel appreciated for the work I do."],
    "compensation_fairness": ["Pay feels fair for the role.", "The recent compensation review was transparent."],
    "inclusion": ["I feel I can be myself at work.", "Inclusive team culture - everyone's voice is heard."],
    "goal_clarity": ["I always know what the priorities are.", "Quarterly goals are clear and realistic."],
}
NEG = {
    "manager_support": ["I rarely get feedback from my manager.", "My manager is stretched too thin to support the team."],
    "career_growth": ["There is no visible path to promotion.", "Growth conversations keep getting postponed."],
    "workload": ["Ticket volume has doubled and the team has not grown.", "I regularly work evenings to keep up.", "Too many priorities, not enough people."],
    "recognition": ["Good work goes unnoticed.", "Remote teammates seem invisible when recognition is handed out."],
    "compensation_fairness": ["I suspect colleagues in similar roles earn more than I do.", "Salary bands are not communicated clearly."],
    "inclusion": ["Meetings are dominated by a few voices.", "Hard to feel included when most people are in the office."],
    "goal_clarity": ["Priorities change every week.", "I am not sure how my work connects to company goals."],
}
# Comments that mention real-looking people: a privacy trap for the "responsible AI" lesson.
PII_COMMENTS = [
    "Honestly, Dana Whitfield (dana.whitfield@brightwave.example) never gives credit to her team.",
    "Please talk to Marcus Ellery about the scheduling chaos - call him on 555-0142.",
    "My skip-level, Rhea Kapoor, has been great, but my direct manager Tom Bailey avoids hard conversations.",
    "I am considering leaving and have already spoken to a recruiter - please keep this anonymous.",
    "I have a medical condition that makes the office commute hard, and nobody has followed up on my accommodation request.",
]


def tenure_band(hire):
    yrs = (AS_OF - hire).days / 365.25
    return "<1 year" if yrs < 1 else "1-3 years" if yrs < 3 else "3-5 years" if yrs < 5 else "5+ years"


survey_rows = []
for dept in DEPTS:
    pool = [e for e in active if e["dept"] == dept]
    rate = 0.40 if dept == "Legal" else 0.72
    take = max(1, round(len(pool) * rate))
    for e in rng.sample(pool, take):
        band = tenure_band(e["hire"])
        scores = {}
        for q in QUESTIONS:
            mu = 3.9 + DEPT_MOD.get(dept, {}).get(q, 0)
            if e["model"] == "Remote" and q in ("recognition", "inclusion"):
                mu -= 0.4
            if band == "<1 year":
                mu += 0.3
            if band == "3-5 years" and q == "career_growth":
                mu -= 0.5
            scores[q] = int(min(5, max(1, round(rng.gauss(mu, 0.9)))))
        mu_e = 7.2 + (0.8 if band == "<1 year" else 0) + sum(DEPT_MOD.get(dept, {}).values()) * 0.8
        enps = int(min(10, max(0, round(rng.gauss(mu_e, 1.8)))))
        comment = ""
        if rng.random() < 0.65:
            q = max(QUESTIONS, key=lambda k: abs(scores[k] - 3) + rng.random() * 0.5)
            comment = rng.choice(POS[q] if scores[q] >= 4 else NEG[q])
        survey_rows.append([dept, e["location"], e["model"], band, enps] + [scores[q] for q in QUESTIONS] + [comment])
rng.shuffle(survey_rows)
for c in PII_COMMENTS:  # replace a handful of blank comments with the privacy-trap comments
    for r in survey_rows:
        if r[-1] == "":
            r[-1] = c
            break
survey_rows = [[f"R{1001 + i}"] + r for i, r in enumerate(survey_rows)]
write_csv("engagement_survey.csv",
          ["response_id", "department", "location", "work_model", "tenure_band", "enps_0_to_10"] + QUESTIONS + ["comment"],
          survey_rows)

# --------------------------------------------------------------------------- recruiting pipeline
REQS = [  # (req, role, dept, volume, mean days to hire)
    ("REQ-2026-001", "Software Engineer", "Engineering", 48, 54), ("REQ-2026-002", "Software Engineer", "Engineering", 44, 51),
    ("REQ-2026-003", "DevOps Engineer", "Engineering", 26, 58), ("REQ-2026-004", "Account Executive", "Sales", 38, 34),
    ("REQ-2026-005", "Account Executive", "Sales", 34, 36), ("REQ-2026-006", "Sales Development Rep", "Sales", 52, 27),
    ("REQ-2026-007", "Support Specialist", "Customer Support", 46, 22), ("REQ-2026-008", "Support Specialist", "Customer Support", 40, 24),
    ("REQ-2026-009", "Marketing Specialist", "Marketing", 28, 33), ("REQ-2026-010", "Product Manager", "Product", 22, 49),
    ("REQ-2026-011", "Financial Analyst", "Finance", 18, 38), ("REQ-2026-012", "Recruiter", "People & Culture", 16, 35),
    ("REQ-2026-013", "Operations Analyst", "Operations", 20, 31), ("REQ-2026-014", "Compliance Specialist", "Legal", 12, 45),
]
SOURCES = ["Referral", "LinkedIn", "Careers Site", "Job Board", "Agency", "University"]
SRC_W = [12, 30, 22, 18, 8, 10]
SRC_Q = {"Referral": 1.5, "LinkedIn": 1.0, "Careers Site": 0.9, "Job Board": 0.7, "Agency": 1.25, "University": 1.1}
RECRUITERS = ["Tessa Brandt", "Ravi Menon", "Claire Dubois", "Marco Bianchi", "Naomi Okoye", "Leo Hartmann"]
STAGES = ["Applied", "Phone Screen", "Interview", "Final Interview", "Offer", "Hired"]
STAGE_P = [0.6, 0.55, 0.55, 0.6, 0.78]  # chance of moving to the next stage

pipe_rows = []
for req, role, dept, vol, mean_days in REQS:
    for _ in range(vol):
        src = wchoice(SOURCES, SRC_W)
        applied = dt.date(2026, 1, 5) + dt.timedelta(days=rng.randint(0, 262))
        idx = 0
        while idx < 5 and rng.random() < (STAGE_P[idx] if idx == 4 else min(0.95, STAGE_P[idx] * SRC_Q[src])):
            idx += 1
        stage = STAGES[idx]
        hired_date, days = "", ""
        if stage == "Hired":
            days = max(8, int(rng.gauss(mean_days, 8)))
            hd = applied + dt.timedelta(days=days)
            if hd > AS_OF:
                stage, status = "Offer", "In Progress"
            else:
                status, hired_date = "Hired", hd.isoformat()
        elif stage == "Offer":
            status = "Offer Declined"
        else:
            recent = (AS_OF - applied).days < 45
            status = wchoice(["In Progress", "Rejected", "Withdrawn"], [70, 20, 10] if recent else [0, 85, 15])
        if status != "Hired":
            days = ""
        pipe_rows.append([req, role, dept, src, rng.choice(RECRUITERS), applied.isoformat(), stage, status, hired_date, days])
pipe_rows.sort(key=lambda r: r[5])
pipe_rows = [[f"C-{1001 + i}"] + r for i, r in enumerate(pipe_rows)]
write_csv("recruiting_pipeline.csv",
          ["candidate_id", "requisition_id", "role_title", "department", "source", "recruiter", "applied_date",
           "furthest_stage", "final_status", "hired_date", "days_to_hire"], pipe_rows)

# --------------------------------------------------------------------------- training completion
COURSES = [("Code of Conduct", dt.date(2026, 3, 31)), ("Data Privacy", dt.date(2026, 6, 30)),
           ("Anti-Harassment", dt.date(2026, 8, 31)), ("Workplace Safety", dt.date(2026, 9, 15)),
           ("Security Awareness", dt.date(2026, 11, 15))]
train_rows = []
for e in active:
    for course, due in COURSES:
        assigned = max(e["hire"], due - dt.timedelta(days=60))
        this_due = due if e["hire"] <= due - dt.timedelta(days=30) else e["hire"] + dt.timedelta(days=30)
        if assigned > AS_OF:
            continue
        past_due = this_due < AS_OF
        p_done = (0.85 if e["dept"] == "Customer Support" else 0.94) if past_due else 0.35
        completed = ""
        if rng.random() < p_done:
            latest = min(AS_OF, this_due + dt.timedelta(days=20))
            span = max(0, (latest - assigned).days)
            completed = (assigned + dt.timedelta(days=rng.randint(0, span))).isoformat()
        status = "Completed" if completed else ("Overdue" if past_due else "Pending")
        train_rows.append([e["id"], course, assigned.isoformat(), this_due.isoformat(), completed, status])
train_rows = [[f"T{10001 + i}"] + r for i, r in enumerate(train_rows)]
write_csv("training_completion.csv",
          ["record_id", "employee_id", "course", "assigned_date", "due_date", "completed_date", "status"], train_rows)

# --------------------------------------------------------------------------- messy onboarding export
managers = [f"{e['first']} {e['last']}" for e in active if e["level"] == "M1"]
NEW = [  # (first, last, dept, title, location, true start)
    ("Imani", "Okonkwo", "Engineering", "Software Engineer", "New York"), ("Pedro", "Almeida", "Sales", "Account Executive", "Austin"),
    ("Hanna", "Berg", "Customer Support", "Support Specialist", "London"), ("Yusuf", "Demir", "Engineering", "DevOps Engineer", "Berlin"),
    ("Clara", "Whitaker", "Marketing", "Content Strategist", "Toronto"), ("Mohan", "Iyer", "Finance", "Financial Analyst", "New York"),
    ("Sienna", "Cross", "Product", "Product Manager", "Austin"), ("Tomas", "Havel", "Operations", "Operations Analyst", "Berlin"),
    ("Aaliyah", "Brooks", "Customer Support", "Support Specialist", "Austin"), ("Gabriel", "Torres", "Sales", "Sales Development Rep", "New York"),
    ("Freya", "Lund", "Engineering", "QA Engineer", "London"), ("Nadia", "Rahman", "People & Culture", "Recruiter", "Toronto"),
    ("Jun", "Watanabe", "Engineering", "Data Engineer", "New York"), ("Elise", "Fontaine", "Marketing", "Designer", "London"),
    ("Dominic", "Pruitt", "Sales", "Solutions Consultant", "Austin"), ("Layla", "Mansour", "Legal", "Compliance Specialist", "London"),
    ("Kai", "Sørensen".replace("ø", "o"), "Engineering", "Software Engineer", "Berlin"), ("Beatriz", "Campos", "Customer Support", "Customer Success Manager", "Toronto"),
    ("Owen", "Gallagher", "Operations", "IT Support Specialist", "New York"), ("Ananya", "Rao", "Finance", "Accountant", "Austin"),
    ("Theo", "Marchetti", "Product", "UX Researcher", "Berlin"), ("Zainab", "Yusuf", "Customer Support", "Support Specialist", "London"),
    ("Callum", "Reid", "Sales", "Account Executive", "Toronto"), ("Mina", "Kobayashi", "Engineering", "Software Engineer", "Toronto"),
    ("Rafael", "Quintero", "Marketing", "Marketing Specialist", "Austin"), ("Esther", "Boateng", "People & Culture", "HR Business Partner", "New York"),
]
mondays = [dt.date(2026, 10, 19), dt.date(2026, 10, 26), dt.date(2026, 11, 2), dt.date(2026, 11, 9), dt.date(2026, 11, 16)]
DEPT_VARIANTS = {"Engineering": ["Engineering", "Eng", "engineering ", "ENGINEERING"], "Sales": ["Sales", "sales", "Sales "],
                 "Customer Support": ["Customer Support", "Support", "CS", "customer support"], "Marketing": ["Marketing", "Mktg", "marketing"],
                 "Finance": ["Finance", "finance", "Fin."], "Product": ["Product", "product", "Prod"],
                 "Operations": ["Operations", "Ops", "operations"], "People & Culture": ["People & Culture", "HR", "People and Culture"],
                 "Legal": ["Legal", "legal"]}
LOC_VARIANTS = {"New York": ["New York", "NYC", "new york, NY"], "Austin": ["Austin", "Austin, TX", "ATX"],
                "London": ["London", "London, UK", "london"], "Toronto": ["Toronto", "Toronto, ON", "TO"], "Berlin": ["Berlin", "berlin", "Berlin, DE"]}
PHONE_FMT = ["(212) 555-01{:02d}", "212-555-01{:02d}", "+1 212 555 01{:02d}", "212.555.01{:02d}", ""]


def fmt_date(d, style, location):
    if style == 0:
        return d.isoformat()
    if style == 1:
        return d.strftime("%m/%d/%Y")
    if style == 2:
        return d.strftime("%d %b %Y")
    if style == 3:
        return f"{d.strftime('%B')} {d.day}, {d.year}"
    if style == 4:
        return d.strftime("%d/%m/%Y") if location in ("London", "Berlin") else d.strftime("%m/%d/%y")
    return d.strftime("%m.%d.%y")


def fmt_name(first, last, style):
    return [f"{first} {last}", f"{first.upper()} {last.upper()}", f"{first.lower()} {last.lower()}",
            f"  {first}  {last} ", f"{last}, {first}", f"{first} {last}"][style % 6]


messy = []
truth = []
for i, (first, last, dept, title, loc) in enumerate(NEW):
    start = mondays[i % 5]
    email = f"{first}.{last}@{DOMAIN}".lower()
    if i in (4, 11, 19):
        email = ""  # missing
    elif i == 8:
        email = f"{first}.{last}@brightwave.exmaple".lower()  # typo'd domain
    elif i % 7 == 0:
        email = email.upper()
    row = [fmt_name(first, last, i), fmt_date(start, i % 6, loc), rng.choice(DEPT_VARIANTS[dept]), title,
           rng.choice(managers) if i % 5 else "", email, rng.choice(PHONE_FMT).format(i * 3 % 100),
           rng.choice(LOC_VARIANTS[loc]), ["Mac", "mac", "MacBook", "Windows", "PC", ""][i % 6],
           rng.choice(managers) if i % 3 == 0 else ""]
    messy.append(row)
    truth.append((first, last, start, dept, loc))
# duplicates: re-entered people (one with a conflicting start date)
dup_idx = [2, 7, 14, 21]
for k, i in enumerate(dup_idx):
    base = list(messy[i])
    first, last, dept, title, loc = NEW[i]
    base[0] = fmt_name(first, last, 4 if k % 2 == 0 else 0)
    if k == 3:
        base[1] = (mondays[(i + 1) % 5]).strftime("%Y-%m-%d")  # conflicting start date
    messy.append(base)
rng.shuffle(messy)
write_csv("new_hires_messy.csv", ["Full Name", "Start Date", "Dept", "Job Title", "Manager", "Work Email", "Phone",
                                  "Location", "Laptop Preference", "Buddy"], messy)

# =========================================================================== answer key
def yrs(d0, d1=AS_OF):
    return (d1 - d0).days / 365.25


def pct(a, b):
    return f"{100 * a / b:.1f}%" if b else "n/a"


def table(header, rows):
    out = ["| " + " | ".join(header) + " |", "|" + "|".join("---" for _ in header) + "|"]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return "\n".join(out)


n_active = len(active)
by_dept = Counter(e["dept"] for e in active)
by_loc = Counter(e["location"] for e in active)
by_model = Counter(e["model"] for e in active)
avg_tenure = statistics.mean(yrs(e["hire"]) for e in active)
new_90 = sum(1 for e in active if (AS_OF - e["hire"]).days <= 90)
start_hc = sum(1 for e in employees if e["hire"] < WINDOW_START and (not e["term"] or e["term"] >= WINDOW_START))
avg_hc = (start_hc + n_active) / 2
attr_rate = len(leavers) / avg_hc
vol = Counter(r[2] for r in exit_rows)
reason_ct = Counter(r[3] for r in exit_rows)
leavers_by_dept = Counter(e["dept"] for e in leavers)
first_year = sum(1 for e in leavers if (e["term"] - e["hire"]).days < 365)

q_avg = {q: statistics.mean(r[6 + QUESTIONS.index(q)] for r in survey_rows) for q in QUESTIONS}
enps_vals = [r[5] for r in survey_rows]
enps = 100 * (sum(v >= 9 for v in enps_vals) - sum(v <= 6 for v in enps_vals)) / len(enps_vals)
dept_resp = Counter(r[1] for r in survey_rows)
dept_q = defaultdict(lambda: defaultdict(list))
for r in survey_rows:
    for q in QUESTIONS:
        dept_q[r[1]][q].append(r[6 + QUESTIONS.index(q)])

reach = Counter()
for r in pipe_rows:
    for s in STAGES[: STAGES.index(r[7]) + 1]:
        reach[s] += 1
src_tot, src_hired = Counter(r[4] for r in pipe_rows), Counter(r[4] for r in pipe_rows if r[8] == "Hired")
days_all = [r[10] for r in pipe_rows if r[8] == "Hired"]
dept_days = defaultdict(list)
for r in pipe_rows:
    if r[8] == "Hired":
        dept_days[r[3]].append(r[10])
offers = sum(1 for r in pipe_rows if r[7] in ("Offer", "Hired") and r[8] != "In Progress")
accepted = sum(1 for r in pipe_rows if r[8] == "Hired")

tr_status = Counter(r[6] for r in train_rows)
overdue_by_course = Counter(r[2] for r in train_rows if r[6] == "Overdue")
overdue_by_dept = Counter()
emp_dept = {e["id"]: e["dept"] for e in employees}
for r in train_rows:
    if r[6] == "Overdue":
        overdue_by_dept[emp_dept[r[1]]] += 1
people_overdue = len({r[1] for r in train_rows if r[6] == "Overdue"})

gender_avg = {g: statistics.mean(e["salary"] for e in active if e["gender"] == g) for g in ("Female", "Male")}
raw_gap = 1 - gender_avg["Female"] / gender_avg["Male"]
adj = {}
for dept in ("Engineering", "Sales", "Customer Support"):
    ratios = []
    for lvl in LEVELS:
        f = [e["salary"] for e in active if e["dept"] == dept and e["level"] == lvl and e["gender"] == "Female"]
        m = [e["salary"] for e in active if e["dept"] == dept and e["level"] == lvl and e["gender"] == "Male"]
        if len(f) >= 2 and len(m) >= 2:
            ratios.append(statistics.mean(f) / statistics.mean(m))
    adj[dept] = 1 - statistics.mean(ratios) if ratios else float("nan")
raw_dept = {}
for dept in ("Engineering", "Sales", "Customer Support"):
    f = [e["salary"] for e in active if e["dept"] == dept and e["gender"] == "Female"]
    m = [e["salary"] for e in active if e["dept"] == dept and e["gender"] == "Male"]
    raw_dept[dept] = 1 - statistics.mean(f) / statistics.mean(m)

key = f"""# Facilitator answer key (generated)

> **Do not share with participants.** Generated by `_facilitator/generate_data.py` (seed {SEED}); regenerate
> after any change to the script. "Today" inside the fictional company is **{AS_OF.isoformat()}**.
> Participants verify against Excel - this key is for you to judge whether Copilot's answer is right.

## Metric definitions used by this key
- **Active employee** = row in `employees.csv` with an empty `termination_date`.
- **12-month attrition rate** = leavers with termination dates {WINDOW_START} - {AS_OF} / average of (headcount on {WINDOW_START}, headcount on {AS_OF}).
- **New hire (last 90 days)** = active employee with `hire_date` within 90 days of {AS_OF}.
- **eNPS** = % scoring 9-10 minus % scoring 0-6 on `enps_0_to_10`.

## Module 1 / 4.1 - Headcount (`employees.csv`)
- Total rows: **{len(employees)}**; active: **{n_active}**; leavers (all in the 12-month window): **{len(leavers)}**
- Average tenure of active employees: **{avg_tenure:.1f} years**; new hires in last 90 days: **{new_90}**
- Contractors among active: **{sum(1 for e in active if e['etype'] == 'Contractor')}**; part-time: **{sum(1 for e in active if e['etype'] == 'Part-time')}**

Active headcount by department:

{table(['Department', 'Active'], sorted(by_dept.items(), key=lambda kv: -kv[1]))}

Active headcount by location: {', '.join(f'{k} {v}' for k, v in by_loc.most_common())}

Active headcount by work model: {', '.join(f'{k} {v}' for k, v in by_model.most_common())}

> **Common trap:** if Copilot answers "{len(employees)}" for headcount, it forgot to exclude leavers. Great teaching moment.

## Module 4.4A - Attrition & exit reasons (`employees.csv` + `exit_interviews.csv`)
- Leavers: **{len(leavers)}**; average headcount: **{avg_hc:.1f}** -> 12-month attrition: **{attr_rate * 100:.1f}%**
- Leavers within first year of tenure: **{first_year}** of {len(leavers)} ({pct(first_year, len(leavers))})
- Exit interviews on file: **{len(exit_rows)}** of {len(leavers)} leavers (not everyone has one - data gap to point out)
- Voluntary vs involuntary (interview records): {dict(vol)}
- Top reasons: {', '.join(f'{k} ({v})' for k, v in reason_ct.most_common(5))}

Leavers by department:

{table(['Department', 'Leavers', 'Attrition vs. dept headcount'], [(d, leavers_by_dept.get(d, 0), pct(leavers_by_dept.get(d, 0), by_dept[d] + leavers_by_dept.get(d, 0))) for d in DEPTS])}

## Module 4.4B - Engagement survey (`engagement_survey.csv`)
- Responses: **{len(survey_rows)}** (approx. {pct(len(survey_rows), n_active)} participation); eNPS: **{enps:.0f}**
- Responses by department: {', '.join(f'{k} {v}' for k, v in dept_resp.most_common())}
- **Small-group trap:** Legal has only **{dept_resp.get('Legal', 0)}** responses - below the minimum group size of 5, so it should be hidden/merged. This is exactly what the privacy rules in Module 5 teach.
- Average score per question (1-5): {', '.join(f'{q} {v:.2f}' for q, v in q_avg.items())}
- Planted insights: Customer Support scores lowest on **workload** ({statistics.mean(dept_q['Customer Support']['workload']):.2f}) and **recognition** ({statistics.mean(dept_q['Customer Support']['recognition']):.2f}); Sales is lowest on **career_growth** ({statistics.mean(dept_q['Sales']['career_growth']):.2f}); remote employees score lower on recognition/inclusion; employees in the "3-5 years" band score lowest on career growth.
- **Privacy trap:** 5 comments contain names, an email, a phone number, a resignation hint, or a medical remark. A good dashboard must not display raw comments without a warning/redaction.

## Module 4.2 - Recruiting funnel (`recruiting_pipeline.csv`)
- Candidates: **{len(pipe_rows)}**; hires: **{accepted}**; offers extended (reached Offer stage, not still in progress): **{offers}** -> offer-accept rate **{pct(accepted, offers)}**
- Average days to hire: **{statistics.mean(days_all):.1f}**

Funnel (candidates who reached each stage or beyond):

{table(['Stage', 'Candidates'], [(s, reach[s]) for s in STAGES])}

Hire rate by source:

{table(['Source', 'Candidates', 'Hired', 'Hire rate'], [(s, src_tot[s], src_hired[s], pct(src_hired[s], src_tot[s])) for s in SOURCES])}

Average days-to-hire by department: {', '.join(f'{d} {statistics.mean(v):.0f}' for d, v in sorted(dept_days.items()))}

## Module 4.4C - Compliance training (`training_completion.csv`)
- Records: **{len(train_rows)}**; status counts: {dict(tr_status)}; employees with at least one overdue course: **{people_overdue}**
- Overdue by course: {dict(overdue_by_course)}
- Overdue by department: {dict(overdue_by_dept.most_common())} (Customer Support is planted as the worst)
- "Security Awareness" is due 2026-11-15 - **Pending is not Overdue** (a good check that Copilot does not mis-flag it).

## Module 4.4D - Pay equity challenge (`employees.csv`, active only)
- Average salary: women **${gender_avg['Female']:,.0f}**, men **${gender_avg['Male']:,.0f}** -> **raw gap {raw_gap * 100:.1f}%**
- Raw gap by department: {', '.join(f'{d} {v * 100:.1f}%' for d, v in raw_dept.items())}
- Gap **after comparing like-for-like levels** (average of per-level ratios): {', '.join(f'{d} {v * 100:.1f}%' for d, v in adj.items())}
- Planted: women in Engineering and Sales are paid roughly 3-4% less at the same level (the raw gap is larger because fewer women reach senior levels). Teaching point: *raw vs. adjusted gap*, small groups, and why this needs HR/Legal review - not a Copilot verdict.

## Module 3 - Cleaning `new_hires_messy.csv`
- The file has **{len(messy)}** rows for **{len(NEW)}** unique people (**{len(dup_idx)} duplicates**, one with a conflicting start date).
- Intended start dates are all Mondays between 2026-10-19 and 2026-11-16. Ambiguous `dd/mm` vs `mm/dd` values should be resolved or **flagged** - a hire in London may be written day-first.
- Three rows have no email; one email has a typo'd domain (`brightwave.exmaple`); some are upper-cased.

Truth table (for judging the cleaned output):

{table(['Name', 'Intended start', 'Department', 'Location'], [(f'{f} {l}', s.isoformat(), d, loc) for f, l, s, d, loc in truth])}

## Module 2 - Policy Q&A (`docs/`)
| Question | Expected answer | Source |
|---|---|---|
| Weeks of paid leave for a birth parent / secondary caregiver? | 16 weeks / 8 weeks, both at 100% pay | parental-leave-policy.md |
| Who is eligible? | Full-time and part-time employees with 6+ months of service; not contractors | parental-leave-policy.md |
| PTO days for a 5-year employee? | 25 + 2 (one extra day per year of service after year 3) = **27** | pto-and-holidays-policy.md |
| Max work-from-abroad days? | **Conflict:** remote-work-policy says 15; pto-and-holidays-policy says 20 | both |
| Learning stipend? | $1,500 per year after 90 days; $3,000 with manager business case; repayment clause for >$1,000 if leaving within 12 months | learning-and-development-policy.md |
| Do we reimburse gym memberships? | **Not covered** - the correct answer is "I can't find this" | none (trap) |
| Home-office budget? | $600 one-time + $40/month connectivity | remote-work-policy.md |

## Module 2.3 - Job description red flags (`docs/job-description-draft.md`)
"rockstar", "ninja", "young and energetic", "digital native", "recent graduate", "native English speaker", gendered pronoun "he", "clean-cut", "aggressive", "work hard, play hard", "10+ years" for an entry-level role, 50 lb lifting for a desk role, missing salary range.

## Module 2.4 - Performance review notes (`docs/performance-review-notes.md`)
Watch for: gendered/personality language ("bossy", "too emotional"), penalising the 3-month medical leave, vague claims without evidence, and Copilot inventing achievements that are not in the notes.
"""
(ROOT / "_facilitator" / "answer-key.md").write_text(key, encoding="utf-8")
print(f"employees={len(employees)} active={n_active} leavers={len(leavers)} exits={len(exit_rows)} survey={len(survey_rows)} "
      f"pipeline={len(pipe_rows)} training={len(train_rows)} messy={len(messy)}")
