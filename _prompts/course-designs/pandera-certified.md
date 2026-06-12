# Pandera for Data Validation — Course Design
Generated: 2026-06-11

```
COURSE_TYPE:      notebook
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

NOTEBOOKS:
  day-01-dataframe-schema-basics
  day-02-check-builtins-custom
  day-03-schema-model-class-api
  day-04-multi-backend-validation
  day-05-function-decorators
  day-06-hypothesis-schema-inference
  day-07-capstone-pipeline-validation

DAYS:
  Day 1:
    Title: DataFrameSchema Basics — Columns, Types, and Coercion
    Badge: learn
    Tasks:
      - {text: "Install pandera and read the DataFrameSchema quickstart", url: "https://pandera.readthedocs.io/en/stable/dataframe_schemas.html"}
      - Create a DataFrameSchema with three columns: name (str), age (int), salary (float) and validate a Pandas DataFrame against it
      - {text: "Use the nullable keyword — set nullable=True on a column and observe what happens with NaN values", url: "https://pandera.readthedocs.io/en/stable/dataframe_schemas.html#null-values-in-columns"}
      - Set coerce=True on the schema and pass a DataFrame where age is stored as strings — verify Pandera coerces it to int
      - Trigger a SchemaError intentionally and inspect the failure_cases attribute on the exception to understand the error report
      - {text: "Read about schema-level coerce vs column-level coerce and when each applies", url: "https://pandera.readthedocs.io/en/stable/dataframe_schemas.html#coercing-types-on-columns"}
    Resources:
      - {text: "Pandera DataFrameSchema Reference", url: "https://pandera.readthedocs.io/en/stable/dataframe_schemas.html"}
      - {text: "Pandera Column — nullable, coerce, required", url: "https://pandera.readthedocs.io/en/stable/reference/generated/pandera.api.pandas.components.Column.html"}
      - {text: "Pandera SchemaError — failure_cases and data", url: "https://pandera.readthedocs.io/en/stable/reference/generated/pandera.errors.SchemaError.html"}
    Tip: "Set coerce=True at the schema level to apply type coercion uniformly to every column. Use column-level coerce=True only when you need selective coercion — mixing both can produce confusing precedence behavior."
    hasScore: false

  Day 2:
    Title: Built-in Checks and Custom Lambda Checks
    Badge: learn
    Tasks:
      - {text: "Read the Check reference — understand the difference between element-wise and vectorized checks", url: "https://pandera.readthedocs.io/en/stable/checks.html"}
      - Apply Check.greater_than(0) to a price column and Check.less_than_or_equal_to(120) to an age column
      - {text: "Use Check.isin(['active','inactive','pending']) to validate a status column against an allowed-values list", url: "https://pandera.readthedocs.io/en/stable/reference/generated/pandera.api.checks.Check.isin.html"}
      - Apply Check.str_matches(r'^\w+@\w+\.\w+$') to an email column and observe which rows fail
      - Write a custom element-wise check using Check(lambda x: x % 2 == 0, element_wise=True) on an even_id column
      - Write a vectorized custom check using Check(lambda s: s.str.len() <= 50) on a description column — verify it operates on the whole Series
      - {text: "Combine multiple checks on a single column and read how Pandera reports multiple failures at once", url: "https://pandera.readthedocs.io/en/stable/checks.html#vectorized-vs-element-wise-custom-checks"}
    Resources:
      - {text: "Pandera Built-in Checks Reference", url: "https://pandera.readthedocs.io/en/stable/reference/generated/pandera.api.checks.Check.html"}
      - {text: "Pandera Checks Overview", url: "https://pandera.readthedocs.io/en/stable/checks.html"}
      - {text: "Pandera Check.str_matches", url: "https://pandera.readthedocs.io/en/stable/reference/generated/pandera.api.checks.Check.str_matches.html"}
    Tip: "Element-wise checks (element_wise=True) receive a scalar and must return bool. Vectorized checks receive the full Series and must return a boolean Series or a scalar bool. Vectorized checks are faster for large DataFrames — prefer them unless you need scalar logic."
    hasScore: false

  Day 3:
    Title: SchemaModel — Class-Based Schemas with pa.DataFrameModel
    Badge: learn
    Tasks:
      - {text: "Read the SchemaModel (class-based API) overview and compare it to the DataFrameSchema dict API", url: "https://pandera.readthedocs.io/en/stable/dataframe_models.html"}
      - Define a TransactionModel(pa.DataFrameModel) with columns amount: float, currency: str, and transaction_id: int using type annotations
      - {text: "Use pa.Field() to attach checks: Field(ge=0) for amount, Field(isin=['USD','EUR','GBP']) for currency", url: "https://pandera.readthedocs.io/en/stable/reference/generated/pandera.api.pandas.model_components.Field.html"}
      - Add a @pa.check('amount') classmethod that raises SchemaError when the column mean exceeds a threshold
      - Use TransactionModel.to_schema() to convert the class to a DataFrameSchema and inspect the generated schema object
      - {text: "Use pa.check_types decorator on a function and annotate its DataFrame argument with the model type", url: "https://pandera.readthedocs.io/en/stable/dataframe_models.html#validating-dataframes"}
      - Add class-level Config: name, coerce=True, and strict=True to the model and observe how strict mode rejects extra columns
    Resources:
      - {text: "Pandera SchemaModel (DataFrameModel)", url: "https://pandera.readthedocs.io/en/stable/dataframe_models.html"}
      - {text: "Pandera pa.Field Reference", url: "https://pandera.readthedocs.io/en/stable/reference/generated/pandera.api.pandas.model_components.Field.html"}
      - {text: "Pandera @pa.check decorator", url: "https://pandera.readthedocs.io/en/stable/dataframe_models.html#adding-custom-checks"}
    Tip: "SchemaModel shines when you want IDE autocompletion and static analysis on your schema definitions. The class-based API produces the exact same runtime validator as DataFrameSchema — it's purely a developer-experience layer, not a different engine."
    hasScore: false

  Day 4:
    Title: Validating Pandas, Polars, and Modin with the Same Schema
    Badge: practice
    Tasks:
      - {text: "Read the Pandera multi-backend overview — pandas, polars, and modin all share the same schema API", url: "https://pandera.readthedocs.io/en/stable/supported_libraries.html"}
      - Define a DataFrameSchema with three columns and validate a Pandas DataFrame; record the output
      - {text: "Install polars and use the same schema to validate a Polars DataFrame — note any behavioral differences", url: "https://pandera.readthedocs.io/en/stable/polars.html"}
      - Write a function that accepts a DataFrame and a schema and validates it regardless of the backend — test it with both Pandas and Polars DataFrames
      - {text: "Use pandera.typing.pandas.DataFrame[MyModel] and pandera.typing.polars.DataFrame[MyModel] type annotations to see backend-specific typing", url: "https://pandera.readthedocs.io/en/stable/dataframe_models.html#pandera-dataframe-typing"}
      - Observe how SchemaError.failure_cases looks different between Pandas and Polars backends — document the differences
    Resources:
      - {text: "Pandera Supported Libraries", url: "https://pandera.readthedocs.io/en/stable/supported_libraries.html"}
      - {text: "Pandera Polars Integration", url: "https://pandera.readthedocs.io/en/stable/polars.html"}
      - {text: "Pandera Typing Module", url: "https://pandera.readthedocs.io/en/stable/reference/generated/pandera.typing.html"}
    Tip: "Pandera's multi-backend design means you can write one schema, then switch your DataFrame library for performance without rewriting validation logic. The pandera.typing module gives you typed DataFrame annotations that carry the schema into function signatures."
    hasScore: false

  Day 5:
    Title: Function Decorators — @pa.check_input and @pa.check_output
    Badge: practice
    Tasks:
      - {text: "Read the check_input and check_output decorator documentation", url: "https://pandera.readthedocs.io/en/stable/decorators.html"}
      - Apply @pa.check_input(InputSchema) to a data cleaning function and trigger it with an invalid DataFrame to see the error raised before the function body executes
      - Apply @pa.check_output(OutputSchema) to the same function and introduce a bug that produces an invalid output — verify the post-call validation catches it
      - Stack @pa.check_input and @pa.check_output on the same function — both schemas validate
      - {text: "Use the obj_getter argument to validate a specific positional or keyword argument when a function takes multiple DataFrames", url: "https://pandera.readthedocs.io/en/stable/decorators.html#validating-a-specific-argument"}
      - {text: "Use @pa.check_io to validate both inputs and outputs in a single decorator", url: "https://pandera.readthedocs.io/en/stable/decorators.html#check_io"}
      - Write a pytest test that calls the decorated function with an invalid DataFrame and asserts that SchemaError is raised
    Resources:
      - {text: "Pandera Decorators Documentation", url: "https://pandera.readthedocs.io/en/stable/decorators.html"}
      - {text: "Pandera @pa.check_io", url: "https://pandera.readthedocs.io/en/stable/decorators.html#check_io"}
      - {text: "Pandera Integration with pytest", url: "https://pandera.readthedocs.io/en/stable/hypothesis.html#using-pytest"}
    Tip: "@pa.check_output is your safety net for data transformation functions — it verifies that your logic actually produces what the schema promises. Use it on every pipeline step that changes column types or adds computed columns."
    hasScore: false

  Day 6:
    Title: Hypothesis Integration and Schema Inference
    Badge: review
    Tasks:
      - {text: "Read the Pandera hypothesis integration overview — generating DataFrames from schemas for property-based testing", url: "https://pandera.readthedocs.io/en/stable/hypothesis.html"}
      - Install hypothesis and call schema.strategy() on a DataFrameSchema to get a Hypothesis strategy; draw a sample and inspect it
      - {text: "Write a @given(schema.strategy()) Hypothesis test that verifies a pure transformation function always produces valid output", url: "https://pandera.readthedocs.io/en/stable/hypothesis.html#using-hypothesis"}
      - Add a Check with a custom strategy using Check.greater_than(0).strategy(st.integers(min_value=1)) to constrain generated data
      - {text: "Use pa.infer_schema() on an existing DataFrame to bootstrap a schema from real data", url: "https://pandera.readthedocs.io/en/stable/schema_inference.html"}
      - Call inferred_schema.to_script() to print a Python code snippet — copy it as a starting point and tighten the inferred checks
      - {text: "Read about lazy validation — schema.validate(df, lazy=True) collects all failures before raising instead of stopping at the first", url: "https://pandera.readthedocs.io/en/stable/dataframe_schemas.html#lazy-validation"}
    Resources:
      - {text: "Pandera Hypothesis Integration", url: "https://pandera.readthedocs.io/en/stable/hypothesis.html"}
      - {text: "Pandera Schema Inference", url: "https://pandera.readthedocs.io/en/stable/schema_inference.html"}
      - {text: "Pandera Lazy Validation", url: "https://pandera.readthedocs.io/en/stable/dataframe_schemas.html#lazy-validation"}
    Tip: "pa.infer_schema() is the fastest way to bootstrap a schema from production data — run it on a representative sample, then harden the inferred bounds. Never ship the inferred schema as-is; treat it as a draft that needs human review."
    hasScore: false

  Day 7:
    Title: Capstone — Production Pipeline Validation with Full Test Coverage
    Badge: exam
    Tasks:
      - Design a three-stage data pipeline: raw ingestion → cleaning → feature engineering, each as a separate Python function
      - Define pa.DataFrameModel schemas for each stage: RawSchema, CleanSchema, and FeatureSchema — use pa.Field with checks appropriate to each stage
      - Decorate each pipeline function with @pa.check_input and @pa.check_output using the corresponding schemas
      - Add at least two custom @pa.check classmethods to FeatureSchema: one verifying a computed ratio column stays in (0, 1) and one verifying no duplicate IDs exist
      - {text: "Run the full pipeline with lazy=True and collect all SchemaErrors into a validation report before raising", url: "https://pandera.readthedocs.io/en/stable/dataframe_schemas.html#lazy-validation"}
      - Write pytest tests for each stage: one happy-path test and one test that injects bad data and asserts SchemaError is raised using pytest.raises
      - Write a Hypothesis property-based test using RawSchema.strategy() that exercises the full pipeline and asserts CleanSchema.validate() always passes on the output
      - {text: "Review the Pandera best practices and production tips before submitting", url: "https://pandera.readthedocs.io/en/stable/"}
    Resources:
      - {text: "Pandera Documentation Home", url: "https://pandera.readthedocs.io/en/stable/"}
      - {text: "Pandera SchemaModel Full Reference", url: "https://pandera.readthedocs.io/en/stable/dataframe_models.html"}
      - {text: "Hypothesis for Property-Based Testing", url: "https://hypothesis.readthedocs.io/en/latest/"}
    Tip: "A Pandera schema at every pipeline boundary is executable documentation — it tells the next developer (and the next function) exactly what shape of data to expect. Combine lazy=True with a structured error logger to make production failures actionable without crashing the pipeline."
    hasScore: true

TOPICS:
  Topic 1:
    Name: Schema Fundamentals
    Color: blue
    Days: 0, 1   # Days 1–2 (0-indexed): DataFrameSchema basics, built-in checks

  Topic 2:
    Name: Class-Based API
    Color: teal
    Days: 2, 3   # Days 3–4 (0-indexed): SchemaModel, multi-backend validation

  Topic 3:
    Name: Function Validation
    Color: coral
    Days: 4      # Day 5 (0-indexed): check_input / check_output decorators

  Topic 4:
    Name: Testing & Inference
    Color: amber
    Days: 5      # Day 6 (0-indexed): hypothesis integration, schema inference

  Topic 5:
    Name: Capstone
    Color: orange
    Days: 6      # Day 7 (0-indexed): production pipeline with full test coverage
```
