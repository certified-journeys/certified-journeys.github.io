# Ray for Distributed Python — Course Design
Generated: 2026-06-10

```
COURSE_TYPE:      notebook
COURSE_ID:        ray-certified
COURSE_FULL_NAME: Ray for Distributed Python
ICON:             RY
ACCENT_COLOR:     #00A5E0
ACCENT_LIGHT:     #E0F6FF
ACCENT_DARK:      #0077AA
ACCENT_DARK_DIM:  #00202E
PROVIDER:         Anyscale (Self-paced)
COST:             Free
TOTAL_DAYS:       10
DIFFICULTY:       Advanced
TAGS:             Distributed Computing, MLOps, Python, Scaling, Parallel Computing
EXAM_LINK:        https://docs.ray.io/en/latest/
EXAM_QUESTIONS:   null
EXAM_MINUTES:     null
EXAM_PASS_SCORE:  N/A
EXAM_NOTES:       No formal exam. Complete all 10 days and the capstone end-to-end distributed ML pipeline to demonstrate proficiency.

NOTEBOOKS:
  day-01-ray-core-tasks
  day-02-actors-object-store
  day-03-ray-cluster-setup
  day-04-ray-data-transforms
  day-05-ray-train-distributed
  day-06-ray-tune-hpo
  day-07-ray-serve-deployments
  day-08-ray-workflows-jobs
  day-09-debugging-observability
  day-10-capstone-ml-pipeline

DAYS:
  Day 1:
    Title: Ray Core — Remote Functions and the Task Model
    Badge: learn
    Tasks:
      - {text: "Read the Ray Core concepts overview — what Ray is, the driver/worker model, and when to use Ray", url: "https://docs.ray.io/en/latest/ray-core/walkthrough.html"}
      - Install Ray and verify the installation: pip install 'ray[default]' then python -c "import ray; print(ray.__version__)"
      - {text: "Read about ray.init() — how to start a local cluster, connect to an existing one, and key parameters like num_cpus and num_gpus", url: "https://docs.ray.io/en/latest/ray-core/api/doc/ray.init.html"}
      - Decorate a plain Python function with @ray.remote and call it with .remote() — observe that it returns an ObjectRef, not a result
      - Use ray.get() on a single ObjectRef and then on a list of ObjectRefs to fetch results; compare the two call patterns
      - {text: "Read about specifying resources with @ray.remote(num_cpus=2) and why resource requests matter for scheduling", url: "https://docs.ray.io/en/latest/ray-core/scheduling/resources.html"}
    Resources:
      - {text: "Ray Core Walkthrough", url: "https://docs.ray.io/en/latest/ray-core/walkthrough.html"}
      - {text: "ray.init() API Reference", url: "https://docs.ray.io/en/latest/ray-core/api/doc/ray.init.html"}
      - {text: "Ray Remote Functions", url: "https://docs.ray.io/en/latest/ray-core/tasks.html"}
    Tip: "ray.get() is a blocking call — it waits until the ObjectRef is ready. For maximum parallelism, submit all .remote() calls first, collect the ObjectRefs into a list, and then call ray.get(refs) once at the end. Never interleave .remote() and ray.get() in a loop."
    hasScore: false

  Day 2:
    Title: Actors and the Object Store — Stateful Distributed Computing
    Badge: learn
    Tasks:
      - {text: "Read the Ray Actors guide — how actors differ from tasks, the actor lifecycle, and when to use each", url: "https://docs.ray.io/en/latest/ray-core/actors.html"}
      - Define an actor class with @ray.remote, instantiate it with .remote(), and call methods using method.remote() — inspect the returned ObjectRefs
      - Build a stateful Counter actor with increment() and get_count() methods; run 100 concurrent increments and verify the final count
      - {text: "Read about the Ray object store (Plasma) — how large objects are stored, zero-copy reads, and object spilling", url: "https://docs.ray.io/en/latest/ray-core/objects.html"}
      - Put a large NumPy array into the object store with ray.put() and pass the ObjectRef to multiple remote tasks — observe that the data is not copied
      - {text: "Read about actor resource requests and actor pools for throughput scaling: ray.util.ActorPool", url: "https://docs.ray.io/en/latest/ray-core/api/doc/ray.util.ActorPool.html"}
    Resources:
      - {text: "Ray Actors Guide", url: "https://docs.ray.io/en/latest/ray-core/actors.html"}
      - {text: "Ray Objects and the Object Store", url: "https://docs.ray.io/en/latest/ray-core/objects.html"}
      - {text: "ActorPool API Reference", url: "https://docs.ray.io/en/latest/ray-core/api/doc/ray.util.ActorPool.html"}
    Tip: "Actors are single-threaded by default — each method call is queued and executed sequentially. If you need concurrent actor method execution, use @ray.remote(max_concurrency=N) to allow N simultaneous method calls. This is essential for serving actors that handle many concurrent requests."
    hasScore: false

  Day 3:
    Title: Ray Clusters — Local, Docker, and Kubernetes Setup
    Badge: learn
    Tasks:
      - {text: "Read the Ray cluster overview — head node, worker nodes, the GCS, and how tasks are scheduled across nodes", url: "https://docs.ray.io/en/latest/cluster/getting-started.html"}
      - Start a multi-process local Ray cluster with ray start --head and connect to it from Python with ray.init(address='auto')
      - {text: "Read the Ray Docker guide and understand the rayproject/ray Docker images and their variants (CPU, GPU, ML)", url: "https://docs.ray.io/en/latest/ray-overview/installation.html#docker-source-images"}
      - Write a ray cluster YAML configuration file for a local Docker-based cluster with one head and two worker nodes
      - {text: "Read about KubeRay — the Kubernetes operator for Ray — and the RayCluster custom resource definition", url: "https://docs.ray.io/en/latest/cluster/kubernetes/getting-started.html"}
      - Use ray status to inspect cluster resources, node availability, and pending tasks; shut down cleanly with ray stop
      - {text: "Read about autoscaling — how Ray clusters scale up workers on demand and scale down idle ones", url: "https://docs.ray.io/en/latest/cluster/key-concepts.html#autoscaling"}
    Resources:
      - {text: "Ray Cluster Getting Started", url: "https://docs.ray.io/en/latest/cluster/getting-started.html"}
      - {text: "KubeRay on Kubernetes", url: "https://docs.ray.io/en/latest/cluster/kubernetes/getting-started.html"}
      - {text: "Ray Autoscaling", url: "https://docs.ray.io/en/latest/cluster/key-concepts.html#autoscaling"}
    Tip: "For local development, ray.init() without arguments spins up a local Ray cluster automatically — you don't need to run ray start manually. Use ray.init(address='auto') only when you want to connect to a pre-existing cluster started with ray start --head."
    hasScore: false

  Day 4:
    Title: Ray Data — Datasets, Transforms, and Reading Files
    Badge: learn
    Tasks:
      - {text: "Read the Ray Data overview — what a Dataset is, how it maps to partitioned data, and how it integrates with Ray tasks", url: "https://docs.ray.io/en/latest/data/data.html"}
      - Read a CSV file into a Ray Dataset with ray.data.read_csv() and inspect schema, count, and a sample with .schema(), .count(), .show()
      - Read a Parquet file with ray.data.read_parquet() and compare the default parallelism with the num_cpus available on your cluster
      - {text: "Apply a row-level transform with .map() using a plain Python function; use .map_batches() for batch transforms with pandas or numpy", url: "https://docs.ray.io/en/latest/data/transforming-data.html"}
      - Chain transforms: .filter() to remove rows, .map_batches() to normalize a numeric column, then .to_pandas() to materialize results
      - {text: "Read about Dataset.write_parquet() and write_csv() — how Ray Data writes output in parallel across partitions", url: "https://docs.ray.io/en/latest/data/saving-data.html"}
    Resources:
      - {text: "Ray Data Overview", url: "https://docs.ray.io/en/latest/data/data.html"}
      - {text: "Ray Data Transformations", url: "https://docs.ray.io/en/latest/data/transforming-data.html"}
      - {text: "Ray Data Loading and Saving", url: "https://docs.ray.io/en/latest/data/saving-data.html"}
    Tip: "Ray Data is lazy by default — transforms like .map() and .filter() are not executed until you call a consuming operation like .to_pandas(), .show(), or .write_parquet(). This lets Ray Data optimize the full transform chain before executing. Use .materialize() to force execution and cache a Dataset in the object store for reuse."
    hasScore: false

  Day 5:
    Title: Ray Train — Distributed Model Training with PyTorch and scikit-learn
    Badge: practice
    Tasks:
      - {text: "Read the Ray Train overview — the Trainer abstraction, train functions, and how data is sharded across workers", url: "https://docs.ray.io/en/latest/train/train.html"}
      - {text: "Read the TorchTrainer guide and understand train_loop_per_worker, the ray.train.context, and checkpointing", url: "https://docs.ray.io/en/latest/train/api/doc/ray.train.torch.TorchTrainer.html"}
      - Write a TorchTrainer that trains a two-layer MLP on the Iris dataset across 2 workers; use ray.train.torch.prepare_model() and prepare_data_loader()
      - Report metrics per epoch using ray.train.report(metrics={'loss': loss_val}) and print the final training results
      - {text: "Read the SklearnTrainer guide for distributing scikit-learn model training across multiple workers", url: "https://docs.ray.io/en/latest/train/api/doc/ray.train.sklearn.SklearnTrainer.html"}
      - Train an XGBoostTrainer with XGBoostTrainer on a Ray Dataset; inspect the returned Result object for metrics and checkpoint path
      - {text: "Read about ScalingConfig — setting num_workers, use_gpu, and resources_per_worker", url: "https://docs.ray.io/en/latest/train/api/doc/ray.train.ScalingConfig.html"}
    Resources:
      - {text: "Ray Train Overview", url: "https://docs.ray.io/en/latest/train/train.html"}
      - {text: "TorchTrainer API", url: "https://docs.ray.io/en/latest/train/api/doc/ray.train.torch.TorchTrainer.html"}
      - {text: "Ray Train ScalingConfig", url: "https://docs.ray.io/en/latest/train/api/doc/ray.train.ScalingConfig.html"}
    Tip: "ray.train.torch.prepare_model() wraps your model in DistributedDataParallel and moves it to the correct device automatically. Call it after instantiating your model but before the training loop — and never call it inside the loop. Similarly, call prepare_data_loader() once per DataLoader, not per batch."
    hasScore: false

  Day 6:
    Title: Ray Tune — Hyperparameter Search at Scale
    Badge: practice
    Tasks:
      - {text: "Read the Ray Tune overview — the Tuner, search spaces, schedulers, and trial lifecycle", url: "https://docs.ray.io/en/latest/tune/index.html"}
      - Define a trainable function that accepts a config dict, trains a model, and calls tune.report(accuracy=val_acc) each epoch
      - Build a search space using tune.grid_search() for discrete values and tune.loguniform() for learning rate; run tuner.fit()
      - {text: "Use the ASHAScheduler to terminate poorly-performing trials early — understand grace_period and reduction_factor", url: "https://docs.ray.io/en/latest/tune/api/doc/ray.tune.schedulers.ASHAScheduler.html"}
      - {text: "Swap in the Optuna search algorithm with OptunaSearch — compare ASHA+Optuna vs grid search on the same problem", url: "https://docs.ray.io/en/latest/tune/api/doc/ray.tune.search.optuna.OptunaSearch.html"}
      - Retrieve the best trial with tuner.get_results().get_best_result() and print the best config and best metric value
      - {text: "Read about PopulationBasedTraining (PBT) — the scheduler that mutates hyperparameters during training", url: "https://docs.ray.io/en/latest/tune/api/doc/ray.tune.schedulers.PopulationBasedTraining.html"}
    Resources:
      - {text: "Ray Tune Overview", url: "https://docs.ray.io/en/latest/tune/index.html"}
      - {text: "ASHAScheduler API", url: "https://docs.ray.io/en/latest/tune/api/doc/ray.tune.schedulers.ASHAScheduler.html"}
      - {text: "OptunaSearch API", url: "https://docs.ray.io/en/latest/tune/api/doc/ray.tune.search.optuna.OptunaSearch.html"}
    Tip: "ASHA (Asynchronous Successive Halving) is the right default scheduler for most HPO jobs. It aggressively kills bad trials at checkpoints without waiting for a synchronization barrier, giving much better GPU utilization than synchronous Hyperband. Start with ASHA + Optuna as your baseline combination."
    hasScore: false

  Day 7:
    Title: Ray Serve — Model Serving, Deployments, and HTTP Endpoints
    Badge: practice
    Tasks:
      - {text: "Read the Ray Serve overview — deployments, the ingress, handle-based composition, and the serve.run() entry point", url: "https://docs.ray.io/en/latest/serve/index.html"}
      - Define a minimal @serve.deployment class with a __call__(self, request) method that returns a JSON response; deploy and query it with curl
      - {text: "Read about deployment configuration: num_replicas, ray_actor_options (CPUs/GPUs), and autoscaling_config", url: "https://docs.ray.io/en/latest/serve/configure-serve-deployment.html"}
      - Load an sklearn model in __init__ and serve predictions via HTTP POST; test with requests.post() from the same notebook
      - {text: "Read about deployment composition — calling one deployment handle from another to build a preprocessing + inference pipeline", url: "https://docs.ray.io/en/latest/serve/model_composition.html"}
      - Chain two deployments: a Preprocessor that normalizes input and a Predictor that runs inference; wire them with serve.handle
      - {text: "Read about FastAPI integration with serve.ingress — expose full OpenAPI docs from a Ray Serve deployment", url: "https://docs.ray.io/en/latest/serve/http-guide.html"}
    Resources:
      - {text: "Ray Serve Overview", url: "https://docs.ray.io/en/latest/serve/index.html"}
      - {text: "Deployment Configuration", url: "https://docs.ray.io/en/latest/serve/configure-serve-deployment.html"}
      - {text: "Model Composition in Ray Serve", url: "https://docs.ray.io/en/latest/serve/model_composition.html"}
    Tip: "Ray Serve deployments are actors under the hood. Setting num_replicas=N creates N actor instances behind a load balancer. For models that are large but fast at inference, keep num_replicas low and increase max_concurrent_queries instead — this amortizes model load cost without duplicating model memory."
    hasScore: false

  Day 8:
    Title: Ray Workflows and Job Submission
    Badge: review
    Tasks:
      - {text: "Read the Ray Jobs overview — submitting jobs via the Jobs API, the Ray dashboard, and the Ray CLI", url: "https://docs.ray.io/en/latest/cluster/running-applications/job-submission/index.html"}
      - Submit a Ray job with ray job submit --working-dir . -- python my_script.py and inspect status with ray job status <job-id>
      - {text: "Read the Ray Workflows guide — durable, fault-tolerant computation graphs that survive driver failures", url: "https://docs.ray.io/en/latest/workflows/basics.html"}
      - Convert a three-step data pipeline into a Ray Workflow using @workflow.step decorators and run it with workflow.run()
      - {text: "Read about workflow durability — how Ray Workflows checkpoint output of each step so the graph can resume after a crash", url: "https://docs.ray.io/en/latest/workflows/basics.html#durability"}
      - Use ray job logs <job-id> to stream logs from a running job; use ray job stop to cancel an in-progress job
      - {text: "Compare Ray Workflows vs raw Ray tasks: when the checkpointing overhead is worth it", url: "https://docs.ray.io/en/latest/workflows/comparison.html"}
    Resources:
      - {text: "Ray Jobs Submission Guide", url: "https://docs.ray.io/en/latest/cluster/running-applications/job-submission/index.html"}
      - {text: "Ray Workflows Guide", url: "https://docs.ray.io/en/latest/workflows/basics.html"}
      - {text: "Ray Workflows vs Tasks Comparison", url: "https://docs.ray.io/en/latest/workflows/comparison.html"}
    Tip: "Ray Workflows write checkpoint data to durable storage after every step — this adds latency per step but makes the pipeline restartable from the last completed step. Use Ray Workflows for multi-hour pipelines where restarting from scratch after a failure is costly; use raw tasks for sub-minute functions where the overhead is not worth it."
    hasScore: false

  Day 9:
    Title: Debugging and Observability — Dashboard, Timeline, and Logs
    Badge: review
    Tasks:
      - {text: "Read the Ray Dashboard guide — how to open it, what the Cluster, Jobs, Actors, and Metrics tabs show", url: "https://docs.ray.io/en/latest/ray-observability/getting-started.html"}
      - Start Ray with ray.init() in a notebook and open the dashboard URL printed to stdout; navigate to the Jobs and Actors tabs
      - {text: "Read about ray.timeline() — generating a Chrome trace of task execution to identify scheduling gaps and hot spots", url: "https://docs.ray.io/en/latest/ray-observability/reference/api.html#ray.timeline"}
      - Run a parallel workload, call ray.timeline(filename='timeline.json'), and open the file in chrome://tracing to inspect task spans
      - {text: "Read about structured logging with ray.runtime_context and how to emit logs visible in the Ray Dashboard", url: "https://docs.ray.io/en/latest/ray-observability/user-guides/ray-logging.html"}
      - Use ray.util.state.list_tasks() and list_actors() to programmatically inspect running tasks and actor state from the driver
      - {text: "Read about memory debugging — ray memory, object spilling thresholds, and detecting object store pressure", url: "https://docs.ray.io/en/latest/ray-core/objects/object-spilling.html"}
    Resources:
      - {text: "Ray Observability Guide", url: "https://docs.ray.io/en/latest/ray-observability/getting-started.html"}
      - {text: "Ray Timeline and Profiling", url: "https://docs.ray.io/en/latest/ray-observability/reference/api.html#ray.timeline"}
      - {text: "Ray Object Spilling", url: "https://docs.ray.io/en/latest/ray-core/objects/object-spilling.html"}
    Tip: "The Ray Dashboard's Metrics tab integrates with Prometheus and Grafana for production monitoring. For development, the built-in timeline is the fastest way to diagnose scheduling inefficiency: a wide gap between task submission (thin bar) and task start (color bar) means workers are not available — check resource requests vs available CPUs."
    hasScore: false

  Day 10:
    Title: Capstone — End-to-End Distributed ML Pipeline (Data → Train → Tune → Serve)
    Badge: exam
    Tasks:
      - Initialize a Ray cluster with ray.init() and verify resource availability with ray.cluster_resources(); log the cluster topology to a JSON file
      - Load a real dataset (e.g. California Housing or Breast Cancer) using ray.data.read_csv() and build a preprocessing pipeline with .map_batches() — normalize features and encode labels in parallel
      - Write a TorchTrainer training function that accepts a config dict; use ScalingConfig(num_workers=2) and report val_loss and val_accuracy each epoch with ray.train.report()
      - Run Ray Tune hyperparameter search over learning_rate (loguniform), batch_size (grid), and hidden_size (choice) using ASHAScheduler and OptunaSearch — budget 20 trials
      - Retrieve the best trial result; reload the best checkpoint with ray.train.Result.checkpoint and run inference on the held-out test set to compute final accuracy
      - Define a Ray Serve deployment class that loads the best checkpoint in __init__, accepts POST /predict requests, and returns predictions as JSON; deploy with serve.run()
      - Write an end-to-end integration test using requests.post() that sends 10 samples to the deployed endpoint and asserts predictions match expected labels
      - {text: "Profile the full pipeline with ray.timeline() and identify the top bottleneck; document it in a markdown cell", url: "https://docs.ray.io/en/latest/ray-observability/reference/api.html#ray.timeline"}
    Resources:
      - {text: "Ray Core API Reference", url: "https://docs.ray.io/en/latest/ray-core/api/index.html"}
      - {text: "Ray Train Documentation", url: "https://docs.ray.io/en/latest/train/train.html"}
      - {text: "Ray Tune Documentation", url: "https://docs.ray.io/en/latest/tune/index.html"}
      - {text: "Ray Serve Documentation", url: "https://docs.ray.io/en/latest/serve/index.html"}
    Tip: "The capstone connects all five Ray libraries in a single pipeline. Key handoff points: Ray Data → Ray Train (pass a Dataset to TorchTrainer via datasets={'train': ds}), Ray Train → Ray Tune (pass TorchTrainer as the trainable to Tuner), Ray Tune → Ray Serve (load the best checkpoint path from tuner.get_results().get_best_result().checkpoint). Get each handoff working in isolation before wiring the full pipeline."
    hasScore: true

TOPICS:
  Topic 1:
    Name: Ray Core
    Color: blue
    Days: 0, 1, 2   # Days 1–3 (0-indexed): remote tasks, actors/object store, cluster setup

  Topic 2:
    Name: Ray Data
    Color: teal
    Days: 3          # Day 4 (0-indexed): datasets, transforms, read/write

  Topic 3:
    Name: Training & Tuning
    Color: purple
    Days: 4, 5       # Days 5–6 (0-indexed): Ray Train, Ray Tune / HPO

  Topic 4:
    Name: Serving & Workflows
    Color: amber
    Days: 6, 7       # Days 7–8 (0-indexed): Ray Serve deployments, Ray Workflows + Jobs

  Topic 5:
    Name: Observability
    Color: coral
    Days: 8          # Day 9 (0-indexed): dashboard, timeline, logging, memory

  Topic 6:
    Name: Capstone
    Color: orange
    Days: 9          # Day 10 (0-indexed): end-to-end pipeline
```
