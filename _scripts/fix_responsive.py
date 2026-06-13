#!/usr/bin/env python3
"""Make all course index.html pages responsive — fluid headings, 12px minimum labels."""
import re
from pathlib import Path

COURSES_DIR = Path(__file__).parent.parent / "courses"

# CSS substitutions: (pattern, replacement)
SUBS = [
    # Fluid course title
    (r'(\.course-title-block h1\{font-size:)20px', r'\g<1>clamp(18px,2.2vw+10px,22px)'),
    # Fluid progress percentage
    (r'(\.prog-pct\{font-size:)22px', r'\g<1>clamp(18px,1.8vw+11px,22px)'),
    # Raise 10px labels → 12px (skip checkmark icon handled separately)
    (r'(\.meta-label\{[^}]*font-size:)10px', r'\g<1>12px'),
    (r'(\.stat-label\{[^}]*font-size:)10px', r'\g<1>12px'),
    (r'(\.day-badge\{[^}]*font-size:)10px', r'\g<1>12px'),
    (r'(\.day-topic-pill\{[^}]*font-size:)10px', r'\g<1>12px'),
    (r'(\.exam-card-label\{[^}]*font-size:)10px', r'\g<1>12px'),
    (r'(\.score-badge\{[^}]*font-size:)10px', r'\g<1>12px'),
    (r'(\.brand-mark\{[^}]*font-size:)10px', r'\g<1>12px'),
    # Raise 11px labels → 12px
    (r'(\.hero-eyebrow\{[^}]*font-size:)11px', r'\g<1>12px'),
    (r'(\.res-pill\{[^}]*font-size:)11px', r'\g<1>12px'),
    (r'(\.task-link\{[^}]*font-size:)11px', r'\g<1>12px'),
    (r'(\.bar-row\{[^}]*font-size:)11px', r'\g<1>12px'),
    (r'(\.sync-ts\{[^}]*font-size:)10px', r'\g<1>11px'),
    # Larger brand mark icon container
    (r'(\.brand-mark\{width:)30px;height:30px', r'\g<1>32px;height:32px'),
]

# Responsive CSS block to inject before </style>
RESPONSIVE_CSS = """
@media(max-width:640px){
  body{font-size:16px;}
  .course-title-block h1{font-size:clamp(17px,5vw,22px);}
  .tab{font-size:14px;padding:8px 16px;}
  .day-title{font-size:15px;}
  .task{font-size:14px;}
  .complete-btn{font-size:14px;padding:11px;}
  .exam-card-label{font-size:12px;}
  .meta-val{font-size:13px;}
  .nav-brand{font-size:14px;}
}
@media(max-width:400px){
  .course-title-block h1{font-size:17px;}
  .day-title{font-size:14px;}
  .task{font-size:13px;}
  .stats-row{gap:1rem;}
}"""

changed = []
skipped = []

for course_dir in sorted(COURSES_DIR.iterdir()):
    html_file = course_dir / "index.html"
    if not html_file.exists():
        skipped.append(course_dir.name)
        continue

    original = html_file.read_text(encoding="utf-8")
    text = original

    # Apply substitutions
    for pattern, replacement in SUBS:
        text = re.sub(pattern, replacement, text)

    # Inject responsive block before </style> (only if not already present)
    if "@media(max-width:640px)" not in text:
        text = text.replace("</style>", RESPONSIVE_CSS + "\n</style>", 1)

    if text != original:
        html_file.write_text(text, encoding="utf-8")
        changed.append(course_dir.name)
    else:
        skipped.append(course_dir.name)

print(f"Updated {len(changed)} courses:")
for name in changed:
    print(f"  ✓ {name}")
if skipped:
    print(f"\nSkipped {len(skipped)}:")
    for name in skipped:
        print(f"  - {name}")
