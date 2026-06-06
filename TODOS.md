# TODOs

## Design / UX

- [ ] **Mobile nav improvement** — The sticky nav is 56px tall (10% of viewport on 375px). No mobile-specific layout changes beyond grid stacking. Revisit when mobile usage is meaningful. Potential directions: reduce nav height on mobile, hide the "☁ Connect" timestamp on mobile, consider a bottom action bar.

- [ ] **CSS token unification across homepage + course pages** — Homepage uses `--r: 14px` and 1px borders; course pages use `--radius: 14px` and 0.5px borders. Font declarations also differ (`link` tag vs shared stylesheet). Align before the 10th course page. See DESIGN.md for the canonical token definitions.

## Possible Features

- [ ] **Course category filters** — Group by domain (Cloud / AI / Data / Agile / IaC). Worth adding at 12+ courses. Premature at 8.
