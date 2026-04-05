# certified-journeys · New Course Generation Prompt

Copy this entire prompt into Claude (or any capable LLM). Fill in the `[COURSE INPUT]` section at the top, then send.

Courses come in **two types** — set `COURSE_TYPE` accordingly:

| Type | Use when | Day-card action row | Output B |
|------|----------|---------------------|---------|
| `notebook` | Hands-on technical (Python, data engineering, ML) | 📓 Notebook · ▶ Colab · 📝 notes/day-NN.md | Jupyter `.ipynb` per day + `notes/day-NN.md` templates |
| `standard` | Certification prep, theory-heavy (Scrum, cloud certs, BI) | 📝 notes/day-NN.md only | `notes/day-NN.md` templates |

Both types include a `📝 notes/day-NN.md` link per day. The difference is whether notebook + Colab buttons also appear.

---

## [COURSE INPUT] — Fill this in before sending

```
COURSE_TYPE:      notebook | standard
COURSE_ID:        e.g. kafka-certified, cka-certified
COURSE_FULL_NAME: e.g. Apache Kafka Streams Developer
ICON:             2-letter abbreviation, e.g. KF
ACCENT_COLOR:     hex, e.g. #E8890C
ACCENT_LIGHT:     light version, e.g. #FEF3E2
ACCENT_DARK:      darkened version, e.g. #A05A00
ACCENT_DARK_DIM:  dark-mode tinted bg, e.g. #2A1500
PROVIDER:         e.g. Confluent, HashiCorp, Google, Self-paced
COST:             e.g. $150, Free
TOTAL_DAYS:       integer, typically 10–21
DIFFICULTY:       Beginner / Intermediate / Advanced
TAGS:             comma-separated, e.g. Streaming, Java, Kafka
EXAM_LINK:        official exam/cert page URL
EXAM_QUESTIONS:   integer or null
EXAM_MINUTES:     integer or null
EXAM_PASS_SCORE:  e.g. 70%, N/A if no formal exam
EXAM_NOTES:       free text about the exam format

DAYS:
  One entry per day —
  Day N | Title | Badge (learn/practice/review/exam) | Tasks (bullet list) | Resources (bullet list with URLs where known) | Tip | hasScore (true/false)

  For tasks and resources, mark primary reading/reference links with [URL]:
    - Read the official docs [https://docs.example.com]
    - Plain text task (no link)

TOPICS:
  4–8 topic groups, each with:
  Name | Accent color (hex) | Day indices (0-based, comma-separated)
```

---

## Prompt (send everything below this line)

---

You are generating a new certified-journeys course. I will give you course metadata and day-by-day content. You will produce:

- **Always** — Output A: `courses/[COURSE_ID]/index.html`
- **If `notebook` type** — Output B: `courses/[COURSE_ID]/notebooks/day-NN-slug.ipynb` per day
- **If `standard` type** — Output B: `courses/[COURSE_ID]/notes/day-NN.md` per day

Follow every spec exactly. Do not add features not described. Produce the full files.

---

## COURSE METADATA

```
[paste your filled-in [COURSE INPUT] block here]
```

---

## OUTPUT A SPEC — `index.html` tracker

### File structure

Single self-contained HTML file. No external JS, no build tools, no npm. Google Fonts only.

### Head

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>[COURSE_FULL_NAME] · certified-journeys</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>/* all CSS inline */</style>
</head>
```

### CSS variables (required — copy exactly, only change accent vars)

```css
:root {
  --green:[ACCENT_COLOR]; --green-light:[ACCENT_LIGHT]; --green-dark:[ACCENT_DARK];
  --blue:#378ADD; --blue-light:#EAF3FD; --blue-dark:#185FA5;
  --amber:#BA7517; --amber-light:#FDF3E3;
  --coral:#D85A30; --coral-light:#FAEDE8; --coral-dark:#993C1D;
  --purple:#7F77DD; --purple-light:#EEEDFE;
  --orange:#E8890C; --orange-light:#FEF3E2;
  --teal:#0891B2; --teal-light:#E0F5FA;
  --bg:#F5F4F0; --surface:#FFFFFF; --surface2:#EEECE5; --surface3:#E8E6DF;
  --border:rgba(0,0,0,0.08); --border2:rgba(0,0,0,0.16);
  --text:#18181A; --text2:#52524E; --text3:#8C8B85;
  --radius:14px; --radius-sm:9px; --radius-xs:5px;
  --shadow:0 1px 3px rgba(0,0,0,0.08),0 4px 16px rgba(0,0,0,0.04);
  --shadow-md:0 4px 12px rgba(0,0,0,0.1),0 1px 3px rgba(0,0,0,0.06);
}
@media(prefers-color-scheme:dark){:root{
  --bg:#111113; --surface:#1C1C1F; --surface2:#252528; --surface3:#2E2E33;
  --border:rgba(255,255,255,0.08); --border2:rgba(255,255,255,0.15);
  --text:#F0EFEA; --text2:#A09F9B; --text3:#5E5D58;
  --green-light:[ACCENT_DARK_DIM];
  --blue-light:#061E38; --amber-light:#221900;
  --coral-light:#2A0E05; --purple-light:#161440;
  --orange-light:#1F1200; --teal-light:#021E26;
}}
```

### Action row CSS (required for both types)

```css
/* Action row — notebook buttons + notes link */
.nb-row{display:flex;gap:8px;margin-bottom:10px;flex-wrap:wrap;}
.nb-btn{font-size:12px;padding:6px 14px;border-radius:99px;border:.5px solid var(--border2);color:var(--text2);background:none;text-decoration:none;display:inline-flex;align-items:center;gap:5px;transition:all .15s;font-family:inherit;}
.nb-btn:hover{background:var(--surface2);color:var(--text);text-decoration:none;}
```

Add these only for **`notebook` type:**
```css
.nb-btn-colab{background:#F9AB00;border-color:#F9AB00;color:#000;}
.nb-btn-colab:hover{background:#e09900;color:#000;text-decoration:none;}
```

### Linked task and resource CSS (required for both types)

```css
/* Linked resources & tasks */
a.res-pill{text-decoration:none;cursor:pointer;}
a.res-pill:hover{background:var(--surface3);border-color:var(--border2);color:var(--text);}
.task-link{color:var(--blue-dark);font-size:11px;margin-left:6px;flex-shrink:0;opacity:0.7;line-height:1.5;}
.task-link:hover{opacity:1;text-decoration:none;}
```

### Task tick + progress bar CSS (required for both types)

```css
/* Task tick checkboxes */
.task-tick{width:16px;height:16px;border-radius:4px;border:1.5px solid var(--border2);flex-shrink:0;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:all .15s;margin-top:2px;background:none;padding:0;}
.task-tick:hover{border-color:var(--green);}
.task-tick.ticked{background:var(--green);border-color:var(--green);}
.task-tick.ticked::after{content:"✓";font-size:10px;color:#fff;font-weight:700;line-height:1;}
.task.task-done>span{text-decoration:line-through;color:var(--text3);}
/* Per-day task progress bar */
.task-progress{height:3px;border-radius:99px;background:var(--surface2);margin-bottom:8px;overflow:hidden;}
.task-progress-fill{height:100%;background:var(--green);border-radius:99px;transition:width .3s;}
```

### All other required CSS classes

Layout: `.app`, `.breadcrumb`, `.breadcrumb-sep`  
Hero: `.course-hero`, `.course-hero-top`, `.course-icon-wrap`, `.course-icon`, `.course-title-block`, `.tag-row`, `.tag`, `.hero-meta`, `.meta-item`, `.meta-label`, `.meta-val`  
Progress: `.prog-strip`, `.prog-strip-top`, `.prog-label`, `.prog-pct`, `.bar-bg`, `.bar-fill`, `.readiness` (+ `.early`, `.close`, `.ready`), `.stats-grid`, `.stat`, `.stat-label`, `.stat-val` (+ `.ok`, `.warn`, `.danger`)  
Tabs: `.tabs`, `.tab` (+ `.active`), `.panel` (+ `.active`)  
Day cards: `.day-card` (+ `.completed`, `.open`), `.day-header`, `.day-num`, `.day-meta`, `.day-title`, `.day-sub`, `.day-badge`, `.chevron`, `.day-body`, `.tip-box`, `.task-list`, `.task` (+ `.task-done`), `.task-tick` (+ `.ticked`), `.task-progress`, `.task-progress-fill`, `.resources-row`, `.res-pill`, `.score-row`, `.score-badge`, `.hours-row`, `.complete-btn` (+ `.done`)  
Topics: `.topic-grid`, `.topic-card`, `.t-bar-bg`, `.t-bar-fill`, `.t-pct`  
AI: `.ai-card`, `.ai-card-head`, `.ai-icon`, `.ai-card-title`, `.ai-card-sub`, `.ai-card-body`, `.ai-prompt-box`, `.ai-link-btn`  
Exam: `.exam-grid`, `.exam-card`, `.exam-card-label`, `.exam-card-val`, `.exam-card-sub`  
Resources: `.res-section`, `.res-section-title`, `.res-link-list`, `.res-link-item`, `.res-link-index`, `.res-link-body`, `.res-link-desc`  
Shared: `.info-box`, `.badge-learn`, `.badge-practice`, `.badge-review`, `.badge-exam`, `.page-footer`  
Responsive: `@media(max-width:640px)` for `.topic-grid`, `.hero-meta`, `.stats-grid`

### HTML body structure (tabs differ by COURSE_TYPE)

```html
<body>
<div class="app">

  <!-- 1. Breadcrumb -->
  <div class="breadcrumb">
    <a href="../../index.html">certified-journeys</a>
    <span class="breadcrumb-sep">›</span>
    <span>[COURSE_FULL_NAME]</span>
  </div>

  <!-- 2. Course hero (icon, title, tags, 4 meta items) -->
  <div class="course-hero"> ... </div>

  <!-- 3. Progress strip (bar, pct, readiness, stats grid) -->
  <div class="prog-strip"> ... </div>

  <!-- 4. Tabs — same for both types -->
  <div class="tabs">
    <button class="tab active" onclick="showPanel('schedule',this)">📅 Daily Plan</button>
    <button class="tab" onclick="showPanel('topics',this)">📚 Topics</button>
    <button class="tab" onclick="showPanel('ai',this)">🤖 AI Tools</button>
    <button class="tab" onclick="showPanel('resources',this)">🔗 Resources</button>
    <button class="tab" onclick="showPanel('exam',this)">🎓 Exam Prep</button>
  </div>

  <!-- 5. Panels (rendered by JS) -->
  <div id="panel-schedule"  class="panel active"></div>
  <div id="panel-topics"    class="panel"></div>
  <div id="panel-ai"        class="panel"></div>
  <div id="panel-resources" class="panel"></div>
  <div id="panel-exam"      class="panel"></div>

  <!-- 6. Footer -->
  <div class="page-footer">
    Progress saved locally · <span id="sk-display">cj_[COURSE_ID]_v1</span> · No account needed · <a href="../../index.html">← All journeys</a>
  </div>

</div>
```

> Both course types use the same 5-tab layout. No separate Notes tab — the notes link appears inline in each day card.

### JavaScript — data constants

```js
const COURSE_ID   = '[COURSE_ID]';
const STORAGE_KEY = 'cj_[COURSE_ID]_v1';
const TOTAL_DAYS  = [TOTAL_DAYS];

// ── notebook type only ──────────────────────────────────────────────────────
// One slug per day, matching filenames in notebooks/
const NOTEBOOKS = [
  'day-01-slug',
  // ...
];
// ── end notebook only ───────────────────────────────────────────────────────

// Tasks and resources support plain strings OR {text, url} objects.
// Use {text, url} for any item that has a primary source link.
const days = [
  {
    title:     "string",
    badge:     "learn" | "practice" | "review" | "exam",
    sub:       "Day N · Theme",
    tasks: [
      {text: "Read the official docs", url: "https://docs.example.com"},  // ↗ link shown
      "Plain text task — no link needed",
    ],
    resources: [
      {text: "Official Docs", url: "https://docs.example.com"},  // becomes <a> pill
      "No-link resource as plain string",
    ],
    tip:      "string",
    hasScore: false,
  },
  // ...
];

const topics = [
  {name: "string", color: "#hex", days: [0, 1, 2]},
  // ...
];

const exam = {
  questions:  null | number,
  minutes:    null | number,
  passScore:  "string",
  cost:       "[COST]",
  provider:   "[PROVIDER]",
  link:       "[EXAM_LINK]",
  notes:      "string"
};
```

### JavaScript — state and functions

```js
let state = {
  completed:    [],
  scores:       {},
  hours:        {},
  completedAt:  {},
  tasksDone:    {},   // per-day tick state: {dayIndex: [taskIndex, ...]}
  openDay:      null,
  startDate:    null,
  lastActivity: null,
  status:       'not_started'
};
```

> **`resetAll` must also reset `tasksDone`:**
> ```js
> state = {completed:[], scores:{}, hours:{}, completedAt:{}, tasksDone:{}, openDay:null, startDate:null, lastActivity:null, status:'not_started'};
> ```

**Required functions — implement all:**

- `loadState()` (**async**), `saveState()`, `broadcastStatus()`, `resetAll()`
- `isCompleted(i)`, `toggleComplete(i)`, `toggleDay(i)`
- `logScore(i, val)`, `logHours(i, val)`
- `scoreClass(s)`, `badgeClass(b)`, `badgeLabel(b)`
- `renderTask(t, di, ti)`, `renderRes(r)` — helpers for linked tasks/resources (see below)
- `tickTask(di, ti)` — handles per-task tick toggle and auto-complete logic
- `updateStats()`
- `renderSchedule()` — action row differs by COURSE_TYPE (see below)
- `renderTopics()` — includes clickable day buttons that navigate to Daily Plan
- `renderAI()` — 3 cards: NotebookLM audio, NotebookLM flashcards, Claude prompts
- `renderExam()` — 4 stat cards + readiness checklist
- `renderResources()` — 4 sections: Core Reading, Hands-On, Ecosystem, Upgrade Path
- `showPanel(name, btn)`, `renderAll()`
- `goToDay(i)` — switches to Daily Plan tab and scrolls to day i
- `updateSyncBadge(s)`, `openGHModal()`, `closeGHModal()`, `saveGHCreds()`, `disconnectGH()` — GitHub sync UI

#### `renderTask`, `tickTask`, and `renderRes` helpers (required for both types)

`renderTask(t, di, ti)` — renders a task row with an interactive tick checkbox.  
- `di` = day index, `ti` = task index within that day.  
- Reads `state.tasksDone[di]` to determine checked state.

```js
function renderTask(t, di, ti) {
  const done = (state.tasksDone[di] || []).includes(ti);
  const text = typeof t === 'string' ? t : t.text;
  const link = (typeof t === 'object' && t.url)
    ? `<a class="task-link" href="${t.url}" target="_blank" rel="noopener">↗</a>` : '';
  return `<div class="task${done ? ' task-done' : ''}">
    <button class="task-tick${done ? ' ticked' : ''}"
      onclick="event.stopPropagation();tickTask(${di},${ti})"></button>
    <span>${text}</span>${link}
  </div>`;
}
```

`tickTask(di, ti)` — toggles a tick; auto-completes the day when all tasks are ticked; un-completes if a tick is removed after auto-complete.

```js
function tickTask(di, ti) {
  const arr = state.tasksDone[di] || (state.tasksDone[di] = []);
  const idx = arr.indexOf(ti);
  if (idx === -1) arr.push(ti); else arr.splice(idx, 1);
  const total = days[di].tasks.length;
  const done  = arr.length;
  if (done === total && !isCompleted(di)) { toggleComplete(di); return; }
  if (done < total  &&  isCompleted(di)) {
    state.completed = state.completed.filter(x => x !== di);
    delete state.completedAt[di];
  }
  saveState(); renderSchedule();
}
```

```js
function renderRes(r) {
  if (typeof r === 'string')
    return `<span class="res-pill">📎 ${r}</span>`;
  return r.url
    ? `<a class="res-pill" href="${r.url}" target="_blank" rel="noopener">📎 ${r.text}</a>`
    : `<span class="res-pill">📎 ${r.text}</span>`;
}
```

#### `renderSchedule` — action row (differs by COURSE_TYPE, rest is identical)

The notes link is present in **both** types. The file name is zero-padded to match `notes/day-NN.md`.

**`notebook` type** — three buttons: notebook · Colab · notes:

```js
`<div class="nb-row">
  <a class="nb-btn" href="notebooks/${NOTEBOOKS[i]}.ipynb" target="_blank">📓 Open notebook</a>
  <a class="nb-btn nb-btn-colab"
     href="https://colab.research.google.com/github/certified-journeys/certified-journeys.github.io/blob/main/courses/[COURSE_ID]/notebooks/${NOTEBOOKS[i]}.ipynb"
     target="_blank">▶ Open in Colab</a>
  <a class="nb-btn" href="https://github.com/certified-journeys/certified-journeys.github.io/edit/main/courses/${COURSE_ID}/notes/day-${String(i+1).padStart(2,'0')}.md" target="_blank">📝 notes/day-NN.md</a>
</div>`
```

**`standard` type** — one button: notes only:

```js
`<div class="nb-row">
  <a class="nb-btn" href="https://github.com/certified-journeys/certified-journeys.github.io/edit/main/courses/${COURSE_ID}/notes/day-${String(i+1).padStart(2,'0')}.md" target="_blank">📝 notes/day-NN.md</a>
</div>`
```

**Both types** — remainder of day card body (identical):

```js
`<div class="tip-box"><p><strong>💡 Tip:</strong> ${d.tip}</p></div>
${(dayTopics[i]||[]).length ? `<div class="day-topic-pills">
  ${(dayTopics[i]||[]).map(t => `<span class="day-topic-pill"
    style="background:${t.color}18;color:${t.color};border-color:${t.color}40"
    onclick="event.stopPropagation();showPanel('topics',document.querySelectorAll('.tab')[1])"
    title="View topic in Topics tab">${t.name}</span>`).join('')}
</div>` : ''}
${(()=>{
  const tot = d.tasks.length;
  const done = (state.tasksDone[i] || []).length;
  return tot
    ? `<div class="task-progress"><div class="task-progress-fill" style="width:${Math.round(done/tot*100)}%"></div></div>`
    : '';
})()}
<div class="task-list">${d.tasks.map((t, j) => renderTask(t, i, j)).join('')}</div>
<div class="resources-row">${d.resources.map(renderRes).join('')}</div>
<!-- score row only if d.hasScore -->
<div class="hours-row">...</div>
<button class="complete-btn ...">...</button>`
```

> The progress bar fills automatically as tasks are ticked. When all tasks are ticked, `tickTask` calls `toggleComplete` and the day auto-completes. The "Mark as complete" button still works independently for days where you want to mark complete without ticking every task.

#### Topic ↔ Day connection (required for both types)

Add CSS for topic pills on day cards and day buttons in Topics tab:

```css
.day-topic-pills{display:flex;flex-wrap:wrap;gap:5px;margin-bottom:10px;}
.day-topic-pill{font-size:10px;padding:2px 9px;border-radius:99px;border:.5px solid;font-weight:500;cursor:pointer;transition:opacity .15s;white-space:nowrap;}
.day-topic-pill:hover{opacity:.7;}
.topic-days{display:flex;flex-wrap:wrap;gap:5px;margin-top:8px;}
.topic-day-btn{font-size:11px;padding:2px 8px;border-radius:99px;border:.5px solid var(--border2);background:var(--surface2);color:var(--text2);cursor:pointer;font-family:'DM Mono',monospace;transition:all .15s;}
.topic-day-btn:hover{background:var(--surface3);color:var(--text);}
.topic-day-btn.done{background:var(--green-light);color:var(--green-dark);border-color:var(--green);}
```

Build the reverse index and `goToDay` after `badgeLabel`:

```js
const dayTopics = (() => {
  const m = {};
  topics.forEach(t => t.days.forEach(d => { (m[d] = m[d] || []).push(t); }));
  return m;
})();

function goToDay(i) {
  showPanel('schedule', document.querySelector('.tab'));
  setTimeout(() => {
    state.openDay = i; saveState(); renderSchedule();
    const el = document.querySelector('.day-card:nth-child(' + (i + 1) + ')');
    if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }, 50);
}
```

Update `renderTopics` to include clickable day buttons:

```js
function renderTopics() {
  document.getElementById('panel-topics').innerHTML = `<div class="topic-grid">${
    topics.map(t => {
      const cov = t.days.filter(d => state.completed.includes(d)).length;
      const pct = Math.round((cov / t.days.length) * 100);
      const dayBtns = t.days.map(d =>
        `<button class="topic-day-btn${state.completed.includes(d) ? ' done' : ''}"
          onclick="goToDay(${d})">Day ${d + 1}</button>`
      ).join('');
      return `<div class="topic-card">
        <h4>${t.name}</h4>
        <div class="t-bar-bg"><div class="t-bar-fill" style="width:${pct}%;background:${t.color}"></div></div>
        <div class="t-pct">${pct}% covered · ${cov}/${t.days.length} sessions</div>
        <div class="topic-days">${dayBtns}</div>
      </div>`;
    }).join('')
  }</div>`;
}
```

#### `broadcastStatus` (required)

```js
function broadcastStatus() {
  const summary = {
    id: COURSE_ID, status: state.status,
    completed: state.completed.length, total: TOTAL_DAYS,
    scores: Object.values(state.scores).filter(s => s > 0),
    totalHours: Object.values(state.hours).reduce((a, b) => a + b, 0),
    completedAt: state.completedAt, startDate: state.startDate,
    lastActivity: state.lastActivity
  };
  try { localStorage.setItem('cj_summary_' + COURSE_ID, JSON.stringify(summary)); } catch(e) {}
}
```

#### `renderAI` — three cards (required content)

Card 1 — **NotebookLM Audio Podcast**: prompt for a 10-minute podcast covering key concepts, exam traps, and must-know items for [COURSE_FULL_NAME]. Link: `https://notebooklm.google.com`

Card 2 — **NotebookLM Flashcards**: prompt for 20 Q&A pairs focused on concept distinctions, misconceptions, scenario questions. Link: `https://notebooklm.google.com`

Card 3 — **Claude Deep Dive Prompts**: three prompts — (1) explain like a senior engineer, (2) exam scenario questions, (3) gap analysis study plan. All tailored to [COURSE_FULL_NAME].

#### `renderResources` — four sections (required)

- **Core Reading** — official docs, primary spec, main reference
- **Hands-On Resources** — tutorials, labs, community forums
- **Ecosystem & Tooling** — related tools, packages, integrations
- **Upgrade Path** — what to study next, follow-on certs

Each link item:
```html
<div class="res-link-item">
  <span class="res-link-index">01</span>
  <div class="res-link-body">
    <a href="URL" target="_blank">Title</a>
    <div class="res-link-desc">One-line description</div>
  </div>
</div>
```

Minimum 3 links per section (12 total).

#### `renderExam` checklist (required items)

- Completed all [TOTAL_DAYS] days of the study plan
- Scored [EXAM_PASS_SCORE] or higher on practice exams
- Can explain every Topics tab item without notes
- Written a cheat sheet from memory and verified it
- Consistent scores — not one lucky attempt

#### `loadState` and `saveState` — GitHub sync integration

`loadState` is **async**. It loads localStorage first for fast paint, then fetches from GitHub if connected:

```js
async function loadState() {
  try { const s = localStorage.getItem(STORAGE_KEY); if (s) state = {...state, ...JSON.parse(s)}; } catch(e) {}
  if (GHSync.isConnected()) {
    updateSyncBadge('syncing');
    const gh = await GHSync.fetchState(COURSE_ID);
    if (gh) { state = {...state, ...gh}; try { localStorage.setItem(STORAGE_KEY, JSON.stringify(state)); } catch(e) {} }
    updateSyncBadge(gh ? 'connected' : 'error');
  } else { updateSyncBadge('disconnected'); }
}
```

`saveState` writes localStorage immediately then debounces a GitHub commit (2.5 s):

```js
function saveState() {
  // ... existing status/localStorage logic ...
  broadcastStatus();
  if (GHSync.isConnected())
    GHSync.saveDebounced(COURSE_ID, state, 2500,
      () => updateSyncBadge('syncing'),
      ok => updateSyncBadge(ok ? 'connected' : 'error'));
}
```

#### GitHub sync UI functions

```js
function updateSyncBadge(s) {
  const el = document.getElementById('sync-badge'); if (!el) return;
  const L = {disconnected:'☁ Connect GitHub', connected:'✓ Synced', syncing:'↑ Syncing…', error:'⚠ Sync failed'};
  el.textContent = L[s] || L.disconnected;
  el.className = 'sync-badge' + (s==='connected' ? ' connected' : s==='syncing' ? ' syncing' : s==='error' ? ' error' : '');
}
function openGHModal() { /* populate fields from GHSync.getCreds(), open modal */ }
function closeGHModal() { document.getElementById('gh-modal').classList.remove('open'); }
async function saveGHCreds() { /* validate fields, GHSync.saveCreds(c), testConnection(), fetchState on success */ }
function disconnectGH() { GHSync.saveCreds(null); updateSyncBadge('disconnected'); closeGHModal(); }
```

### HTML — footer and modal

**Footer** — replace "Progress saved locally" text with sync badge:

```html
<div class="page-footer">
  <button class="sync-badge" id="sync-badge" onclick="openGHModal()">☁ Connect GitHub</button>
  · <span id="sk-display">cj_[COURSE_ID]_v1</span> · <a href="../../index.html">← All journeys</a>
</div>
```

**Modal + shared script** — add between closing `</div>` of `.app` and the inline `<script>`:

```html
<!-- GitHub sync modal -->
<div class="gh-modal" id="gh-modal" onclick="if(event.target===this)closeGHModal()">
  <div class="gh-modal-box">
    <h3>☁ GitHub Sync</h3>
    <p class="gh-modal-sub">Progress is committed to <code>courses/[COURSE_ID]/progress.json</code>
    in your repo on every change. Generate a Fine-grained token with Contents: Read &amp; Write.</p>
    <div class="gh-field"><label>Personal Access Token</label><input id="gh-pat" type="password" placeholder="github_pat_…" autocomplete="off"></div>
    <div class="gh-field"><label>Owner</label><input id="gh-owner" type="text" placeholder="your-username"></div>
    <div class="gh-field"><label>Repository</label><input id="gh-repo" type="text" placeholder="certified-journeys.github.io"></div>
    <div class="gh-field"><label>Branch</label><input id="gh-branch" type="text" placeholder="main"></div>
    <div class="gh-modal-actions">
      <button class="gh-btn-save" onclick="saveGHCreds()">Test &amp; Save</button>
      <button class="gh-btn-cancel" onclick="closeGHModal()">Cancel</button>
      <button class="gh-btn-disconnect" id="gh-disconnect-btn" style="display:none" onclick="disconnectGH()">Disconnect</button>
      <span class="gh-modal-msg" id="gh-modal-msg"></span>
    </div>
  </div>
</div>

<script src="../../github-sync.js"></script>
```

> `github-sync.js` lives at the repo root (`certified-journeys.github.io/github-sync.js`) and is shared by all courses. Do not inline it — always load with `../../github-sync.js`.

### Init (last lines of `<script>`)

```js
loadState().then(renderAll);
```

---

## OUTPUT B SPEC — Secondary files (differs by COURSE_TYPE)

### If `notebook` — Jupyter notebooks

**One file per day:** `courses/[COURSE_ID]/notebooks/day-NN-slug.ipynb`

**Slug:** 1–3 word kebab-case summary of the day title.

**Format:** Valid **nbformat 4.5** JSON:

```json
{
  "nbformat": 4,
  "nbformat_minor": 5,
  "metadata": {
    "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
    "language_info": {"name": "python", "version": "3.10.0"},
    "colab": {"provenance": []}
  },
  "cells": [ ... ]
}
```

> **`language_info` is required.** Without it, VS Code and JupyterLab cannot identify the kernel.

Every **markdown cell:**
```json
{"cell_type": "markdown", "id": "a1b2c3d4", "metadata": {}, "source": ["line 1\n"]}
```

Every **code cell:**
```json
{"cell_type": "code", "id": "e5f6a7b8", "metadata": {}, "execution_count": null, "outputs": [], "source": ["line 1\n"]}
```

> **`id` required on every cell** (8-char hex, unique per cell). Missing ids → "error loading this notebook".  
> **`outputs` and `execution_count` required on every code cell**, even when empty/null.

**Required cell sequence:**

Cell 1 — Header (markdown):
```markdown
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/certified-journeys/certified-journeys.github.io/blob/main/courses/[COURSE_ID]/notebooks/day-NN-slug.ipynb#scrollTo=[FIRST_CELL_ID])

---
# Day N · [Day Title]
**certified-journeys / [COURSE_ID]** · [Sub label]

> **Goal for today:** [one sentence — what the learner can do by the end]
```

> **Colab URL:** repo is always `certified-journeys/certified-journeys.github.io`. Path includes full `courses/[COURSE_ID]/notebooks/` prefix. Append `#scrollTo=[FIRST_CELL_ID]`.

Cell 2 — Install (code): `%pip install -q [packages]`

Cells 3–N — For each task, an alternating triple:
1. **Concept (markdown):** one concept, comparison table where helpful, `##` heading with `Step N ·` prefix, max ~15 lines
2. **Code:** working, runnable, inline comments on non-obvious lines
3. **"What just happened?" (markdown):** 3–5 bullets, key insight in bold

Second-to-last — Challenge (code):
```python
# Challenge: [clear instruction]
# Your solution here
# [scaffold — not the full answer]
```

Last — Recap (markdown):
```markdown
---
## Day N key concepts recap
| Concept | What to remember |
|---|---|

> **Tip:** [day tip]

---
## What's next
**Day N+1** → [brief preview]

Mark Day N complete in your [tracker](../index.html).
```

**Depth requirements:**

| Badge | Min code cells | Min markdown cells | Min total lines |
|-------|---------------|-------------------|-----------------|
| `learn` | 5 | 8 | 150 |
| `practice` | 8 | 5 | 200 |
| `review` | 4 | 10 | 150 |
| `exam` (capstone) | 10 | 8 | 250 |

**Code quality rules:**
- All code must run without errors in a fresh Colab environment after the install cell
- No pseudocode, no `# TODO` stubs (except in the Challenge cell)
- Use free local alternatives for paid cloud services (DuckDB not BigQuery, JSONPlaceholder not real APIs) and document the production equivalent
- Import packages at the top of the first code cell that uses them

---

### Notes templates (both types)

**One file per day for every course:** `courses/[COURSE_ID]/notes/day-NN.md`

```markdown
# Day N: [Day Title]

## Notes

_Your notes for today._

## Key takeaways

-

## Questions

-
```

The `📝 notes/day-NN.md` link in each day card points to this file. Users fill it in locally or in their fork.

No Jupyter notebooks are generated for `standard` courses.

---

## Quality checklist

### Both types
- [ ] `broadcastStatus()` writes to `cj_summary_[COURSE_ID]`
- [ ] `STORAGE_KEY` is `cj_[COURSE_ID]_v1`
- [ ] All panels render without JS errors
- [ ] `renderTask(t, di, ti)`, `tickTask(di, ti)`, and `renderRes(r)` helpers present and used
- [ ] `state` includes `tasksDone: {}` and `resetAll()` resets it too
- [ ] Per-day task progress bar (`.task-progress`) appears above each task list
- [ ] Ticking all tasks auto-completes the day; unticking any un-completes it
- [ ] All `{text, url}` objects in `tasks` and `resources` have real, working URLs
- [ ] Every day card has `.nb-row` with a `📝 notes/day-NN.md` link
- [ ] `dayTopics` reverse index is built and `goToDay(i)` function is present
- [ ] Topic pills appear in each day card body (clickable → Topics tab)
- [ ] Topics tab shows clickable day buttons (completed days highlighted green)
- [ ] `renderAI()` has 3 cards with prompts tailored to this course
- [ ] Dark mode CSS variables are correct
- [ ] `.breadcrumb-sep` rule has no trailing `"`
- [ ] `notes/day-01.md` through `notes/day-NN.md` template files generated
- [ ] GitHub sync: `loadState` is `async`, `saveState` calls `GHSync.saveDebounced`
- [ ] GitHub sync: modal (`id="gh-modal"`), sync badge (`id="sync-badge"`) present in HTML
- [ ] GitHub sync: `<script src="../../github-sync.js"></script>` loads before inline script
- [ ] Init is `loadState().then(renderAll)` — not `loadState(); renderAll()`

### `notebook` type only
- [ ] `const NOTEBOOKS` array present, one slug per day
- [ ] Every day card's `.nb-row` has notebook + Colab + notes_by_day.md buttons (3 total)
- [ ] Colab URL repo is `certified-journeys/certified-journeys.github.io`
- [ ] Colab URL path is `/blob/main/courses/[COURSE_ID]/notebooks/[filename].ipynb#scrollTo=[first_cell_id]`
- [ ] `nbformat: 4`, `nbformat_minor: 5` at notebook top level
- [ ] `metadata.language_info.name` is `"python"`
- [ ] Every cell has a unique `"id"` (8-char hex)
- [ ] Every code cell has `"outputs": []` and `"execution_count": null`
- [ ] Notebook filenames match `NOTEBOOKS` array exactly
- [ ] All code cells are runnable (no pseudocode outside Challenge)
- [ ] Challenge cell has scaffold, not full solution

### `standard` type only
- [ ] No `const NOTEBOOKS` array present
- [ ] No `.nb-btn-colab` in HTML or CSS
- [ ] Every day card's `.nb-row` has only the `📝 notes/day-NN.md` button (1 total)

---

## Output file structure

**`notebook` type:**
```
courses/[COURSE_ID]/
  index.html
  notebooks/
    day-01-[slug].ipynb
    ...
    day-NN-[slug].ipynb
  notes/
    day-01.md          ← linked from each day card
    ...
    day-NN.md
```

**`standard` type:**
```
courses/[COURSE_ID]/
  index.html
  notes/
    day-01.md          ← linked from each day card
    ...
    day-NN.md
```

Output each file with a header:

```
## FILE: courses/[COURSE_ID]/index.html
[full content]

## FILE: courses/[COURSE_ID]/notebooks/day-01-[slug].ipynb   ← notebook type only
[full content]

## FILE: courses/[COURSE_ID]/notes/day-01.md                 ← both types
[full content]
```

---

*certified-journeys prompt v6 · two course types · notes/day-NN.md link in every day card · topic ↔ day navigation · per-task tick checkboxes + auto-complete progress bar · GitHub repo sync via PAT*
