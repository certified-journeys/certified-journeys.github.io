# Pydantic for Python Engineers — Course Design
Generated: 2026-06-10

```
COURSE_TYPE:      notebook
COURSE_ID:        pydantic-certified
COURSE_FULL_NAME: Pydantic for Python Engineers
ICON:             PD
ACCENT_COLOR:     #E92063
ACCENT_LIGHT:     #FDE8EF
ACCENT_DARK:      #B5004A
ACCENT_DARK_DIM:  #2D0014
PROVIDER:         Self-paced
COST:             Free
TOTAL_DAYS:       10
DIFFICULTY:       Intermediate
TAGS:             Python, Data Validation, Type Safety, Pydantic
EXAM_LINK:        https://docs.pydantic.dev/latest/
EXAM_QUESTIONS:   null
EXAM_MINUTES:     null
EXAM_PASS_SCORE:  N/A
EXAM_NOTES:       No formal exam. Complete all 10 days and the capstone type-safe pipeline to demonstrate proficiency.

NOTEBOOKS:
  day-01-basemodel-basics
  day-02-field-types-defaults
  day-03-validators
  day-04-model-validators-custom-types
  day-05-serialization
  day-06-settings-management
  day-07-nested-discriminated-unions
  day-08-fastapi-integration
  day-09-performance-patterns
  day-10-capstone-ml-schema-layer

DAYS:
  Day 1:
    Title: BaseModel Basics — Pydantic v2 from the Ground Up
    Badge: learn
    Tasks:
      - {text: "Read the Pydantic v2 migration overview and what changed from v1", url: "https://docs.pydantic.dev/latest/migration/"}
      - Install pydantic v2 and verify the version: pip install 'pydantic>=2.0' then python -c "import pydantic; print(pydantic.VERSION)"
      - {text: "Read the BaseModel quickstart — define a model, instantiate it, access fields", url: "https://docs.pydantic.dev/latest/concepts/models/"}
      - Define a User model with name, age, and email fields using Python type hints
      - Observe what happens when you pass invalid types: instantiate User(name=123, age="not-a-number", email=None)
      - {text: "Read about ValidationError: iterate over .errors() to inspect individual field failures", url: "https://docs.pydantic.dev/latest/concepts/models/#error-handling"}
    Resources:
      - {text: "Pydantic v2 Concepts — Models", url: "https://docs.pydantic.dev/latest/concepts/models/"}
      - {text: "Pydantic v2 Migration Guide", url: "https://docs.pydantic.dev/latest/migration/"}
      - {text: "Pydantic v2 API Reference — BaseModel", url: "https://docs.pydantic.dev/latest/api/base_model/"}
    Tip: "Pydantic v2 ships with a Rust core (pydantic-core) that makes validation 5–50× faster than v1. You get the speed boost automatically — no code changes needed, just upgrade."
    hasScore: false

  Day 2:
    Title: Fields, Types, and Defaults — Controlling Your Schema
    Badge: learn
    Tasks:
      - {text: "Read the Field() function reference — default, default_factory, alias, title, description", url: "https://docs.pydantic.dev/latest/concepts/fields/"}
      - Use Field(default=...) with Ellipsis to make a field required with no default
      - Use Field(default_factory=list) for mutable defaults instead of default=[]
      - {text: "Use annotated types: PositiveInt, NonNegativeFloat, constr, conlist from pydantic", url: "https://docs.pydantic.dev/latest/concepts/types/"}
      - Add alias and validation_alias to a field and instantiate using model_validate({'snake_case': ...})
      - {text: "Read about strict mode vs lax mode: Field(strict=True) prevents implicit coercion", url: "https://docs.pydantic.dev/latest/concepts/strict_mode/"}
      - Combine Annotated[] with Field() to create reusable constrained types with Annotated[str, Field(min_length=1, max_length=100)]
    Resources:
      - {text: "Pydantic Fields", url: "https://docs.pydantic.dev/latest/concepts/fields/"}
      - {text: "Pydantic Built-in Types", url: "https://docs.pydantic.dev/latest/concepts/types/"}
      - {text: "Pydantic Strict Mode", url: "https://docs.pydantic.dev/latest/concepts/strict_mode/"}
    Tip: "Prefer Annotated[T, Field(...)] over class-level Field() assignments for reusable constrained types — you can share them across models with a simple type alias: EmailStr = Annotated[str, Field(pattern=r'.+@.+')]."
    hasScore: false

  Day 3:
    Title: Field Validators — @field_validator and Custom Logic
    Badge: learn
    Tasks:
      - {text: "Read the validators overview — when to use @field_validator vs @model_validator", url: "https://docs.pydantic.dev/latest/concepts/validators/"}
      - Write a @field_validator('email', mode='after') that normalises email to lowercase
      - {text: "Understand validator modes: 'before', 'after', 'wrap', and 'plain'", url: "https://docs.pydantic.dev/latest/concepts/validators/#field-validators"}
      - Use mode='before' to coerce a comma-separated string into a list before type validation fires
      - Write a validator that raises ValueError with a descriptive message and verify it appears in ValidationError.errors()
      - {text: "Use @field_validator with multiple field names: @field_validator('field_a', 'field_b')", url: "https://docs.pydantic.dev/latest/concepts/validators/#reuse-validators"}
      - Apply @classmethod correctly — Pydantic v2 requires it on all @field_validator decorated methods
    Resources:
      - {text: "Pydantic Validators", url: "https://docs.pydantic.dev/latest/concepts/validators/"}
      - {text: "Pydantic v2 Validator Modes", url: "https://docs.pydantic.dev/latest/concepts/validators/#field-validators"}
      - {text: "Pydantic ValidationError API", url: "https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError"}
    Tip: "In Pydantic v2, all @field_validator methods must be @classmethod. The first argument is cls, not self. Forgetting this silently ignores the validator in some IDE setups — always run a test to confirm it fires."
    hasScore: false

  Day 4:
    Title: Model Validators and Custom Types — Cross-Field Logic
    Badge: practice
    Tasks:
      - {text: "Read about @model_validator — validate across multiple fields at once", url: "https://docs.pydantic.dev/latest/concepts/validators/#model-validators"}
      - Use @model_validator(mode='after') to check that end_date > start_date in a DateRange model
      - Use @model_validator(mode='before') to pre-process raw dict input before any field parsing
      - {text: "Read about custom types with __get_validators__ replaced by Annotated + BeforeValidator in v2", url: "https://docs.pydantic.dev/latest/concepts/types/#custom-types"}
      - Build a custom Slug type using Annotated[str, BeforeValidator(slugify)] that normalises input strings
      - {text: "Use RootModel for models that wrap a single value (replaces __root__ from v1)", url: "https://docs.pydantic.dev/latest/concepts/models/#rootmodel-and-custom-root-types"}
      - Create a RootModel[List[int]] and validate a JSON array directly: RootModel.model_validate([1, 2, 3])
    Resources:
      - {text: "Pydantic Model Validators", url: "https://docs.pydantic.dev/latest/concepts/validators/#model-validators"}
      - {text: "Pydantic Custom Types", url: "https://docs.pydantic.dev/latest/concepts/types/#custom-types"}
      - {text: "Pydantic RootModel", url: "https://docs.pydantic.dev/latest/concepts/models/#rootmodel-and-custom-root-types"}
    Tip: "@model_validator(mode='after') receives a fully-validated model instance — all field validators have already run. This makes it the right place for cross-field business rules, not pre-parsing transformations."
    hasScore: false

  Day 5:
    Title: Serialization — model_dump, model_dump_json, and JSON Schema
    Badge: practice
    Tasks:
      - {text: "Read the serialization documentation — model_dump() replaces .dict() from v1", url: "https://docs.pydantic.dev/latest/concepts/serialization/"}
      - Call model_dump() with exclude_unset=True and compare output to the default — understand the difference
      - Use model_dump(mode='json') to get a JSON-safe dict with datetime objects serialized as ISO strings
      - {text: "Use model_dump_json() for direct JSON bytes output — faster than json.dumps(model.model_dump())", url: "https://docs.pydantic.dev/latest/concepts/serialization/#modelmodel_dump_json"}
      - {text: "Use @computed_field to expose a derived property in serialized output", url: "https://docs.pydantic.dev/latest/concepts/serialization/#computed-fields"}
      - Generate a JSON Schema with model_json_schema() and inspect the output structure
      - {text: "Use @field_serializer to customize how a specific field is serialized (e.g. datetime → epoch int)", url: "https://docs.pydantic.dev/latest/concepts/serialization/#field-serializer"}
    Resources:
      - {text: "Pydantic Serialization", url: "https://docs.pydantic.dev/latest/concepts/serialization/"}
      - {text: "Pydantic JSON Schema", url: "https://docs.pydantic.dev/latest/concepts/json_schema/"}
      - {text: "Pydantic Computed Fields", url: "https://docs.pydantic.dev/latest/concepts/serialization/#computed-fields"}
    Tip: "model_dump_json() is not just a convenience wrapper — it bypasses Python dict construction and calls the Rust serializer directly. For high-throughput APIs, this can be 2–4× faster than model.model_dump() + json.dumps()."
    hasScore: false

  Day 6:
    Title: Settings Management — BaseSettings and .env Files
    Badge: practice
    Tasks:
      - {text: "Install pydantic-settings: pip install pydantic-settings", url: "https://docs.pydantic.dev/latest/concepts/pydantic_settings/"}
      - {text: "Read the pydantic-settings documentation — BaseSettings, env files, secrets dirs", url: "https://docs.pydantic.dev/latest/concepts/pydantic_settings/"}
      - Create a Settings class with database_url, api_key, and debug fields using BaseSettings
      - Write a .env file and load it via model_config = SettingsConfigDict(env_file='.env')
      - Override a setting with an environment variable and verify it takes priority over .env
      - {text: "Use nested settings with env_nested_delimiter='__' so DATABASE__URL maps to database.url", url: "https://docs.pydantic.dev/latest/concepts/pydantic_settings/#nested-models"}
      - Implement a singleton settings pattern: @lru_cache(maxsize=1) def get_settings() -> Settings: return Settings()
    Resources:
      - {text: "pydantic-settings Documentation", url: "https://docs.pydantic.dev/latest/concepts/pydantic_settings/"}
      - {text: "pydantic-settings on PyPI", url: "https://pypi.org/project/pydantic-settings/"}
      - {text: "Twelve-Factor App Config", url: "https://12factor.net/config"}
    Tip: "The lru_cache singleton pattern for Settings is idiomatic in FastAPI applications: define get_settings() once, inject it everywhere with Depends(get_settings). During tests, override it with app.dependency_overrides[get_settings] = lambda: Settings(database_url='sqlite:///:memory:')."
    hasScore: false

  Day 7:
    Title: Nested Models, Discriminated Unions, and Recursive Types
    Badge: review
    Tasks:
      - {text: "Read about nested models — how Pydantic validates and serializes nested BaseModel instances", url: "https://docs.pydantic.dev/latest/concepts/models/#nested-models"}
      - Build an Order model containing a list of LineItem models and a ShippingAddress model
      - Validate a deeply nested dict and observe that Pydantic coerces nested dicts to model instances automatically
      - {text: "Read about Union types and discriminated unions — Literal fields as discriminators", url: "https://docs.pydantic.dev/latest/concepts/unions/"}
      - Build an Event model as a discriminated union: Annotated[Union[ClickEvent, ScrollEvent, PageViewEvent], Field(discriminator='event_type')]
      - {text: "Read about recursive models — a model that references itself, e.g. a tree node", url: "https://docs.pydantic.dev/latest/concepts/postponed_annotations/"}
      - Build a TreeNode model with children: Optional[List['TreeNode']] and call model_rebuild() to resolve the forward reference
    Resources:
      - {text: "Pydantic Nested Models", url: "https://docs.pydantic.dev/latest/concepts/models/#nested-models"}
      - {text: "Pydantic Unions and Discriminated Unions", url: "https://docs.pydantic.dev/latest/concepts/unions/"}
      - {text: "Pydantic Postponed Annotations", url: "https://docs.pydantic.dev/latest/concepts/postponed_annotations/"}
    Tip: "Discriminated unions are dramatically faster than plain Union types because Pydantic reads the discriminator field first and jumps directly to the correct validator — no trial-and-error across branches. Always add a discriminator when your union variants differ by a type tag field."
    hasScore: false

  Day 8:
    Title: FastAPI Integration — Request and Response Models
    Badge: practice
    Tasks:
      - {text: "Read FastAPI's Pydantic integration overview — how path operations use BaseModel", url: "https://fastapi.tiangolo.com/tutorial/body/"}
      - Define a CreateUserRequest and UserResponse model; use UserResponse as the response_model to strip sensitive fields
      - {text: "Use response_model_exclude_unset=True on a path operation to omit fields not set by the handler", url: "https://fastapi.tiangolo.com/tutorial/response-model/#use-the-response_model_exclude_unset-parameter"}
      - Add an HTTPException with a Pydantic-shaped detail dict and observe the OpenAPI error schema
      - {text: "Use Pydantic's model_json_schema() to preview the JSON Schema that FastAPI will publish in /openapi.json", url: "https://docs.pydantic.dev/latest/concepts/json_schema/"}
      - Write a dependency that validates a query parameter struct using model_validate({'limit': limit, 'offset': offset})
      - {text: "Add an example to a field using Field(examples=['user@example.com']) and verify it appears in Swagger UI", url: "https://fastapi.tiangolo.com/tutorial/schema-extra-example/"}
    Resources:
      - {text: "FastAPI Request Body", url: "https://fastapi.tiangolo.com/tutorial/body/"}
      - {text: "FastAPI Response Model", url: "https://fastapi.tiangolo.com/tutorial/response-model/"}
      - {text: "FastAPI OpenAPI Examples", url: "https://fastapi.tiangolo.com/tutorial/schema-extra-example/"}
    Tip: "Use separate Request and Response models — never expose your internal ORM model directly. The response_model parameter is your API contract: adding fields is safe, removing them is a breaking change."
    hasScore: false

  Day 9:
    Title: Performance, Patterns, and Pydantic Internals
    Badge: review
    Tasks:
      - {text: "Read about model_config — ConfigDict options: frozen, populate_by_name, str_strip_whitespace", url: "https://docs.pydantic.dev/latest/concepts/config/"}
      - Use model_config = ConfigDict(frozen=True) and verify that models become hashable and immutable
      - {text: "Read about model_rebuild() — when and why you need to call it for forward references", url: "https://docs.pydantic.dev/latest/concepts/postponed_annotations/#self-referential-models"}
      - Use TypeAdapter to validate arbitrary types without a BaseModel: TypeAdapter(List[int]).validate_python([1, 2, 'three'])
      - {text: "Read the Pydantic v2 performance benchmarks and understand where the Rust core wins", url: "https://docs.pydantic.dev/latest/concepts/performance/"}
      - Benchmark model_validate_json() vs model_validate(json.loads(raw)) on 10,000 iterations to see the direct JSON path speedup
      - {text: "Use model_construct() to skip validation entirely for trusted data — and understand the risks", url: "https://docs.pydantic.dev/latest/concepts/models/#model-methods-and-properties"}
    Resources:
      - {text: "Pydantic ConfigDict", url: "https://docs.pydantic.dev/latest/concepts/config/"}
      - {text: "Pydantic Performance Tips", url: "https://docs.pydantic.dev/latest/concepts/performance/"}
      - {text: "Pydantic TypeAdapter", url: "https://docs.pydantic.dev/latest/concepts/type_adapter/"}
    Tip: "model_construct() bypasses all validation — it's for trusted internal data paths (e.g. deserializing from your own database). Never use it on user-supplied data. A safer pattern: validate once at the boundary, use model_construct() for internal copies."
    hasScore: false

  Day 10:
    Title: Capstone — Type-Safe Config and Schema Layer for an ML Pipeline
    Badge: exam
    Tasks:
      - Design a schema layer for a three-stage ML pipeline: DataConfig, TrainingConfig, and InferenceConfig models using BaseSettings for environment-driven values
      - Implement discriminated union ModelSpec — variants LinearModelSpec, TreeModelSpec, NeuralModelSpec each with a model_type Literal discriminator
      - Add cross-field validators: e.g. @model_validator ensuring test_size + val_size < 1.0 and learning_rate > 0 only when optimizer == 'adam'
      - Write a PipelineRun model with nested DataConfig, ModelSpec, and a computed_field run_id that hashes the config deterministically
      - Implement full serialization round-trip: PipelineRun → model_dump_json() → model_validate_json() → assert reconstructed == original
      - Generate and save the JSON Schema for PipelineRun with model_json_schema() and verify it validates correctly against a jsonschema validator
      - Expose a /run endpoint in a minimal FastAPI app: accept PipelineRun as request body, validate fully, return a RunResponse with status and run_id
      - {text: "Review the Pydantic best practices guide before submitting", url: "https://docs.pydantic.dev/latest/concepts/best_practices/"}
    Resources:
      - {text: "Pydantic Best Practices", url: "https://docs.pydantic.dev/latest/concepts/best_practices/"}
      - {text: "Pydantic v2 Full API Reference", url: "https://docs.pydantic.dev/latest/api/"}
      - {text: "pydantic-settings Documentation", url: "https://docs.pydantic.dev/latest/concepts/pydantic_settings/"}
    Tip: "A Pydantic schema layer is the single source of truth for your ML pipeline: the same models drive runtime validation, JSON Schema for contract testing, OpenAPI docs for your serving API, and .env-driven configuration — four concerns, one definition."
    hasScore: true

TOPICS:
  Topic 1:
    Name: Model Foundations
    Color: blue
    Days: 0, 1, 2   # Days 1–3 (0-indexed)

  Topic 2:
    Name: Validation
    Color: coral
    Days: 3, 4      # Days 4–5 (0-indexed): model validators + custom types, serialization

  Topic 3:
    Name: Serialization
    Color: teal
    Days: 4         # Day 5 (0-indexed)

  Topic 4:
    Name: Configuration & Settings
    Color: orange
    Days: 5         # Day 6 (0-indexed)

  Topic 5:
    Name: Advanced Types
    Color: purple
    Days: 6, 7      # Days 7–8 (0-indexed): nested/discriminated unions, FastAPI integration

  Topic 6:
    Name: Performance & Capstone
    Color: amber
    Days: 8, 9      # Days 9–10 (0-indexed): performance patterns, capstone
```
