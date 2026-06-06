# certified-journeys · Course Queue Orchestrator

Invoke this whenever you want to run the queue: say `/orchestrate` or "run the course orchestrator."

The orchestrator reads the queue, generates the next pending course using the multiagent
approach from `new-course-multiagent.md`, validates it, commits it, and loops.
It saves progress after every phase so it can always resume from where it stopped.

---

## State machine

```
pending → designing → designed → generating → generated → validating → done
                                                                    ↓
                                                             needs_review (stop)
```

Each phase writes to `_prompts/orchestrator-state.json` before doing expensive work,
so a crash or rate limit at any point is recoverable.

---

## Step 0: Load state

Read `_prompts/orchestrator-state.json` and `_prompts/course-queue.md`.

Print a status table:

```
COURSE QUEUE STATUS
───────────────────────────────────────────────
  mlflow-certified     pending
  prefect-certified    pending
  ...
───────────────────────────────────────────────
  Current: [none]   Phase: [none]
```

Find the **first course** that is NOT `done` or `needs_review`. That is the target.

- If none found → print "All courses complete." and stop.
- If target status is `needs_review` → print the error, stop, ask the user to fix and update state to `pending` to retry.
- If target status is `in_progress` or a mid-phase state → resume from that phase (skip to the right step below).

---

## Step 1: Design phase

**Goal:** Generate the full COURSE INPUT (all days, slugs, topics) and save it so
all downstream agents have a consistent, persistent spec.

**Skip if:** `_prompts/course-designs/[COURSE_ID].md` already exists AND state is `designed` or later.

### 1a. Update state

Write to `orchestrator-state.json`:
```json
{ "current_course": "[COURSE_ID]", "current_phase": "designing",
  "last_updated": "[ISO timestamp]",
  "courses": { "[COURSE_ID]": { "status": "designing", "started_at": "[ISO timestamp]" } } }
```

### 1b. Spawn the Design Agent (foreground — wait for result)

Spawn a **foreground** Agent with the following prompt:

```
You are designing a certified-journeys course. Your output is a complete COURSE INPUT
block that will be used by the multiagent generation system.

Working directory: /home/ht/Documents/HT_GitHub/certified-journeys.github.io

Step 1: Read /home/ht/Documents/HT_GitHub/certified-journeys.github.io/_prompts/new-course-multiagent.md
        (understand the COURSE INPUT format, especially NOTEBOOKS and DAYS)

Step 2: Read the course entry for [COURSE_ID] in
        /home/ht/Documents/HT_GitHub/certified-journeys.github.io/_prompts/course-queue.md

Step 3: Using the metadata and core topics from the queue entry, design the full
        COURSE INPUT block. Requirements:

        NOTEBOOKS slugs:
        - One per day, kebab-case, 2-4 words, unique, derived from the day title
        - Pre-declare ALL slugs before writing DAYS

        DAYS:
        - One entry per day with: Title | Badge | Tasks (4-6) | Resources (2-3 with URLs) | Tip | hasScore
        - Badge distribution: ~40% learn, ~35% practice, ~15% review, ~10% exam (last day = exam)
        - Tasks must be concrete and actionable with real documentation URLs
        - Last day (capstone) has hasScore: true

        TOPICS:
        - 5-8 topic groups
        - Each covers 2-5 days (0-indexed)
        - Colors may reuse the palette from CSS vars (blue, amber, coral, purple, orange, teal)
          but MUST NOT duplicate the course accent color

        Quality bar: match the depth and specificity of the metaflow-certified course at
        /home/ht/Documents/HT_GitHub/certified-journeys.github.io/courses/metaflow-certified/index.html

Step 4: Write the complete COURSE INPUT block to:
        /home/ht/Documents/HT_GitHub/certified-journeys.github.io/_prompts/course-designs/[COURSE_ID].md

        File format:
        # [COURSE_FULL_NAME] — Course Design
        Generated: [ISO date]

        \`\`\`
        COURSE_TYPE: notebook
        COURSE_ID: [COURSE_ID]
        ... (full COURSE INPUT block)
        \`\`\`

        Do not truncate. Write the complete block.
```

### 1c. Update state after design

```json
{ "current_phase": "designed", "last_updated": "[ISO timestamp]",
  "courses": { "[COURSE_ID]": { "status": "designed", "designed_at": "[ISO timestamp]" } } }
```

---

## Step 2: Generation phase

**Goal:** Spawn 7 parallel background agents to generate all course files.

**Skip if:** state is `generated` or later (all files already exist).

### 2a. Read the design file

Read `_prompts/course-designs/[COURSE_ID].md`. Extract the full COURSE INPUT block.
Parse out:
- All NOTEBOOKS slugs (in order)
- All DAYS content
- TOTAL_DAYS

### 2b. Update state

```json
{ "current_phase": "generating", "last_updated": "[ISO timestamp]",
  "courses": { "[COURSE_ID]": { "status": "generating" } } }
```

### 2c. Spawn all 7 agents in a single message (all background, all parallel)

Use the agent prompt templates from `_prompts/new-course-multiagent.md`.
Substitute the COURSE INPUT block from the design file.

**Agent routing (14-day course):**

| Agent | Files | Days |
|-------|-------|------|
| HTML Agent | `courses/[ID]/index.html` | — |
| Notebook Agent A | `notebooks/day-01…day-03.ipynb` | Days 1–3 |
| Notebook Agent B | `notebooks/day-04…day-06.ipynb` | Days 4–6 |
| Notebook Agent C | `notebooks/day-07…day-09.ipynb` | Days 7–9 |
| Notebook Agent D | `notebooks/day-10…day-12.ipynb` | Days 10–12 |
| Notebook Agent E | `notebooks/day-13…day-14.ipynb` | Days 13–14 |
| Notes Agent | `notes/day-01.md…day-NN.md` | All days |

**For 10-day courses**, merge notebook batches:
- A = Days 1–3, B = Days 4–6, C = Days 7–10, D = skip, E = skip
  (only spawn A, B, C + HTML + Notes = 5 agents total)

**For 7-day courses**, merge to:
- A = Days 1–3, B = Days 4–7, C = skip, D = skip, E = skip
  (only spawn A, B + HTML + Notes = 4 agents total)

### 2d. Wait for all agent completions

You will receive completion notifications. Wait until ALL spawned agents have
reported back before proceeding to Step 3.

**Rate limit handling during wait:**
If you receive a rate limit error on any agent spawn:
1. Note which agents were successfully spawned vs which failed
2. Save state with the error:
   ```json
   { "current_phase": "generating",
     "error": "rate_limit: agents [list] failed to spawn at [timestamp]",
     "last_updated": "[ISO timestamp]" }
   ```
3. Call ScheduleWakeup with `delaySeconds: 900` and `prompt: "/orchestrate"`
4. Print: "Rate limited. State saved. Auto-resuming in 15 minutes."
5. Stop.

**On resume after rate limit:**
Re-read the state. Check which notebooks already exist on disk
(`ls courses/[COURSE_ID]/notebooks/`). Only re-spawn agents for missing files.

### 2e. Update state after generation

```json
{ "current_phase": "generated", "last_updated": "[ISO timestamp]",
  "courses": { "[COURSE_ID]": { "status": "generated", "generated_at": "[ISO timestamp]" } } }
```

---

## Step 3: Validation phase

**Goal:** Run the Manager Agent to check cross-file consistency.

**Skip if:** state is already `done`.

### 3a. Update state

```json
{ "current_phase": "validating", "last_updated": "[ISO timestamp]",
  "courses": { "[COURSE_ID]": { "status": "validating" } } }
```

### 3b. Spawn the Manager Agent (foreground — wait for result)

Use the Manager Agent prompt from `_prompts/new-course-multiagent.md`,
substituting `[COURSE_ID]` and `[TOTAL_DAYS]`.

### 3c. Evaluate the result

**If the Manager reports "✓ All consistency checks passed.":**
- Proceed to Step 4.

**If the Manager reports failures:**
```json
{ "current_phase": "validating",
  "error": "[paste manager failure report here]",
  "last_updated": "[ISO timestamp]",
  "courses": { "[COURSE_ID]": { "status": "needs_review", "error": "[failures]" } } }
```
Print the failures. Print: "Validation failed for [COURSE_ID]. Fix the issues listed above,
then update orchestrator-state.json to set [COURSE_ID].status = 'generated' to retry
validation, or 'pending' to regenerate from scratch."
**STOP. Do not continue to the next course.**

---

## Step 4: Commit and push

**Only run if `auto_commit: true` in settings.**

### 4a. Add the metaflow course to the main index.html

Read `index.html` to find the COURSES array. Add the new course:

```js
{id:'[COURSE_ID]', name:'[SHORT_NAME]', fullName:'[COURSE_FULL_NAME]',
 icon:'[ICON]', color:'[ACCENT_COLOR]', colorDim:'[ACCENT_LIGHT]',
 provider:'[PROVIDER]', cost:'[COST]', totalDays:[TOTAL_DAYS],
 tags:[TAGS_ARRAY], examLink:'[EXAM_LINK]'}
```

Also add to `NEXT_JOURNEY`: point the new course to the most topically related existing course.

### 4b. Commit

Stage only the new course files + index.html + orchestrator-state.json:

```bash
git add courses/[COURSE_ID]/ index.html _prompts/orchestrator-state.json
git commit -m "feat: add [COURSE_FULL_NAME] course ([TOTAL_DAYS] days)"
git push origin main
```

### 4c. Update state

```json
{ "current_phase": null,
  "last_updated": "[ISO timestamp]",
  "courses": { "[COURSE_ID]": { "status": "done", "completed_at": "[ISO timestamp]" } } }
```

Print: "✓ [COURSE_FULL_NAME] shipped. Pushed to main."

---

## Step 5: Cooldown and loop

Wait `cooldown_seconds` (60) seconds, then go back to **Step 0** and pick the next
pending course.

If you are approaching Claude's context limit during the loop:
1. Save current state (Step 4c format, but with the next course's status unchanged)
2. Call ScheduleWakeup with `delaySeconds: 900` and `prompt: "/orchestrate"`
3. Print: "Context limit approaching. State saved. Auto-resuming in 15 minutes."
4. Stop.

---

## Rate limit and context limit — detection heuristics

**Rate limit signals:**
- Agent spawn returns a rate limit or 429 error message
- Explicit "rate limit" text in an error response

**Context limit signals:**
- You notice your responses getting shorter or losing earlier context
- You've completed 2+ courses in one session (safe to preempt after each course)
- The conversation has been running for 60+ minutes

**When in doubt, save and schedule.** An unnecessary 15-minute pause is cheaper
than losing half-generated files.

---

## Manual resume

If the orchestrator stopped for any reason, just say `/orchestrate` again.
It reads `orchestrator-state.json`, picks up from the last saved phase, and continues.

To skip a course: set its `status` to `"skipped"` in `orchestrator-state.json`.
To retry a failed course: set its `status` back to `"pending"`.
To retry from a specific phase: set `status` to the phase before the one you want
(e.g., `"designed"` to re-run generation without re-doing the design).

---

## Adding new courses

1. Append a course entry to `_prompts/course-queue.md` (copy an existing entry as template)
2. Add its ID to `_prompts/orchestrator-state.json` with `"status": "pending"`
3. Run `/orchestrate`

---

*Orchestrator v1.0 — 1 course at a time — 60s cooldown — 15min retry — auto-commit*
