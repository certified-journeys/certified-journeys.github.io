# Prefect for Data Engineers — Course Design
Generated: 2026-06-07

```
COURSE_TYPE:      notebook
COURSE_ID:        prefect-certified
COURSE_FULL_NAME: Prefect for Data Engineers
ICON:             PF
ACCENT_COLOR:     #2563EB
ACCENT_LIGHT:     #EFF6FF
ACCENT_DARK:      #1D4ED8
ACCENT_DARK_DIM:  #0A1A3E
PROVIDER:         Prefect (Self-paced)
COST:             Free
TOTAL_DAYS:       14
DIFFICULTY:       Intermediate
TAGS:             MLOps, Python, Workflows, Data Engineering
EXAM_LINK:        https://docs.prefect.io/latest/
EXAM_QUESTIONS:   null
EXAM_MINUTES:     null
EXAM_PASS_SCORE:  N/A
EXAM_NOTES:       No formal exam. Build the capstone pipeline to demonstrate proficiency.

NOTEBOOKS:
  day-01-intro-prefect
  day-02-flows-tasks
  day-03-task-dependencies
  day-04-retries-caching
  day-05-subflows-modular
  day-06-results-artifacts
  day-07-deployments-basics
  day-08-work-pools-workers
  day-09-schedules-automations
  day-10-prefect-cloud-server
  day-11-notifications-states
  day-12-docker-kubernetes
  day-13-review-advanced
  day-14-capstone-etl-pipeline

DAYS:
  Day 1:
    Title: Introduction to Prefect: From Script to Workflow
    Badge: learn
    Tasks:
      - {text: "Read the Prefect Getting Started overview", url: "https://docs.prefect.io/latest/getting-started/quickstart/"}
      - Install Prefect locally: pip install prefect
      - Start the local Prefect server with prefect server start and open the UI at http://127.0.0.1:4200
      - Convert a plain Python function into a flow by adding the @flow decorator and run it
      - Observe the flow run appear in the Prefect UI — inspect state, logs, and duration
    Resources:
      - {text: "Prefect Quickstart", url: "https://docs.prefect.io/latest/getting-started/quickstart/"}
      - {text: "Prefect Concepts Overview", url: "https://docs.prefect.io/latest/concepts/"}
      - {text: "Prefect GitHub Repository", url: "https://github.com/PrefectHQ/prefect"}
    Tip: "Prefect's biggest win over raw scripts is automatic state tracking — every run, whether it succeeds or fails, gets a persistent record you can query later."
    hasScore: false

  Day 2:
    Title: Flows and Tasks — The Building Blocks
    Badge: learn
    Tasks:
      - {text: "Read the Prefect flows and tasks documentation", url: "https://docs.prefect.io/latest/concepts/flows/"}
      - Add the @task decorator to individual units of work inside a flow
      - Understand task vs flow distinction: flows orchestrate, tasks execute
      - Pass return values from one task as arguments to another to create dependencies
      - Use flow_run.name and task_run.name in the UI to trace exactly which code ran
      - Inspect the task run graph in the Prefect UI Runs view
    Resources:
      - {text: "Prefect Flows Docs", url: "https://docs.prefect.io/latest/concepts/flows/"}
      - {text: "Prefect Tasks Docs", url: "https://docs.prefect.io/latest/concepts/tasks/"}
      - {text: "Prefect Tutorial", url: "https://docs.prefect.io/latest/tutorial/"}
    Tip: "Keep tasks small and single-purpose — a task that does one thing is easy to retry, cache, and test independently."
    hasScore: false

  Day 3:
    Title: Task Dependencies and Data Passing
    Badge: learn
    Tasks:
      - {text: "Read about task dependencies and futures", url: "https://docs.prefect.io/latest/concepts/tasks/#task-results"}
      - Build a flow with a linear chain of 4+ tasks where each passes data to the next
      - Use PrefectFuture to submit tasks concurrently with task.submit() and task.map()
      - Call task.result() to block and collect values from concurrent submissions
      - Use wait_for parameter to express non-data dependencies between tasks
      - Run the flow and observe the parallel vs sequential task timelines in the UI
    Resources:
      - {text: "Task Concurrency with .submit()", url: "https://docs.prefect.io/latest/concepts/tasks/#concurrency"}
      - {text: "Task Results and Futures", url: "https://docs.prefect.io/latest/concepts/tasks/#task-results"}
      - {text: "Prefect API Reference", url: "https://prefect-python-sdk-docs.netlify.app/"}
    Tip: "Use task.submit() instead of calling tasks directly when you want non-blocking, concurrent execution — Prefect will respect data-dependency order automatically."
    hasScore: false

  Day 4:
    Title: Retries, Timeouts, and Caching with cache_key_fn
    Badge: practice
    Tasks:
      - {text: "Read the retries and caching documentation", url: "https://docs.prefect.io/latest/concepts/tasks/#retries"}
      - Add retries=3 and retry_delay_seconds=10 to a task that simulates transient failures
      - Set a timeout_seconds limit on a long-running task and observe the TaskRunTimeout state
      - Enable task result caching with cache_key_fn=task_input_hash and verify the cache hit in the UI
      - Implement a custom cache_key_fn that incorporates an external file's modification time
      - Test cache expiry with cache_expiration=timedelta(minutes=5)
    Resources:
      - {text: "Retries Docs", url: "https://docs.prefect.io/latest/concepts/tasks/#retries"}
      - {text: "Caching Docs", url: "https://docs.prefect.io/latest/concepts/tasks/#caching"}
      - {text: "task_input_hash API", url: "https://docs.prefect.io/latest/api-ref/prefect/tasks/#prefect.tasks.task_input_hash"}
    Tip: "task_input_hash hashes all task arguments — if inputs haven't changed, the task is skipped entirely and returns the cached result. Use it aggressively for expensive data fetching steps."
    hasScore: false

  Day 5:
    Title: Subflows and Modular Pipeline Design
    Badge: learn
    Tasks:
      - {text: "Read about subflows and nested flows", url: "https://docs.prefect.io/latest/concepts/flows/#composing-flows"}
      - Refactor a large flow into a parent flow that calls two @flow-decorated subflows
      - Pass parameters between the parent flow and subflows using function arguments
      - Understand how subflow states bubble up to affect the parent flow state
      - Use return_state=True to inspect a subflow's final state programmatically
      - Observe the subflow run hierarchy in the Prefect UI Runs view
    Resources:
      - {text: "Composing Flows (Subflows)", url: "https://docs.prefect.io/latest/concepts/flows/#composing-flows"}
      - {text: "Flow Run States", url: "https://docs.prefect.io/latest/concepts/states/"}
      - {text: "Prefect Design Patterns", url: "https://discourse.prefect.io/"}
    Tip: "Break large pipelines into subflows by domain (ingest, transform, load) — each subflow can be scheduled, tested, and retried independently."
    hasScore: false

  Day 6:
    Title: Results, Artifacts, and State Persistence
    Badge: practice
    Tasks:
      - {text: "Read the Prefect results and storage documentation", url: "https://docs.prefect.io/latest/concepts/results/"}
      - Configure a LocalFileSystemResultStorage to persist task results to disk between runs
      - Use persist_result=True on a task and verify the result file is written
      - Create a Prefect artifact with create_table_artifact() to publish a Markdown summary visible in the UI
      - Create a link artifact with create_link_artifact() pointing to an external data source
      - Understand the difference between task results (for pipeline wiring) and artifacts (for human-readable reporting)
    Resources:
      - {text: "Results Docs", url: "https://docs.prefect.io/latest/concepts/results/"}
      - {text: "Artifacts Docs", url: "https://docs.prefect.io/latest/concepts/artifacts/"}
      - {text: "Result Storage Backends", url: "https://docs.prefect.io/latest/concepts/results/#result-storage"}
    Tip: "Artifacts are surfaced directly in the Prefect UI alongside each run — use create_markdown_artifact() to publish a human-readable summary of what your pipeline produced."
    hasScore: false

  Day 7:
    Title: Prefect Deployments — Packaging Flows for Scheduled Execution
    Badge: practice
    Tasks:
      - {text: "Read the deployments documentation", url: "https://docs.prefect.io/latest/concepts/deployments/"}
      - Create a deployment from Python using flow.from_source().deploy() with a local storage block
      - Understand the deployment manifest: flow_name, entrypoint, parameters, schedule, work_pool
      - Run the deployment from the UI by clicking the Quick Run button
      - Override deployment parameters at run time using the UI parameter form or prefect deployment run
      - Inspect deployment run history and compare multiple runs side-by-side in the UI
    Resources:
      - {text: "Deployments Overview", url: "https://docs.prefect.io/latest/concepts/deployments/"}
      - {text: "Deploying Flows Guide", url: "https://docs.prefect.io/latest/tutorial/deployments/"}
      - {text: "prefect deployment CLI", url: "https://docs.prefect.io/latest/api-ref/cli/deployment/"}
    Tip: "A deployment is the bridge between your flow code and its runtime environment — define it once and you can trigger it from the UI, CLI, API, or a schedule."
    hasScore: false

  Day 8:
    Title: Work Pools and Workers — Local, Docker, and Subprocess
    Badge: practice
    Tasks:
      - {text: "Read the work pools and workers documentation", url: "https://docs.prefect.io/latest/concepts/work-pools/"}
      - Create a local process work pool with prefect work-pool create --type process my-pool
      - Start a worker that polls the pool: prefect worker start --pool my-pool
      - Deploy a flow to the work pool and verify the worker picks it up
      - Create a Docker work pool and configure it to run flows in a container image
      - Understand the polling interval and how workers fetch work items from the pool queue
    Resources:
      - {text: "Work Pools Docs", url: "https://docs.prefect.io/latest/concepts/work-pools/"}
      - {text: "Workers Docs", url: "https://docs.prefect.io/latest/concepts/workers/"}
      - {text: "Docker Infrastructure", url: "https://docs.prefect.io/latest/guides/docker/"}
    Tip: "Work pools decouple scheduling from execution — your Prefect server schedules runs, but workers running anywhere (laptop, VM, K8s pod) do the actual work."
    hasScore: false

  Day 9:
    Title: Schedules, Automations, and Event-Driven Triggers
    Badge: practice
    Tasks:
      - {text: "Read the schedules documentation", url: "https://docs.prefect.io/latest/concepts/schedules/"}
      - Add a CronSchedule to a deployment: every weekday at 07:00 UTC
      - Add an IntervalSchedule with interval=timedelta(hours=6) and anchor_date set
      - Create an automation in the UI that triggers a deployment run when another flow enters a Failed state
      - Create a webhook-triggered automation that runs a flow on an external HTTP POST event
      - Pause and resume a schedule from the UI and verify no runs are missed on resume
    Resources:
      - {text: "Schedules Docs", url: "https://docs.prefect.io/latest/concepts/schedules/"}
      - {text: "Automations Docs", url: "https://docs.prefect.io/latest/concepts/automations/"}
      - {text: "Webhooks Guide", url: "https://docs.prefect.io/latest/guides/webhooks/"}
    Tip: "Automations are the glue of event-driven pipelines — use them to chain flows, send alerts, or cancel stuck runs without any custom polling code."
    hasScore: false

  Day 10:
    Title: Prefect Cloud vs Self-Hosted Server — Setup and Tradeoffs
    Badge: review
    Tasks:
      - {text: "Read the Prefect Cloud documentation", url: "https://docs.prefect.io/latest/cloud/"}
      - Create a free Prefect Cloud account at app.prefect.cloud and generate an API key
      - Connect your local environment to Prefect Cloud: prefect cloud login --key <api-key>
      - Re-run an existing flow and verify it appears in the Cloud UI under your workspace
      - Compare Cloud vs self-hosted: list 5 feature differences (RBAC, audit logs, SLA monitoring)
      - Configure a second workspace in Cloud and understand workspace isolation for multi-team setups
    Resources:
      - {text: "Prefect Cloud Overview", url: "https://docs.prefect.io/latest/cloud/"}
      - {text: "Workspaces Docs", url: "https://docs.prefect.io/latest/cloud/workspaces/"}
      - {text: "Prefect Cloud Pricing", url: "https://www.prefect.io/pricing"}
    Tip: "Prefect Cloud's managed server means zero infrastructure to maintain — for personal projects and small teams, the free tier covers everything you need."
    hasScore: false

  Day 11:
    Title: Notifications — Email, Slack, and PagerDuty on Flow State Changes
    Badge: learn
    Tasks:
      - {text: "Read the notifications and automations guide", url: "https://docs.prefect.io/latest/concepts/automations/#notifications"}
      - Create a Prefect automation that sends a Slack notification when any flow enters a Failed state
      - Configure a Slack webhook block with your workspace Incoming Webhook URL
      - Create an email notification automation for successful completion of the capstone flow
      - Understand the on_failure, on_cancellation, and on_completion flow hooks for in-process callbacks
      - Implement a custom on_failure hook that logs the failed run URL and error message
    Resources:
      - {text: "Automations and Notifications", url: "https://docs.prefect.io/latest/concepts/automations/"}
      - {text: "Slack Notification Block", url: "https://docs.prefect.io/latest/concepts/blocks/#block-catalog"}
      - {text: "Flow Run Hooks", url: "https://docs.prefect.io/latest/concepts/flows/#flow-run-hooks"}
    Tip: "Flow run hooks (on_failure, on_completion) are simpler than automations for in-process callbacks — use hooks for immediate reactions and automations for cross-flow or time-delayed triggers."
    hasScore: false

  Day 12:
    Title: Docker and Kubernetes Infrastructure for Production Flows
    Badge: practice
    Tasks:
      - {text: "Read the Docker work pool guide", url: "https://docs.prefect.io/latest/guides/docker/"}
      - Write a Dockerfile that installs your flow's dependencies and copies flow code
      - Build and tag the image: docker build -t my-flow:latest .
      - Create a Docker work pool and configure it to use the built image
      - Deploy a flow to the Docker work pool and verify it runs inside a container
      - {text: "Read the Kubernetes worker documentation", url: "https://docs.prefect.io/latest/guides/deployment/kubernetes/"}
      - Understand how a Kubernetes work pool creates Job resources per flow run
    Resources:
      - {text: "Docker Work Pools", url: "https://docs.prefect.io/latest/guides/docker/"}
      - {text: "Kubernetes Work Pools", url: "https://docs.prefect.io/latest/guides/deployment/kubernetes/"}
      - {text: "prefect-docker Collection", url: "https://prefecthq.github.io/prefect-docker/"}
    Tip: "Pin your flow image tag to a specific version (never :latest in production) — reproducible container images are the single biggest reliability improvement for production pipelines."
    hasScore: false

  Day 13:
    Title: Review — Advanced Patterns and Real-World Gotchas
    Badge: review
    Tasks:
      - {text: "Read the Prefect troubleshooting and FAQ guide", url: "https://docs.prefect.io/latest/guides/troubleshooting/"}
      - Review your flow runs from Days 1–12 in the UI — identify any Failed or Crashed states and trace their root cause
      - Implement idempotent task logic: verify that re-running a flow with the same inputs produces the same outputs without side effects
      - Understand why tasks that call external APIs should always have retries and a timeout — implement both on a mock HTTP task
      - Compare three deployment strategies: Python API (flow.deploy()), prefect.yaml, and CI/CD pipeline dispatch
      - Write a runbook: 6 bullet points covering the most common Prefect production issues (worker crashes, stale schedules, cache key collisions, state mismatch)
    Resources:
      - {text: "Prefect Troubleshooting Guide", url: "https://docs.prefect.io/latest/guides/troubleshooting/"}
      - {text: "Prefect Discourse Community", url: "https://discourse.prefect.io/"}
      - {text: "Prefect Changelog", url: "https://github.com/PrefectHQ/prefect/releases"}
    Tip: "The most common production issue: a worker goes down and deployments silently stop running. Set up an automation that alerts you if no runs complete within a given time window."
    hasScore: false

  Day 14:
    Title: Capstone — Production ETL Pipeline with Scheduling, Retries, and Notifications
    Badge: exam
    Tasks:
      - {text: "Review the end-to-end Prefect tutorial", url: "https://docs.prefect.io/latest/tutorial/"}
      - Build a multi-task ETL flow: extract records from a public API (e.g. Open-Meteo or JSONPlaceholder), transform them with Pandas, and write the result to a local Parquet file
      - Add retries=3 and retry_delay_seconds=30 to the extract task, and task_input_hash caching to the transform task
      - Refactor the flow into a parent orchestrator with two subflows: ingest_subflow and transform_subflow
      - Create a deployment with a CronSchedule (every 15 minutes) targeting a process work pool; start a worker and let it execute two scheduled runs
      - Add a Slack (or email) automation that fires on flow failure and verify it triggers by intentionally breaking the extract task
      - Write a two-paragraph retrospective: what Prefect handled automatically vs what required explicit configuration
    Resources:
      - {text: "Prefect End-to-End Tutorial", url: "https://docs.prefect.io/latest/tutorial/"}
      - {text: "Deployments Deep-Dive", url: "https://docs.prefect.io/latest/concepts/deployments/"}
      - {text: "Prefect Recipes on GitHub", url: "https://github.com/PrefectHQ/prefect/tree/main/docs/recipes"}
    Tip: "In the capstone, treat each subflow as a deployable unit — even if you only deploy the parent today, designing for independent deployability makes the pipeline far easier to maintain and debug."
    hasScore: true

TOPICS:
  Topic 1:
    Name: Core Concepts
    Color: teal
    Days: [0, 1, 2]
    Description: The @flow and @task decorators, data passing between tasks, PrefectFuture concurrency, and understanding Prefect state in the UI.

  Topic 2:
    Name: Reliability Patterns
    Color: amber
    Days: [3, 4]
    Description: Retries, timeouts, caching with task_input_hash and custom cache_key_fn functions, and subflow composition for modular pipeline design.

  Topic 3:
    Name: Results and Artifacts
    Color: coral
    Days: [5]
    Description: Persisting task results with LocalFileSystemResultStorage and publishing human-readable artifacts to the Prefect UI.

  Topic 4:
    Name: Deployments
    Color: purple
    Days: [6, 7]
    Description: Packaging flows as deployments, work pools, workers (local, Docker, Kubernetes), and running flows on schedule or on demand.

  Topic 5:
    Name: Scheduling and Automation
    Color: orange
    Days: [8]
    Description: CronSchedule, IntervalSchedule, event-driven automations, and webhook triggers for fully reactive pipelines.

  Topic 6:
    Name: Prefect Cloud and Notifications
    Color: teal
    Days: [9, 10]
    Description: Prefect Cloud vs self-hosted server tradeoffs, workspace setup, Slack/email notifications, and flow run hooks.

  Topic 7:
    Name: Production Infrastructure
    Color: amber
    Days: [11]
    Description: Building and deploying flows with Docker images and Kubernetes work pools for production-grade, containerized execution.

  Topic 8:
    Name: Review and Capstone
    Color: coral
    Days: [12, 13]
    Description: Advanced gotchas review, idempotency patterns, deployment strategies, and the end-to-end ETL capstone with scheduling, retries, and notifications.
```
