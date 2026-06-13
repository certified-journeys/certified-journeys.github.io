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

---

### 10. altair-certified

```
COURSE_ID:        altair-certified
COURSE_FULL_NAME: Vega-Altair for Data Visualization
ICON:             AL
ACCENT_COLOR:     #4F86C6
ACCENT_LIGHT:     #EBF3FB
ACCENT_DARK:      #2D5F8A
ACCENT_DARK_DIM:  #0A1A2E
PROVIDER:         Self-paced
COST:             Free
TOTAL_DAYS:       10
DIFFICULTY:       Intermediate
TAGS:             Visualization, Python, Data Science, Vega-Lite
EXAM_LINK:        https://altair-viz.github.io/
EXAM_QUESTIONS:   null
EXAM_MINUTES:     null
EXAM_PASS_SCORE:  N/A
EXAM_NOTES:       No formal exam. Complete all 10 days and the capstone interactive dashboard.
```

**Core topics for Design Agent to expand:**
- Altair fundamentals: declarative grammar, `Chart`, `mark_*`, `encode()`, `alt.X/Y/Color`
- Data: Pandas DataFrames, Polars, URL sources, long-form vs wide-form, `fold` transform
- Marks: point, line, bar, area, rect, arc (pie/donut), boxplot, rule, text
- Encodings: quantitative, ordinal, nominal, temporal — shorthand vs longhand
- Transforms: filter, calculate, aggregate, bin, window, fold, flatten
- Compound charts: layering (`+`), faceting (`facet`), concatenation (`|`, `&`)
- Interactivity: `selection_point`, `selection_interval`, `bind`, linked brushing across charts
- Customization: themes, color schemes, axis/legend config, `alt.Chart.configure_*`
- Geographic visualization: choropleth maps with TopoJSON, `mark_geoshape`
- Capstone: build a fully interactive multi-panel EDA dashboard from a real dataset

---

---

### 11. huggingface-nlp-certified

```
COURSE_ID:        huggingface-nlp-certified
COURSE_FULL_NAME: Hugging Face NLP for Engineers
ICON:             HF
ACCENT_COLOR:     #FF9D00
ACCENT_LIGHT:     #FFF7E6
ACCENT_DARK:      #CC7A00
ACCENT_DARK_DIM:  #2E1B00
PROVIDER:         Hugging Face (Self-paced)
COST:             Free
TOTAL_DAYS:       14
DIFFICULTY:       Intermediate
TAGS:             NLP, Python, Transformers, Deep Learning
EXAM_LINK:        https://huggingface.co/learn/nlp-course
EXAM_QUESTIONS:   null
EXAM_MINUTES:     null
EXAM_PASS_SCORE:  N/A
EXAM_NOTES:       No formal exam. Complete all 14 days and the capstone fine-tuning project.
```

**Core topics for Design Agent to expand:**
- Tokenizers: BPE, WordPiece, SentencePiece — how they work and when to choose
- The `transformers` pipeline API: text classification, NER, summarization, translation
- Loading pretrained models with `AutoModel` and `AutoTokenizer`
- Fine-tuning BERT/RoBERTa for text classification with the Trainer API
- Datasets library: loading, filtering, mapping, and tokenizing HuggingFace datasets
- Evaluate library: computing metrics (F1, BLEU, ROUGE, accuracy) after fine-tuning
- Token classification: NER with IOB tagging and sequence labeling heads
- Question answering: extractive QA with squad-style models
- Pushing models to the Hub: `model.push_to_hub()`, model cards, spaces
- Capstone: fine-tune a transformer on a custom NLP task and deploy to HuggingFace Spaces

---

### 12. llm-engineering-certified

```
COURSE_ID:        llm-engineering-certified
COURSE_FULL_NAME: LLM Engineering with LangChain
ICON:             LC
ACCENT_COLOR:     #1C7A4A
ACCENT_LIGHT:     #E6F5ED
ACCENT_DARK:      #145C37
ACCENT_DARK_DIM:  #051A0F
PROVIDER:         Self-paced
COST:             Free
TOTAL_DAYS:       14
DIFFICULTY:       Intermediate
TAGS:             LLMs, Python, LangChain, RAG, Prompt Engineering
EXAM_LINK:        https://python.langchain.com/docs/introduction/
EXAM_QUESTIONS:   null
EXAM_MINUTES:     null
EXAM_PASS_SCORE:  N/A
EXAM_NOTES:       No formal exam. Build the capstone RAG application to demonstrate proficiency.
```

**Core topics for Design Agent to expand:**
- LangChain fundamentals: chains, runnables, LCEL (LangChain Expression Language)
- Chat models and LLM wrappers: OpenAI, Anthropic, local models via Ollama
- Prompt templates: `ChatPromptTemplate`, few-shot prompting, dynamic examples
- Output parsers: structured outputs with Pydantic, JSON, and custom parsers
- Document loaders and text splitters: PDFs, web pages, chunking strategies
- Embeddings and vector stores: FAISS, Chroma, pgvector for semantic search
- Retrieval-Augmented Generation (RAG): full pipeline from ingestion to retrieval
- Memory: `ConversationBufferMemory`, `ConversationSummaryMemory` for chat history
- LangChain agents: `create_react_agent`, tool calling, custom tools
- Capstone: build a production RAG chatbot over custom documents with LangChain

---

### 13. ai-agents-certified

```
COURSE_ID:        ai-agents-certified
COURSE_FULL_NAME: Building AI Agents with LangGraph
ICON:             AG
ACCENT_COLOR:     #6366F1
ACCENT_LIGHT:     #EEF2FF
ACCENT_DARK:      #4338CA
ACCENT_DARK_DIM:  #0F0E35
PROVIDER:         Self-paced
COST:             Free
TOTAL_DAYS:       10
DIFFICULTY:       Advanced
TAGS:             AI Agents, LangGraph, Python, LLMs, Workflows
EXAM_LINK:        https://langchain-ai.github.io/langgraph/
EXAM_QUESTIONS:   null
EXAM_MINUTES:     null
EXAM_PASS_SCORE:  N/A
EXAM_NOTES:       No formal exam. Ship a working multi-agent system as the capstone.
```

**Core topics for Design Agent to expand:**
- LangGraph fundamentals: StateGraph, nodes, edges, and state schemas
- Conditional edges and branching: routing logic between agent nodes
- Human-in-the-loop: `interrupt_before`, `interrupt_after`, resuming from breakpoints
- Persistence: checkpointers with SQLite and PostgreSQL for long-running agents
- ReAct agents in LangGraph: tool calling loop with `ToolNode`
- Multi-agent architectures: supervisor pattern, handoffs between specialized agents
- Streaming: token-level and node-level streaming for real-time UX
- Memory store: long-term memory with `InMemoryStore` and vector-backed stores
- LangGraph Platform: deploying agents as APIs with LangServe
- Capstone: build a multi-agent research system that searches, summarizes, and drafts reports

---

### 14. llama-certified

```
COURSE_ID:        llama-certified
COURSE_FULL_NAME: Llama & Local LLMs in Production
ICON:             LL
ACCENT_COLOR:     #0057FF
ACCENT_LIGHT:     #E6EEFF
ACCENT_DARK:      #003FCC
ACCENT_DARK_DIM:  #000F33
PROVIDER:         Meta / Ollama (Self-paced)
COST:             Free
TOTAL_DAYS:       10
DIFFICULTY:       Advanced
TAGS:             LLMs, Llama, Ollama, Python, Inference
EXAM_LINK:        https://llama.meta.com/docs/
EXAM_QUESTIONS:   null
EXAM_MINUTES:     null
EXAM_PASS_SCORE:  N/A
EXAM_NOTES:       No formal exam. Run and serve a fine-tuned Llama model as the capstone.
```

**Core topics for Design Agent to expand:**
- Llama model family: Llama 3.1/3.2 variants, parameter counts, context windows
- Running Llama locally with Ollama: `ollama run`, Modelfile, custom model configs
- Quantization: GGUF formats (Q4_K_M, Q8_0), tradeoffs between speed and quality
- Inference backends: llama.cpp, vLLM, Transformers for different deployment needs
- Prompt formatting: Llama chat templates, system prompts, instruction formatting
- Fine-tuning with QLoRA: `peft`, `trl`, `SFTTrainer` on consumer hardware
- GGUF conversion: converting HuggingFace checkpoints to GGUF for llama.cpp
- Serving with Ollama REST API and OpenAI-compatible endpoints
- Benchmarking: measuring tokens/sec, memory usage, quality vs quantization level
- Capstone: fine-tune Llama on a domain dataset and serve it via an OpenAI-compatible API

---

### 15. prompt-engineering-certified

```
COURSE_ID:        prompt-engineering-certified
COURSE_FULL_NAME: Prompt Engineering for Developers
ICON:             PE
ACCENT_COLOR:     #E040FB
ACCENT_LIGHT:     #FCE4FF
ACCENT_DARK:      #AA00CC
ACCENT_DARK_DIM:  #280030
PROVIDER:         DeepLearning.AI (Self-paced)
COST:             Free
TOTAL_DAYS:       7
DIFFICULTY:       Beginner
TAGS:             Prompt Engineering, LLMs, Python, AI
EXAM_LINK:        https://www.deeplearning.ai/short-courses/
EXAM_QUESTIONS:   null
EXAM_MINUTES:     null
EXAM_PASS_SCORE:  N/A
EXAM_NOTES:       No formal exam. Seven focused days covering prompting techniques from basics to advanced patterns.
```

**Core topics for Design Agent to expand:**
- Prompting principles: clarity, specificity, role assignment, output format control
- Zero-shot vs few-shot prompting: when examples help and when they hurt
- Chain-of-thought (CoT): step-by-step reasoning, self-consistency sampling
- Iterative prompt refinement: identifying failure modes and fixing them systematically
- Structured outputs: JSON mode, function calling, schema-constrained generation
- Advanced techniques: ReAct, Tree of Thought, self-reflection, meta-prompting
- Evaluation: building prompt test suites, LLM-as-judge, benchmark datasets
- Capstone: design and evaluate a prompt system for a real NLP task with measurable quality gates

---

### 16. github-actions-certified

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
EXAM_NOTES:       No formal exam. Seven days building automated ML pipelines with GitHub Actions.
```

**Core topics for Design Agent to expand:**
- GitHub Actions fundamentals: workflows, jobs, steps, runners, triggers
- YAML syntax: `on`, `jobs`, `steps`, `uses`, `with`, `env`, `secrets`
- Reusable workflows and composite actions: DRY CI/CD patterns
- Matrix strategies: testing across Python versions, OS, and model configs
- Caching dependencies: `actions/cache` for pip, conda, model weights
- Secrets management: `GITHUB_TOKEN`, repo secrets, environment secrets
- ML-specific patterns: training on GPU runners, DVC integration, model registry push
- Container actions: running ML jobs in Docker with GPU support
- Branch protection and required checks: enforcing quality gates before merge
- Capstone: build a full ML CI/CD pipeline — test, train, evaluate, and deploy on push

---

### 17. dbt-certified

```
COURSE_ID:        dbt-certified
COURSE_FULL_NAME: dbt for Analytics Engineers
ICON:             DT
ACCENT_COLOR:     #FF694B
ACCENT_LIGHT:     #FFF0ED
ACCENT_DARK:      #CC4429
ACCENT_DARK_DIM:  #330E06
PROVIDER:         dbt Labs (Self-paced)
COST:             Free
TOTAL_DAYS:       10
DIFFICULTY:       Intermediate
TAGS:             Analytics Engineering, SQL, dbt, Data Modeling
EXAM_LINK:        https://courses.getdbt.com/
EXAM_QUESTIONS:   null
EXAM_MINUTES:     null
EXAM_PASS_SCORE:  N/A
EXAM_NOTES:       No formal exam. Build a complete dbt project with staging, marts, and tests as the capstone.
```

**Core topics for Design Agent to expand:**
- dbt fundamentals: models, materializations (table, view, incremental, ephemeral)
- Sources and refs: `{{ source() }}`, `{{ ref() }}`, lineage and DAG
- Testing: `dbt test`, schema tests (not_null, unique, accepted_values, relationships)
- Documentation: `dbt docs generate`, `dbt docs serve`, descriptions in YAML
- Jinja and macros: reusable SQL logic, `{{ config() }}`, custom macros
- Incremental models: `is_incremental()`, unique keys, merge strategies
- Seeds and snapshots: loading static data, SCD Type 2 with `dbt snapshot`
- Packages: dbt-utils, dbt-expectations, installing from dbt Hub
- dbt Cloud vs dbt Core: job scheduling, environments, CI integration
- Capstone: build a full analytics engineering project — raw → staging → marts with full test coverage

---

### 18. great-expectations-certified

```
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
EXAM_NOTES:       No formal exam. Seven days building a complete data quality framework with GX.
```

**Core topics for Design Agent to expand:**
- GX architecture: Data Context, Data Sources, Expectations, Checkpoints, Data Docs
- Connecting to data: Pandas, Spark, SQL databases, S3/GCS file backends
- Expectations: `expect_column_values_to_not_be_null`, `expect_column_mean_to_be_between`, custom expectations
- Expectation Suites: grouping expectations, editing and versioning suites
- Validators and Checkpoints: running validation and generating Data Docs reports
- Data Docs: auto-generated HTML reports, sharing results with stakeholders
- Integrating GX into pipelines: Airflow operators, Prefect tasks, dbt tests
- Custom expectations: subclassing `ColumnMapExpectation`, registering new expectations
- Schema validation and drift detection: catching upstream schema changes automatically
- Capstone: add a full GX validation layer to a multi-step data pipeline with CI gating

---

*Queue v1.0 — 18 courses — updated 2026-06-13*
