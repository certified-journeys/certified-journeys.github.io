# MLflow for ML Engineers — Course Design
Generated: 2026-06-06

```
COURSE_TYPE:      notebook
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

NOTEBOOKS:
  day-01-intro-mlflow
  day-02-tracking-experiments
  day-03-logging-artifacts
  day-04-mlflow-ui
  day-05-autologging
  day-06-model-flavors
  day-07-model-registry
  day-08-mlflow-projects
  day-09-custom-pyfunc
  day-10-model-serving
  day-11-cloud-backends
  day-12-pipelines-preprocessing
  day-13-review-advanced
  day-14-capstone-pipeline

DAYS:
  Day 1:
    Title: Introduction to MLflow: Tracking Your First Experiment
    Badge: learn
    Tasks:
      - {text: "Read the MLflow quickstart guide", url: "https://mlflow.org/docs/latest/getting-started/intro-quickstart/index.html"}
      - Install MLflow locally: pip install mlflow
      - Launch the MLflow UI with mlflow ui and open http://127.0.0.1:5000
      - Write a script that trains a simple sklearn model and calls mlflow.log_param, mlflow.log_metric, and mlflow.log_artifact
      - Observe the run appear in the UI — expand it and inspect the logged values
    Resources:
      - {text: "MLflow Quickstart", url: "https://mlflow.org/docs/latest/getting-started/intro-quickstart/index.html"}
      - {text: "MLflow Tracking Concepts", url: "https://mlflow.org/docs/latest/tracking.html"}
      - {text: "MLflow GitHub Repository", url: "https://github.com/mlflow/mlflow"}
    Tip: "The MLflow UI is the fastest way to understand what was logged — always run mlflow ui in a terminal while experimenting."
    hasScore: false

  Day 2:
    Title: Tracking Experiments with Runs, Params, and Metrics
    Badge: learn
    Tasks:
      - {text: "Read the MLflow Tracking API reference", url: "https://mlflow.org/docs/latest/python_api/mlflow.html"}
      - Create a named experiment with mlflow.set_experiment('my-experiment')
      - Start and end runs explicitly with mlflow.start_run() / mlflow.end_run()
      - Log a time-series of metrics across training epochs with mlflow.log_metric(step=epoch)
      - Tag runs with mlflow.set_tag and filter by tag in the UI
      - Compare two runs side-by-side using the UI's Compare Runs feature
    Resources:
      - {text: "Tracking API Docs", url: "https://mlflow.org/docs/latest/python_api/mlflow.html"}
      - {text: "Managing Experiments", url: "https://mlflow.org/docs/latest/tracking/experiments.html"}
      - {text: "MLflow Tracking Server", url: "https://mlflow.org/docs/latest/tracking/server.html"}
    Tip: "Use mlflow.set_experiment() at the top of every script — orphaned runs in the Default experiment are hard to find later."
    hasScore: false

  Day 3:
    Title: Logging Artifacts and Datasets
    Badge: learn
    Tasks:
      - {text: "Read about artifact logging", url: "https://mlflow.org/docs/latest/tracking/artifacts.html"}
      - Log a trained sklearn model with mlflow.sklearn.log_model()
      - Log a Matplotlib figure as a PNG artifact with mlflow.log_figure()
      - Log a Pandas DataFrame as a CSV artifact with mlflow.log_table()
      - Log an entire directory of files with mlflow.log_artifacts(local_dir=)
      - Navigate the artifact browser in the UI to verify stored files
    Resources:
      - {text: "Artifact Logging Guide", url: "https://mlflow.org/docs/latest/tracking/artifacts.html"}
      - {text: "mlflow.log_artifact API", url: "https://mlflow.org/docs/latest/python_api/mlflow.html#mlflow.log_artifact"}
      - {text: "MLflow Models Overview", url: "https://mlflow.org/docs/latest/models.html"}
    Tip: "log_artifact copies a local file into the run's artifact store — always log your model, feature list, and evaluation plots together so a run is self-contained."
    hasScore: false

  Day 4:
    Title: Mastering the MLflow UI — Comparing and Filtering Runs
    Badge: practice
    Tasks:
      - {text: "Read about searching runs with the Search API", url: "https://mlflow.org/docs/latest/search-runs.html"}
      - Run at least 6 training runs with different hyperparameters (vary learning rate, n_estimators, etc.)
      - Use the UI column selector to show params and metrics side-by-side
      - Apply a filter expression in the UI: metrics.accuracy > 0.85 AND params.n_estimators = '100'
      - Use mlflow.search_runs() in Python to reproduce the same filter programmatically
      - Export the comparison table to CSV and analyze it in a notebook
    Resources:
      - {text: "Searching Runs", url: "https://mlflow.org/docs/latest/search-runs.html"}
      - {text: "MLflow Client API", url: "https://mlflow.org/docs/latest/python_api/mlflow.client.html"}
      - {text: "Search Syntax Reference", url: "https://mlflow.org/docs/latest/search-runs.html#syntax"}
    Tip: "mlflow.search_runs() returns a Pandas DataFrame — you can sort, filter, and plot experiment results without ever opening the UI."
    hasScore: false

  Day 5:
    Title: Autologging with sklearn, XGBoost, and PyTorch
    Badge: learn
    Tasks:
      - {text: "Read the MLflow autologging guide", url: "https://mlflow.org/docs/latest/tracking/autologging.html"}
      - Enable global autologging with mlflow.autolog() before model training
      - Train an sklearn Pipeline and verify autologged params, metrics, and model artifact
      - Train an XGBoost Booster with xgb.train() and inspect autologged eval metrics per round
      - Disable autologging for specific libraries with mlflow.sklearn.autolog(disable=True)
      - Compare manual logging vs autologging output for the same model
    Resources:
      - {text: "Autologging Docs", url: "https://mlflow.org/docs/latest/tracking/autologging.html"}
      - {text: "sklearn Autologging", url: "https://mlflow.org/docs/latest/python_api/mlflow.sklearn.html#mlflow.sklearn.autolog"}
      - {text: "XGBoost Integration", url: "https://mlflow.org/docs/latest/python_api/mlflow.xgboost.html"}
    Tip: "mlflow.autolog() is a one-liner that covers most workflows — only add manual log_metric calls when you need custom metrics autologging doesn't capture."
    hasScore: false

  Day 6:
    Title: MLflow Models and Flavors (sklearn, PyFunc, ONNX)
    Badge: learn
    Tasks:
      - {text: "Read the MLflow Models format docs", url: "https://mlflow.org/docs/latest/models.html"}
      - Log an sklearn model with mlflow.sklearn.log_model() and inspect the MLmodel file
      - Understand model flavors: python_function, sklearn, xgboost, pytorch
      - Add a model signature with mlflow.models.infer_signature(X_train, y_pred)
      - Add input example with input_example=X_train.head() when logging the model
      - Load the saved model back with mlflow.sklearn.load_model() and run inference
    Resources:
      - {text: "MLflow Models", url: "https://mlflow.org/docs/latest/models.html"}
      - {text: "Model Signatures", url: "https://mlflow.org/docs/latest/model-registry.html#adding-an-mlflow-model-to-the-model-registry"}
      - {text: "Model Flavors Reference", url: "https://mlflow.org/docs/latest/models.html#built-in-model-flavors"}
    Tip: "Always log a model signature and input example — they enable the model serving REST API to validate request payloads automatically."
    hasScore: false

  Day 7:
    Title: The MLflow Model Registry — Staging, Production, Archiving
    Badge: practice
    Tasks:
      - {text: "Read the Model Registry guide", url: "https://mlflow.org/docs/latest/model-registry.html"}
      - Register a model from a run using mlflow.register_model(run_uri, name)
      - Transition a model version to Staging using the UI and MlflowClient.transition_model_version_stage()
      - Promote the Staging model to Production after verifying its metrics
      - Add a description and alias to the production version with client.update_model_version()
      - Load a model by stage: mlflow.sklearn.load_model('models:/my-model/Production')
    Resources:
      - {text: "Model Registry Docs", url: "https://mlflow.org/docs/latest/model-registry.html"}
      - {text: "MlflowClient Reference", url: "https://mlflow.org/docs/latest/python_api/mlflow.client.html"}
      - {text: "Model Aliases (MLflow 2.x)", url: "https://mlflow.org/docs/latest/model-registry.html#using-model-aliases"}
    Tip: "Use model aliases like 'champion' and 'challenger' (MLflow 2.x) instead of stage names — aliases are more flexible and stage deprecation is planned."
    hasScore: false

  Day 8:
    Title: MLflow Projects — Packaging Reproducible Code
    Badge: practice
    Tasks:
      - {text: "Read the MLflow Projects guide", url: "https://mlflow.org/docs/latest/projects.html"}
      - Create an MLproject file with name, conda_env, and entry_points defined
      - Define a train entry point with parameters for learning_rate and n_estimators
      - Run the project locally with mlflow run . -P learning_rate=0.01
      - Run the project from a GitHub URL: mlflow run https://github.com/mlflow/mlflow-example
      - Understand how MLflow Projects pin dependencies via conda.yaml or pip requirements
    Resources:
      - {text: "MLflow Projects", url: "https://mlflow.org/docs/latest/projects.html"}
      - {text: "MLproject File Syntax", url: "https://mlflow.org/docs/latest/projects.html#mlproject-file"}
      - {text: "MLflow Examples on GitHub", url: "https://github.com/mlflow/mlflow/tree/master/examples"}
    Tip: "An MLproject file turns any directory into a runnable, shareable experiment — teammates can reproduce your results with a single mlflow run command."
    hasScore: false

  Day 9:
    Title: Custom Python Function Models and Preprocessing Pipelines
    Badge: practice
    Tasks:
      - {text: "Read the custom pyfunc model guide", url: "https://mlflow.org/docs/latest/python_api/mlflow.pyfunc.html"}
      - Create a class that extends mlflow.pyfunc.PythonModel and implements predict()
      - Bundle a preprocessing step (StandardScaler) inside the custom model class
      - Log the custom pyfunc model with mlflow.pyfunc.log_model()
      - Load the model and run inference: mlflow.pyfunc.load_model(uri).predict(df)
      - Add artifacts dict to the custom model so external files are bundled at log time
    Resources:
      - {text: "Custom PyFunc Models", url: "https://mlflow.org/docs/latest/python_api/mlflow.pyfunc.html"}
      - {text: "PythonModel API", url: "https://mlflow.org/docs/latest/python_api/mlflow.pyfunc.html#mlflow.pyfunc.PythonModel"}
      - {text: "Saving Model Artifacts", url: "https://mlflow.org/docs/latest/models.html#custom-python-models"}
    Tip: "PyFunc is the universal MLflow model format — if your model isn't a standard library, wrap it in a PythonModel and you get serving, signature validation, and registry support for free."
    hasScore: false

  Day 10:
    Title: Model Serving with mlflow models serve and REST API
    Badge: practice
    Tasks:
      - {text: "Read the MLflow model serving docs", url: "https://mlflow.org/docs/latest/deployment/index.html"}
      - Serve a registered Production model: mlflow models serve -m 'models:/my-model/Production' -p 5001
      - Send a prediction request with curl using the /invocations endpoint and split-orient JSON
      - Test the same endpoint with Python requests library and a DataFrame payload
      - Understand the difference between mlflow models serve (local) and Databricks Model Serving
      - Build a simple FastAPI wrapper around mlflow.pyfunc.load_model() for a custom serving pattern
    Resources:
      - {text: "MLflow Deployment", url: "https://mlflow.org/docs/latest/deployment/index.html"}
      - {text: "REST API Reference", url: "https://mlflow.org/docs/latest/rest-api.html"}
      - {text: "Deploy to Databricks", url: "https://mlflow.org/docs/latest/deployment/deploy-model-to-databricks-model-serving.html"}
    Tip: "Always test the /invocations endpoint with a real sample payload before deploying — the split-orient format (columns + data) is easiest to construct from a DataFrame."
    hasScore: false

  Day 11:
    Title: Cloud Backends — S3, Azure Blob, and GCS Tracking Stores
    Badge: review
    Tasks:
      - {text: "Read about remote tracking server setup", url: "https://mlflow.org/docs/latest/tracking/server.html"}
      - Understand the two backends: artifact store (S3/GCS/Azure) and tracking store (Postgres/MySQL)
      - Configure an S3 artifact store URI: s3://my-bucket/mlflow-artifacts
      - Set MLFLOW_TRACKING_URI to point to a remote MLflow server
      - Understand how mlflow.set_tracking_uri() overrides the env variable programmatically
      - Review the boto3 credential chain that MLflow uses for S3 access
    Resources:
      - {text: "Remote Tracking Server", url: "https://mlflow.org/docs/latest/tracking/server.html"}
      - {text: "Artifact Store Configuration", url: "https://mlflow.org/docs/latest/tracking/artifacts.html#artifact-stores"}
      - {text: "Backend Store Configuration", url: "https://mlflow.org/docs/latest/tracking/backend-stores.html"}
    Tip: "Run the tracking server with --backend-store-uri postgresql://... and --default-artifact-root s3://... to get a production-grade, multi-user MLflow setup."
    hasScore: false

  Day 12:
    Title: Integrating MLflow into Training Pipelines and CI/CD
    Badge: practice
    Tasks:
      - {text: "Read about MLflow system tags and run metadata", url: "https://mlflow.org/docs/latest/tracking/tracking-api.html#system-tags"}
      - Wrap a multi-step sklearn Pipeline (imputer → scaler → model) in a single MLflow run
      - Log pipeline steps as nested runs using mlflow.start_run(nested=True)
      - Tag runs with git commit SHA: mlflow.set_tag('git_commit', subprocess.check_output(['git', 'rev-parse', 'HEAD']))
      - Write a GitHub Actions workflow step that runs training and pushes results to a remote MLflow server
      - Add a model promotion script that reads search_runs() and auto-promotes the best run
    Resources:
      - {text: "Nested Runs", url: "https://mlflow.org/docs/latest/tracking/tracking-api.html#nested-runs"}
      - {text: "System Tags Reference", url: "https://mlflow.org/docs/latest/tracking/tracking-api.html#system-tags"}
      - {text: "MLflow + GitHub Actions Example", url: "https://github.com/mlflow/mlflow/tree/master/examples"}
    Tip: "Use nested runs when you have a parent training job with multiple child model variants — the parent run collects overall metadata while children log per-model metrics."
    hasScore: false

  Day 13:
    Title: Review — Advanced Patterns and Real-World Gotchas
    Badge: review
    Tasks:
      - {text: "Read the MLflow FAQ and troubleshooting guide", url: "https://mlflow.org/docs/latest/faq.html"}
      - Review your runs from Days 1–12 in the UI — identify any missing artifacts or inconsistent tagging
      - Implement run name deduplication: use mlflow.set_experiment() + a timestamp-based run_name
      - Understand mlflow.last_active_run() and why it can cause silent bugs in threaded code
      - Compare the three model loading APIs: mlflow.pyfunc.load_model, mlflow.sklearn.load_model, mlflow.models.Model.load
      - Write a runbook: 5 bullet points covering the most common MLflow production issues and fixes
    Resources:
      - {text: "MLflow FAQ", url: "https://mlflow.org/docs/latest/faq.html"}
      - {text: "MLflow Changelog", url: "https://github.com/mlflow/mlflow/blob/master/CHANGELOG.md"}
      - {text: "MLflow Community Forum", url: "https://github.com/mlflow/mlflow/discussions"}
    Tip: "The most common production gotcha: mlflow.autolog() logs the model with the wrong signature when your input is a NumPy array — always pass an explicit signature."
    hasScore: false

  Day 14:
    Title: Capstone — Full MLOps Pipeline: Train → Track → Register → Serve
    Badge: exam
    Tasks:
      - {text: "Review the end-to-end MLflow scenario guide", url: "https://mlflow.org/docs/latest/introduction/index.html"}
      - Build a TrainFlow script that loads data, engineers features, trains 3 model variants, and logs each as a separate MLflow run with full params + metrics + artifacts
      - Select the best model by querying search_runs() and programmatically register it to the Model Registry
      - Transition the registered model to Production via MlflowClient and add a champion alias
      - Serve the Production model with mlflow models serve and verify predictions via the REST API with a test payload
      - Write a two-paragraph retrospective covering: what MLflow gave you for free vs what required extra effort
    Resources:
      - {text: "MLflow End-to-End Guide", url: "https://mlflow.org/docs/latest/introduction/index.html"}
      - {text: "Model Registry API", url: "https://mlflow.org/docs/latest/python_api/mlflow.client.html"}
      - {text: "MLflow Recipes (Structured Pipelines)", url: "https://mlflow.org/docs/latest/recipes.html"}
    Tip: "In the capstone, treat each model variant as a reproducible unit — log the exact training data hash, all hyperparams, and the evaluation split so any run can be rebuilt from scratch."
    hasScore: true

TOPICS:
  Topic 1:
    Name: Core Tracking
    Color: blue
    Days: [0, 1, 2]
    Description: The MLflow tracking API — logging params, metrics, artifacts, and navigating runs in the UI.

  Topic 2:
    Name: UI and Search
    Color: teal
    Days: [3]
    Description: Comparing and filtering runs with the MLflow UI and the search_runs() Python API.

  Topic 3:
    Name: Autologging and Integrations
    Color: purple
    Days: [4, 5]
    Description: One-line autologging for sklearn, XGBoost, and PyTorch; model flavors and signatures.

  Topic 4:
    Name: Model Registry
    Color: amber
    Days: [6]
    Description: Registering, staging, promoting, and loading models from the MLflow Model Registry.

  Topic 5:
    Name: Projects and Custom Models
    Color: coral
    Days: [7, 8]
    Description: Packaging reproducible experiments with MLproject files and building custom PyFunc models with bundled preprocessing.

  Topic 6:
    Name: Serving and Deployment
    Color: orange
    Days: [9, 10]
    Description: Serving registered models via the REST API, cloud artifact stores, and remote tracking servers.

  Topic 7:
    Name: Pipelines and CI/CD
    Color: teal
    Days: [11]
    Description: Nested runs, git tagging, auto-promotion scripts, and integrating MLflow into GitHub Actions workflows.

  Topic 8:
    Name: Review and Capstone
    Color: purple
    Days: [12, 13]
    Description: Advanced gotchas review and the end-to-end capstone: train → track → register → serve a production model.
```
