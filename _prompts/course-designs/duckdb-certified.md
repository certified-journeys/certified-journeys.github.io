# DuckDB — Course Design
Generated: 2026-06-07

```
COURSE_TYPE:      notebook
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
EXAM_NOTES:       No formal exam. Complete all 10 days and the capstone analytical pipeline to demonstrate proficiency.

NOTEBOOKS:
  day-01-duckdb-fundamentals
  day-02-reading-files
  day-03-advanced-sql
  day-04-python-api
  day-05-pandas-polars-arrow
  day-06-extensions
  day-07-writing-exporting
  day-08-performance-profiling
  day-09-persistent-db-transactions
  day-10-capstone-lakehouse

DAYS:
  Day 1:
    Title: DuckDB Fundamentals: In-Process OLAP Explained
    Badge: learn
    Tasks:
      - {text: "Read the DuckDB Why DuckDB overview", url: "https://duckdb.org/why_duckdb"}
      - Install DuckDB: pip install duckdb and verify with python -c "import duckdb; print(duckdb.__version__)"
      - {text: "Read the DuckDB architecture overview (columnar engine, vectorized execution)", url: "https://duckdb.org/docs/internals/overview"}
      - Open a DuckDB in-memory connection, run SELECT 42 AS answer, and fetch the result
      - Compare DuckDB query speed against SQLite on a 1M-row synthetic table and record the difference
      - {text: "Explore the DuckDB SQL introduction to understand supported dialects", url: "https://duckdb.org/docs/sql/introduction"}
    Resources:
      - {text: "DuckDB Docs — Why DuckDB", url: "https://duckdb.org/why_duckdb"}
      - {text: "DuckDB Architecture Internals", url: "https://duckdb.org/docs/internals/overview"}
      - {text: "DuckDB GitHub Repository", url: "https://github.com/duckdb/duckdb"}
    Tip: "DuckDB runs entirely in-process — no server to start, no daemon to manage. It's SQLite for analytics: embed it anywhere, query anything."
    hasScore: false

  Day 2:
    Title: Reading Files Directly — Parquet, CSV, and JSON
    Badge: learn
    Tasks:
      - {text: "Read the DuckDB data import documentation", url: "https://duckdb.org/docs/data/overview"}
      - Use read_csv_auto() to query a CSV file without loading it into a table — SELECT directly from the file path
      - {text: "Read the Parquet support documentation and use read_parquet() on a public dataset", url: "https://duckdb.org/docs/data/parquet/overview"}
      - Use read_json_auto() to query a JSON file and extract nested fields with dot-notation
      - Combine multiple Parquet files with a glob pattern: read_parquet('data/*.parquet')
      - Use CREATE TABLE AS SELECT to materialise a filtered subset of a large CSV into DuckDB
    Resources:
      - {text: "DuckDB CSV Import", url: "https://duckdb.org/docs/data/csv/overview"}
      - {text: "DuckDB Parquet Support", url: "https://duckdb.org/docs/data/parquet/overview"}
      - {text: "DuckDB JSON Support", url: "https://duckdb.org/docs/data/json/overview"}
    Tip: "DuckDB treats file paths as table names — you can JOIN a CSV against a Parquet file in a single query without materialising either. This is the key productivity unlock."
    hasScore: false

  Day 3:
    Title: Advanced SQL in DuckDB — Window Functions, CTEs, and Macros
    Badge: learn
    Tasks:
      - {text: "Read the DuckDB window functions documentation", url: "https://duckdb.org/docs/sql/window_functions"}
      - Write a query using ROW_NUMBER(), RANK(), and LAG() over a sales dataset partitioned by region
      - {text: "Read about DuckDB CTEs and recursive CTEs", url: "https://duckdb.org/docs/sql/query_syntax/with"}
      - Refactor a complex nested subquery into readable CTEs (at least 3 levels)
      - {text: "Explore DuckDB-specific extensions to SQL: PIVOT, UNPIVOT, and list comprehensions", url: "https://duckdb.org/docs/sql/statements/pivot"}
      - Create a reusable SQL macro with CREATE MACRO and call it from a SELECT statement
    Resources:
      - {text: "DuckDB Window Functions", url: "https://duckdb.org/docs/sql/window_functions"}
      - {text: "DuckDB SQL — WITH Clause", url: "https://duckdb.org/docs/sql/query_syntax/with"}
      - {text: "DuckDB PIVOT Statement", url: "https://duckdb.org/docs/sql/statements/pivot"}
    Tip: "DuckDB supports QUALIFY — a window-function analogue of HAVING that lets you filter on window results without a subquery. It's a huge readability win once you know it exists."
    hasScore: false

  Day 4:
    Title: The Python API — Connecting, Executing, and Fetching
    Badge: practice
    Tasks:
      - {text: "Read the DuckDB Python API reference", url: "https://duckdb.org/docs/api/python/overview"}
      - Open both in-memory and file-backed connections using duckdb.connect() — understand the difference
      - Execute parameterised queries with .execute(sql, [params]) to prevent SQL injection
      - Fetch results as Python lists with .fetchall(), as dicts with .fetchdf(), and as Arrow tables with .fetch_arrow_table()
      - {text: "Use the duckdb.sql() shortcut for one-shot queries without managing a connection", url: "https://duckdb.org/docs/api/python/dbapi"}
      - Register a Python list and a dict as a virtual table with con.register() and query it with SQL
      - Write a helper function that wraps duckdb.connect(), executes a query, returns a DataFrame, and closes the connection safely
    Resources:
      - {text: "DuckDB Python API Overview", url: "https://duckdb.org/docs/api/python/overview"}
      - {text: "DuckDB Python DB-API Reference", url: "https://duckdb.org/docs/api/python/dbapi"}
      - {text: "DuckDB Relational API", url: "https://duckdb.org/docs/api/python/relational_api"}
    Tip: "Prefer parameterised queries (?) over f-strings for SQL — duckdb.execute() handles escaping correctly. It also avoids re-parsing the query plan when you loop over batches."
    hasScore: false

  Day 5:
    Title: Zero-Copy Integration — Pandas, Polars, and Apache Arrow
    Badge: practice
    Tasks:
      - {text: "Read the DuckDB integration with Pandas documentation", url: "https://duckdb.org/docs/guides/python/sql_on_pandas"}
      - Query a Pandas DataFrame directly from SQL: SELECT * FROM df WHERE col > 10 (no copy needed)
      - Use .df() to convert a DuckDB result set back to a Pandas DataFrame
      - {text: "Read the DuckDB Polars integration guide and run a SQL query over a Polars LazyFrame", url: "https://duckdb.org/docs/guides/python/polars"}
      - Use .arrow() and .fetch_arrow_table() to exchange data via PyArrow zero-copy
      - Benchmark: compare duckdb.sql().df() vs pd.read_parquet() + groupby for a 5M-row aggregation and record memory and time
    Resources:
      - {text: "DuckDB + Pandas Guide", url: "https://duckdb.org/docs/guides/python/sql_on_pandas"}
      - {text: "DuckDB + Polars Guide", url: "https://duckdb.org/docs/guides/python/polars"}
      - {text: "DuckDB + Apache Arrow", url: "https://duckdb.org/docs/guides/python/sql_on_arrow"}
    Tip: "When DuckDB queries a Pandas or Polars DataFrame it reads the underlying memory buffer directly — no serialisation, no copy. For large frames this can be 10–50× faster than converting first."
    hasScore: false

  Day 6:
    Title: DuckDB Extensions — httpfs, spatial, json, and iceberg
    Badge: learn
    Tasks:
      - {text: "Read the DuckDB extensions documentation and understand auto-loading vs manual INSTALL/LOAD", url: "https://duckdb.org/docs/extensions/overview"}
      - Install and load the httpfs extension: INSTALL httpfs; LOAD httpfs; then read a public Parquet file directly from an S3 URL
      - {text: "Configure S3 credentials (or use the public MotherDuck demo bucket) and run a remote query", url: "https://duckdb.org/docs/extensions/httpfs/s3api"}
      - Install the spatial extension and run a point-in-polygon query on a GeoJSON dataset
      - {text: "Explore the json extension's to_json() and from_json() functions for shaping API payloads", url: "https://duckdb.org/docs/extensions/json"}
      - List all available extensions with SELECT * FROM duckdb_extensions() and note which are bundled vs community
    Resources:
      - {text: "DuckDB Extensions Overview", url: "https://duckdb.org/docs/extensions/overview"}
      - {text: "httpfs Extension — S3 API", url: "https://duckdb.org/docs/extensions/httpfs/s3api"}
      - {text: "DuckDB Spatial Extension", url: "https://duckdb.org/docs/extensions/spatial/overview"}
    Tip: "Most core extensions (httpfs, json, parquet, icu) are auto-loaded in DuckDB v0.10+. You only need an explicit INSTALL for community extensions. Check duckdb_extensions() before adding manual load statements."
    hasScore: false

  Day 7:
    Title: Writing and Exporting — COPY TO, EXPORT DATABASE, and Parquet Tuning
    Badge: practice
    Tasks:
      - {text: "Read the DuckDB COPY statement documentation", url: "https://duckdb.org/docs/sql/statements/copy"}
      - Use COPY (SELECT ...) TO 'output.parquet' (FORMAT PARQUET) to export a query result
      - Export to CSV with custom delimiter, header, and quoting options via COPY TO
      - {text: "Use EXPORT DATABASE to snapshot an entire DuckDB file to a directory of Parquet + schema SQL", url: "https://duckdb.org/docs/sql/statements/export"}
      - Write a Parquet file with ROW_GROUP_SIZE and COMPRESSION options (try ZSTD vs SNAPPY) and compare sizes
      - Use IMPORT DATABASE to restore the exported snapshot into a fresh DuckDB file and verify row counts match
    Resources:
      - {text: "DuckDB COPY Statement", url: "https://duckdb.org/docs/sql/statements/copy"}
      - {text: "DuckDB EXPORT DATABASE", url: "https://duckdb.org/docs/sql/statements/export"}
      - {text: "DuckDB Parquet Writing Options", url: "https://duckdb.org/docs/data/parquet/overview#writing-to-parquet-files"}
    Tip: "Prefer ZSTD compression for Parquet files you'll read back with DuckDB — it's typically 20–30% smaller than Snappy and DuckDB's vectorised reader handles it at nearly the same speed."
    hasScore: false

  Day 8:
    Title: Performance and Query Profiling — EXPLAIN ANALYZE and Parallel Execution
    Badge: review
    Tasks:
      - {text: "Read the DuckDB query profiling documentation", url: "https://duckdb.org/docs/dev/profiling"}
      - Run EXPLAIN on a complex query and identify the physical operators (Hash Join, Filter, Projection)
      - Run EXPLAIN ANALYZE and compare estimated vs actual row counts for each operator
      - Enable query profiling output to JSON with PRAGMA enable_profiling='json' and parse the output
      - {text: "Read about DuckDB parallel execution and how to control thread count with SET threads", url: "https://duckdb.org/docs/guides/performance/threads"}
      - Identify a slow query using profiling, apply a fix (predicate pushdown, column pruning, or reordering joins), and measure the improvement
      - {text: "Review the DuckDB performance guide best practices checklist", url: "https://duckdb.org/docs/guides/performance/overview"}
    Resources:
      - {text: "DuckDB Query Profiling", url: "https://duckdb.org/docs/dev/profiling"}
      - {text: "DuckDB Performance Guide", url: "https://duckdb.org/docs/guides/performance/overview"}
      - {text: "DuckDB Parallel Execution — Threads", url: "https://duckdb.org/docs/guides/performance/threads"}
    Tip: "EXPLAIN ANALYZE is your best debugging tool — focus on operators where actual rows >> estimated rows. Large discrepancies often mean missing statistics; run ANALYZE on your table to refresh them."
    hasScore: false

  Day 9:
    Title: Persistent Databases, Transactions, and ACID Guarantees
    Badge: review
    Tasks:
      - {text: "Read the DuckDB data ingestion and persistence documentation", url: "https://duckdb.org/docs/connect/overview"}
      - Create a persistent DuckDB file with duckdb.connect('analytics.duckdb') and verify the file is written to disk
      - Demonstrate ACID behaviour: start a transaction, insert rows, rollback, and confirm the rows are not visible
      - Use ATTACH to mount a second DuckDB file and run a cross-database JOIN
      - {text: "Understand DuckDB's concurrency model: single-writer / multiple-readers and what happens on contention", url: "https://duckdb.org/docs/connect/concurrency"}
      - Implement a safe upsert pattern using INSERT OR REPLACE and verify idempotency with repeated runs
    Resources:
      - {text: "DuckDB Connection Overview", url: "https://duckdb.org/docs/connect/overview"}
      - {text: "DuckDB Concurrency", url: "https://duckdb.org/docs/connect/concurrency"}
      - {text: "DuckDB Transactions", url: "https://duckdb.org/docs/sql/statements/transactions"}
    Tip: "DuckDB supports only one writer at a time — design your pipelines so that a single process writes while readers operate on snapshots. For concurrent writes, partition your data by day or entity and use separate files."
    hasScore: false

  Day 10:
    Title: Capstone — Analytical Lakehouse Pipeline on Remote Data
    Badge: exam
    Tasks:
      - Design a multi-layer lakehouse: raw ingestion from S3/HTTP Parquet → cleaned staging table → analytical summary table, all in DuckDB
      - Ingest at least two public datasets (e.g., NYC Taxi trips + weather data) using read_parquet() with httpfs over HTTP or S3
      - Write SQL transformations that join the datasets, apply window functions, and produce a summary fact table
      - Export the final summary to a compressed Parquet file and verify the schema with duckdb.read_parquet().dtypes
      - Profile the end-to-end query with EXPLAIN ANALYZE and document at least one optimisation you applied
      - Write a Python orchestration script that runs all pipeline steps in order and reports row counts at each stage
      - {text: "Submit your completed notebook and pipeline script for peer review or self-assessment against the DuckDB best-practices checklist", url: "https://duckdb.org/docs/guides/performance/overview"}
    Resources:
      - {text: "DuckDB Performance Best Practices", url: "https://duckdb.org/docs/guides/performance/overview"}
      - {text: "DuckDB httpfs — Querying Remote Files", url: "https://duckdb.org/docs/extensions/httpfs/overview"}
      - {text: "NYC TLC Trip Data (public Parquet)", url: "https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page"}
    Tip: "A production lakehouse in DuckDB is just three CREATE TABLE AS SELECT statements chained together. Keep raw data untouched, transform in staging, and aggregate in gold — the same medallion pattern works at any scale."
    hasScore: true

TOPICS:
  Topic 1:
    Name: Core Engine & SQL
    Color: blue
    Days: 0, 1, 2   # Days 1–3 (0-indexed)

  Topic 2:
    Name: Python API
    Color: teal
    Days: 3, 4       # Days 4–5 (0-indexed)

  Topic 3:
    Name: Extensions & Remote Data
    Color: purple
    Days: 5          # Day 6 (0-indexed)

  Topic 4:
    Name: Writing & Export
    Color: orange
    Days: 6          # Day 7 (0-indexed)

  Topic 5:
    Name: Performance & Profiling
    Color: coral
    Days: 7          # Day 8 (0-indexed)

  Topic 6:
    Name: Persistence & Transactions
    Color: blue
    Days: 8          # Day 9 (0-indexed)

  Topic 7:
    Name: Capstone Project
    Color: teal
    Days: 9          # Day 10 (0-indexed)
```
