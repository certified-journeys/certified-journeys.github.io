# Course Design: GitHub Actions for MLOps

## Metadata

```
COURSE_ID:        github-actions-certified
COURSE_FULL_NAME: GitHub Actions for MLOps
ICON:             GA
ACCENT_COLOR:     #24292F
ACCENT_LIGHT:     #F0F2F4
ACCENT_DARK:      #1A1E22
ACCENT_DARK_DIM:  #050607
PROVIDER:         GitHub (Self-paced)
COST:             Free
TOTAL_DAYS:       7
DIFFICULTY:       Intermediate
TAGS:             CI/CD, MLOps, GitHub, Automation, DevOps
EXAM_LINK:        https://skills.github.com/
EXAM_QUESTIONS:   null
EXAM_MINUTES:     null
EXAM_PASS_SCORE:  N/A
EXAM_NOTES:       No formal exam. Seven days building automated ML pipelines with GitHub Actions. Ship a full ML CI/CD pipeline as the capstone.
CAPSTONE_PROJECT: Build a complete ML CI/CD pipeline in GitHub Actions: on every push to main, run pytest on the training code, train a sklearn model, evaluate it against a baseline threshold, push the model artifact to GitHub Releases if it passes, and post a summary comment on the PR with accuracy and a confusion matrix rendered as a markdown table.
```

## AI Deep Dive Topics (3 cards)

1. **GitHub Actions runner architecture** — the difference between GitHub-hosted runners (ephemeral VMs reset after every job, billed per minute) and self-hosted runners (persistent, GPU-capable, zero billed minutes), and why ephemeral runners make secret injection safe but make model weight caching expensive — and how `actions/cache` with a deterministic cache key bridges the gap.

2. **Reusable workflow vs composite action vs action.yml** — when each abstraction is the right choice: reusable workflows (`workflow_call`) for full job-level isolation with their own runner and environment, composite actions for step-level reuse within the calling job's runner, and `action.yml` published to the Marketplace for cross-org sharing — and the one thing only reusable workflows can do: inherit secrets with `secrets: inherit`.

3. **ML pipeline security with OIDC** — how to scope `GITHUB_TOKEN` permissions to least-privilege (`contents: read`, `packages: write`), why environment protection rules block accidental prod deployments by requiring manual approval, and how OpenID Connect (OIDC) lets a workflow authenticate to AWS or GCP without storing long-lived credentials as repository secrets.

## Notebooks

```
NOTEBOOKS:
  day-01-actions-fundamentals
  day-02-yaml-syntax
  day-03-reusable-workflows
  day-04-matrix-and-caching
  day-05-secrets-and-security
  day-06-ml-cicd-patterns
  day-07-capstone-ml-pipeline
```

## Days

### Day 1 — GitHub Actions Fundamentals: Workflows, Jobs, Steps, and Triggers
**Badge:** learn
**Tasks:**
- Read the GitHub Actions quickstart guide [https://docs.github.com/en/actions/writing-workflows/quickstart]
- Create a hello-world workflow: one job, one step, triggered on push to main
- Add a second job that depends on the first using `needs:` and inspect the job graph in the Actions UI
- Trigger the same workflow on `push`, `pull_request`, and `workflow_dispatch` — observe which events fire
- Read the events that trigger workflows reference [https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows]
**Resources:**
- GitHub Actions Quickstart [https://docs.github.com/en/actions/writing-workflows/quickstart]
- Events That Trigger Workflows [https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows]
- GitHub Skills — Introduction to GitHub Actions [https://skills.github.com/]
**Tip:** "Jobs run in parallel by default. `needs:` is the only thing that serializes them. If you forget `needs:`, your deploy job will race your test job — and sometimes win."

### Day 2 — YAML Syntax Deep Dive: on, jobs, steps, uses, with, env
**Badge:** learn
**Tasks:**
- Read the workflow syntax reference [https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions]
- Write a workflow that sets environment variables at three levels: workflow, job, and step — verify precedence
- Use `actions/checkout@v4` and `actions/setup-python@v5` with explicit `with:` inputs
- Add a `run:` step with a multi-line shell script using the `|` YAML literal block scalar
- Read the contexts and expressions reference and write a step that uses `${{ github.actor }}` [https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/contexts]
**Resources:**
- Workflow Syntax Reference [https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions]
- Contexts and Expressions [https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/contexts]
- actions/checkout [https://github.com/actions/checkout]
**Tip:** "YAML indentation errors are the #1 cause of 'workflow file is invalid' errors. Always use 2-space indentation, never tabs, and validate locally with `actionlint` before pushing."

### Day 3 — Reusable Workflows and Composite Actions
**Badge:** practice
**Tasks:**
- Read the reusable workflows guide [https://docs.github.com/en/actions/sharing-automations/reusing-workflows]
- Extract a lint + test job into a reusable workflow triggered by `workflow_call` with one input and one secret
- Call the reusable workflow from two separate caller workflows and verify both pass
- Read the composite actions guide [https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-composite-action]
- Build a composite action that installs Python dependencies and caches them — use it in 3 steps of a single job
**Resources:**
- Reusing Workflows [https://docs.github.com/en/actions/sharing-automations/reusing-workflows]
- Creating a Composite Action [https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-composite-action]
- GitHub Actions Best Practices [https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions]
**Tip:** "Use reusable workflows when you need a full job with its own runner and environment isolation. Use composite actions when you just need to share a few steps inside a job. The key difference: only reusable workflows can use `secrets: inherit`."

### Day 4 — Matrix Strategies and Dependency Caching
**Badge:** practice
**Tasks:**
- Read the matrix strategy documentation [https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/running-variations-of-jobs-in-a-matrix]
- Build a matrix that tests across Python 3.10, 3.11, 3.12 and Ubuntu + macOS — verify 6 parallel jobs fire
- Add `fail-fast: false` and `max-parallel: 3` and observe the difference in job behavior
- Read the caching dependencies guide [https://docs.github.com/en/actions/writing-workflows/caching-dependencies-to-speed-up-workflows]
- Add `actions/cache` with a pip cache key based on `hashFiles('**/requirements.txt')` — verify cache hit on second run
**Resources:**
- Matrix Strategy Docs [https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/running-variations-of-jobs-in-a-matrix]
- Caching Dependencies [https://docs.github.com/en/actions/writing-workflows/caching-dependencies-to-speed-up-workflows]
- actions/cache [https://github.com/actions/cache]
**Tip:** "Cache keys must be deterministic and specific. A key like `${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}` hits only when the exact requirements file matches. Add a `restore-keys:` fallback for partial hits when requirements change."

### Day 5 — Secrets Management and Security Best Practices
**Badge:** practice
**Tasks:**
- Read the encrypted secrets guide [https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions]
- Add a repository secret and consume it in a workflow step — verify it is masked in logs
- Read the security hardening guide [https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions]
- Scope `GITHUB_TOKEN` permissions to least-privilege using the `permissions:` key at the job level
- Read the OIDC guide and write a workflow step that authenticates to a cloud provider without stored secrets [https://docs.github.com/en/actions/security-for-github-actions/security-guides/about-security-hardening-with-openid-connect]
**Resources:**
- Using Secrets in GitHub Actions [https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions]
- Security Hardening for GitHub Actions [https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions]
- About OIDC with GitHub Actions [https://docs.github.com/en/actions/security-for-github-actions/security-guides/about-security-hardening-with-openid-connect]
**Tip:** "Never echo a secret directly. GitHub masks registered secrets in logs, but `echo $MY_SECRET | base64` will print it unmasked. Pass secrets via environment variables to subprocess calls, never via positional arguments."

### Day 6 — ML-Specific Patterns: Training, Evaluation, and Model Registry
**Badge:** practice
**Tasks:**
- Read the GitHub Releases API documentation for uploading artifacts [https://docs.github.com/en/rest/releases/assets]
- Write a workflow that trains a sklearn model on push to main and uploads the `.pkl` file as a release asset
- Add an evaluation step that fails the workflow if accuracy drops below a threshold — block the merge
- Read the DVC GitHub Actions integration guide [https://dvc.org/doc/start/data-management/data-versioning]
- Add a step that posts a PR comment with the evaluation results using `actions/github-script` [https://github.com/actions/github-script]
**Resources:**
- GitHub Releases — Uploading Assets [https://docs.github.com/en/rest/releases/assets]
- DVC — Data Versioning with GitHub Actions [https://dvc.org/doc/start/data-management/data-versioning]
- actions/github-script [https://github.com/actions/github-script]
**Tip:** "Use `softprops/action-gh-release` to upload model artifacts to GitHub Releases — it handles asset uploads and tag creation in one step. Pin it to a commit SHA, not a tag, to prevent supply chain attacks."

### Day 7 — Capstone: Full ML CI/CD Pipeline
**Badge:** exam
**Tasks:**
- Design the full pipeline on paper: triggers, jobs, steps, artifacts, and quality gates
- Write the test job: run `pytest tests/` and fail fast if any test fails
- Write the train job: depends on test, trains sklearn model, saves `.pkl` artifact with `actions/upload-artifact`
- Write the evaluate job: downloads the artifact, scores it on a held-out set, fails if accuracy < threshold
- Write the release job: depends on evaluate, uploads `.pkl` to GitHub Releases using `softprops/action-gh-release`
- Write a PR comment step using `actions/github-script` that posts accuracy and a confusion matrix markdown table
**Resources:**
- actions/upload-artifact and download-artifact [https://github.com/actions/upload-artifact]
- softprops/action-gh-release [https://github.com/softprops/action-gh-release]
- actions/github-script [https://github.com/actions/github-script]
**Tip:** "The hardest part of the capstone is passing the model artifact between jobs. Use `actions/upload-artifact` in the train job and `actions/download-artifact` in evaluate and release. Both must reference the exact same artifact name."

## Topics

```
Topic 1: Fundamentals — color #24292F — Days 0,1
Topic 2: YAML and Syntax — color teal — Days 1,2
Topic 3: Reuse Patterns — color purple — Days 2,3
Topic 4: Performance and Security — color orange — Days 3,4
Topic 5: ML Patterns and Capstone — color amber — Days 5,6
```
