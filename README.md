# pspo-certified

A free, open-source learning tracker for the **Professional Scrum Product Owner I (PSPO I)** certification exam — built for senior professionals who want a structured, no-fluff 14-day study plan.

Live demo → `https://certified-journeys.github.io/pspo-certified`

---

> **Disclaimer:** This project is an independent, community-built study tool. It is not affiliated with, endorsed by, sponsored by, or in any way officially connected to Scrum.org, the Scrum Alliance, or any other certification body. All trademarks, including Professional Scrum™, PSPO™, and Scrum.org™, are the property of their respective owners and are referenced here solely for descriptive and educational purposes.
>
> This tracker does not sell, provide, or substitute for the official PSPO I certification exam. To earn the official credential, you must register and pay directly at [scrum.org](https://www.scrum.org/assessments/professional-scrum-product-owner-i-certification). This tool charges nothing and makes no money.

---

## What it is

A single-file HTML application that runs entirely in the browser. No backend, no account, no login, and no payment of any kind. Your progress is saved automatically using `localStorage` — it never leaves your device.

Built specifically for experienced professionals (5+ years) who need exam-ready structure without starting from scratch.

**This tool is completely free.** There is no premium tier, no upsell, no email capture, and no hidden cost. Fork it, use it, share it.

---

## Features

- **14-day daily schedule** — every day has a clear learning objective, senior-level tip, task checklist, and resource links
- **Progress tracking** — visual progress bar and completion stats update as you check off days
- **Practice score logging** — log your mock exam scores on practice and exam days; average score is tracked automatically
- **Topic coverage map** — 8 PSPO I exam domains with coverage bars that update as you progress
- **Resources tab** — all key free and paid resources in one place with cost labels
- **Built-in quiz** — 8 scenario-based questions with full explanations, scored and tracked
- **Dark mode** — automatically follows your system preference
- **Mobile friendly** — fully responsive layout
- **localStorage persistence** — progress survives page refresh and browser restarts, on the same device

---

## How to use

### Option 1 — GitHub Pages (recommended)

1. Fork or clone this repo
2. Go to **Settings → Pages**
3. Set source to `main` branch, `/ (root)` folder
4. Your tracker is live at `https://certified-journeys.github.io/pspo-certified`

### Option 2 — Run locally

No build step needed. Just open `index.html` in any modern browser.

```bash
git clone https://github.com/certified-journeys/pspo-certified.git
cd pspo-certified
open index.html
```

---

## Exam at a glance

| Detail | Info |
|--------|------|
| Provider | Scrum.org |
| Cost | $200 USD per attempt |
| Format | 80 questions, 60 minutes |
| Pass mark | 85% (68 of 80 correct) |
| Password expiry | Never — use when ready |
| Prep time | 2 weeks (senior level) |
| Source of truth | Scrum Guide 2020 only |

---

## Recommended study resources

**Free — must use**
- [Scrum Guide 2020](https://scrumguides.org) — the only document the exam is based on
- [PSPO Open Assessment](https://www.scrum.org/open-assessments) — free official practice questions
- [Mikhail Lapshin PSPO Quiz](https://mlapshin.com/index.php/scrum-quizzes/po-learning-mode/) — 80 questions with explanations
- [Scrum.org Learning Path](https://www.scrum.org/pathway) — structured free content

**Paid — optional**
- [PrepForScrum Exam Simulator](https://prepforscrum.com) — 800+ questions, $19.99
- [Coursera PSPO I Prep by SkillUp](https://www.coursera.org/specializations/product-owner-certification-pspo1-preparation) — 2-week structured course
- *Professional Product Owner* — Don McGreal (book)

---

## Score benchmarks

| Practice score | Readiness |
|---------------|-----------|
| Below 80% | Not ready — re-read Scrum Guide |
| 80–89% | Getting close — target weak areas |
| 90%+ consistently | Ready to book the exam |

---

## Tech stack

| Layer | Choice |
|-------|--------|
| Framework | Vanilla HTML/CSS/JS — zero dependencies |
| Fonts | DM Sans + DM Mono (Google Fonts) |
| Storage | Browser `localStorage` |
| Hosting | GitHub Pages (free) |
| Build step | None |

---

## File structure

```
pspo-certified/
├── index.html   ← entire application (self-contained)
└── README.md    ← this file
```

---

## Resetting progress

Click the **Reset progress** button in the top-right corner of the tracker. This clears all completed days, scores, and quiz answers from `localStorage`. Nothing is stored on any server — reset only affects your local browser.

---

## Privacy

This tool collects no data whatsoever. There is no analytics, no tracking, no cookies, and no network requests made by the application. All state lives in your browser's `localStorage` and is never transmitted anywhere.

---

## Part of the CertForge ecosystem

`pspo-certified` is the first tool in the **CertForge** series — a collection of free, open-source certification trackers built for senior technology professionals.

| Repo | Certification | Status |
|------|--------------|--------|
| [`pspo-certified`](https://github.com/certified-journeys/pspo-certified) | Scrum.org PSPO I | ✅ Live |
| `own-your-backlog` | Scrum.org PSPO I / II | 🔜 Coming soon |
| `psm-certified` | Scrum.org PSM I | 🔜 Coming soon |
| `aws-ml-certified` | AWS ML Specialty | 🔜 Coming soon |
| `gcp-ml-certified` | GCP Professional ML Engineer | 🔜 Coming soon |
| `databricks-certified` | Databricks ML Professional | 🔜 Coming soon |

Every tool in the series follows the same principles: single HTML file, zero dependencies, no login, no cost, works offline, GitHub Pages hosted.

---

## Developer

Built and maintained by a senior MLOps engineer based in Toronto, Canada — 5+ years in machine learning infrastructure, agile delivery, and cross-functional product teams.

For the full profile including tech stack, certifications in progress, the story behind this project, and how to connect — see [DEVELOPER.md](./DEVELOPER.md).

---

## Fork this and build your own tracker

This repo is designed to be forked and personalised. The entire tracker lives in a single `index.html` file — no build tools, no package managers, no configuration files. If you can edit HTML, you can make your own tracker in under an hour.

Here is exactly how to do it.

---

### Step 1 — Fork the repo

Click **Fork** at the top right of this page. Give your fork a name that reflects your cert — for example `aws-ml-certified`, `psm-certified`, or `cka-certified`.

---

### Step 2 — Open `index.html` and find the data

Everything you need to change is in two JavaScript arrays near the top of the `<script>` block. Search for:

```js
const days = [ ... ]
const topics = [ ... ]
```

These are the only two things you need to edit to make a completely different tracker.

---

### Step 3 — Rewrite the `days` array

Each object in `days` represents one day of your study plan. Replace the content with your own cert's schedule:

```js
const days = [
  {
    title: "Your day 1 title here",
    badge: "learn",          // learn | practice | review | exam
    sub: "Week 1 · Foundation",
    tasks: [
      "First task for this day",
      "Second task for this day",
      "Third task for this day",
      "Fourth task for this day"
    ],
    resources: [
      "Resource name (url or platform)",
      "Second resource name"
    ],
    tip: "Your senior tip or insight for this day goes here.",
    hasScore: false          // set true on practice/mock exam days
  },
  // repeat for each day of your plan ...
]
```

**Badge types and when to use them:**

| Badge | Value | Use when |
|-------|-------|----------|
| Green | `"learn"` | Reading, studying new concepts |
| Blue | `"practice"` | Mock exams, quizzes, open assessments |
| Amber | `"review"` | Revisiting weak areas, consolidation |
| Red | `"exam"` | Timed full mocks, final prep, booking day |

Set `hasScore: true` on any day where you want to log a practice exam score. The tracker will show a score input field and include that day in your average score calculation.

---

### Step 4 — Rewrite the `topics` array

Each object represents one exam domain or knowledge area. Replace with your cert's actual topic areas:

```js
const topics = [
  { name: "Your first exam domain", color: "#1D9E75", days: [0, 2, 6] },
  { name: "Your second exam domain", color: "#378ADD", days: [1, 3, 7] },
  // add one per domain — typically 6–10 for most certs
]
```

- `name` — the exam domain or knowledge area as it appears in the official exam guide
- `color` — any hex colour; pick one per domain for the coverage bar
- `days` — the index numbers (0-based) of the days in your plan that cover this topic

The tracker automatically calculates how much of each topic you have covered based on which days you have completed.

---

### Step 5 — Update the quiz questions

Find the `quizzes` array and replace with questions relevant to your cert:

```js
const quizzes = [
  {
    q: "Your scenario-based question here?",
    opts: [
      "Option A",
      "Option B — the correct one",
      "Option C",
      "Option D"
    ],
    correct: 1,   // 0-based index of the correct option
    exp: "Explanation of why this answer is correct. Reference the official source."
  },
  // add 5–10 questions for a good quiz experience
]
```

---

### Step 6 — Update the header text

Find and update the title and subtitle in the HTML section:

```html
<h1>PSPO I certification tracker</h1>
<p>14-day daily learning plan — senior level</p>
```

Also update the `<title>` tag at the very top of the file to match your cert name.

---

### Step 7 — Change the storage key

To avoid conflicts if someone has multiple trackers open in the same browser, update the storage key to something unique to your cert:

```js
const STORAGE_KEY = 'pspo1_tracker_v1';
// change to something like:
const STORAGE_KEY = 'aws_ml_tracker_v1';
```

---

### Step 8 — Deploy to GitHub Pages

1. Go to your forked repo → **Settings → Pages**
2. Set source to `main` branch, `/ (root)` folder
3. Click **Save**
4. Your tracker is live at `https://yourusername.github.io/your-repo-name`

---

### Tracker ideas from the community

Built one? Open a PR to add it to this table.

| Cert | Suggested repo name | Days recommended |
|------|-------------------|-----------------|
| AWS ML Specialty | `aws-ml-certified` | 21 days |
| GCP Professional ML Engineer | `gcp-ml-certified` | 21 days |
| Databricks ML Professional | `databricks-certified` | 14 days |
| Scrum.org PSM I | `psm-certified` | 14 days |
| CKA (Kubernetes) | `cka-certified` | 30 days |
| AWS Solutions Architect | `aws-sa-certified` | 30 days |
| PMP | `pmp-certified` | 60 days |
| Google Data Engineer | `gde-certified` | 21 days |

---

## Contributing

Found a mistake in the study content? Have a better senior tip? Want to add a question to the quiz?

1. Fork the repo
2. Make your changes to `index.html` or `README.md`
3. Open a pull request with a clear description of what changed and why

All contributions are welcome. Please do not submit PRs that add tracking, analytics, paywalls, or external service dependencies — this tool must remain free and self-contained forever.

---

MIT — free to use, modify, and share. No attribution required.

---

## Trademark notice

Professional Scrum™, PSPO™, PSM™, Scrum.org™, and related marks are trademarks of Scrum.org. CSM®, CSPO®, and Scrum Alliance® are trademarks of the Scrum Alliance. This project uses these terms for descriptive and educational purposes only and claims no association with either organisation.

The PSPO I certification exam is owned and administered exclusively by Scrum.org. Visit [scrum.org](https://www.scrum.org) to register for the official assessment.

---

> Built to pass PSPO I, not to sell you a course. Free forever.
