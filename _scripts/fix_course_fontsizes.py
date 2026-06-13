#!/usr/bin/env python3
"""Increase course page font sizes to match homepage 15px button scale."""
import re
from pathlib import Path

COURSES_DIR = Path(__file__).parent.parent / "courses"

SUBS = [
    # Body font: 15px → 16px
    (r'body\{([^}]*?)font-size:15px', r'body{\g<1>font-size:16px'),
    # Course title h1: bump clamp minimum and preferred
    (r'(\.course-title-block h1\{font-size:)clamp\(18px,2\.2vw\+10px,22px\)', r'\g<1>clamp(20px,2.2vw+10px,24px)'),
    # Also handle pages where fix_responsive already set it and pages with original 22px
    (r'(\.course-title-block h1\{font-size:)22px', r'\g<1>clamp(20px,2.2vw+10px,24px)'),
    # Tab font: 12px → 14px
    (r'(\.tab\{[^}]*?font-size:)12px', r'\g<1>14px'),
    # Task font: 14px → 15px
    (r'(\.task\{[^}]*?font-size:)14px', r'\g<1>15px'),
    # Day title: 15px → 16px (some pages)
    (r'(\.day-title\{[^}]*?font-size:)15px', r'\g<1>16px'),
    # complete-btn: 14px → 15px
    (r'(\.complete-btn\{[^}]*?font-size:)14px', r'\g<1>15px'),
    # breadcrumb: 13px → 14px
    (r'(\.breadcrumb\{[^}]*?font-size:)13px', r'\g<1>14px'),
    # meta-val: 14px → 15px
    (r'(\.meta-val\{[^}]*?font-size:)14px', r'\g<1>15px'),
    # prog-label: 13px → 14px
    (r'(\.prog-label\{[^}]*?font-size:)13px', r'\g<1>14px'),
    # readiness: 13px → 14px
    (r'(\.readiness\{[^}]*?font-size:)13px', r'\g<1>14px'),
    # task-link: existing 11px already raised to 12px, leave
    # exam card body text: 13px → 14px
    (r'(\.exam-card-body\{[^}]*?font-size:)13px', r'\g<1>14px'),
    (r'(\.exam-card-desc\{[^}]*?font-size:)13px', r'\g<1>14px'),
    (r'(\.ai-body\{[^}]*?font-size:)13px', r'\g<1>14px'),
    (r'(\.res-item\{[^}]*?font-size:)13px', r'\g<1>14px'),
]

changed = []

for course_dir in sorted(COURSES_DIR.iterdir()):
    html_file = course_dir / "index.html"
    if not html_file.exists():
        continue

    original = html_file.read_text(encoding="utf-8")
    text = original

    for pattern, replacement in SUBS:
        text = re.sub(pattern, replacement, text)

    if text != original:
        html_file.write_text(text, encoding="utf-8")
        changed.append(course_dir.name)

print(f"Updated {len(changed)} courses:")
for name in changed:
    print(f"  ✓ {name}")
