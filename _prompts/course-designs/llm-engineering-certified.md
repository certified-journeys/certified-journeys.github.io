# LLM Engineering with LangChain — Course Design
Generated: 2026-06-13

```
COURSE_TYPE:      notebook
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

CAPSTONE_PROJECT: Build a production-ready multi-document RAG chatbot that ingests PDFs and web
                  pages, stores embeddings in a persistent Chroma vector store, retrieves context
                  with MMR re-ranking, streams answers through a conversational chain with
                  ConversationSummaryMemory, and exposes the full pipeline as a Gradio interface.

EXAM_CHECKLIST:
  - Can write an LCEL chain from scratch — PromptTemplate | ChatModel | OutputParser — without looking at docs
  - Built and queried a vector store end-to-end: loaded docs, split, embedded, stored in Chroma, and ran similarity_search
  - Implemented a RAG pipeline with retrieval, context injection, and a grounded answer — no hallucinated citations
  - Can explain the difference between ConversationBufferMemory and ConversationSummaryMemory and choose correctly for a given context window budget
  - Wired at least two custom tools to a ReAct agent and verified the tool-calling loop with a real query

AI_DEEP_DIVE_TOPICS:
  - LCEL (LangChain Expression Language) — the pipe operator, Runnables, RunnablePassthrough, and how the execution graph is built and invoked
  - Chunking strategy tradeoffs — RecursiveCharacterTextSplitter vs TokenTextSplitter, chunk size vs overlap, and how chunk design directly impacts RAG retrieval quality
  - ReAct agent tool-calling loop — how the agent decides when to call a tool vs answer directly, stop conditions, and how to debug a stuck reasoning loop

NOTEBOOKS:
  day-01-langchain-fundamentals
  day-02-chat-models-prompts
  day-03-output-parsers
  day-04-lcel-chains
  day-05-document-loaders
  day-06-text-splitting
  day-07-embeddings-vectorstores
  day-08-rag-retrieval
  day-09-conversation-memory
  day-10-langchain-agents
  day-11-custom-tools
  day-12-advanced-rag
  day-13-review-and-eval
  day-14-rag-chatbot-capstone

DAYS:
  Day 1 | LangChain Fundamentals | learn |
    Tasks:
      - Read the LangChain introduction and architecture overview [https://python.langchain.com/docs/introduction/]
      - Install langchain, langchain-openai, and langchain-community with pip
      - Instantiate a ChatOpenAI model and make your first chat completion call
      - Explore the LangChain expression: messages, HumanMessage, AIMessage, SystemMessage [https://python.langchain.com/docs/concepts/messages/]
      - Inspect the response object — understand content, usage_metadata, and response_metadata
    Resources:
      - {text: "LangChain Docs — Introduction", url: "https://python.langchain.com/docs/introduction/"}
      - {text: "LangChain Conceptual Guide", url: "https://python.langchain.com/docs/concepts/"}
      - {text: "langchain-openai PyPI", url: "https://pypi.org/project/langchain-openai/"}
    Tip: Set OPENAI_API_KEY in a .env file and load it with python-dotenv — never hardcode keys in notebooks.
    hasScore: false

  Day 2 | Chat Models and Prompt Templates | learn |
    Tasks:
      - Read the ChatPromptTemplate docs and understand SystemMessage, HumanMessage roles [https://python.langchain.com/docs/concepts/prompt_templates/]
      - Build a ChatPromptTemplate with system and human message slots and invoke it with variable substitution
      - Create a few-shot prompt using FewShotChatMessagePromptTemplate [https://python.langchain.com/docs/how_to/few_shot_examples_chat/]
      - Compare outputs from gpt-3.5-turbo vs gpt-4o-mini on the same prompt template
      - Log temperature, model name, and latency for each call to compare quality vs cost
    Resources:
      - {text: "LangChain Prompt Templates", url: "https://python.langchain.com/docs/concepts/prompt_templates/"}
      - {text: "Few-Shot Chat Examples", url: "https://python.langchain.com/docs/how_to/few_shot_examples_chat/"}
      - {text: "ChatOpenAI API Reference", url: "https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html"}
    Tip: Use model="gpt-4o-mini" for everyday experimentation — it's 10× cheaper than gpt-4o with similar instruction-following quality.
    hasScore: false

  Day 3 | Output Parsers and Structured Outputs | learn |
    Tasks:
      - Read the output parsers overview and understand StrOutputParser vs PydanticOutputParser [https://python.langchain.com/docs/concepts/output_parsers/]
      - Use StrOutputParser to extract clean string output from a ChatModel response
      - Define a Pydantic model and use PydanticOutputParser to extract structured JSON from an LLM
      - Handle output parser errors with OutputFixingParser wrapping a PydanticOutputParser [https://python.langchain.com/docs/how_to/output_parser_fixing/]
      - Use JsonOutputParser for schema-free JSON extraction and verify with json.loads()
    Resources:
      - {text: "LangChain Output Parsers", url: "https://python.langchain.com/docs/concepts/output_parsers/"}
      - {text: "PydanticOutputParser How-To", url: "https://python.langchain.com/docs/how_to/output_parser_pydantic/"}
      - {text: "OutputFixingParser", url: "https://python.langchain.com/docs/how_to/output_parser_fixing/"}
    Tip: Always include the parser's get_format_instructions() in your prompt — without it the LLM doesn't know what format to emit.
    hasScore: false

  Day 4 | LCEL — LangChain Expression Language | practice |
    Tasks:
      - Read the LCEL conceptual guide and understand how the pipe operator builds a Runnable chain [https://python.langchain.com/docs/concepts/lcel/]
      - Build a simple chain: prompt | model | parser and call .invoke(), .stream(), and .batch()
      - Use RunnablePassthrough to pass the original input alongside transformed outputs [https://python.langchain.com/docs/how_to/passthrough/]
      - Build a branching chain with RunnableParallel to run two sub-chains and merge results [https://python.langchain.com/docs/how_to/parallel/]
      - Inspect the chain with .get_graph().print_ascii() to visualize the execution DAG
      - Add error handling with RunnableLambda and a try/except fallback
    Resources:
      - {text: "LCEL Conceptual Guide", url: "https://python.langchain.com/docs/concepts/lcel/"}
      - {text: "RunnablePassthrough", url: "https://python.langchain.com/docs/how_to/passthrough/"}
      - {text: "RunnableParallel", url: "https://python.langchain.com/docs/how_to/parallel/"}
    Tip: Chain streaming works only if every component in the pipe supports it — ChatModels do, but most retrievers don't. Test .stream() early.
    hasScore: true

  Day 5 | Document Loaders | learn |
    Tasks:
      - Read the document loaders concept page and understand the Document object: page_content and metadata [https://python.langchain.com/docs/concepts/document_loaders/]
      - Load a PDF with PyPDFLoader and inspect the Document list it returns [https://python.langchain.com/docs/how_to/document_loader_pdf/]
      - Load a web page with WebBaseLoader using BeautifulSoup [https://python.langchain.com/docs/integrations/document_loaders/web_base/]
      - Load a directory of .txt files with DirectoryLoader and glob pattern matching
      - Enrich document metadata — add source, loaded_at, and domain fields to each Document
    Resources:
      - {text: "LangChain Document Loaders", url: "https://python.langchain.com/docs/concepts/document_loaders/"}
      - {text: "PDF Loader How-To", url: "https://python.langchain.com/docs/how_to/document_loader_pdf/"}
      - {text: "WebBaseLoader Integration", url: "https://python.langchain.com/docs/integrations/document_loaders/web_base/"}
    Tip: Always inspect a sample Document after loading — metadata.source is what gets passed to citations, so make it readable.
    hasScore: false

  Day 6 | Text Splitting Strategies | practice |
    Tasks:
      - Read the text splitter concept page to understand chunk_size, chunk_overlap, and length_function [https://python.langchain.com/docs/concepts/text_splitters/]
      - Split a long PDF with RecursiveCharacterTextSplitter at chunk_size=1000, overlap=200
      - Re-split the same document with TokenTextSplitter (tiktoken) at chunk_size=256 tokens
      - Compare chunk count, average length, and boundary quality between the two strategies
      - Use MarkdownTextSplitter on a README and verify that headers are preserved as natural split points [https://python.langchain.com/docs/how_to/markdown_header_metadata_splitter/]
      - Print a histogram of chunk lengths to identify outlier-sized chunks
    Resources:
      - {text: "LangChain Text Splitters", url: "https://python.langchain.com/docs/concepts/text_splitters/"}
      - {text: "RecursiveCharacterTextSplitter", url: "https://python.langchain.com/docs/how_to/recursive_text_splitter/"}
      - {text: "MarkdownHeaderTextSplitter", url: "https://python.langchain.com/docs/how_to/markdown_header_metadata_splitter/"}
    Tip: Start with chunk_size=1000 and overlap=200. If retrieval misses context that clearly lives in one paragraph, reduce chunk_size — don't increase overlap blindly.
    hasScore: true

  Day 7 | Embeddings and Vector Stores | learn |
    Tasks:
      - Read the embeddings concept page and understand dimensionality and cosine similarity [https://python.langchain.com/docs/concepts/embedding_models/]
      - Embed a list of sentences with OpenAIEmbeddings and compute pairwise cosine similarity in NumPy
      - Create a Chroma vector store from a set of Documents with from_documents() [https://python.langchain.com/docs/integrations/vectorstores/chroma/]
      - Run similarity_search() and similarity_search_with_score() and compare the ranked results
      - Persist the Chroma store to disk and reload it without re-embedding
    Resources:
      - {text: "LangChain Embedding Models", url: "https://python.langchain.com/docs/concepts/embedding_models/"}
      - {text: "Chroma Vector Store", url: "https://python.langchain.com/docs/integrations/vectorstores/chroma/"}
      - {text: "FAISS Vector Store", url: "https://python.langchain.com/docs/integrations/vectorstores/faiss/"}
    Tip: Chroma is the easiest persistent store for local development. Switch to pgvector or Pinecone only when you need multi-user access or cloud scalability.
    hasScore: false

  Day 8 | Retrieval-Augmented Generation | practice |
    Tasks:
      - Read the RAG concept page and understand the retrieve-then-read architecture [https://python.langchain.com/docs/concepts/rag/]
      - Build a retriever from a Chroma store with as_retriever(search_type="similarity", k=4)
      - Construct a RAG chain using LCEL: retriever | format_docs | prompt | model | StrOutputParser
      - Test with 5 questions and verify answers are grounded in retrieved chunks — not hallucinated
      - Switch to MMR retrieval (search_type="mmr") and compare diversity of retrieved docs [https://python.langchain.com/docs/how_to/MultiQueryRetriever/]
      - Add source metadata to each answer so the user can see which document was cited
    Resources:
      - {text: "LangChain RAG Conceptual Guide", url: "https://python.langchain.com/docs/concepts/rag/"}
      - {text: "Vector Store Retriever", url: "https://python.langchain.com/docs/how_to/vectorstore_retriever/"}
      - {text: "MultiQueryRetriever", url: "https://python.langchain.com/docs/how_to/MultiQueryRetriever/"}
    Tip: Always print the retrieved docs alongside the answer during development — if retrieval is wrong, no prompt engineering will fix it.
    hasScore: true

  Day 9 | Conversation Memory | learn |
    Tasks:
      - Read the memory concept page and understand why stateless LLMs need explicit memory management [https://python.langchain.com/docs/concepts/memory/]
      - Implement ConversationBufferMemory and run a 5-turn chat — inspect the full message history
      - Implement ConversationSummaryMemory with ChatOpenAI and verify the history is compressed after 3 turns [https://python.langchain.com/docs/how_to/summary_memory/]
      - Measure token usage with ConversationBufferMemory vs ConversationSummaryMemory over 10 turns
      - Add memory to a RAG chain so follow-up questions use prior context without re-retrieving the same docs
    Resources:
      - {text: "LangChain Memory Concepts", url: "https://python.langchain.com/docs/concepts/memory/"}
      - {text: "ConversationSummaryMemory", url: "https://python.langchain.com/docs/how_to/summary_memory/"}
      - {text: "How to add memory to chatbots", url: "https://python.langchain.com/docs/how_to/chatbots_memory/"}
    Tip: ConversationSummaryMemory saves tokens on long chats but adds one LLM call per turn for summarization — budget for that latency.
    hasScore: false

  Day 10 | LangChain Agents | practice |
    Tasks:
      - Read the agents concept page — understand the ReAct loop: Thought → Action → Observation [https://python.langchain.com/docs/concepts/agents/]
      - Create a ReAct agent with create_react_agent and two built-in tools: DuckDuckGoSearchRun and a calculator [https://python.langchain.com/docs/how_to/agent_executor/]
      - Run the agent on a multi-step question requiring both search and arithmetic
      - Enable verbose=True and trace through each Thought/Action/Observation step in the output
      - Handle agent errors: set max_iterations=6 and handle AgentExecutor timeout gracefully
      - Inspect agent.tools to list registered tools and their descriptions
    Resources:
      - {text: "LangChain Agents Conceptual Guide", url: "https://python.langchain.com/docs/concepts/agents/"}
      - {text: "AgentExecutor How-To", url: "https://python.langchain.com/docs/how_to/agent_executor/"}
      - {text: "Built-in LangChain Tools", url: "https://python.langchain.com/docs/integrations/tools/"}
    Tip: Set verbose=True while developing agents — blind agents fail silently. Only turn it off in production.
    hasScore: true

  Day 11 | Custom Tools for Agents | practice |
    Tasks:
      - Read the custom tools how-to guide and understand @tool decorator vs StructuredTool [https://python.langchain.com/docs/how_to/custom_tools/]
      - Write a @tool-decorated function that fetches a Wikipedia summary via the wikipedia package
      - Write a StructuredTool with a Pydantic args schema for a weather lookup that takes city and units
      - Register both tools in an AgentExecutor and run a query that forces use of both tools
      - Write a tool that queries a local DuckDB database and returns a formatted result string
      - Test tool failure: raise an exception inside a tool and verify the agent recovers with an error message
    Resources:
      - {text: "Custom Tools How-To", url: "https://python.langchain.com/docs/how_to/custom_tools/"}
      - {text: "StructuredTool Reference", url: "https://python.langchain.com/docs/concepts/tools/"}
      - {text: "Tool calling with ChatModels", url: "https://python.langchain.com/docs/how_to/tool_calling/"}
    Tip: Write clear, specific tool descriptions — the agent picks tools based entirely on their docstrings. Vague descriptions cause wrong tool selection.
    hasScore: true

  Day 12 | Advanced RAG Techniques | practice |
    Tasks:
      - Read the advanced retrieval how-to docs — understand HyDE, multi-query, and contextual compression [https://python.langchain.com/docs/how_to/MultiQueryRetriever/]
      - Implement MultiQueryRetriever: generate 3 query variants per question to widen retrieval recall [https://python.langchain.com/docs/how_to/MultiQueryRetriever/]
      - Implement ContextualCompressionRetriever with LLMChainExtractor to strip irrelevant content from chunks [https://python.langchain.com/docs/how_to/contextual_compression/]
      - Run an Ensemble Retriever combining BM25 (keyword) and Chroma (semantic) with RRF fusion [https://python.langchain.com/docs/how_to/ensemble_retriever/]
      - Evaluate retrieval quality for each method: compute recall@4 against 10 labeled query-answer pairs
      - Choose the best retriever for your corpus and document the tradeoffs in a markdown cell
    Resources:
      - {text: "MultiQueryRetriever", url: "https://python.langchain.com/docs/how_to/MultiQueryRetriever/"}
      - {text: "Contextual Compression Retriever", url: "https://python.langchain.com/docs/how_to/contextual_compression/"}
      - {text: "Ensemble Retriever", url: "https://python.langchain.com/docs/how_to/ensemble_retriever/"}
    Tip: MultiQueryRetriever is the highest-leverage advanced RAG technique — 3 LLM calls per retrieval but it dramatically boosts recall on ambiguous questions.
    hasScore: true

  Day 13 | Review and Evaluation | review |
    Tasks:
      - Review LCEL chain construction: rebuild a full prompt | model | parser chain from memory
      - Review RAG pipeline: reconstruct the retriever → context injection → grounded answer pattern
      - Use LangSmith or a manual eval loop to score 10 RAG answers on groundedness (0/1) [https://docs.smith.langchain.com/]
      - Audit your agent: run it on 5 adversarial inputs and verify it fails gracefully
      - Write a cheat sheet covering: LCEL operators, retriever search types, memory classes, agent creation functions
    Resources:
      - {text: "LangSmith Evaluation Docs", url: "https://docs.smith.langchain.com/evaluation"}
      - {text: "LangChain How-To Index", url: "https://python.langchain.com/docs/how_to/"}
      - {text: "LCEL Cheatsheet", url: "https://python.langchain.com/docs/how_to/lcel_cheatsheet/"}
    Tip: If you can rebuild the RAG pipeline from a blank notebook in under 20 minutes without docs, you're ready for the capstone.
    hasScore: true

  Day 14 | RAG Chatbot Capstone | exam |
    Tasks:
      - Ingest a set of PDFs and web pages using PyPDFLoader and WebBaseLoader — at least 3 documents
      - Split all documents with RecursiveCharacterTextSplitter and store embeddings in a persistent Chroma store
      - Build a retriever with MMR re-ranking (search_type="mmr", k=5) for diverse context retrieval
      - Wire a conversational RAG chain using ConversationSummaryMemory so follow-up questions use prior context
      - Add streaming output via .stream() so the Gradio interface renders tokens as they arrive
      - Build a Gradio ChatInterface that connects to the chain, shows sources below each answer, and resets memory on clear
    Resources:
      - {text: "LangChain RAG How-To", url: "https://python.langchain.com/docs/how_to/chatbots_retrieval/"}
      - {text: "Gradio ChatInterface Docs", url: "https://www.gradio.app/docs/gradio/chatinterface"}
      - {text: "Chroma Persistence", url: "https://python.langchain.com/docs/integrations/vectorstores/chroma/"}
    Tip: Test with at least 5 follow-up questions that require memory — "What did you just say about X?" is the canonical memory health check.
    hasScore: true

TOPICS:
  LangChain Foundations | #378ADD | 0, 1, 2, 3
  Document Ingestion | #BA7517 | 4, 5
  Embeddings and Vector Search | #7F77DD | 6, 7
  Retrieval-Augmented Generation | #0891B2 | 7, 8, 11
  Memory and Conversation | #E8890C | 8, 9
  Agents and Tools | #D85A30 | 9, 10
  Evaluation and Capstone | #BA7517 | 12, 13
```
