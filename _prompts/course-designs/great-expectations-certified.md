# Course Design: Great Expectations for Data Quality

## Metadata

```
COURSE_TYPE:      notebook
COURSE_ID:        great-expectations-certified
COURSE_FULL_NAME: Great Expectations for Data Quality
ICON:             GX
ACCENT_COLOR:     #FF6B6B
ACCENT_LIGHT:     #FFF0F0
ACCENT_DARK:      #CC3333
ACCENT_DARK_DIM:  #330000
PROVIDER:         Great Expectations (Self-paced)
COST:             Free
TOTAL_DAYS:       7
DIFFICULTY:       Intermediate
TAGS:             Data Quality, Python, Testing, Data Engineering
EXAM_LINK:        https://docs.greatexpectations.io/
EXAM_QUESTIONS:   null
EXAM_MINUTES:     null
EXAM_PASS_SCORE:  N/A
EXAM_NOTES:       No formal proctored exam — this is a portfolio-driven self-paced course. Completion is demonstrated by a working GX validation layer integrated into a multi-step pipeline with CI gating.

CAPSTONE_PROJECT: A full GX validation layer added to a four-step data pipeline (ingest → clean → aggregate → load) using a multi-suite Checkpoint, auto-generated Data Docs served locally, and a CI gate script that exits non-zero on any validation failure.

EXAM_CHECKLIST:
  • Can instantiate a FileSystemDataContext, add a Pandas datasource, and run a Checkpoint entirely from memory without docs
  • Written at least one custom ColumnMapExpectation with a working _validate method and registered it in a fresh Python environment
  • Checkpoint run produces a Data Docs report that correctly reflects pass/fail per suite
  • Pipeline CI gate script exits non-zero when any Expectation Suite fails — verified by deliberately injecting a bad row
  • Schema drift test: added a column to the source CSV, re-ran the suite, and observed the unexpected-columns expectation fire

AI_DEEP_DIVE_TOPICS:
  1. Expectation internals and the rendering pipeline (how expect_* calls resolve through the MetaExpectation metaclass, build an ExpectationConfiguration, get stored in an ExpectationSuite, and then render to both JSON and human-readable prescriptive/diagnostic strings via the renderer dispatch system)
  2. Checkpoint execution model (how a Checkpoint resolves its BatchRequest list, selects a Validator per batch, runs each ExpectationSuite in sequence, collects ValidationResults into a ValidationResultCollection, decides the overall success flag, and triggers configured Actions such as UpdateDataDocsAction and SlackNotificationAction)
  3. Schema drift detection with expect_table_columns_to_match_ordered_list and expect_column_to_exist (how GX compares observed schema against the stored suite at validation time, why column order matters, and how to design suites that catch additive vs. destructive upstream schema changes without breaking on benign additions)

NOTEBOOKS:
  day-01-gx-architecture
  day-02-connecting-data
  day-03-core-expectations
  day-04-expectation-suites
  day-05-checkpoints-data-docs
  day-06-pipeline-integration
  day-07-custom-expectations-capstone

DAYS:
  Day 1 | GX Architecture and Data Context | learn
  Day 2 | Connecting to Data Sources | learn
  Day 3 | Core Expectations | practice
  Day 4 | Expectation Suites | practice
  Day 5 | Checkpoints and Data Docs | practice
  Day 6 | Pipeline Integration and Drift Detection | review
  Day 7 | Custom Expectations and Capstone | exam

TOPICS:
  Foundations         | #FF6B6B | 0, 1
  Expectations        | #CC3333 | 2, 3
  Validation Pipeline | #E07B53 | 4, 5
  Production & Capstone | #991111 | 5, 6
```

---

## AI Deep Dive Topics (3 cards)

**1. Expectation internals and the rendering pipeline**

When you call `expect_column_values_to_not_be_null("email")`, what actually happens is more than a function call. GX uses a `MetaExpectation` metaclass that intercepts the method invocation on a `Validator`, wraps the arguments into an `ExpectationConfiguration` object (a typed dict with `expectation_type` and `kwargs`), and appends it to the in-memory `ExpectationSuite`. Nothing is evaluated at call time — the suite is just a serialisable list of configurations stored as JSON.

The rendering pipeline activates at report time. Each `Expectation` class declares `@renderer` methods decorated with a string key like `"renderer.prescriptive"` or `"renderer.diagnostic.observed_value"`. When Data Docs builds an HTML page, it dispatches each `ExpectationConfiguration` to its class's renderer registry and calls the matching renderer method, which returns `RenderedStringTemplateContent` objects that are templated into HTML. This is why custom Expectations must implement `_prescriptive_renderer` (to appear correctly in Data Docs) separately from `_validate` (which performs the actual check). Skipping the renderer means your custom expectation shows as a raw JSON blob in the report, even if the validation logic is correct.

Understanding this two-phase architecture — configuration capture vs. render-time dispatch — is the key to debugging unexpected Data Docs output and to building custom Expectations that look polished in reports.

---

**2. Checkpoint execution model**

A `Checkpoint` is not just a "run this suite" alias — it is a mini-orchestrator with its own resolution order. When you call `checkpoint.run()`, GX walks through its `validations` list, and for each entry resolves a `BatchRequest` (specifying datasource, data connector, data asset, and optional batch filters) into one or more concrete `Batch` objects. A `Validator` is then instantiated by binding a `Batch` to an `ExecutionEngine` (Pandas, Spark, or SQLAlchemy) and loading the specified `ExpectationSuite` from the `DataContext` store.

Each `(Batch, Suite)` pair is validated independently, producing a `ValidationResult`. All results are collected into a `CheckpointResult` dictionary keyed by `(run_id, batch_identifier, suite_name)`. After all validations complete, the Checkpoint evaluates its `result_format` and triggers each configured `Action` in order — `StoreValidationResultAction` persists the result, `UpdateDataDocsAction` rebuilds the HTML site, `SlackNotificationAction` posts a message. The overall `success` flag on the `CheckpointResult` is `True` only if every `ValidationResult.success` is `True`.

The implication for CI gates: check `checkpoint_result["success"]` and `sys.exit(1)` on `False` — do not parse individual results unless you need per-suite granularity.

---

**3. Schema drift detection with GX Expectations**

GX has no background schema monitor — drift detection is triggered at validation time by Expectations that compare the observed table schema against what was captured in the suite. The two primary tools are `expect_table_columns_to_match_ordered_list` (exact column set, exact order) and `expect_column_to_exist` (per-column existence check). A subtler option is `expect_table_columns_to_match_set` which ignores order but still enforces an exact column set.

The distinction matters in practice: upstream ETL teams often add columns (additive drift) which is usually safe, but rename or drop columns (destructive drift) which breaks downstream consumers. A well-designed suite uses `expect_table_columns_to_match_set` for the required-column baseline, plus individual `expect_column_to_exist` expectations for the columns your pipeline actively reads — this catches destructive drift without false-positives on benign additions.

Capturing the initial schema is done by running `validator.expect_table_columns_to_match_ordered_list(list(df.columns))` once during the bootstrapping phase and saving the suite. On every subsequent pipeline run, the Checkpoint validates that schema Expectation first. Because GX stores suites as JSON, schema snapshots are version-controllable and diff-able in PRs, making schema contract changes explicit and reviewable.

---

## Notebooks

```
day-01-gx-architecture
day-02-connecting-data
day-03-core-expectations
day-04-expectation-suites
day-05-checkpoints-data-docs
day-06-pipeline-integration
day-07-custom-expectations-capstone
```

---

## Days

### Day 1 — GX Architecture and Data Context

**Badge:** learn  
**hasScore:** false

**Tasks:**
1. {text: "Read the GX OSS Architecture overview in the official docs", url: "https://docs.greatexpectations.io/docs/reference/learn/conceptual_guides/gx_overview"}
2. {text: "Install great-expectations in a fresh virtualenv: `pip install great-expectations` and run `great_expectations --version` to confirm", url: "https://docs.greatexpectations.io/docs/core/installation_and_setup/install_gx"}
3. {text: "Read the Data Context reference — understand FileSystemDataContext vs. EphemeralDataContext and when to use each", url: "https://docs.greatexpectations.io/docs/reference/learn/conceptual_guides/data_context"}
4. {text: "In the notebook: instantiate a FileSystemDataContext using `gx.get_context(mode='file')` in a temp directory and inspect the scaffolded folder structure", url: "https://docs.greatexpectations.io/docs/core/installation_and_setup/manage_data_contexts"}
5. "Sketch a diagram (on paper or in your notes) mapping the four main GX objects: DataContext → Datasource → Validator → ExpectationSuite"

**Resources:**
- {text: "GX OSS Docs — Get Started", url: "https://docs.greatexpectations.io/docs/core/introduction"}
- {text: "GX GitHub Repository", url: "https://github.com/great-expectations/great_expectations"}
- {text: "GX Conceptual Guides", url: "https://docs.greatexpectations.io/docs/reference/learn/conceptual_guides/"}

**Tip:** The `FileSystemDataContext` scaffolds a `great_expectations/` folder with `great_expectations.yml`, an `expectations/` store, and a `checkpoints/` directory. Commit this folder to your repo — the YAML stores your datasource config and suite references, making your validation layer reproducible across machines.

---

### Day 2 — Connecting to Data Sources

**Badge:** learn  
**hasScore:** false

**Tasks:**
1. {text: "Read the Datasource and Data Asset concepts in the GX docs", url: "https://docs.greatexpectations.io/docs/reference/learn/conceptual_guides/datasource"}
2. {text: "Connect a Pandas datasource to a local CSV file using `context.data_sources.add_pandas_filesystem()` and create a CSV Data Asset", url: "https://docs.greatexpectations.io/docs/core/connect_to_data/file_system/"}
3. "In the notebook: use `batch_request = data_asset.build_batch_request()` and `context.get_validator(batch_request=batch_request)` to load a batch and inspect `validator.head()`"
4. {text: "Read the SQL datasource guide and add a SQLite datasource using `context.data_sources.add_sqlite()` with a DuckDB or SQLite in-memory engine", url: "https://docs.greatexpectations.io/docs/core/connect_to_data/sql/"}
5. "Explore the BatchRequest parameters: data_asset_name, datasource_name, and batch_slice — print the batch metadata to understand what a 'batch' contains"

**Resources:**
- {text: "GX Data Sources Reference", url: "https://docs.greatexpectations.io/docs/core/connect_to_data/"}
- {text: "GX Pandas Datasource API", url: "https://docs.greatexpectations.io/docs/core/connect_to_data/file_system/"}
- {text: "GX SQL Datasource Guide", url: "https://docs.greatexpectations.io/docs/core/connect_to_data/sql/"}

**Tip:** A `DataAsset` is a named logical pointer to a data source (e.g. "orders_csv") and a `Batch` is a concrete slice of that asset at a point in time. Understanding this two-level abstraction early prevents confusion: you define the asset once and generate batch requests many times — one per pipeline run or date partition.

---

### Day 3 — Core Expectations

**Badge:** practice  
**hasScore:** true

**Tasks:**
1. {text: "Browse the full Expectations Gallery — identify at least 10 expectations you would use in a real data pipeline", url: "https://greatexpectations.io/expectations/"}
2. {text: "In the notebook: run `expect_column_values_to_not_be_null`, `expect_column_values_to_be_between`, and `expect_column_values_to_match_regex` on a sample DataFrame and inspect the `ExpectationValidationResult` dict", url: "https://docs.greatexpectations.io/docs/reference/learn/expectations/"}
3. "Chain 6 expectations on a single Validator instance and call `validator.validate()` — compare the returned `ValidationResult.success` flag against the individual results"
4. {text: "Read the result_format reference — switch between BASIC, SUMMARY, and COMPLETE and observe how the unexpected_list and partial_unexpected_list change", url: "https://docs.greatexpectations.io/docs/reference/learn/expectations/result_format"}
5. "Write a utility function `audit_df(df, validator)` that runs validation and prints a pass/fail table to stdout with column name, expectation type, success, and unexpected count"
6. "Add `expect_table_row_count_to_be_between` and `expect_table_columns_to_match_set` to your suite and test against a DataFrame with an injected schema violation"

**Resources:**
- {text: "GX Expectations Gallery", url: "https://greatexpectations.io/expectations/"}
- {text: "GX Expectation Validation Result reference", url: "https://docs.greatexpectations.io/docs/reference/learn/expectations/"}
- {text: "GX result_format docs", url: "https://docs.greatexpectations.io/docs/reference/learn/expectations/result_format"}

**Tip:** When you call an `expect_*` method on a Validator, GX does not run the check immediately — it appends an `ExpectationConfiguration` to the in-memory suite and returns a result. Call `validator.validate()` once at the end to execute all expectations in a single pass, not one by one — this is much more efficient on large DataFrames.

---

### Day 4 — Expectation Suites

**Badge:** practice  
**hasScore:** true

**Tasks:**
1. {text: "Read the Expectation Suite management guide — understand how suites are stored in the Expectations Store as JSON", url: "https://docs.greatexpectations.io/docs/core/define_expectations/manage_expectation_suites"}
2. "In the notebook: create and save two named suites — `orders.critical` (nullness, schema, row count) and `orders.distributions` (value ranges, regex formats) — using `context.suites.add()` and `context.suites.save()`"
3. {text: "Use the Profiler (or `validator.expect_*` calls) to auto-generate a draft suite from a sample DataFrame, then edit the generated JSON to tighten thresholds", url: "https://docs.greatexpectations.io/docs/core/define_expectations/"}
4. "Load an existing suite with `context.suites.get('orders.critical')`, add two new expectations, and save — confirm the JSON file on disk updated correctly"
5. "Write a `version_suite(suite_name, tag)` helper that copies the suite JSON to `expectations/archive/suite_name_tag.json` before overwriting the live suite"
6. {text: "Read the ExpectationSuite serialization docs and write a unit test that round-trips a suite to JSON and back, asserting the expectation count and types are preserved", url: "https://docs.greatexpectations.io/docs/reference/api/core/ExpectationSuite"}

**Resources:**
- {text: "GX Expectation Suites docs", url: "https://docs.greatexpectations.io/docs/core/define_expectations/manage_expectation_suites"}
- {text: "GX ExpectationSuite API Reference", url: "https://docs.greatexpectations.io/docs/reference/api/core/ExpectationSuite"}
- {text: "GX Expectations Store reference", url: "https://docs.greatexpectations.io/docs/core/configure_project_settings/configure_expectation_stores/"}

**Tip:** Treat suite JSON files like migrations — name them semantically (`orders.critical`, not `suite_1`), commit them to version control, and never overwrite them without archiving the previous version. A suite is your data contract: if it changes, the change should be explicit and reviewable in a PR diff.

---

### Day 5 — Checkpoints and Data Docs

**Badge:** practice  
**hasScore:** true

**Tasks:**
1. {text: "Read the Checkpoint conceptual guide — understand the difference between a Checkpoint, a ValidationDefinition, and a CheckpointResult", url: "https://docs.greatexpectations.io/docs/core/validate_data/checkpoints/"}
2. "In the notebook: create a Checkpoint that runs both `orders.critical` and `orders.distributions` suites against the same batch in a single `checkpoint.run()` call"
3. "Inspect the `CheckpointResult` object — print `checkpoint_result.success`, iterate over `checkpoint_result.run_results`, and display the success flag per suite"
4. {text: "Enable the `UpdateDataDocsAction` in the Checkpoint config and run the Checkpoint — then open the generated `great_expectations/uncommitted/data_docs/local_site/index.html` in a browser", url: "https://docs.greatexpectations.io/docs/core/validate_data/actions/"}
5. "Write a CI gate function: `def ci_gate(checkpoint_result): if not checkpoint_result.success: sys.exit(1)` and demonstrate it failing on a bad batch"
6. {text: "Read the Data Docs customization guide and change the site name and logo in `great_expectations.yml`", url: "https://docs.greatexpectations.io/docs/core/configure_project_settings/configure_data_docs_sites/"}

**Resources:**
- {text: "GX Checkpoints docs", url: "https://docs.greatexpectations.io/docs/core/validate_data/checkpoints/"}
- {text: "GX Checkpoint Actions reference", url: "https://docs.greatexpectations.io/docs/core/validate_data/actions/"}
- {text: "GX Data Docs configuration", url: "https://docs.greatexpectations.io/docs/core/configure_project_settings/configure_data_docs_sites/"}

**Tip:** The `CheckpointResult.success` attribute is the single source of truth for CI gates — it is `False` if _any_ suite in the Checkpoint fails. Do not try to parse individual ValidationResults in your CI script unless you need per-suite granularity; a simple `if not result.success: sys.exit(1)` is the correct pattern.

---

### Day 6 — Pipeline Integration and Drift Detection

**Badge:** review  
**hasScore:** true

**Tasks:**
1. {text: "Read the GX + Airflow integration guide — understand how to call a Checkpoint inside a PythonOperator or use the `GreatExpectationsOperator`", url: "https://docs.greatexpectations.io/docs/deployment_patterns/how_to_use_great_expectations_with_airflow"}
2. "In the notebook: build a four-step simulated pipeline (ingest → clean → aggregate → load) where each step calls a dedicated GX Checkpoint before passing data to the next step"
3. "Design schema-drift Expectations: add `expect_table_columns_to_match_set`, `expect_column_to_exist('user_id')`, and `expect_column_to_exist('event_ts')` to the ingest suite — then simulate drift by removing `event_ts` from the source and re-running"
4. {text: "Read the Prefect GX integration guide and sketch (in your notes) how you would replace the Checkpoint call with a Prefect task that reports results as a flow artifact", url: "https://docs.greatexpectations.io/docs/deployment_patterns/how_to_use_great_expectations_in_prefect_flows"}
5. "Implement a drift report function that compares the current batch's column list against the stored suite's `expect_table_columns_to_match_set` kwargs and prints added/removed columns as a structured dict"

**Resources:**
- {text: "GX Deployment Patterns", url: "https://docs.greatexpectations.io/docs/deployment_patterns/"}
- {text: "GX + Airflow integration", url: "https://docs.greatexpectations.io/docs/deployment_patterns/how_to_use_great_expectations_with_airflow"}
- {text: "GX + Prefect integration", url: "https://docs.greatexpectations.io/docs/deployment_patterns/how_to_use_great_expectations_in_prefect_flows"}

**Tip:** When integrating GX into a pipeline, run the Checkpoint at the _start_ of each stage (validating the stage's input), not at the end. This ensures a failing Checkpoint aborts the stage before any side effects (writes, API calls, downstream triggers) occur — the "validate inputs, not outputs" pattern is the canonical GX data contract model.

---

### Day 7 — Custom Expectations and Capstone

**Badge:** exam  
**hasScore:** false

**Tasks:**
1. {text: "Read the Custom Expectations guide — understand the class hierarchy: Expectation → ColumnMapExpectation → your subclass, and the required methods `_validate` and `map_metric`", url: "https://docs.greatexpectations.io/docs/core/define_expectations/custom_expectations/"}
2. "In the notebook: implement a custom `ExpectColumnValuesToBeValidEmail` by subclassing `ColumnMapExpectation`, define the `map_metric`, implement `_validate` with a regex check, and register it with `@public_api`"
3. "Add a `_prescriptive_renderer` classmethod to your custom Expectation so it renders a human-readable description (not raw JSON) in Data Docs"
4. {text: "Run your custom expectation on a sample DataFrame with both valid and invalid emails — confirm the `unexpected_list` contains exactly the bad rows and the Data Docs page shows your prescriptive description", url: "https://docs.greatexpectations.io/docs/core/define_expectations/custom_expectations/"}
5. "Capstone: assemble the full GX validation layer — four-step pipeline with per-stage Checkpoints, two named suites (`pipeline.schema` and `pipeline.values`), Data Docs served locally, and a CI gate script that exits 1 on any failure. Inject a bad row and confirm the gate fires."
6. "Write a `README.md` for your capstone project explaining the suite design decisions, the schema-drift strategy, and how to extend the validation layer with a new Expectation"

**Resources:**
- {text: "GX Custom Expectations guide", url: "https://docs.greatexpectations.io/docs/core/define_expectations/custom_expectations/"}
- {text: "GX ColumnMapExpectation API", url: "https://docs.greatexpectations.io/docs/reference/api/expectations/core/"}
- {text: "GX Expectation Gallery (for inspiration)", url: "https://greatexpectations.io/expectations/"}

**Tip:** The most common mistake when writing custom Expectations is implementing `_validate` correctly but forgetting `_prescriptive_renderer` — your expectation then shows as a raw JSON blob in Data Docs even though the validation logic is perfect. Always test your custom Expectation by running a Checkpoint with `UpdateDataDocsAction` and opening the HTML report, not just by checking the Python return value.
