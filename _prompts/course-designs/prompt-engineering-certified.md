# Course Design: Prompt Engineering for Developers

## Metadata

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
EXAM_NOTES:       No formal exam. Seven focused days covering prompting techniques from basics to advanced patterns. Build a prompt evaluation system as the capstone.
CAPSTONE_PROJECT: Design a prompt system for a multi-step summarization + classification task: write a prompt suite with zero-shot, few-shot, and CoT variants, run all variants against a 20-item test set using an LLM-as-judge scorer, produce a results table showing accuracy and consistency across variants, and ship a final prompt with documented failure modes.
```

## AI Deep Dive Topics (3 cards)

1. **Chain-of-thought mechanics** — how step-by-step reasoning improves accuracy on multi-step problems and when self-consistency sampling (running CoT N times and majority-voting the answers) beats a single-pass response, and the failure mode where CoT confidently rationalizes a wrong answer.

2. **Structured output reliability** — the difference between JSON mode, function calling/tool use, and schema-constrained generation (Outlines/Guidance); why vanilla "output JSON" prompts fail at scale (truncation, key hallucination, nesting errors); and how to write prompts that stay within a schema even with smaller models.

3. **LLM-as-judge evaluation** — how to build automated prompt test suites using a judge LLM to score outputs for accuracy, relevance, and format compliance; how to calibrate judge agreement with human raters; and how to avoid positional bias (always-picks-first) and verbosity bias (always-picks-longer) in LLM judges.

## Notebooks

```
NOTEBOOKS:
  day-01-prompting-principles
  day-02-zero-shot-few-shot
  day-03-chain-of-thought
  day-04-iterative-refinement
  day-05-structured-outputs
  day-06-advanced-techniques
  day-07-capstone-prompt-system
```

## Days

### Day 1 — Prompting Principles: Clarity, Specificity, and Role Assignment
**Badge:** learn
**Tasks:**
- Read the OpenAI prompt engineering guide [https://platform.openai.com/docs/guides/prompt-engineering]
- Write three versions of the same prompt — vague, specific, role-assigned — and compare outputs
- Identify the failure mode in each vague prompt (hallucination, wrong format, off-topic)
- Practice output format control: ask for bullet points, JSON, and numbered steps from the same underlying question
- Read the Anthropic prompt engineering overview [https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview]
**Resources:**
- OpenAI Prompt Engineering Guide [https://platform.openai.com/docs/guides/prompt-engineering]
- Anthropic Prompt Engineering Overview [https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview]
- Learn Prompting — Basics [https://learnprompting.org/docs/basics/intro]
**Tip:** Specificity is the single highest-leverage lever in prompting. A vague prompt forces the model to guess your intent; a specific prompt with a concrete output format almost always beats it.

### Day 2 — Zero-Shot and Few-Shot Prompting
**Badge:** learn
**Tasks:**
- Read the few-shot prompting section of the Prompt Engineering Guide [https://www.promptingguide.ai/techniques/fewshot]
- Write a zero-shot classifier for sentiment (positive/negative/neutral) and measure accuracy on 10 examples
- Add 3 few-shot examples and measure the accuracy improvement
- Test the limit: find a task where few-shot examples hurt performance (label bias, format confusion)
- Read the paper "Few-Shot Learners are Zero-Shot Reasoners" overview [https://arxiv.org/abs/2205.01068]
**Resources:**
- Prompt Engineering Guide — Few-Shot [https://www.promptingguide.ai/techniques/fewshot]
- OpenAI Cookbook — Techniques to Improve Reliability [https://cookbook.openai.com/articles/techniques_to_improve_reliability]
- Learn Prompting — Few Shot [https://learnprompting.org/docs/basics/few_shot]
**Tip:** Few-shot examples should be diverse, representative, and in the same format as your expected output. Homogeneous examples (all positive, all simple) teach the model to pattern-match format, not understand the task.

### Day 3 — Chain-of-Thought Reasoning
**Badge:** practice
**Tasks:**
- Read the chain-of-thought prompting guide [https://www.promptingguide.ai/techniques/cot]
- Implement zero-shot CoT ("Let's think step by step") on three math word problems and compare to direct answers
- Implement few-shot CoT: write 3 worked examples with explicit reasoning steps and measure accuracy
- Implement self-consistency: run the same CoT prompt 5 times and majority-vote the final answers
- Find a case where CoT produces a confident but wrong answer — document why it failed
**Resources:**
- Prompt Engineering Guide — Chain-of-Thought [https://www.promptingguide.ai/techniques/cot]
- Original CoT Paper (Wei et al. 2022) [https://arxiv.org/abs/2201.11903]
- Self-Consistency Paper (Wang et al. 2022) [https://arxiv.org/abs/2203.11171]
**Tip:** Zero-shot CoT works by triggering the model's in-weights reasoning patterns. Few-shot CoT works by teaching the format of valid reasoning chains. Use few-shot CoT when the task has a specific structure; zero-shot CoT when you need quick improvement without writing examples.

### Day 4 — Iterative Prompt Refinement
**Badge:** practice
**Tasks:**
- Read the iterative prompt development section of the DeepLearning.AI course notes [https://learn.deeplearning.ai/courses/chatgpt-prompt-eng]
- Take a failing prompt, identify its failure mode (wrong format, hallucination, off-topic), and apply one fix at a time
- Build a 3-column refinement log: prompt version | failure observed | fix applied
- Run at least 3 refinement iterations on a summarization prompt until it passes on 8/10 test cases
- Write a post-mortem: what made the original prompt fail and what the minimal fix was
**Resources:**
- DeepLearning.AI ChatGPT Prompt Engineering for Developers [https://learn.deeplearning.ai/courses/chatgpt-prompt-eng]
- Anthropic — Be Clear and Direct [https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/be-clear-and-direct]
- OpenAI — Six Prompt Engineering Strategies [https://platform.openai.com/docs/guides/prompt-engineering/six-strategies-for-getting-better-results]
**Tip:** Fix one variable at a time. If you change the role, the format instruction, and the examples simultaneously, you cannot tell which fix worked. Treat prompt refinement like an A/B test — isolate each change.

### Day 5 — Structured Outputs: JSON Mode and Function Calling
**Badge:** practice
**Tasks:**
- Read the OpenAI structured outputs documentation [https://platform.openai.com/docs/guides/structured-outputs]
- Write a prompt that extracts entities (name, date, location) from unstructured text using JSON mode
- Implement function calling / tool use to extract the same entities — compare reliability vs JSON mode
- Demonstrate a failure: write a vanilla "output JSON" prompt and show it truncating or hallucinating keys
- Use Pydantic to validate the extracted output and handle the validation error gracefully
**Resources:**
- OpenAI — Structured Outputs [https://platform.openai.com/docs/guides/structured-outputs]
- Anthropic — Tool Use Guide [https://docs.anthropic.com/en/docs/build-with-claude/tool-use]
- Outlines Library for Schema-Constrained Generation [https://dottxt-ai.github.io/outlines/]
**Tip:** JSON mode guarantees valid JSON syntax but not schema compliance — the model can still hallucinate keys or skip required fields. Function calling / tool use with a strict schema is the only reliable way to get exact-shape output at production scale.

### Day 6 — Advanced Techniques: ReAct, Tree of Thought, and Meta-Prompting
**Badge:** practice
**Tasks:**
- Read the ReAct prompting paper overview [https://www.promptingguide.ai/techniques/react]
- Implement a ReAct loop: Thought → Action → Observation → repeat, with a search tool mock
- Read the Tree of Thought overview [https://www.promptingguide.ai/techniques/tot]
- Implement a simplified ToT: generate 3 candidate next steps, score each, pick the best, and repeat
- Write a meta-prompt: a prompt that generates prompts for a new task, then evaluate its output
**Resources:**
- Prompt Engineering Guide — ReAct [https://www.promptingguide.ai/techniques/react]
- Prompt Engineering Guide — Tree of Thought [https://www.promptingguide.ai/techniques/tot]
- Meta-Prompting Paper Overview [https://www.promptingguide.ai/techniques/meta-prompting]
**Tip:** ReAct is the foundation of most production agents. The Thought step forces the model to plan before acting; without it, tool calls are random rather than intentional. Always include a Thought before every Action.

### Day 7 — Capstone: Prompt System Design and Evaluation
**Badge:** exam
**Tasks:**
- Design a prompt suite for a summarization + classification task: write zero-shot, few-shot, and CoT variants
- Build a 20-item test set with ground-truth labels covering edge cases (short text, long text, ambiguous cases)
- Implement an LLM-as-judge scorer: send each model output to a judge LLM with a scoring rubric
- Run all three prompt variants against the test set and produce a results table: accuracy, consistency, avg tokens
- Document failure modes for the best-performing prompt and propose one further improvement
- Write a one-page prompt engineering decision guide: when to use zero-shot, few-shot, CoT, and structured output
**Resources:**
- Prompt Engineering Guide — LLM-as-Judge [https://www.promptingguide.ai/research/llm-eval]
- MT-Bench and Chatbot Arena Paper [https://arxiv.org/abs/2306.05685]
- Anthropic — Evaluations Guide [https://docs.anthropic.com/en/docs/test-and-evaluate/eval-overview]
**Tip:** The capstone is a miniature evaluation pipeline. Start with ground truth labels on your 20-item set before writing any prompts — anchoring on expected outputs prevents you from unconsciously tuning to your own model's tendencies.

## Topics

```
Topic 1: Prompting Fundamentals — color #E040FB — Days 0,1
Topic 2: Reasoning Techniques — color orange — Days 2,3
Topic 3: Refinement and Output Control — color teal — Days 3,4
Topic 4: Advanced Patterns — color purple — Days 5,6
Topic 5: Evaluation and Capstone — color amber — Days 6
```
