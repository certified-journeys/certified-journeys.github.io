# Design System — certified-journeys

## Typography

| Role | Font | Weight | Size |
|------|------|--------|------|
| Body | DM Sans | 400/500 | 15px |
| Headings | DM Sans | 600/700 | variable |
| Monospace | DM Mono | 400/500 | inherit |

No fallback to `Inter`, `Roboto`, `Arial`, or `system-ui` as primary display font.

## Color Tokens

### Base palette (shared across homepage + course pages)
```css
--bg:      #F5F4F0   /* warm off-white page background */
--surface: #FFFFFF   /* card / modal surface */
--surface2: #EEECE5  /* muted fill, hover states */
--surface3: #E8E6DF  /* deeper muted fill */

--border:  rgba(0,0,0,0.08)
--border2: rgba(0,0,0,0.16)

--text:  #18181A    /* primary body text */
--text2: #52524E    /* secondary / metadata */
--text3: #767676    /* muted labels — minimum 4.5:1 contrast on --bg */
```

### Brand color (homepage + shared nav)
```css
--brand:     #1a1a2e   /* dark navy — CJ mark, primary CTAs */
--brand-dim: #eeeef5   /* light navy tint */
```

### Action colors (course pages + card actions)
```css
--green: #16a37f   /* default action / progress green */
--blue:  #2563eb   /* link / info */
```

### Per-course accent colors
Each course has its own `color` and `colorDim`. These are used ONLY on:
- Card icon background/foreground
- Progress bar fill
- Course page headings and accents

Never use per-course colors for navigation, primary CTAs, or shared UI chrome.

| Course | Accent | Dim |
|--------|--------|-----|
| Claude API | `#D97757` | `#FAEDE8` |
| PSPO I | `#16a37f` | `#dcf5ed` |
| AWS ML | `#E8890C` | `#FEF3E2` |
| dlt | `#2563eb` | `#dbeafe` |
| Polars | `#0891B2` | `#E0F5FA` |
| Terraform | `#7F77DD` | `#EEEDFE` |
| Power BI | `#D85A30` | `#FAEDE8` |
| Typer CLI | `#6C47FF` | `#EEE9FF` |
| Hamilton  | `#3B82F6` | `#EFF6FF` |

## Dark Mode

All `--bg`, `--surface`, `--surface2`, `--surface3`, `--border`, `--border2`, `--text`, `--text2`, `--text3`, and per-course `colorDim` values have dark mode overrides via `@media (prefers-color-scheme: dark)`. Always add dark overrides when introducing new color variables.

## Border Radius

```css
--radius:    14px   /* cards, modals, panels */
--radius-sm: 9px    /* smaller panels, stat boxes */
--radius-xs: 5px    /* inline elements */
/* pills / badges: 99px (always) */
```

## Spacing Scale

Use multiples of 4px. Common values: 4, 8, 12, 16, 20, 24, 32, 40, 48.

## Component Rules

### Cards
- Cards earn their existence — use when the card IS the interaction (course nav, day list)
- No decorative card grids where a list would work
- Card border: 0.5px solid `var(--border)` (course pages) or 1px solid `var(--border)` (homepage)
- Hover: `box-shadow: var(--shadow)`, `border-color: var(--border2)`, `transform: translateY(-1px)`

### Buttons
- Primary CTA: dark navy (`var(--brand)`) on homepage; course accent on course pages
- Touch targets: minimum 44px height on interactive buttons
- Always use `aria-label` when button text lacks context (e.g., "Start →" needs the course name)
- Pills: `border-radius: 99px`

### Badges / Status
- `badge-ns` (not started): `--surface2` bg, `--text3` text
- `badge-ip` (in progress): `--blue-dim` bg, `--blue` text
- `badge-done` (completed): `--green-dim` bg, `--green` text

### Progress bars
- Height: 8px (course pages), 3px (homepage cards)
- Fill color: per-course accent
- Background: `var(--surface2)`

### Forms / Modals
- Input focus ring: `box-shadow: 0 0 0 3px rgba(22,163,127,0.12)`, `border-color: var(--green)`
- Modal overlay: `rgba(0,0,0,0.4)` + `backdrop-filter: blur(4px)`
- Modal width: max 400px on homepage modals

## Accessibility

- Body text: minimum 15px
- Muted text (`--text3`): #767676 — minimum 4.5:1 contrast on `--bg: #F5F4F0`
- Touch targets: 44px minimum height on interactive elements
- All action buttons need `aria-label` when text alone is ambiguous
- Form inputs must have visible labels (no placeholder-as-label)
- Keyboard focus: use browser default + enhance with visible `:focus-visible` outline

## Adding a New Course

When adding a course to `COURSES` in `index.html`:
1. Pick a unique `color` + `colorDim` from the per-course palette above (or pick a new pair — warm/saturated accent on white/pastel dim)
2. Use a 2-letter `icon` abbreviation (all-caps)
3. Add a `NEXT_JOURNEY` mapping pointing to a related course
4. Create `courses/<id>/index.html` using the course page template (DM Sans, course accent as `--green`)
5. Update this file with the new course's accent color
