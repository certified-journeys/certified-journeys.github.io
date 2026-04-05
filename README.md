# certified-journeys

Free, open-source certification trackers for senior engineers and data professionals. Every journey is a structured daily study plan with interactive Jupyter notebooks, progress tracking, AI study tools, and exam prep — all in one place. No sign-ups. No paywalls. No tracking.

**Live site:** [certified-journeys.github.io](https://certified-journeys.github.io)

---

## What's included

| Course | Days | Notebooks | Provider | Cost |
|---|---|---|---|---|
| [dlt (data load tool) Practitioner](courses/dlt-certified/) | 10 | 10 | dltHub | Free |
| [Polars DataFrame Mastery](courses/polars-certified/) | 10 | 10 | Self-paced | Free |
| [HashiCorp Terraform Associate (003)](courses/terraform-certified/) | 14 | — | HashiCorp | $70 |
| [Professional Scrum Product Owner I](courses/pspo-certified/) | 14 | — | Scrum.org | $200 |
| [Microsoft PL-300: Power BI Data Analyst](courses/powerbi-certified/) | 14 | — | Microsoft | $165 |
| [AWS Certified ML – Specialty](courses/aws-ml-certified/) | 21 | — | Amazon | $300 |

---

## Why this exists

Plenty of study resources exist for most certifications — docs, YouTube, practice tests — but nobody built a structured daily plan with progress tracking. Most certification prep involves:

- Spending hours creating a study schedule from scratch
- Tracking progress in a spreadsheet
- Switching between 5 different tabs for resources, notes, and practice

This project collapses all of that into a single HTML file per course, with interactive notebooks for hands-on learning.

**What makes this different:**

- **Day-by-day plan** — exactly what to do on Day 1, Day 2, Day 3
- **Interactive Jupyter notebooks** — learn by running code, not reading slides
- **Progress lives in your browser** — localStorage only, no account, no server
- **AI study tools built in** — NotebookLM and Claude prompts tailored to each course
- **Fork and own it** — your copy auto-configures to your GitHub username

---

## How to use it

### Option 1 — Use the live site

Go to [certified-journeys.github.io](https://certified-journeys.github.io), pick a course, and start. Progress is saved in your browser automatically.

### Option 2 — Fork and self-host on GitHub Pages

Fork the repo and GitHub Pages does the rest — your progress stays in your own browser storage, isolated from anyone else's.

```
1. Fork this repo on GitHub
2. Go to Settings → Pages → Deploy from branch → main
3. Your site is live at https://[your-username].github.io/certified-journeys.github.io
```

No configuration needed. No build step. No environment variables.

### Opening notebooks

Every day in a course has two buttons:

- **📓 Open notebook** — opens the `.ipynb` file locally (requires Jupyter or VS Code)
- **▶ Open in Colab** — opens in Google Colab with one click, no local setup needed

Colab links follow this format:
```
https://colab.research.google.com/github/certified-journeys/certified-journeys.github.io/blob/main/courses/[course-id]/notebooks/[filename].ipynb#scrollTo=[first-cell-id]
```

---

## Project structure

```
certified-journeys.github.io/
├── index.html                        # Landing page — course grid + progress
├── courses/
│   ├── dlt-certified/
│   │   ├── index.html                # Course tracker (daily plan, topics, AI tools, exam prep, resources)
│   │   └── notebooks/
│   │       ├── day-01-fundamentals.ipynb
│   │       ├── day-02-sources.ipynb
│   │       └── ...                   # One notebook per day
│   ├── polars-certified/
│   │   ├── index.html
│   │   └── notebooks/
│   │       └── ...
│   └── [other courses]/
│       └── index.html
├── _prompts/
│   └── new-course.md                 # Prompt template for generating new courses with an LLM
└── notes-sync.js                     # Shared localStorage sync utility
```

Each course tracker (`index.html`) is fully self-contained — no build tools, no frameworks, no `node_modules`. The only external dependency is Google Fonts.

---

## How to contribute

### Add a notebook to an existing course

Each course directory has a `notebooks/` folder. To add or improve a notebook:

1. Fork the repo
2. Navigate to `courses/[course-id]/notebooks/`
3. Add or edit a `.ipynb` file — the filename must match the slug in the course's `NOTEBOOKS` array (in `courses/[course-id]/index.html`)
4. Follow the notebook format below
5. Submit a PR

### Create a new course

Use the prompt template in [`_prompts/new-course.md`](_prompts/new-course.md):

1. Open `_prompts/new-course.md`
2. Fill in the `[COURSE INPUT]` block at the top with your course metadata and day-by-day content
3. Paste the full file into Claude (or any capable LLM)
4. The model outputs a complete `index.html` tracker + all `.ipynb` notebooks
5. Drop the files into a new `courses/[course-id]/` directory and submit a PR

### Improve an existing course

- **Study plan corrections** — wrong info, outdated links, better task sequencing
- **Notebook improvements** — better explanations, additional code examples, fixed bugs
- **New resources** — add links to the Resources tab in the course tracker

### Hard rules (please read before contributing)

- No tracking, no analytics scripts, no cookies
- No external JavaScript libraries — vanilla JS only
- No build tools, no npm, no CI required to run the project
- No paywalls, premium tiers, or email capture — ever
- All code cells in notebooks must run in a fresh Google Colab environment without credentials (use free alternatives where needed)

---

## Notebook format

All notebooks follow the certified-journeys standard defined in [`_prompts/new-course.md`](_prompts/new-course.md). Key requirements:

- **nbformat 4.5** — every cell must have a unique `id` field (8-char hex), `language_info` in top-level metadata
- **Colab badge** as the first line of the first cell, with `#scrollTo=[first-cell-id]` suffix
- **Structure per day:** install cell → concept/code/"What just happened?" triples → challenge cell → recap table
- **All code must run** — no pseudocode outside the challenge scaffold
- **Synthetic data only** — no external file downloads, no credentials required

---

## Tech stack

| Layer | Choice | Reason |
|---|---|---|
| Hosting | GitHub Pages | Free, zero config |
| Frontend | Vanilla HTML/CSS/JS | No build step, forkable instantly |
| Fonts | Google Fonts (DM Sans + DM Mono) | Only external dependency |
| Progress storage | `localStorage` | No server, no account, no tracking |
| Notebooks | Jupyter / Google Colab | Interactive, zero-install via Colab |
| Course generation | LLM + `_prompts/new-course.md` | Consistent format across courses |

---

## Principles

1. **Single HTML file per course** — open it anywhere, no server needed
2. **localStorage only** — your progress is yours, stored locally
3. **MIT licensed** — fork, modify, redistribute freely
4. **Zero paywalls** — no premium tier, no upsell, no email capture, ever
5. **Learn in public** — if your fork worked, share it

---

## License

MIT — see [LICENSE](LICENSE) if present, otherwise assume MIT. Fork freely.

---

*Built and maintained by the certified-journeys community. Star the repo if it helped you pass.*
