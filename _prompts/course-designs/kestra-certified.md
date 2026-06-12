# Kestra — Course Design
Generated: 2026-06-07

```
COURSE_TYPE:      notebook
COURSE_ID:        kestra-certified
COURSE_FULL_NAME: Kestra for Data Engineers
ICON:             KS
ACCENT_COLOR:     #6366F1
ACCENT_LIGHT:     #EEF2FF
ACCENT_DARK:      #4338CA
ACCENT_DARK_DIM:  #0D0A2E
PROVIDER:         Kestra (Self-paced)
COST:             Free
TOTAL_DAYS:       10
DIFFICULTY:       Intermediate
TAGS:             Orchestration, Workflows, Python, Data Engineering
EXAM_LINK:        https://kestra.io/docs/
EXAM_QUESTIONS:   null
EXAM_MINUTES:     null
EXAM_PASS_SCORE:  N/A
EXAM_NOTES:       No formal exam. Complete all 10 days and the capstone workflow to demonstrate proficiency.

NOTEBOOKS:
  day-01-kestra-concepts
  day-02-first-flow
  day-03-tasks-plugins
  day-04-triggers-scheduling
  day-05-inputs-outputs
  day-06-error-handling
  day-07-subflows-namespaces
  day-08-secrets-variables
  day-09-python-scripts
  day-10-capstone-pipeline

DAYS:
  Day 1:
    Title: Kestra Concepts — Declarative Orchestration Explained
    Badge: learn
    Tasks:
      - {text: "Read the Kestra introduction and core concepts", url: "https://kestra.io/docs/getting-started/"}
      - Understand Kestra's key entities: Flows, Tasks, Triggers, Executions, and Namespaces
      - {text: "Read the Kestra architecture overview — server, worker, and executor components", url: "https://kestra.io/docs/architecture/"}
      - Compare Kestra's YAML-first approach to code-first orchestrators (Airflow, Prefect)
      - {text: "Install Kestra locally with Docker: docker run --pull=always --rm -it -p 8080:8080 kestra/kestra:latest server local", url: "https://kestra.io/docs/getting-started/quickstart"}
      - Explore the Kestra UI: flows list, executions log, topology view
    Resources:
      - {text: "Kestra Getting Started", url: "https://kestra.io/docs/getting-started/"}
      - {text: "Kestra Architecture", url: "https://kestra.io/docs/architecture/"}
      - {text: "Kestra Concepts Glossary", url: "https://kestra.io/docs/concepts/"}
    Tip: "Kestra's YAML-first design means your entire workflow is version-controlled, reviewable in a PR, and executable by anyone who can run Docker — no Python environment to manage."
    hasScore: false

  Day 2:
    Title: Your First Flow — YAML Structure and Hello World
    Badge: learn
    Tasks:
      - {text: "Read the Kestra flow syntax reference", url: "https://kestra.io/docs/workflow-components/flow"}
      - Write a minimal flow with id, namespace, and a single Log task
      - {text: "Understand required fields: id, namespace, tasks", url: "https://kestra.io/docs/workflow-components/flow#flow-properties"}
      - Add a description and labels to the flow for discoverability
      - Chain two tasks in sequence and observe the execution graph in the UI topology view
      - {text: "Read about task properties: id, type, and task-specific configuration", url: "https://kestra.io/docs/workflow-components/tasks"}
      - Export the flow YAML and import it into a different namespace
    Resources:
      - {text: "Kestra Flow Syntax", url: "https://kestra.io/docs/workflow-components/flow"}
      - {text: "Kestra Task Reference", url: "https://kestra.io/docs/workflow-components/tasks"}
      - {text: "Kestra Hello World Tutorial", url: "https://kestra.io/docs/getting-started/quickstart"}
    Tip: "Every Kestra flow is a YAML file. The id + namespace pair is the unique key — keep namespaces hierarchical (e.g. company.team.project) to group related flows."
    hasScore: false

  Day 3:
    Title: Tasks and Plugins — Shell, Python, HTTP, and More
    Badge: learn
    Tasks:
      - {text: "Browse the Kestra plugin library", url: "https://kestra.io/plugins/"}
      - Use io.kestra.plugin.core.log.Log to emit structured messages during execution
      - {text: "Run a Bash script with io.kestra.plugin.scripts.shell.Commands", url: "https://kestra.io/plugins/plugin-script-shell"}
      - Fetch a public JSON API with io.kestra.plugin.core.http.Request and log the response body
      - {text: "Read about the Python script task and how Kestra manages virtualenvs", url: "https://kestra.io/plugins/plugin-script-python"}
      - Run a Python task that imports pandas and prints a DataFrame summary
      - Explore task output variables: understand how outputs.taskId.vars work
    Resources:
      - {text: "Kestra Plugin Library", url: "https://kestra.io/plugins/"}
      - {text: "Kestra Shell Plugin", url: "https://kestra.io/plugins/plugin-script-shell"}
      - {text: "Kestra Python Plugin", url: "https://kestra.io/plugins/plugin-script-python"}
    Tip: "Kestra manages Python virtualenvs automatically per task — no pip install needed in the flow. Declare dependencies in the task's requirements list and Kestra caches them."
    hasScore: false

  Day 4:
    Title: Triggers and Scheduling — Time, Event, and Webhook
    Badge: practice
    Tasks:
      - {text: "Read the Kestra triggers documentation", url: "https://kestra.io/docs/workflow-components/triggers"}
      - Add a Schedule trigger with a cron expression (e.g. 0 9 * * 1-5 for weekdays at 9am)
      - {text: "Read about backfill execution for catching up missed scheduled runs", url: "https://kestra.io/docs/workflow-components/triggers/schedule-trigger"}
      - Add a Webhook trigger and test it by sending a POST request with curl
      - {text: "Read about Flow triggers — trigger a flow when another flow completes", url: "https://kestra.io/docs/workflow-components/triggers/flow-trigger"}
      - Create a downstream flow that triggers on the success of an upstream flow
      - Use trigger metadata ({{ trigger.date }}) in task commands to reference the scheduled time
    Resources:
      - {text: "Kestra Triggers", url: "https://kestra.io/docs/workflow-components/triggers"}
      - {text: "Kestra Schedule Trigger", url: "https://kestra.io/docs/workflow-components/triggers/schedule-trigger"}
      - {text: "Kestra Webhook Trigger", url: "https://kestra.io/docs/workflow-components/triggers/webhook-trigger"}
    Tip: "Use {{ trigger.date | date('yyyy-MM-dd') }} in your task command to make it idempotent — the same flow run produces the same output regardless of when you trigger it manually vs on schedule."
    hasScore: false

  Day 5:
    Title: Inputs, Outputs, and Passing Data Between Tasks
    Badge: practice
    Tasks:
      - {text: "Read the Kestra inputs documentation", url: "https://kestra.io/docs/workflow-components/inputs"}
      - Define typed inputs (STRING, INT, BOOLEAN, FILE) and provide defaults
      - Reference an input in a task: {{ inputs.my_param }}
      - {text: "Read about task outputs and how to reference them downstream", url: "https://kestra.io/docs/workflow-components/outputs"}
      - Pass the output of a Python task to a Shell task via {{ outputs.taskId.vars.result }}
      - {text: "Use internal storage to pass large files between tasks", url: "https://kestra.io/docs/developer-guide/storage"}
      - Write a flow where Task A generates a CSV, Task B reads it, Task C uploads the result
    Resources:
      - {text: "Kestra Inputs", url: "https://kestra.io/docs/workflow-components/inputs"}
      - {text: "Kestra Outputs", url: "https://kestra.io/docs/workflow-components/outputs"}
      - {text: "Kestra Internal Storage", url: "https://kestra.io/docs/developer-guide/storage"}
    Tip: "Kestra's internal storage is an S3-compatible object store. Large outputs (files, DataFrames) are automatically stored there and referenced by URI — you never need to worry about serialization."
    hasScore: false

  Day 6:
    Title: Error Handling — Retries, Timeouts, and Failure Flows
    Badge: review
    Tasks:
      - {text: "Read the Kestra error handling documentation", url: "https://kestra.io/docs/workflow-components/errors"}
      - Add retry configuration to a task: maxAttempts, delay, and multiplier for exponential backoff
      - Set a task-level timeout and observe the TIMEOUT execution state
      - {text: "Read about flow-level error handlers with errors: tasks", url: "https://kestra.io/docs/workflow-components/errors#flow-level-error-handlers"}
      - Add an errors: block that sends an alert notification when the flow fails
      - {text: "Use allowFailure: true to continue the flow when a non-critical task fails", url: "https://kestra.io/docs/workflow-components/tasks#task-properties"}
      - Test the full error handling path by intentionally failing a task
    Resources:
      - {text: "Kestra Error Handling", url: "https://kestra.io/docs/workflow-components/errors"}
      - {text: "Kestra Task Retries", url: "https://kestra.io/docs/workflow-components/retries"}
      - {text: "Kestra Execution States", url: "https://kestra.io/docs/concepts/execution"}
    Tip: "Use exponential backoff (multiplier: 2.0) for network-dependent tasks — a 5-second base delay with 3 retries gives you 5s, 10s, 20s before failing. This handles transient API rate limits gracefully."
    hasScore: false

  Day 7:
    Title: Subflows and Namespaces — Modular Workflow Design
    Badge: review
    Tasks:
      - {text: "Read about subflows in Kestra", url: "https://kestra.io/docs/workflow-components/subflows"}
      - Extract a reusable extract-and-validate sequence into a child flow
      - Call the child flow with io.kestra.plugin.core.flow.Subflow and pass inputs
      - {text: "Understand namespace inheritance and how parent namespaces share variables", url: "https://kestra.io/docs/workflow-components/namespace-files"}
      - Organize flows into a hierarchy: data.ingestion, data.transformation, data.reporting
      - {text: "Read about namespace files — YAML, Python, and SQL files stored at the namespace level", url: "https://kestra.io/docs/workflow-components/namespace-files"}
      - Reference a namespace file in a Python task using the {{ flow.namespace }} variable
    Resources:
      - {text: "Kestra Subflows", url: "https://kestra.io/docs/workflow-components/subflows"}
      - {text: "Kestra Namespace Files", url: "https://kestra.io/docs/workflow-components/namespace-files"}
      - {text: "Kestra Flow Design Patterns", url: "https://kestra.io/docs/developer-guide/"}
    Tip: "Design subflows like functions: a single responsibility, typed inputs, and predictable outputs. A subflow for 'validate a CSV schema' can be reused by 10 parent flows without duplication."
    hasScore: false

  Day 8:
    Title: Secrets, Variables, and Environment Configuration
    Badge: review
    Tasks:
      - {text: "Read the Kestra secrets documentation", url: "https://kestra.io/docs/concepts/secret"}
      - Store a secret in Kestra and reference it in a task: {{ secret('MY_API_KEY') }}
      - {text: "Read about Kestra variables for reusable non-secret values", url: "https://kestra.io/docs/workflow-components/variables"}
      - Define namespace-level variables and reference them across multiple flows
      - Use Pebble template expressions to transform variable values: {{ vars.env | upper }}
      - {text: "Read about environment variables and how to pass them to script tasks", url: "https://kestra.io/docs/workflow-components/tasks#environment-variables"}
      - Parameterise a flow for dev/staging/prod environments using a single ENV input
    Resources:
      - {text: "Kestra Secrets", url: "https://kestra.io/docs/concepts/secret"}
      - {text: "Kestra Variables", url: "https://kestra.io/docs/workflow-components/variables"}
      - {text: "Kestra Pebble Templating", url: "https://kestra.io/docs/concepts/pebble"}
    Tip: "Never hardcode credentials in flow YAML. Use {{ secret('NAME') }} for sensitive values and namespace variables for environment-specific config. Both are masked in execution logs."
    hasScore: false

  Day 9:
    Title: Python Scripts — Tasks, Docker, and Working with Data
    Badge: practice
    Tasks:
      - {text: "Read the Python script task deep-dive", url: "https://kestra.io/plugins/plugin-script-python"}
      - Write a Python task that uses pandas to read a public CSV and compute summary statistics
      - Pass the summary as a JSON output variable back to Kestra using Kestra.outputs()
      - {text: "Run a Python task in a Docker container with a custom image", url: "https://kestra.io/plugins/plugin-script-python#runner"}
      - Use the PROCESS runner vs DOCKER runner and understand the trade-offs
      - Write a multi-file Python task using inputFiles to pass helper modules
      - Chain two Python tasks where the second reads the output of the first
    Resources:
      - {text: "Kestra Python Plugin", url: "https://kestra.io/plugins/plugin-script-python"}
      - {text: "Kestra Script Runner Options", url: "https://kestra.io/plugins/plugin-script-python#runner"}
      - {text: "Kestra Output Variables", url: "https://kestra.io/docs/workflow-components/outputs"}
    Tip: "Use Kestra.outputs({'key': value}) at the end of your Python script to expose computed values to downstream tasks. The Kestra runtime injects this function automatically — no import needed."
    hasScore: false

  Day 10:
    Title: Capstone — End-to-End Data Pipeline with Kestra
    Badge: exam
    Tasks:
      - Design a complete data pipeline: ingest public CSV from HTTP → validate schema → transform with Python → export summary → alert on completion
      - Implement the ingestion task using io.kestra.plugin.core.http.Download to fetch a public dataset
      - Write a Python validation task that checks column names, row count, and null percentage
      - Write a Python transformation task that computes aggregations and outputs a summary CSV
      - Export the summary to a local path using io.kestra.plugin.core.storage.LocalFiles
      - Add retry (maxAttempts: 3) to the ingestion task and a flow-level error handler
      - Add a Schedule trigger (daily at 7am) and parameterise the source URL as an input
      - {text: "Review the Kestra best practices guide before submitting", url: "https://kestra.io/docs/developer-guide/"}
    Resources:
      - {text: "Kestra Developer Guide", url: "https://kestra.io/docs/developer-guide/"}
      - {text: "Kestra Plugin Library", url: "https://kestra.io/plugins/"}
      - {text: "Kestra Flow Examples", url: "https://github.com/kestra-io/blueprints"}
    Tip: "A complete Kestra pipeline is just a YAML file. Use namespace variables for environment-specific config, secrets for credentials, and subflows for reusable stages — and the whole thing fits in a git repo."
    hasScore: true

TOPICS:
  Topic 1:
    Name: Core Concepts
    Color: indigo
    Days: 0, 1, 2   # Days 1–3 (0-indexed)

  Topic 2:
    Name: Triggers & Data Flow
    Color: blue
    Days: 3, 4      # Days 4–5 (0-indexed)

  Topic 3:
    Name: Reliability
    Color: purple
    Days: 5, 6      # Days 6–7 (0-indexed)

  Topic 4:
    Name: Configuration
    Color: orange
    Days: 7         # Day 8 (0-indexed)

  Topic 5:
    Name: Python Integration
    Color: teal
    Days: 8         # Day 9 (0-indexed)

  Topic 6:
    Name: Capstone Project
    Color: indigo
    Days: 9         # Day 10 (0-indexed)
```
