# Guide: Using `new-course.md` Without Exhausting Context

---

## Why Context Runs Out

The prompt itself is ~900 lines. A single `index.html` output is typically 800–1,200 lines. Each notebook is 150–250+ lines. A 14-day notebook course asks the model to generate **~5,000–7,000 lines in one shot** — that's a near-certain context overflow before it finishes the last notebook.

---

## Strategy: Split Into Three Passes

### Pass 1 — Fill the `[COURSE INPUT]` block only

Before touching the full prompt, fill in every field in the `[COURSE INPUT]` section completely. The most common failure mode is vague `DAYS` entries — the model invents filler. Be specific:

```
Day 3 | Partitioning & Bucketing | practice |
  Tasks:
    - Read the official partitioning guide [https://docs.delta.io/latest/...]
    - Run the bucketing notebook locally
    - Compare query plans with and without partitioning
  Resources:
    - Delta Lake partitioning docs [https://...]
    - Stack Overflow: partition vs bucket [https://...]
  Tip: Z-ordering is not the same as partitioning — know the difference for the exam.
  hasScore: true
```

Sparse `DAYS` input → sparse output. The prompt can't invent good resources.

---

### Pass 2 — Generate `index.html` alone (one conversation)

Send the full prompt with this instruction appended at the bottom:

> **Generate Output A only (`index.html`). Do not generate any notebooks or notes files yet.**

The HTML file is the largest single output. Isolating it keeps the context well under limit and lets you verify the tracker works before investing in notebooks.

**After receiving it:** open it in a browser, click through all 5 tabs, mark a day complete, tick a task, and check dark mode. Catch structure issues here, not after 10 notebooks.

---

### Pass 3 — Generate secondary files in batches

**For `standard` type** (notes only): all `notes/day-NN.md` files are tiny templates — ask for all of them in one follow-up message. They total ~200 lines regardless of course length.

**For `notebook` type**: generate 3–4 notebooks per conversation. Append to the prompt:

> **Generate Output B for Days 1–3 only** (`notebooks/day-01-*.ipynb`, `day-02-*.ipynb`, `day-03-*.ipynb`). Use the NOTEBOOKS slugs and COURSE_ID from the input above.

Keep a fresh conversation per batch. Each notebook is stateless — the model doesn't need the prior ones to generate the next.

---

## Recommended Model per Task

| Task | Model | Reason |
|---|---|---|
| `index.html` (standard course) | Sonnet | HTML + JS generation is well within capability; faster and cheaper |
| `index.html` (notebook course) | Sonnet or Opus | Same — structure is templated |
| Notebooks (`learn`/`practice` badge) | **Opus** | Code quality, concept depth, and runnable cells matter here |
| Notebooks (`review`/`exam` badge) | **Opus** | Highest depth requirements; Sonnet tends to produce shallow recap cells |
| `notes/day-NN.md` templates | Haiku | Pure fill-in-the-blank templates; no reasoning needed |

---

## Best Practices for the `DAYS` Input

**1. Link everything you can.** Tasks and resources with `[URL]` markers become clickable `{text, url}` objects in the JS data. Plain strings become inert pills. More links = more useful tracker.

**2. Write tips as exam gotchas, not summaries.** "Read Chapter 3" is not a tip. "The exam distinguishes between Scrum Master accountability and authority — they have the former, never the latter" is.

**3. Match `badge` to actual day intent.** Over-using `learn` leads to flat progress visuals. A good 14-day course has roughly: 6 `learn`, 4 `practice`, 2 `review`, 1–2 `exam`.

**4. Set `hasScore: true` only on days with a practice test.** Leaving it `false` keeps the day card clean and avoids an empty score input sitting there for every day.

---

## Verification Checklist (run after each pass)

After generating `index.html`, spot-check against these — they're the most common generation failures:

- [ ] Open in browser, open DevTools console — zero JS errors on load
- [ ] Tick all tasks on Day 1 → day auto-completes (tests `tickTask` → `toggleComplete`)
- [ ] Reset all → `tasksDone` clears (tests `resetAll`)
- [ ] Click a topic pill in a day card → jumps to Topics tab
- [ ] Click a Day button in Topics tab → jumps back to Daily Plan, scrolls to that day
- [ ] Click "☁ Connect GitHub" → modal opens with correct `COURSE_ID` in the `<p>` tag
- [ ] Dark mode toggle (OS-level) → no broken colors

---

## Quick Reference: What Goes in One Message vs Multiple

| Output | One message? |
|---|---|
| Full prompt + `[COURSE INPUT]` | Yes — this is your master input |
| `index.html` | Yes — request alone |
| All `notes/day-NN.md` (standard) | Yes — tiny files |
| Notebooks, days 1–3 | Yes |
| Notebooks, days 4–6 | New conversation |
| Notebooks, days 7–9 | New conversation |

---

## Iterating on `index.html`

If you need to fix something after generation, paste only the relevant JS function or CSS section back into Claude with a targeted instruction — don't regenerate the whole file. The sections are clearly delimited (`renderSchedule`, `renderAI`, etc.) and the model can patch one function without context from the rest.
