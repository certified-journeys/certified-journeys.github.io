# Building AI Agents with LangGraph — Course Design
Generated: 2026-06-13

```
COURSE_TYPE:      notebook
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
EXAM_NOTES:       No formal exam. Ship a working multi-agent research system as the capstone.

CAPSTONE_PROJECT: Build a multi-agent research system in LangGraph with a supervisor node that routes between a web-search agent and a summarization agent, persists conversation state to a SQLite checkpointer, streams node-level output to a terminal UI, and produces a structured Markdown research report.

EXAM_CHECKLIST:
  - Built at least 3 distinct LangGraph StateGraphs from scratch without referencing docs
  - Can explain the difference between interrupt_before, interrupt_after, and Command-based resumption — and when each is appropriate
  - Implemented the supervisor multi-agent pattern with handoffs between at least 2 specialized subagents
  - Connected a SQLite checkpointer and verified that a graph resumes correctly after mid-run interruption
  - Streamed node-level events using astream_events and rendered them in a real terminal output

AI_DEEP_DIVE_TOPICS:
  - LangGraph state schemas and reducer functions — how add_messages and custom reducers control state merging across nodes
  - Human-in-the-loop breakpoints — the difference between interrupt_before, interrupt_after, and Command-based resumption, and why graph thread IDs matter for long-running agents
  - The supervisor multi-agent pattern — how a router LLM decides handoffs, why subgraphs need their own state namespaces, and how to prevent infinite delegation loops

NOTEBOOKS:
  day-01-langgraph-fundamentals
  day-02-state-and-reducers
  day-03-conditional-edges
  day-04-tool-calling-react
  day-05-human-in-the-loop
  day-06-persistence-checkpointers
  day-07-multi-agent-supervisor
  day-08-streaming-and-memory
  day-09-review-and-patterns
  day-10-capstone-research-system

DAYS:
  Day 1 | LangGraph Fundamentals | learn | 
    Tasks:
      - {text: "Read the LangGraph conceptual overview — graphs, nodes, edges, and state", url: "https://langchain-ai.github.io/langgraph/concepts/low_level/"}
      - {text: "Install langgraph, langchain-openai, and langchain-community in a Colab notebook", url: "https://pypi.org/project/langgraph/"}
      - Build a minimal two-node graph: one node that appends text to state, a second that reverses it
      - Run the graph with invoke and inspect the final state dict
      - {text: "Read the LangGraph quickstart end-to-end", url: "https://langchain-ai.github.io/langgraph/tutorials/introduction/"}
    Resources:
      - {text: "LangGraph Docs — Low Level Concepts", url: "https://langchain-ai.github.io/langgraph/concepts/low_level/"}
      - {text: "LangGraph GitHub Repository", url: "https://github.com/langchain-ai/langgraph"}
      - {text: "LangGraph Quickstart Tutorial", url: "https://langchain-ai.github.io/langgraph/tutorials/introduction/"}
    Tip: "Start with the absolute minimum: one StateGraph, two nodes, one edge. Add complexity only after you can explain what state is and how it flows."
    hasScore: false

  Day 2 | State Schemas and Reducers | learn |
    Tasks:
      - {text: "Read the LangGraph state documentation — TypedDict, Annotated fields, and reducers", url: "https://langchain-ai.github.io/langgraph/concepts/low_level/#state"}
      - {text: "Study how add_messages works as a reducer and why it replaces list append for chat history", url: "https://langchain-ai.github.io/langgraph/how-tos/state-reducers/"}
      - Implement a custom reducer that deduplicates items when merging two lists in a state field
      - Build a graph that uses MessagesState as its base type and traces the full message list after three LLM turns
      - Compare StateGraph with TypedDict state vs Pydantic BaseModel state — verify both work identically
    Resources:
      - {text: "LangGraph — State & Reducers How-To", url: "https://langchain-ai.github.io/langgraph/how-tos/state-reducers/"}
      - {text: "LangGraph MessagesState reference", url: "https://langchain-ai.github.io/langgraph/concepts/low_level/#messagesstate"}
      - {text: "Python typing — Annotated and TypedDict docs", url: "https://docs.python.org/3/library/typing.html#typing.TypedDict"}
    Tip: "Every state field that uses a mutable default needs a reducer. If you skip the reducer, later nodes silently overwrite what earlier nodes wrote — a bug that only shows up at scale."
    hasScore: false

  Day 3 | Conditional Edges and Routing | practice |
    Tasks:
      - {text: "Read the conditional edges how-to guide", url: "https://langchain-ai.github.io/langgraph/how-tos/branching/"}
      - Implement a routing function that inspects last_message.content for keywords and returns one of three node names
      - Build a graph where the router sends inputs to a math node, a code node, or an END node based on intent classification
      - Add a fallback edge so an unknown intent routes to a clarification node rather than crashing
      - Write a unit test with pytest that drives the graph through all three branches using mock LLM responses
      - {text: "Read the how-to on adding nodes and edges reference", url: "https://langchain-ai.github.io/langgraph/concepts/low_level/#edges"}
    Resources:
      - {text: "LangGraph — Branching How-To", url: "https://langchain-ai.github.io/langgraph/how-tos/branching/"}
      - {text: "LangGraph — Edges Concept Reference", url: "https://langchain-ai.github.io/langgraph/concepts/low_level/#edges"}
      - {text: "LangGraph — add_conditional_edges API", url: "https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.StateGraph.add_conditional_edges"}
    Tip: "Routing functions must return a string that exactly matches a registered node name or the special END constant. A typo here produces a silent graph hang, not a Python error."
    hasScore: true

  Day 4 | ReAct Agents and Tool Calling | practice |
    Tasks:
      - {text: "Read the ReAct agent pattern documentation", url: "https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#react-agents"}
      - {text: "Study the create_react_agent convenience function and when to use it vs building manually", url: "https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/"}
      - Build a ReAct agent using ToolNode and a manually wired tool-call loop — no create_react_agent shortcut
      - Add three tools: a calculator, a DuckDuckGo search wrapper, and a Python REPL tool
      - Force the agent to use the calculator tool on a multi-step arithmetic word problem and log the full tool-call chain
      - Implement a max_iterations guard so the agent stops gracefully after N tool calls without hitting LLM rate limits
    Resources:
      - {text: "LangGraph — ReAct Agent How-To", url: "https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/"}
      - {text: "LangGraph — ToolNode Reference", url: "https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.ToolNode"}
      - {text: "LangChain Tool Calling Docs", url: "https://python.langchain.com/docs/concepts/tool_calling/"}
    Tip: "Always add a max_iterations ceiling in the tool-call loop. LLMs occasionally get stuck repeating the same tool call — a ceiling is the safety valve that makes agents production-safe."
    hasScore: true

  Day 5 | Human-in-the-Loop Breakpoints | learn |
    Tasks:
      - {text: "Read the human-in-the-loop concept documentation", url: "https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/"}
      - {text: "Study the how-to for interrupt_before and interrupt_after — understand what a snapshot looks like", url: "https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/"}
      - Build a graph that interrupts before a dangerous tool call, prints the pending action, and waits for user approval
      - Resume the graph from its snapshot using the same thread_id and verify the state is preserved exactly
      - Implement Command-based resumption so the user can also supply a corrected value mid-graph rather than just approving
      - {text: "Read the Command-based interruption how-to", url: "https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/command/"}
    Resources:
      - {text: "LangGraph — Human-in-the-Loop Concepts", url: "https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/"}
      - {text: "LangGraph — Wait for User Input How-To", url: "https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/"}
      - {text: "LangGraph — Command Resumption How-To", url: "https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/command/"}
    Tip: "Thread IDs are the key to HITL. If you call invoke with a different thread_id after an interrupt, you get a fresh run, not a resumed one. Always store and reuse the exact same thread_id."
    hasScore: false

  Day 6 | Persistence and Checkpointers | practice |
    Tasks:
      - {text: "Read the persistence and checkpointing concepts page", url: "https://langchain-ai.github.io/langgraph/concepts/persistence/"}
      - {text: "Study the SQLite checkpointer setup guide", url: "https://langchain-ai.github.io/langgraph/how-tos/persistence/"}
      - Wire a SqliteSaver checkpointer to a multi-turn chatbot graph and confirm state survives process restart
      - Inspect raw checkpoint rows in SQLite using sqlite3 to understand what langgraph serialises per turn
      - Build a graph that resumes correctly after simulating a mid-run crash: kill the process at an interrupt and recover the full history
      - {text: "Study the PostgreSQL checkpointer for production deployments", url: "https://langchain-ai.github.io/langgraph/how-tos/persistence-postgres/"}
    Resources:
      - {text: "LangGraph — Persistence Concepts", url: "https://langchain-ai.github.io/langgraph/concepts/persistence/"}
      - {text: "LangGraph — SQLite Checkpointer How-To", url: "https://langchain-ai.github.io/langgraph/how-tos/persistence/"}
      - {text: "LangGraph — PostgreSQL Checkpointer How-To", url: "https://langchain-ai.github.io/langgraph/how-tos/persistence-postgres/"}
    Tip: "Use thread_id to isolate conversations and checkpoint_id to retrieve a specific snapshot. The combination of both is what makes time-travel debugging possible in production agents."
    hasScore: true

  Day 7 | Multi-Agent Supervisor Pattern | practice |
    Tasks:
      - {text: "Read the multi-agent architecture concepts page", url: "https://langchain-ai.github.io/langgraph/concepts/multi_agent/"}
      - {text: "Study the supervisor how-to guide — understand the router LLM and handoff mechanism", url: "https://langchain-ai.github.io/langgraph/tutorials/multi_agent/agent_supervisor/"}
      - Implement a supervisor graph that routes between a research agent (DuckDuckGo search) and a writer agent (text summarization)
      - Give each subagent its own private state namespace so they cannot overwrite each other's working memory
      - Add a FINISH sentinel so the supervisor can decide when the task is complete rather than looping indefinitely
      - Test with a multi-step research question that requires at least two handoffs between agents before completion
    Resources:
      - {text: "LangGraph — Multi-Agent Concepts", url: "https://langchain-ai.github.io/langgraph/concepts/multi_agent/"}
      - {text: "LangGraph — Supervisor Tutorial", url: "https://langchain-ai.github.io/langgraph/tutorials/multi_agent/agent_supervisor/"}
      - {text: "LangGraph — Subgraphs How-To", url: "https://langchain-ai.github.io/langgraph/how-tos/subgraph/"}
    Tip: "The supervisor's router LLM only needs to output a single token: the next agent's name or FINISH. Keep its system prompt to one paragraph — complexity in the router causes hallucinated handoffs."
    hasScore: true

  Day 8 | Streaming and Long-Term Memory | practice |
    Tasks:
      - {text: "Read the streaming documentation — values, updates, messages, and events modes", url: "https://langchain-ai.github.io/langgraph/concepts/streaming/"}
      - {text: "Study astream_events and how to filter for specific event types", url: "https://langchain-ai.github.io/langgraph/how-tos/streaming-events-from-within-tools/"}
      - Implement a streaming agent that prints each token to the terminal as it arrives using astream with stream_mode="messages"
      - Add node-level streaming so the terminal shows which node is currently executing before the LLM output begins
      - {text: "Read the long-term memory store documentation", url: "https://langchain-ai.github.io/langgraph/concepts/memory/"}
      - Wire an InMemoryStore to your agent and store one user preference per session, then retrieve it on the next turn
    Resources:
      - {text: "LangGraph — Streaming Concepts", url: "https://langchain-ai.github.io/langgraph/concepts/streaming/"}
      - {text: "LangGraph — Streaming How-To Guides", url: "https://langchain-ai.github.io/langgraph/how-tos/#streaming"}
      - {text: "LangGraph — Memory Store Concepts", url: "https://langchain-ai.github.io/langgraph/concepts/memory/"}
    Tip: "Use stream_mode='messages' for token-level streaming and stream_mode='updates' for node-level updates. Mixing both in astream_events lets you build a rich terminal UI without any extra dependencies."
    hasScore: true

  Day 9 | Review and Patterns | review |
    Tasks:
      - {text: "Re-read the LangGraph how-to index and scan any sections you skipped", url: "https://langchain-ai.github.io/langgraph/how-tos/"}
      - Rebuild the supervisor graph from Day 7 from memory without referencing your previous notebook
      - Write a one-page cheat sheet covering: state reducers, conditional edge routing, HITL resumption, checkpointer setup, and supervisor handoff pattern
      - Identify and fix at least one edge case in your Day 7 graph: what happens when both agents return empty results?
      - {text: "Read the LangGraph Platform deployment overview as preview material", url: "https://langchain-ai.github.io/langgraph/concepts/langgraph_platform/"}
    Resources:
      - {text: "LangGraph — How-To Index", url: "https://langchain-ai.github.io/langgraph/how-tos/"}
      - {text: "LangGraph — Conceptual Guides Index", url: "https://langchain-ai.github.io/langgraph/concepts/"}
      - {text: "LangGraph Platform Overview", url: "https://langchain-ai.github.io/langgraph/concepts/langgraph_platform/"}
    Tip: "The review day is not passive reading — rebuild the hardest graph from memory. What you can reconstruct from memory is what you actually understand; everything else is just familiarity."
    hasScore: true

  Day 10 | Capstone — Multi-Agent Research System | exam |
    Tasks:
      - Design the full graph architecture on paper first: supervisor node, research subagent, summarizer subagent, state schema, and output format
      - {text: "Set up the SQLite checkpointer and verify state persists across invocations before writing any agent logic", url: "https://langchain-ai.github.io/langgraph/how-tos/persistence/"}
      - Implement the supervisor router that classifies research tasks, delegates to the correct subagent, and detects FINISH
      - Wire the research subagent with DuckDuckGo search tool and a scratchpad state field for intermediate notes
      - Wire the summarizer subagent to condense the research scratchpad into a structured Markdown report with a title, bullet summary, and sources section
      - Implement node-level streaming so the terminal prints which agent is active and streams each LLM token as it arrives
      - {text: "Test the full system end-to-end with a multi-hop research question requiring at least 3 handoffs", url: "https://langchain-ai.github.io/langgraph/tutorials/multi_agent/agent_supervisor/"}
    Resources:
      - {text: "LangGraph — Multi-Agent Supervisor Tutorial", url: "https://langchain-ai.github.io/langgraph/tutorials/multi_agent/agent_supervisor/"}
      - {text: "LangGraph — Streaming How-To Guides", url: "https://langchain-ai.github.io/langgraph/how-tos/#streaming"}
      - {text: "LangGraph — Persistence How-To", url: "https://langchain-ai.github.io/langgraph/how-tos/persistence/"}
    Tip: "The capstone is an integration test for everything you have built this week. Start with the state schema and wiring before writing any prompt — the graph structure is harder to change than the prompts."
    hasScore: false

TOPICS:
  LangGraph Core | #6366F1 | 0, 1, 2
  Tool Calling & ReAct | #E8890C | 3, 4
  Human-in-the-Loop | #0891B2 | 4, 5
  Persistence & State | #7F77DD | 5, 6
  Multi-Agent Systems | #D85A30 | 6, 7, 9
  Streaming & Memory | #1C7A4A | 7, 8
  Capstone Integration | #BA7517 | 8, 9
```
