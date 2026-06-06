# TODOs

## Design / UX

- [x] **Mobile nav improvement** — Hid `.sync-ts` timestamp and GitHub link on ≤600px. Nav height stays 56px (acceptable). Bottom action bar deferred — revisit if mobile usage grows.

- [x] **CSS token unification across homepage + course pages** — Homepage now uses `--radius: 14px`, `--radius-sm: 9px`, `--radius-xs: 5px`, and `--surface3`. All `var(--r)` references replaced with `var(--radius)`.

## Possible Features

- [x] **Course category filters** — Domain filter bar added (All / Cloud / AI / Data / Python / Agile / IaC). Each course has a `domains` array. Filter is client-side, zero network requests.
