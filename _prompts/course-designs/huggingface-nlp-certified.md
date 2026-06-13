# Hugging Face NLP for Engineers — Course Design
Generated: 2026-06-13

```
COURSE_TYPE:      notebook
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

NOTEBOOKS:
  day-01-hf-ecosystem
  day-02-tokenizers-deep-dive
  day-03-pipeline-api
  day-04-automodel-autotokenizer
  day-05-datasets-library
  day-06-evaluate-metrics
  day-07-trainer-api-finetune
  day-08-token-classification-ner
  day-09-question-answering
  day-10-summarization-translation
  day-11-hub-model-cards
  day-12-accelerate-training
  day-13-review-advanced-patterns
  day-14-capstone-finetune-deploy

DAYS:
  Day 1:
    Title: The Hugging Face Ecosystem — Hub, Libraries, and First Pipeline
    Badge: learn
    Tasks:
      - {text: "Read the Hugging Face NLP Course Chapter 1", url: "https://huggingface.co/learn/nlp-course/chapter1/1"}
      - Install the core libraries: pip install transformers datasets evaluate accelerate
      - Browse the Hub at huggingface.co/models and filter by task (text-classification) and language (en)
      - Run your first pipeline in three lines: from transformers import pipeline; classifier = pipeline('sentiment-analysis'); print(classifier('I love NLP!'))
      - Explore the model card for bert-base-uncased — read the training data, limitations, and intended use sections
    Resources:
      - {text: "HF NLP Course Chapter 1", url: "https://huggingface.co/learn/nlp-course/chapter1/1"}
      - {text: "Hugging Face Hub Docs", url: "https://huggingface.co/docs/hub/index"}
      - {text: "Transformers Installation Guide", url: "https://huggingface.co/docs/transformers/installation"}
    Tip: "The Hub is more than a model zoo — it hosts datasets, Spaces (demo apps), and model cards. Spend 10 minutes browsing before writing any code."
    hasScore: false

  Day 2:
    Title: Tokenizers Deep Dive — BPE, WordPiece, and SentencePiece
    Badge: learn
    Tasks:
      - {text: "Read the Hugging Face NLP Course Chapter 2 on tokenizers", url: "https://huggingface.co/learn/nlp-course/chapter2/4"}
      - Load the BERT tokenizer and tokenize a sentence: inspect input_ids, attention_mask, and token_type_ids
      - Compare tokenization output between bert-base-uncased (WordPiece) and gpt2 (BPE) for the same input
      - Tokenize a batch with padding and truncation: tokenizer(texts, padding=True, truncation=True, max_length=128)
      - Decode token IDs back to strings with tokenizer.decode() and tokenizer.batch_decode()
      - {text: "Explore the tokenizer vocabulary size and special tokens for three models", url: "https://huggingface.co/docs/transformers/main_classes/tokenizer"}
    Resources:
      - {text: "Tokenizers API Reference", url: "https://huggingface.co/docs/transformers/main_classes/tokenizer"}
      - {text: "NLP Course: Tokenizers Chapter", url: "https://huggingface.co/learn/nlp-course/chapter2/4"}
      - {text: "Tokenizers Library (Fast Tokenizers)", url: "https://huggingface.co/docs/tokenizers/index"}
    Tip: "Use fast tokenizers (the default) — they are backed by Rust and are 10-100x faster than slow Python tokenizers, especially for large batches."
    hasScore: false

  Day 3:
    Title: The Pipeline API — Classification, NER, Summarization, and More
    Badge: learn
    Tasks:
      - {text: "Read the pipeline API docs", url: "https://huggingface.co/docs/transformers/main_classes/pipelines"}
      - Run a zero-shot classification pipeline with candidate_labels on a custom text snippet
      - Run a named-entity-recognition pipeline and inspect the entity spans and confidence scores
      - Run a text-generation pipeline with GPT-2 using max_new_tokens=100 and num_return_sequences=3
      - Run a summarization pipeline on a 500-word article and compare the output length with min_length and max_length settings
      - Benchmark pipeline inference time for a batch of 32 examples using time.perf_counter
    Resources:
      - {text: "Pipeline API Reference", url: "https://huggingface.co/docs/transformers/main_classes/pipelines"}
      - {text: "Zero-Shot Classification", url: "https://huggingface.co/docs/transformers/en/model_doc/roberta#transformers.RobertaForSequenceClassification"}
      - {text: "Task Summary on Hugging Face", url: "https://huggingface.co/docs/transformers/task_summary"}
    Tip: "Set device=0 in the pipeline() call to move inference to GPU — on CPU, batching with batch_size=8 or larger is the next-best speedup."
    hasScore: false

  Day 4:
    Title: AutoModel and AutoTokenizer — Loading Any Model from the Hub
    Badge: learn
    Tasks:
      - {text: "Read the Auto Classes documentation", url: "https://huggingface.co/docs/transformers/model_doc/auto"}
      - Load distilbert-base-uncased with AutoTokenizer.from_pretrained() and AutoModel.from_pretrained()
      - Understand model output: extract last_hidden_state and the [CLS] token embedding
      - Load a task-specific head with AutoModelForSequenceClassification.from_pretrained() on a fine-tuned checkpoint
      - Run a forward pass manually: pass tokenized inputs as a dict of tensors and inspect logits shape
      - {text: "Use torch.no_grad() for inference and understand why it matters for memory", url: "https://huggingface.co/docs/transformers/en/quicktour"}
    Resources:
      - {text: "Auto Classes Reference", url: "https://huggingface.co/docs/transformers/model_doc/auto"}
      - {text: "Model Outputs Guide", url: "https://huggingface.co/docs/transformers/main_classes/output"}
      - {text: "Quick Tour of Transformers", url: "https://huggingface.co/docs/transformers/quicktour"}
    Tip: "AutoModelForSequenceClassification automatically adds a classification head on top of the base model — always pick the task-specific Auto class over the base AutoModel for downstream tasks."
    hasScore: false

  Day 5:
    Title: The Datasets Library — Loading, Filtering, Mapping, and Tokenizing
    Badge: practice
    Tasks:
      - {text: "Read the Datasets quickstart", url: "https://huggingface.co/docs/datasets/quickstart"}
      - Load the imdb dataset with load_dataset('imdb') and inspect splits, features, and a few examples
      - Filter the training set to retain only examples with label=1 using dataset.filter()
      - Apply a tokenization function across the entire dataset with dataset.map(tokenize_fn, batched=True)
      - Shuffle and select a 1000-example subset with dataset.shuffle(seed=42).select(range(1000))
      - Save the processed dataset to disk with dataset.save_to_disk() and reload it with load_from_disk()
    Resources:
      - {text: "Datasets Docs", url: "https://huggingface.co/docs/datasets/index"}
      - {text: "Dataset.map() Reference", url: "https://huggingface.co/docs/datasets/package_reference/main_classes#datasets.Dataset.map"}
      - {text: "Hugging Face Dataset Hub", url: "https://huggingface.co/datasets"}
    Tip: "Use batched=True in dataset.map() — it passes lists of examples to your function instead of one at a time, making tokenization 10x faster on large datasets."
    hasScore: false

  Day 6:
    Title: The Evaluate Library — Metrics After Fine-Tuning (F1, BLEU, ROUGE)
    Badge: learn
    Tasks:
      - {text: "Read the Evaluate library quickstart", url: "https://huggingface.co/docs/evaluate/index"}
      - Load and compute accuracy: evaluate.load('accuracy').compute(predictions=[1,0,1], references=[1,1,1])
      - Load the F1 metric and compute macro-averaged F1 for a multi-class classification output
      - Load the ROUGE metric and evaluate a list of model-generated summaries against references
      - Load the BLEU metric and evaluate three machine translation outputs with sacrebleu
      - {text: "Use evaluator.compute() end-to-end with a pipeline and a dataset split", url: "https://huggingface.co/docs/evaluate/choosing_a_metric"}
    Resources:
      - {text: "Evaluate Docs", url: "https://huggingface.co/docs/evaluate/index"}
      - {text: "Choosing a Metric Guide", url: "https://huggingface.co/docs/evaluate/choosing_a_metric"}
      - {text: "Metrics on the Hub", url: "https://huggingface.co/evaluate-metric"}
    Tip: "ROUGE scores are notoriously sensitive to whitespace and case — always use rouge_types=['rouge1','rouge2','rougeL'] and stemming=True for consistent comparisons across runs."
    hasScore: false

  Day 7:
    Title: Fine-Tuning BERT for Text Classification with the Trainer API
    Badge: practice
    Tasks:
      - {text: "Read the Trainer API fine-tuning guide", url: "https://huggingface.co/docs/transformers/training"}
      - Tokenize the SST-2 (or imdb) dataset and set format to torch tensors with dataset.set_format()
      - Define TrainingArguments with output_dir, num_train_epochs=3, per_device_train_batch_size=16, evaluation_strategy='epoch'
      - Instantiate a Trainer with model, args, train_dataset, eval_dataset, and a compute_metrics function returning accuracy
      - Run trainer.train() and watch the eval loss and accuracy improve per epoch
      - Save and reload the fine-tuned model with trainer.save_model() and AutoModelForSequenceClassification.from_pretrained()
    Resources:
      - {text: "Fine-Tuning Guide", url: "https://huggingface.co/docs/transformers/training"}
      - {text: "TrainingArguments Reference", url: "https://huggingface.co/docs/transformers/main_classes/trainer#transformers.TrainingArguments"}
      - {text: "NLP Course Chapter 3: Fine-Tuning", url: "https://huggingface.co/learn/nlp-course/chapter3/1"}
    Tip: "Set load_best_model_at_end=True and save_strategy='epoch' in TrainingArguments so the Trainer automatically restores the checkpoint with the best eval metric."
    hasScore: false

  Day 8:
    Title: Token Classification — NER with IOB Tagging and Sequence Labeling Heads
    Badge: practice
    Tasks:
      - {text: "Read the token classification task guide", url: "https://huggingface.co/docs/transformers/tasks/token_classification"}
      - Load the conll2003 dataset and inspect the ner_tags feature with its ClassLabel mapping
      - Understand IOB2 tagging: B- (beginning), I- (inside), O (outside) prefixes and why they matter for span detection
      - Write a tokenize_and_align_labels function that handles subword tokenization by propagating labels across subword tokens
      - Fine-tune bert-base-cased for NER using AutoModelForTokenClassification with num_labels set to the tag count
      - Evaluate with the seqeval metric which computes entity-level precision, recall, and F1
    Resources:
      - {text: "Token Classification Guide", url: "https://huggingface.co/docs/transformers/tasks/token_classification"}
      - {text: "seqeval Metric", url: "https://huggingface.co/spaces/evaluate-metric/seqeval"}
      - {text: "CoNLL-2003 Dataset", url: "https://huggingface.co/datasets/conll2003"}
    Tip: "Set the label for the first subword token of each word and use -100 for continuation tokens — PyTorch's CrossEntropyLoss ignores index -100 by default, so continuation tokens don't contribute to the loss."
    hasScore: false

  Day 9:
    Title: Question Answering — Extractive QA with SQuAD-Style Models
    Badge: practice
    Tasks:
      - {text: "Read the QA task guide", url: "https://huggingface.co/docs/transformers/tasks/question_answering"}
      - Run the question-answering pipeline with deepset/roberta-base-squad2 on a custom context+question pair
      - Load the squad dataset and understand the context, question, answers (answer_start, text) structure
      - Write a preprocessing function that tokenizes question-context pairs and computes start/end token positions for the answer span
      - Fine-tune bert-base-uncased for extractive QA using AutoModelForQuestionAnswering
      - Evaluate using the squad metric (exact match and F1) from the evaluate library
    Resources:
      - {text: "Question Answering Task Guide", url: "https://huggingface.co/docs/transformers/tasks/question_answering"}
      - {text: "SQuAD Dataset", url: "https://huggingface.co/datasets/squad"}
      - {text: "NLP Course Chapter 7: QA", url: "https://huggingface.co/learn/nlp-course/chapter7/7"}
    Tip: "Long contexts get truncated during tokenization — use stride (doc_stride) to create overlapping windows so answer spans near chunk boundaries are still recoverable."
    hasScore: false

  Day 10:
    Title: Summarization and Translation — Seq2Seq Models and Generation Configs
    Badge: learn
    Tasks:
      - {text: "Read the summarization task guide", url: "https://huggingface.co/docs/transformers/tasks/summarization"}
      - Load facebook/bart-large-cnn and run the summarization pipeline on a news article
      - Fine-tune t5-small for abstractive summarization on the cnn_dailymail dataset using Seq2SeqTrainer
      - Set generation_config: num_beams=4, length_penalty=2.0, early_stopping=True in TrainingArguments
      - Load Helsinki-NLP/opus-mt-en-fr and translate five English sentences to French with the translation pipeline
      - Compare ROUGE-L scores between greedy decoding and beam search for the same model
    Resources:
      - {text: "Summarization Task Guide", url: "https://huggingface.co/docs/transformers/tasks/summarization"}
      - {text: "Seq2SeqTrainer Docs", url: "https://huggingface.co/docs/transformers/main_classes/trainer#transformers.Seq2SeqTrainer"}
      - {text: "Generation Configuration", url: "https://huggingface.co/docs/transformers/main_classes/text_generation"}
    Tip: "Seq2SeqTrainer needs predict_with_generate=True in Seq2SeqTrainingArguments so that compute_metrics receives decoded strings instead of raw logits."
    hasScore: false

  Day 11:
    Title: Pushing to the Hub — Model Cards, Spaces, and Sharing Your Model
    Badge: practice
    Tasks:
      - {text: "Read the Hub sharing guide", url: "https://huggingface.co/docs/hub/models-uploading"}
      - Authenticate with huggingface-cli login using a write-access token from your HF account
      - Push your fine-tuned Day 7 model to your Hub namespace: trainer.push_to_hub('your-username/bert-imdb-sentiment')
      - Write a model card (README.md) covering: model description, training data, evaluation results, intended use, and limitations
      - Load your pushed model from the Hub in a new session to verify it works: pipeline('text-classification', model='your-username/bert-imdb-sentiment')
      - {text: "Create a Gradio Space that demos your model with a text input and label output", url: "https://huggingface.co/docs/hub/spaces-sdks-gradio"}
    Resources:
      - {text: "Uploading Models to the Hub", url: "https://huggingface.co/docs/hub/models-uploading"}
      - {text: "Model Cards Guide", url: "https://huggingface.co/docs/hub/model-cards"}
      - {text: "Hugging Face Spaces with Gradio", url: "https://huggingface.co/docs/hub/spaces-sdks-gradio"}
    Tip: "Add language, license, and tags metadata to your model card YAML front matter — these fields make your model discoverable in Hub search and the pipeline() task filter."
    hasScore: false

  Day 12:
    Title: Accelerate and Efficient Training — Multi-GPU, Mixed Precision, Gradient Checkpointing
    Badge: review
    Tasks:
      - {text: "Read the Accelerate library overview", url: "https://huggingface.co/docs/accelerate/index"}
      - Refactor a bare PyTorch training loop to use Accelerator: wrap model, optimizer, and dataloader with accelerator.prepare()
      - Enable fp16 mixed precision training by passing fp16=True to TrainingArguments (or Accelerator(mixed_precision='fp16'))
      - Enable gradient checkpointing to reduce VRAM usage: model.gradient_checkpointing_enable()
      - Understand the tradeoff: gradient checkpointing reduces memory by ~40% at the cost of ~30% more compute
      - {text: "Profile GPU memory during training using torch.cuda.max_memory_allocated()", url: "https://huggingface.co/docs/accelerate/usage_guides/memory"}
    Resources:
      - {text: "Accelerate Docs", url: "https://huggingface.co/docs/accelerate/index"}
      - {text: "Efficient Training Techniques", url: "https://huggingface.co/docs/transformers/perf_train_gpu_one"}
      - {text: "Mixed Precision Training Guide", url: "https://huggingface.co/docs/accelerate/usage_guides/mixed_precision"}
    Tip: "Start every fine-tuning job with fp16=True — it halves memory consumption and speeds up training on modern GPUs with no measurable loss in accuracy for most NLP tasks."
    hasScore: false

  Day 13:
    Title: Review — Advanced Patterns, Common Pitfalls, and Production Readiness
    Badge: review
    Tasks:
      - {text: "Read the transformers best practices guide", url: "https://huggingface.co/docs/transformers/pipeline_tutorial"}
      - Review Days 1–12 notebooks: check every fine-tuning run has a saved model, evaluation metrics, and a descriptive output_dir name
      - Understand the difference between tokenizer.pad_token and tokenizer.eos_token — and why GPT-2 requires pad_token = eos_token for batch inference
      - Debug a common shape mismatch: explain why labels must be shifted by one position in causal LM training
      - Review the three most common OOM errors in transformer fine-tuning: batch size too large, sequence length too long, no gradient accumulation
      - Write a production checklist: 6 bullet points covering tokenizer saving, model saving, HF Hub push, eval results, model card, and inference test
    Resources:
      - {text: "Transformers Best Practices", url: "https://huggingface.co/docs/transformers/pipeline_tutorial"}
      - {text: "Troubleshooting Guide", url: "https://huggingface.co/docs/transformers/debugging"}
      - {text: "NLP Course Chapter 8: Debugging", url: "https://huggingface.co/learn/nlp-course/chapter8/1"}
    Tip: "Always call tokenizer.save_pretrained(output_dir) alongside model.save_pretrained(output_dir) — loading a model without its matching tokenizer is a silent bug that causes subtle mismatches."
    hasScore: false

  Day 14:
    Title: Capstone — Fine-Tune a Transformer on a Custom NLP Task and Deploy to Spaces
    Badge: exam
    Tasks:
      - {text: "Review the end-to-end NLP Course walkthrough", url: "https://huggingface.co/learn/nlp-course/chapter7/1"}
      - Choose a classification or sequence labeling task and source a dataset from the Hub (or prepare a custom CSV with load_dataset('csv'))
      - Fine-tune a pretrained checkpoint (bert-base-uncased or distilbert-base-uncased) for 3 epochs using Trainer with fp16=True and load_best_model_at_end=True
      - Evaluate on a held-out test split with the appropriate metric (F1 for NER, accuracy for classification, ROUGE for summarization) and report the final score
      - Push the fine-tuned model and tokenizer to your Hub namespace with trainer.push_to_hub() and write a complete model card
      - Deploy a Gradio demo Space that loads your Hub model, accepts user text input, and displays predictions with confidence scores
    Resources:
      - {text: "NLP Course Chapter 7: Full Fine-Tuning Walkthroughs", url: "https://huggingface.co/learn/nlp-course/chapter7/1"}
      - {text: "Gradio Quickstart", url: "https://www.gradio.app/guides/quickstart"}
      - {text: "Hugging Face Spaces Guide", url: "https://huggingface.co/docs/hub/spaces"}
    Tip: "For the capstone, document every training decision in your model card: why you chose the base model, what learning rate and batch size you used, and what the final eval metric was — this is what makes a Hub model genuinely useful to others."
    hasScore: true

TOPICS:
  Topic 1:
    Name: Ecosystem and Foundations
    Color: blue
    Days: [0, 1]
    Description: The Hugging Face Hub, core library installation, tokenizer internals (BPE, WordPiece, SentencePiece), and understanding input IDs, attention masks, and special tokens.

  Topic 2:
    Name: Pipelines and Auto Classes
    Color: teal
    Days: [2, 3]
    Description: High-level pipeline API for all NLP tasks, and loading any model from the Hub with AutoModel, AutoTokenizer, and task-specific Auto classes.

  Topic 3:
    Name: Datasets and Evaluation
    Color: purple
    Days: [4, 5]
    Description: Loading, filtering, mapping, and tokenizing datasets with the Datasets library; computing F1, BLEU, ROUGE, and accuracy with the Evaluate library.

  Topic 4:
    Name: Fine-Tuning Core Tasks
    Color: coral
    Days: [6, 7, 8]
    Description: Trainer API fine-tuning for text classification, NER with IOB tagging and label alignment, and extractive QA with SQuAD-style span prediction.

  Topic 5:
    Name: Seq2Seq and Generation
    Color: amber
    Days: [9]
    Description: Summarization and translation with seq2seq models, Seq2SeqTrainer, beam search, and generation configuration.

  Topic 6:
    Name: Hub and Sharing
    Color: blue
    Days: [10]
    Description: Pushing models and tokenizers to the Hub, writing model cards, and deploying Gradio demo Spaces.

  Topic 7:
    Name: Efficient Training
    Color: teal
    Days: [11]
    Description: Accelerate library, mixed-precision fp16 training, gradient checkpointing, and profiling GPU memory during transformer fine-tuning.

  Topic 8:
    Name: Review and Capstone
    Color: purple
    Days: [12, 13]
    Description: Common pitfalls, production readiness checklist, and the end-to-end capstone: fine-tune a transformer on a custom task and ship it to Hugging Face Spaces.
```
