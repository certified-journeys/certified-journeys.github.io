# certified-journeys · Course Queue

Add courses here. The orchestrator reads this file and `orchestrator-state.json` to
decide what to generate next. To add a new course: append an entry below and add its
ID to `orchestrator-state.json` with `"status": "pending"`.

---

## Settings

```
PARALLELISM:        1          # courses running at once (keep at 1 to avoid rate limits)
COOLDOWN_SECONDS:   60         # wait between courses
RETRY_DELAY_MIN:    15         # minutes to wait before retrying after a rate limit
AUTO_COMMIT:        true       # commit + push after each successful course
ON_VALIDATION_FAIL: stop       # stop | skip  — what to do when manager reports issues
```

---

## Courses

---

### 1. mlflow-certified

```
COURSE_ID:        mlflow-certified
COURSE_FULL_NAME: MLflow for ML Engineers
ICON:             ML
ACCENT_COLOR:     #E8500A
ACCENT_LIGHT:     #FEF0E7
ACCENT_DARK:      #B83B00
ACCENT_DARK_DIM:  #2A1500
PROVIDER:         Databricks (Self-paced)
COST:             Free
TOTAL_DAYS:       14
DIFFICULTY:       Intermediate
TAGS:             MLOps, Python, Experiment Tracking, Model Registry
EXAM_LINK:        https://mlflow.org/docs/latest/index.html
EXAM_QUESTIONS:   null
EXAM_MINUTES:     null
EXAM_PASS_SCORE:  N/A
EXAM_NOTES:       No formal exam. Completion of all 14 days and the capstone project demonstrates proficiency.
```

**Core topics for Design Agent to expand:**
- Tracking experiments with `mlflow.log_metric`, `mlflow.log_param`, `mlflow.log_artifact`
- MLflow UI: comparing runs, filtering, tagging
- The MLflow Model Registry: staging, production, archiving model versions
- MLflow Projects: packaging reproducible code with MLproject files
- MLflow Models: flavors (sklearn, pytorch, pyfunc), model signatures
- Model serving with `mlflow models serve` and REST API
- Autologging with `mlflow.autolog()` for sklearn, XGBoost, PyTorch
- Integration with cloud backends (S3, Azure Blob, GCS tracking stores)
- Custom Python function models and preprocessing pipelines
- Capstone: full MLOps pipeline — train → track → register → serve

---

### 2. prefect-certified

```
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
```

**Core topics for Design Agent to expand:**
- @flow and @task decorators, task dependencies and data passing
- Retries, timeouts, and caching with `cache_key_fn`
- Prefect deployments: packaging flows for scheduled execution
- Work pools and workers: local, subprocess, Docker, Kubernetes
- Prefect Cloud vs self-hosted server: setup and tradeoffs
- Artifacts, results, and state persistence between runs
- Notifications: email, Slack, PagerDuty on flow state changes
- Subflows and nested flows: modular pipeline design
- Automations: trigger flows on events or schedules
- Capstone: production ETL pipeline with scheduling, retries, notifications

---

### 3. duckdb-certified

```
COURSE_ID:        duckdb-certified
COURSE_FULL_NAME: DuckDB for Analytical Engineers
ICON:             DB
ACCENT_COLOR:     #EAB308
ACCENT_LIGHT:     #FEFCE8
ACCENT_DARK:      #A16207
ACCENT_DARK_DIM:  #1A1200
PROVIDER:         DuckDB Labs (Self-paced)
COST:             Free
TOTAL_DAYS:       10
DIFFICULTY:       Intermediate
TAGS:             Analytics, SQL, Python, Data Engineering
EXAM_LINK:        https://duckdb.org/docs/
EXAM_QUESTIONS:   null
EXAM_MINUTES:     null
EXAM_PASS_SCORE:  N/A
EXAM_NOTES:       No formal exam. Complete all 10 days and the capstone analytical pipeline.
```

**Core topics for Design Agent to expand:**
- DuckDB fundamentals: in-process OLAP, columnar execution engine
- Reading Parquet, CSV, JSON directly without loading: `read_parquet()`, `read_csv_auto()`
- Window functions, CTEs, and advanced SQL in DuckDB
- Python API: `duckdb.connect()`, `.execute()`, `.df()`, `.arrow()`
- Integrating with Pandas and Polars via zero-copy Arrow
- DuckDB extensions: `httpfs` for S3/GCS, `spatial`, `json`, `parquet`
- Writing to Parquet and other formats: `COPY TO` and `EXPORT DATABASE`
- Performance: query profiling with `EXPLAIN ANALYZE`, parallel execution
- In-memory vs persistent databases, transactions, and ACID guarantees
- Capstone: build an analytical lakehouse pipeline querying S3-like data

---

### 4. fastapi-certified

```
COURSE_ID:        fastapi-certified
COURSE_FULL_NAME: FastAPI for ML Engineers
ICON:             FA
ACCENT_COLOR:     #009688
ACCENT_LIGHT:     #E0F2F1
ACCENT_DARK:      #00695C
ACCENT_DARK_DIM:  #001A18
PROVIDER:         Self-paced
COST:             Free
TOTAL_DAYS:       10
DIFFICULTY:       Intermediate
TAGS:             Python, APIs, ML Serving, Backend
EXAM_LINK:        https://fastapi.tiangolo.com/
EXAM_QUESTIONS:   null
EXAM_MINUTES:     null
EXAM_PASS_SCORE:  N/A
EXAM_NOTES:       No formal exam. Ship a working ML-serving API as the capstone.
```

**Core topics for Design Agent to expand:**
- FastAPI basics: path operations, request/response models with Pydantic
- Type hints and automatic OpenAPI docs with Swagger UI
- Async endpoints: `async def` vs `def`, when each matters
- Dependency injection: shared DB connections, auth, config
- Background tasks and `asyncio` for non-blocking ML inference
- Loading and serving ML models: singleton pattern, warmup, batching
- File uploads, streaming responses, and large model outputs
- Authentication: API keys, OAuth2, JWT with FastAPI security
- Testing with `TestClient` and `pytest-asyncio`
- Capstone: deploy an sklearn model behind a production-ready FastAPI service

---

### 5. kestra-certified

```
COURSE_ID:        kestra-certified
COURSE_FULL_NAME: Kestra for Data Orchestration
ICON:             KS
ACCENT_COLOR:     #7C3AED
ACCENT_LIGHT:     #EDE9FE
ACCENT_DARK:      #5B21B6
ACCENT_DARK_DIM:  #150D3A
PROVIDER:         Kestra (Self-paced)
COST:             Free
TOTAL_DAYS:       14
DIFFICULTY:       Intermediate
TAGS:             Orchestration, YAML, Data Engineering, Workflows
EXAM_LINK:        https://kestra.io/docs/
EXAM_QUESTIONS:   null
EXAM_MINUTES:     null
EXAM_PASS_SCORE:  N/A
EXAM_NOTES:       No formal exam. Build and deploy the capstone multi-task flow.
```

**Core topics for Design Agent to expand:**
- Kestra architecture: server, executor, workers, storage backend
- Flows and tasks: YAML-based DAG definition
- Kestra vs Airflow vs Prefect: when to choose each
- Triggers: schedule, webhook, flow completion, file detection
- Namespaces, labels, and flow versioning
- Plugins: Python scripts, Docker tasks, HTTP requests, database queries
- Variables, inputs, outputs: passing data between tasks
- Error handling: retries, fallbacks, allowFailure, onKill handlers
- Kestra UI: flow graph, logs, replay, and monitoring
- Capstone: orchestrate a multi-step data pipeline with scheduling and alerting

---

### 6. pydantic-certified

```
COURSE_ID:        pydantic-certified
COURSE_FULL_NAME: Pydantic v2 for Python Engineers
ICON:             PD
ACCENT_COLOR:     #E11D48
ACCENT_LIGHT:     #FFF1F2
ACCENT_DARK:      #9F1239
ACCENT_DARK_DIM:  #200010
PROVIDER:         Self-paced
COST:             Free
TOTAL_DAYS:       7
DIFFICULTY:       Beginner
TAGS:             Python, Data Validation, Type Safety
EXAM_LINK:        https://docs.pydantic.dev/latest/
EXAM_QUESTIONS:   null
EXAM_MINUTES:     null
EXAM_PASS_SCORE:  N/A
EXAM_NOTES:       No formal exam. Seven focused days covering Pydantic v2 from basics to advanced patterns.
```

**Core topics for Design Agent to expand:**
- BaseModel: field definitions, types, defaults, aliases
- Validation: `@field_validator`, `@model_validator`, custom types
- Pydantic v2 performance: Rust core, model_rebuild, benchmarks vs v1
- Settings management with `BaseSettings` and `.env` files
- Serialization: `.model_dump()`, `.model_dump_json()`, `.model_json_schema()`
- Nested models, discriminated unions, and recursive types
- Capstone: build a fully type-safe config + API schema layer for an ML pipeline

---

### 7. ray-certified

```
COURSE_ID:        ray-certified
COURSE_FULL_NAME: Ray for Distributed ML
ICON:             RY
ACCENT_COLOR:     #0284C7
ACCENT_LIGHT:     #E0F2FE
ACCENT_DARK:      #0369A1
ACCENT_DARK_DIM:  #001A2E
PROVIDER:         Anyscale (Self-paced)
COST:             Free
TOTAL_DAYS:       14
DIFFICULTY:       Advanced
TAGS:             Distributed Computing, MLOps, Python, Scaling
EXAM_LINK:        https://docs.ray.io/en/latest/
EXAM_QUESTIONS:   null
EXAM_MINUTES:     null
EXAM_PASS_SCORE:  N/A
EXAM_NOTES:       No formal exam. Build the capstone distributed training pipeline.
```

**Core topics for Design Agent to expand:**
- Ray Core: `@ray.remote`, object store, tasks vs actors
- Ray cluster: local, Docker, Kubernetes — setup and teardown
- Parallel and distributed data processing with Ray Data
- Ray Train: distributed model training with PyTorch, XGBoost, sklearn
- Ray Tune: hyperparameter search at scale with ASHA, PBT schedulers
- Ray Serve: model serving with autoscaling and deployment graphs
- Ray Workflows: durable, fault-tolerant computation graphs
- Memory management: plasma store, spilling, large object handling
- Debugging Ray: `ray.timeline()`, dashboard, logs, `ray status`
- Capstone: distributed hyperparameter search + serving pipeline on a Ray cluster

---

### 8. sodacore-certified

```
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
```

**Core topics for Design Agent to expand:**
- Soda Core architecture: checks YAML, SodaCL language, scan execution
- Connecting to data sources: DuckDB, PostgreSQL, Snowflake, BigQuery
- Writing checks: row count, missing values, duplicates, schema drift
- Threshold checks: valid ranges, freshness, volume anomaly detection
- Custom SQL checks and metric expressions
- Integrating Soda scans into Airflow, Prefect, and CI/CD pipelines
- Soda Cloud: publishing scan results, alerting, data contracts
- Schema evolution: detecting and handling upstream schema changes
- Test-driven data development: writing checks before transformations
- Capstone: build a full data quality framework for a multi-table pipeline

---

---

### 9. pandera-certified

```
COURSE_ID:        pandera-certified
COURSE_FULL_NAME: Pandera for Data Validation
ICON:             PA
ACCENT_COLOR:     #7C3AED
ACCENT_LIGHT:     #EDE9FE
ACCENT_DARK:      #5B21B6
ACCENT_DARK_DIM:  #150D3A
PROVIDER:         Self-paced
COST:             Free
TOTAL_DAYS:       7
DIFFICULTY:       Intermediate
TAGS:             Data Validation, Python, DataFrames, Testing
EXAM_LINK:        https://pandera.readthedocs.io/en/stable/
EXAM_QUESTIONS:   null
EXAM_MINUTES:     null
EXAM_PASS_SCORE:  N/A
EXAM_NOTES:       No formal exam. Seven focused days covering Pandera from schema basics to production pipeline validation.
```

**Core topics for Design Agent to expand:**
- DataFrameSchema: defining column types, nullable, coerce, checks
- Check built-ins: `Check.greater_than`, `Check.isin`, `Check.str_matches`, custom lambdas
- SchemaModel (class-based API): `pa.DataFrameModel`, `Field`, `@pa.check`
- Validating Pandas, Polars, and Modin DataFrames with the same schema
- `@pa.check_input` and `@pa.check_output` decorators for function-level validation
- Hypothesis integration: property-based testing with Pandera-generated DataFrames
- Schema inference: `pa.infer_schema()` to bootstrap schemas from existing data
- Capstone: add Pandera validation to a multi-step Pandas pipeline with full test coverage

---

*Queue v1.0 — 9 courses — updated 2026-06-06*
