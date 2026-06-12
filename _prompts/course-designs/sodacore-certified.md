# Soda Core for Data Quality — Course Design
Generated: 2026-06-11

```
COURSE_TYPE:      notebook
COURSE_ID:        sodacore-certified
COURSE_FULL_NAME: Soda Core for Data Quality
ICON:             SC
ACCENT_COLOR:     #0D9488
ACCENT_LIGHT:     #CCFBF1
ACCENT_DARK:      #0F766E
ACCENT_DARK_DIM:  #012220
PROVIDER:         Soda (Self-paced)
COST:             Free
TOTAL_DAYS:       10
DIFFICULTY:       Intermediate
TAGS:             Data Quality, Data Engineering, Testing, SQL
EXAM_LINK:        https://docs.soda.io/soda-core/overview-main.html
EXAM_QUESTIONS:   null
EXAM_MINUTES:     null
EXAM_PASS_SCORE:  N/A
EXAM_NOTES:       No formal exam. Complete all checks and the capstone pipeline quality framework.

NOTEBOOKS:
  day-01-soda-core-intro
  day-02-connecting-data-sources
  day-03-writing-checks-sodacl
  day-04-threshold-freshness-checks
  day-05-custom-sql-checks
  day-06-pipeline-integration
  day-07-soda-cloud-contracts
  day-08-schema-evolution
  day-09-test-driven-data-dev
  day-10-capstone-quality-framework

DAYS:
  Day 1:
    Title: Soda Core Architecture — Checks, SodaCL, and Scan Execution
    Badge: learn
    Tasks:
      - {text: "Read the Soda Core overview and understand where it fits in the data quality landscape", url: "https://docs.soda.io/soda-core/overview-main.html"}
      - Install Soda Core with DuckDB support: pip install -i https://pypi.cloud.soda.io soda-core-duckdb and verify the CLI with soda --version
      - {text: "Read the SodaCL introduction to understand the checks YAML structure and scan lifecycle", url: "https://docs.soda.io/soda-cl/soda-cl-overview.html"}
      - Create your first checks.yml file with a row_count check on a sample CSV table and run soda scan
      - Inspect the scan output: understand PASS, FAIL, WARN states and the structured results JSON
      - {text: "Read how Soda Core resolves data sources, checks files, and configuration through its configuration.yml", url: "https://docs.soda.io/soda-core/configuration.html"}
    Resources:
      - {text: "Soda Core Overview", url: "https://docs.soda.io/soda-core/overview-main.html"}
      - {text: "SodaCL Language Overview", url: "https://docs.soda.io/soda-cl/soda-cl-overview.html"}
      - {text: "Soda Core — Get Started Locally", url: "https://docs.soda.io/soda-core/get-started-locally.html"}
    Tip: "Soda Core separates concerns cleanly: configuration.yml holds connection details, checks YAML holds quality rules, and the scan CLI wires them together. Keep these files in version control from day one."
    hasScore: false

  Day 2:
    Title: Connecting to Data Sources — DuckDB, PostgreSQL, and Snowflake
    Badge: learn
    Tasks:
      - {text: "Read the Soda data source configuration reference for all supported connectors", url: "https://docs.soda.io/soda-core/configuration.html"}
      - Configure a DuckDB data source in configuration.yml pointing to a local .duckdb file and run a successful scan
      - {text: "Study the PostgreSQL connector documentation and write a configuration.yml for a local Postgres instance", url: "https://docs.soda.io/soda/connect-postgresql.html"}
      - Use environment variable substitution (${VAR}) in configuration.yml for credentials — never hardcode passwords
      - {text: "Read the Snowflake connector guide and understand how warehouse, role, and schema map to Soda config keys", url: "https://docs.soda.io/soda/connect-snowflake.html"}
      - Run soda test-connection -d <datasource> -c configuration.yml to validate connectivity without executing checks
    Resources:
      - {text: "Soda Data Source Configuration", url: "https://docs.soda.io/soda-core/configuration.html"}
      - {text: "Connect to PostgreSQL", url: "https://docs.soda.io/soda/connect-postgresql.html"}
      - {text: "Connect to Snowflake", url: "https://docs.soda.io/soda/connect-snowflake.html"}
    Tip: "Always use ${ENV_VAR} placeholders for credentials in configuration.yml. Soda Core resolves them at runtime so you can commit the config file to git without leaking secrets."
    hasScore: false

  Day 3:
    Title: Writing Checks in SodaCL — Row Count, Missing Values, and Duplicates
    Badge: learn
    Tasks:
      - {text: "Read the SodaCL checks reference — row count, missing, invalid, and duplicate checks", url: "https://docs.soda.io/soda-cl/metrics-and-checks.html"}
      - Write a row_count check with a fail threshold (must be > 0) and a warn threshold (must be > 1000)
      - {text: "Read the missing values check documentation and write checks for missing_count and missing_percent on nullable columns", url: "https://docs.soda.io/soda-cl/missing-metrics.html"}
      - Write a duplicate_count check on a primary-key column and verify it catches an injected duplicate row
      - {text: "Explore the invalid values check (valid_values, valid_regex, valid_min, valid_max) to enforce domain constraints", url: "https://docs.soda.io/soda-cl/validity-metrics.html"}
      - Organise checks across three tables in a single checks file and confirm each section runs independently
    Resources:
      - {text: "SodaCL Metrics and Checks Reference", url: "https://docs.soda.io/soda-cl/metrics-and-checks.html"}
      - {text: "Missing Values Checks", url: "https://docs.soda.io/soda-cl/missing-metrics.html"}
      - {text: "Validity Metrics", url: "https://docs.soda.io/soda-cl/validity-metrics.html"}
    Tip: "Separate your fail and warn thresholds deliberately: warn on 1% missing, fail on 5%. This gives you an early-warning signal before data quality degrades past an acceptable threshold."
    hasScore: false

  Day 4:
    Title: Threshold Checks — Valid Ranges, Freshness, and Volume Anomaly Detection
    Badge: practice
    Tasks:
      - {text: "Read the numeric metrics documentation for min, max, avg, sum, and percentile checks", url: "https://docs.soda.io/soda-cl/numeric-metrics.html"}
      - Write range checks (min >= 0, max <= 1000) on a revenue column and verify they FAIL when out-of-range data is inserted
      - {text: "Read the freshness check documentation and write a freshness check that fails when data is older than 24 hours", url: "https://docs.soda.io/soda-cl/freshness.html"}
      - Configure a freshness check with both a warn (12h) and fail (24h) threshold and observe which state triggers under each condition
      - {text: "Read about Soda's anomaly score check for automated volume anomaly detection without hard thresholds", url: "https://docs.soda.io/soda-cl/anomaly-score.html"}
      - Write a volume_diff check that detects when today's row count deviates more than 20% from yesterday's baseline
    Resources:
      - {text: "Numeric Metrics in SodaCL", url: "https://docs.soda.io/soda-cl/numeric-metrics.html"}
      - {text: "Freshness Checks", url: "https://docs.soda.io/soda-cl/freshness.html"}
      - {text: "Anomaly Score Check", url: "https://docs.soda.io/soda-cl/anomaly-score.html"}
    Tip: "Freshness checks require a column that marks when each row was written (e.g. updated_at, loaded_at). If your source tables don't have one, add a pipeline-managed ingestion timestamp — it pays for itself in debuggability."
    hasScore: false

  Day 5:
    Title: Custom SQL Checks and Metric Expressions
    Badge: practice
    Tasks:
      - {text: "Read the custom SQL checks documentation to understand the failed rows check and user-defined SQL metrics", url: "https://docs.soda.io/soda-cl/failed-rows-checks.html"}
      - Write a failed rows check using an inline SQL query that identifies orders with a shipped_date before order_date
      - {text: "Read how to define custom metrics using the metric expression syntax in SodaCL", url: "https://docs.soda.io/soda-cl/custom-metric-templates.html"}
      - Create a custom metric that computes revenue_per_order = sum(revenue) / count(*) and assert it is between 50 and 500
      - Write a multi-table referential integrity check: verify that every order's customer_id exists in the customers table
      - Combine a failed rows check with a warn threshold so that up to 0.1% bad rows produce a WARN but more than 1% produces a FAIL
    Resources:
      - {text: "Failed Rows Checks", url: "https://docs.soda.io/soda-cl/failed-rows-checks.html"}
      - {text: "Custom Metric Templates", url: "https://docs.soda.io/soda-cl/custom-metric-templates.html"}
      - {text: "SodaCL Check Reference — SQL Checks", url: "https://docs.soda.io/soda-cl/sql-checks.html"}
    Tip: "The failed rows check is the escape hatch for anything SodaCL can't express natively. Return only the offending rows from your SQL — Soda counts them and applies your threshold, then optionally sends the samples to Soda Cloud."
    hasScore: false

  Day 6:
    Title: Integrating Soda Scans into Airflow, Prefect, and CI/CD
    Badge: practice
    Tasks:
      - {text: "Read the Soda Core programmatic scan API to understand how to trigger scans from Python", url: "https://docs.soda.io/soda-core/programmatic.html"}
      - Write a Python function using soda.scan.Scan() that loads configuration, adds a checks file, and runs a scan — capture the exit code
      - {text: "Read the Soda Airflow integration guide and implement a PythonOperator that runs a Soda scan and raises AirflowException on FAIL", url: "https://docs.soda.io/soda/orchestrate-scans.html"}
      - Implement the same pattern in a Prefect flow using a @task that wraps the programmatic scan and returns scan results as a Prefect artifact
      - Add a Soda scan step to a GitHub Actions CI workflow that runs against a DuckDB fixture database on every pull request
      - Design a scan-gating pattern: block downstream pipeline tasks from running if any data quality check returns FAIL
    Resources:
      - {text: "Soda Core Programmatic Scan API", url: "https://docs.soda.io/soda-core/programmatic.html"}
      - {text: "Orchestrating Soda Scans", url: "https://docs.soda.io/soda/orchestrate-scans.html"}
      - {text: "Soda GitHub Actions Example", url: "https://docs.soda.io/soda-core/get-started-locally.html"}
    Tip: "When embedding Soda in Airflow, use scan.get_scan_results() to inspect individual check outcomes and only raise exceptions for checks tagged as critical — this lets non-critical quality warnings surface without stopping the DAG."
    hasScore: false

  Day 7:
    Title: Soda Cloud — Publishing Scan Results, Alerting, and Data Contracts
    Badge: review
    Tasks:
      - {text: "Read the Soda Cloud overview and understand how scan results are pushed from Soda Core", url: "https://docs.soda.io/soda-cloud/overview.html"}
      - Create a free Soda Cloud account, generate an API key, and add the soda_cloud block to configuration.yml
      - Run a scan and verify results appear in the Soda Cloud dataset health dashboard with check statuses and trends
      - {text: "Read the Soda Cloud alerting documentation and configure an email or Slack notification for FAIL checks", url: "https://docs.soda.io/soda-cloud/collaborate.html"}
      - {text: "Read the data contracts documentation and write a contract that enforces schema, row count, and freshness for a critical table", url: "https://docs.soda.io/soda-core/data-contracts.html"}
      - Review the scan history graph in Soda Cloud to identify a trend where a metric is slowly degrading — document the root cause
    Resources:
      - {text: "Soda Cloud Overview", url: "https://docs.soda.io/soda-cloud/overview.html"}
      - {text: "Soda Cloud Collaboration and Alerts", url: "https://docs.soda.io/soda-cloud/collaborate.html"}
      - {text: "Soda Data Contracts", url: "https://docs.soda.io/soda-core/data-contracts.html"}
    Tip: "Data contracts are the bridge between data producers and consumers. Write contracts that express what the downstream team needs — not what the upstream pipeline happens to produce today. The distinction matters when schemas change."
    hasScore: false

  Day 8:
    Title: Schema Evolution — Detecting and Handling Upstream Schema Changes
    Badge: review
    Tasks:
      - {text: "Read the SodaCL schema checks documentation to understand column existence, type, and order checks", url: "https://docs.soda.io/soda-cl/schema.html"}
      - Write a schema check that asserts required columns are present, have the correct data type, and are in the expected order
      - Simulate a breaking schema change (drop a column) and verify the schema check transitions to FAIL immediately
      - Simulate a non-breaking schema change (add a nullable column) and configure the check to WARN instead of FAIL
      - {text: "Read about using Soda's column_delta metric to detect unplanned column additions or removals in automated scans", url: "https://docs.soda.io/soda-cl/schema.html#schema-check-optional-config"}
      - Build a schema change notification workflow: scan → detect WARN → auto-open a GitHub issue with the column diff as the body
    Resources:
      - {text: "SodaCL Schema Checks", url: "https://docs.soda.io/soda-cl/schema.html"}
      - {text: "Soda Core Programmatic Scan API", url: "https://docs.soda.io/soda-core/programmatic.html"}
      - {text: "Soda Cloud Dataset Overview", url: "https://docs.soda.io/soda-cloud/overview.html"}
    Tip: "Never treat schema checks as a one-time baseline. Re-run them after every upstream release. A column renamed silently from 'customer_id' to 'client_id' can break dozens of downstream queries before anyone notices."
    hasScore: false

  Day 9:
    Title: Test-Driven Data Development — Writing Checks Before Transformations
    Badge: review
    Tasks:
      - {text: "Read the Soda documentation on using checks as dbt test replacements or complements in a transformation workflow", url: "https://docs.soda.io/soda/integrate-dbt.html"}
      - Apply the red-green workflow: write a failing check for a column that does not exist yet, then write the transformation that makes it pass
      - Write pre-transformation checks on raw source data (completeness, type, schema) that act as contracts for your dbt models
      - Write post-transformation checks on the output table (row count relative to source, no nulls in key columns, referential integrity)
      - {text: "Read how to use Soda scan variables to parameterise checks for partition-aware testing (e.g. filter by date)", url: "https://docs.soda.io/soda-cl/filters.html"}
      - Design a quality gate matrix: a table mapping each transformation to its pre/post checks and the FAIL action (halt vs warn vs log)
    Resources:
      - {text: "Integrating Soda with dbt", url: "https://docs.soda.io/soda/integrate-dbt.html"}
      - {text: "SodaCL Filters and Variables", url: "https://docs.soda.io/soda-cl/filters.html"}
      - {text: "Soda Core Programmatic Scan API", url: "https://docs.soda.io/soda-core/programmatic.html"}
    Tip: "Write your post-transformation checks before you write the transformation SQL. It forces you to define 'done' clearly — and the first green scan run is far more satisfying than any unit test passing."
    hasScore: false

  Day 10:
    Title: Capstone — Build a Full Data Quality Framework for a Multi-Table Pipeline
    Badge: exam
    Tasks:
      - Design a multi-table data quality framework for an e-commerce pipeline (orders, customers, products, order_items) — document the check strategy for each table
      - Write a checks YAML file covering row count, freshness, missing values, duplicates, schema, and at least two custom SQL checks across all four tables
      - Implement a Python orchestration script using the programmatic scan API that runs all checks in dependency order and halts if any upstream table fails
      - Integrate the scan into a simulated CI pipeline (GitHub Actions or local shell script) that runs on every schema migration and reports a pass/fail badge
      - Connect to Soda Cloud and verify all scan results are published; configure a FAIL alert to a Slack webhook or email address
      - Write a data contract for the orders table that formalises the schema, key column constraints, and freshness SLA
      - Document your framework as a QUALITY.md: one section per table, listing each check, its threshold rationale, and the owner responsible for investigating failures
    Resources:
      - {text: "Soda Core Documentation Hub", url: "https://docs.soda.io/soda-core/overview-main.html"}
      - {text: "SodaCL Full Checks Reference", url: "https://docs.soda.io/soda-cl/metrics-and-checks.html"}
      - {text: "Soda Data Contracts", url: "https://docs.soda.io/soda-core/data-contracts.html"}
    Tip: "A great data quality framework is not a big checks.yml — it is a prioritised decision: which checks block the pipeline, which warn, and which just log. Start with two blocking checks per table and expand from there."
    hasScore: true

TOPICS:
  Topic 1:
    Name: Architecture & Sources
    Color: blue
    Days: 0, 1   # Days 1–2 (0-indexed)

  Topic 2:
    Name: Core Checks
    Color: purple
    Days: 2, 3   # Days 3–4 (0-indexed)

  Topic 3:
    Name: Custom SQL & Metrics
    Color: coral
    Days: 4      # Day 5 (0-indexed)

  Topic 4:
    Name: Pipeline Integration
    Color: orange
    Days: 5      # Day 6 (0-indexed)

  Topic 5:
    Name: Cloud & Contracts
    Color: amber
    Days: 6      # Day 7 (0-indexed)

  Topic 6:
    Name: Schema Evolution
    Color: blue
    Days: 7      # Day 8 (0-indexed)

  Topic 7:
    Name: Test-Driven Data
    Color: purple
    Days: 8      # Day 9 (0-indexed)

  Topic 8:
    Name: Capstone Project
    Color: coral
    Days: 9      # Day 10 (0-indexed)
```
