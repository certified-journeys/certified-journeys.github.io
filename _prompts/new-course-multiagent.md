# certified-journeys · Multi-Agent Course Generation

Use this instead of `new-course.md` when generating a full notebook course. Each output is assigned to a dedicated agent running in parallel, eliminating context exhaustion and cutting total generation time ~5×.

---

## Why multi-agent

A 14-day notebook course generates ~5,000–7,000 lines of output. One model, one context window → near-certain overflow before the last notebook. Splitting by output:

- Each agent has a focused task with enough context budget to produce quality output
- Parallel execution: notebooks for days 1–3, 4–6, 7–9, 10–12, 13–14 generate simultaneously
- The Manager catches cross-file consistency bugs (mismatched slugs, wrong COURSE_ID, broken Colab URLs) before you open the browser

---

## [COURSE INPUT] — Fill this in first

Same format as `new-course.md`, with one addition: **`NOTEBOOKS`** — pre-define all slugs before spawning. This is what makes true parallelism possible: all agents know filenames without waiting for `index.html`.

```
COURSE_TYPE:      notebook | standard
COURSE_ID:        e.g. metaflow-certified
COURSE_FULL_NAME: e.g. Metaflow for ML Engineers
ICON:             2-letter abbreviation, e.g. MF
ACCENT_COLOR:     hex
ACCENT_LIGHT:     light version
ACCENT_DARK:      darkened version
ACCENT_DARK_DIM:  dark-mode tinted bg
PROVIDER:         e.g. Outerbounds (Self-paced)
COST:             e.g. Free
TOTAL_DAYS:       integer
DIFFICULTY:       Beginner / Intermediate / Advanced
TAGS:             comma-separated
EXAM_LINK:        URL
EXAM_QUESTIONS:   integer or null
EXAM_MINUTES:     integer or null
EXAM_PASS_SCORE:  e.g. 70%, N/A
EXAM_NOTES:       free text

NOTEBOOKS:                    ← NEW: required for notebook type
  day-01-slug                 Slug = 2-4 word kebab-case summary of day title.
  day-02-slug                 Pre-define ALL slugs. File = notebooks/[slug].ipynb
  ...
  day-NN-slug

DAYS:
  [same format as new-course.md]

TOPICS:
  [same format as new-course.md]
```

### Slug naming rules

- 2–4 words, kebab-case, derived from the day title
- Must be unique across the course
- Used as-is in `NOTEBOOKS` JS constant and as filename

---

## Agent routing table

| # | Agent | Files written | Model | Spawn |
|---|-------|---------------|-------|-------|
| 1 | HTML Agent | `courses/[ID]/index.html` | Sonnet | parallel |
| 2 | Notebook Agent A | `notebooks/day-01…day-03.ipynb` | Sonnet | parallel |
| 3 | Notebook Agent B | `notebooks/day-04…day-06.ipynb` | Sonnet | parallel |
| 4 | Notebook Agent C | `notebooks/day-07…day-09.ipynb` | Sonnet | parallel |
| 5 | Notebook Agent D | `notebooks/day-10…day-12.ipynb` | Sonnet | parallel |
| 6 | Notebook Agent E | `notebooks/day-13…day-14.ipynb` | Sonnet | parallel |
| 7 | Notes Agent | `notes/day-01.md…day-14.md` | Sonnet | parallel |
| 8 | Manager Agent | Validation report (no files) | Sonnet | **after 1–7 complete** |

For courses shorter than 14 days, merge notebook batches (e.g. 10-day: A=1–3, B=4–6, C=7–10).  
For `standard` type: skip all Notebook Agents; Notes Agent generates all notes.

---

## Execution steps

1. Fill `[COURSE INPUT]` including all `NOTEBOOKS` slugs
2. Spawn agents 1–7 **in a single message** (all background, all parallel)
3. Wait for all 7 completion notifications
4. Spawn Manager Agent — it reads all output files and reports issues
5. Fix any Manager-reported issues
6. Open `index.html` in a browser and run the verification checklist below

---

## HTML Agent — Prompt Template

```
You are generating the index.html progress tracker for a certified-journeys course.

Working directory: /home/ht/Documents/HT_GitHub/certified-journeys.github.io
Write the complete file to: courses/[COURSE_ID]/index.html (use the Write tool)

Step 1: Read /home/ht/Documents/HT_GitHub/certified-journeys.github.io/_prompts/new-course.md
Step 2: Follow the OUTPUT A SPEC exactly to generate index.html
Step 3: Write the complete file — do not truncate

## COURSE INPUT

[paste filled COURSE INPUT here, including NOTEBOOKS slugs]

## Critical requirements (notebook type)

- NOTEBOOKS JS constant must use the pre-defined slugs above, in order
- STORAGE_KEY = 'cj_[COURSE_ID]_v1'
- broadcastStatus writes to 'cj_summary_[COURSE_ID]'
- loadState must be async with GitHub sync integration
- Init = loadState().then(renderAll)
- GitHub modal (id="gh-modal"), sync badge (id="sync-badge") in HTML
- <script src="../../github-sync.js"></script> before inline script
- GHSync fallback object defined after that script tag
- 3-button action row per day: notebook + Colab + notes
- Colab URLs: repo = certified-journeys/certified-journeys.github.io
- renderAI: 3 cards with prompts tailored to [COURSE_FULL_NAME]
- renderResources: 4 sections, minimum 12 numbered links total
- dayTopics reverse index + goToDay function present
- renderTask, tickTask, renderRes helpers present and used
- state.tasksDone: {} initialized; resetAll() resets it
- ALL [TOTAL_DAYS] days in the days[] array
- Run the both-types quality checklist from new-course.md before writing
```

---

## Notebook Agent — Prompt Template

Use for each batch; customize the "Days to generate" section.

```
You are generating Jupyter notebooks (Days [X]–[Y]) for a certified-journeys course.

Working directory: /home/ht/Documents/HT_GitHub/certified-journeys.github.io
Write these files using the Write tool:
  courses/[COURSE_ID]/notebooks/[slug-X].ipynb
  courses/[COURSE_ID]/notebooks/[slug-X+1].ipynb
  ...
  courses/[COURSE_ID]/notebooks/[slug-Y].ipynb

Step 1: Read /home/ht/Documents/HT_GitHub/certified-journeys.github.io/_prompts/new-course.md
Step 2: Follow the OUTPUT B SPEC (Jupyter notebooks section) exactly
Step 3: Write all [N] notebooks — complete, not truncated

## Course context

COURSE_ID:        [COURSE_ID]
COURSE_FULL_NAME: [COURSE_FULL_NAME]

## Days to generate

[paste Day X through Day Y from filled COURSE INPUT]

## Critical requirements

- nbformat: 4, nbformat_minor: 5
- metadata.language_info.name = "python"
- Every cell: unique 8-char hex "id"
- Every code cell: "outputs": [], "execution_count": null
- Cell order: Header (Colab badge) → Install → concept/code/recap triples → Challenge → Recap
- Colab badge URL: certified-journeys/certified-journeys.github.io repo,
  path: /blob/main/courses/[COURSE_ID]/notebooks/[filename].ipynb#scrollTo=[first_cell_id]
- All code runs without errors in fresh Colab after install cell
- No pseudocode outside the Challenge cell
- Depth per badge: learn = 5+ code, 8+ markdown, 150+ lines;
  practice = 8+ code, 5+ markdown, 200+ lines;
  review = 4+ code, 10+ markdown, 150+ lines;
  exam = 10+ code, 8+ markdown, 250+ lines
```

---

## Notes Agent — Prompt Template

```
You are generating notes template files for a certified-journeys course.

Working directory: /home/ht/Documents/HT_GitHub/certified-journeys.github.io
Write [TOTAL_DAYS] files using the Write tool — one per day:
  courses/[COURSE_ID]/notes/day-01.md through day-[NN].md (zero-padded)

Day titles:
  Day 1:  [title]
  ...
  Day N:  [title]

Each file must use this exact template:

# Day N: [Day Title]

## Notes

_Your notes for today._

## Key takeaways

-

## Questions

-
```

---

## Manager Agent — Prompt Template

Run this **after all other agents complete**.

```
You are validating a certified-journeys course for cross-file consistency.

Working directory: /home/ht/Documents/HT_GitHub/certified-journeys.github.io
Course directory: courses/[COURSE_ID]/

Read all relevant files and check every item below. For each failure, report:
  [filename] — [issue] — expected: [correct value]

If all checks pass, output: "✓ All consistency checks passed."

### Consistency contract

NOTEBOOKS array (read index.html, extract the JS constant):
- [ ] Exactly [TOTAL_DAYS] slugs
- [ ] Each slug matches an actual .ipynb filename in notebooks/

File existence:
- [ ] courses/[COURSE_ID]/index.html
- [ ] notebooks/day-01-[slug].ipynb through day-[NN]-[slug].ipynb ([TOTAL_DAYS] files)
- [ ] notes/day-01.md through day-[NN].md ([TOTAL_DAYS] files)

index.html — JS constants:
- [ ] COURSE_ID = '[COURSE_ID]'
- [ ] STORAGE_KEY = 'cj_[COURSE_ID]_v1'
- [ ] TOTAL_DAYS = [TOTAL_DAYS]
- [ ] broadcastStatus writes to 'cj_summary_[COURSE_ID]'

index.html — GitHub sync:
- [ ] <script src="../../github-sync.js"></script> present
- [ ] GHSync fallback object defined immediately after
- [ ] loadState().then(renderAll) at bottom of inline script
- [ ] id="gh-modal" and id="sync-badge" in HTML

index.html — structure:
- [ ] id="panel-schedule", "panel-topics", "panel-ai", "panel-resources", "panel-exam" all present
- [ ] Hero has exactly 4 meta items (Cost, Duration, Provider, Difficulty)
- [ ] dayTopics reverse index present
- [ ] goToDay function present
- [ ] renderTask, tickTask, renderRes functions present
- [ ] state includes tasksDone: {} and resetAll() resets it

Notebooks (spot-check day-01, a middle day, day-[NN]):
- [ ] nbformat: 4, nbformat_minor: 5
- [ ] metadata.language_info.name = "python"
- [ ] All cell ids are 8-char hex and unique within the file
- [ ] All code cells have "outputs": [] and "execution_count": null
- [ ] Colab badge URL contains 'certified-journeys/certified-journeys.github.io'
- [ ] Colab badge URL path contains 'courses/[COURSE_ID]/notebooks/'

Notes:
- [ ] Each notes file has the 3-section template (Notes, Key takeaways, Questions)
```

---

## Verification checklist (after Manager reports clean)

Open `courses/[COURSE_ID]/index.html` in a browser:

- [ ] DevTools console — zero JS errors on load
- [ ] Tick all tasks on Day 1 → day auto-completes
- [ ] Reset all → tasksDone clears
- [ ] Click a topic pill on a day card → jumps to Topics tab
- [ ] Click a Day button in Topics tab → jumps to Daily Plan, scrolls to that day
- [ ] Click "☁ Connect GitHub" → modal opens with correct COURSE_ID in the `<p>` tag
- [ ] Dark mode (OS-level) → no broken colors
- [ ] Open a notebook in VS Code/JupyterLab → loads without "error loading this notebook"
- [ ] Click the Colab badge in a notebook → URL is correct

---

*certified-journeys prompt v7 · multi-agent · NOTEBOOKS pre-declaration · manager consistency validation*
