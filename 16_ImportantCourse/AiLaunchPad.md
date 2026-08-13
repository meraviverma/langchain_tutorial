
```markdown
# 📅 01 August (Saturday)  
**In person @ IITH Campus**  

## 🌟 Foundations of Reliable AI Agents  
**LLM runtime, structured outputs, tools, and single-agent control loops.**

### 📖 Lectures  
- How agentic systems differ from simple chatbots  
- Model selection, context windows, tokens, sessions, and state  
- Structured outputs with Pydantic and schema validation  
- Native tool calling, retries, rate limits, callbacks, and failure recovery  

### 🧪 Hands-on Labs  
- Build a raw Python LLM client with session state  
- Convert messy business emails into typed JSON objects  
- Implement a tool-calling loop with exception handling and retry logic  

---

## 🧠 Knowledge, Memory, and Production RAG  
**Embeddings, vector stores, retrieval quality, and memory design.**

### 📖 Lectures  
- Semantic search, embeddings, vector spaces, and similarity  
- Chunking, metadata filters, reranking, and query expansion  
- Short-term memory, long-term memory, and session continuity  
- Prompt injection risk in RAG and defensive retrieval patterns  

### 🧪 Hands-on Labs  
- Spin up Qdrant or Chroma locally and run metadata-filtered queries  
- Build a RAG assistant over policy and operations documents  
- Add memory summaries and evaluate retrieval precision  

---

## 🔗 Graph-Based Multi-Agent Systems  
**LangGraph orchestration, checkpoints, plugins, skills, and human review.**

### 📖 Lectures  
- When to use one agent versus many agents  
- Supervisor, choreography, planner-executor, reflection, and review patterns  
- LangGraph state, edges, checkpoints, breakpoints, and resumability  
- MCP, plugins, skills, and safe enterprise tool integration  

### 🧪 Hands-on Labs  
- Build a researcher-writer-reviewer workflow in LangGraph  
- Add checkpointing and resume a paused workflow  
- Expose a local business API or file tool through an MCP-style interface  

---

## 🚀 Evaluation, Observability, and Launch Readiness  
**Tracing, guardrails, deployment patterns, and continuous improvement.**

### 📖 Lectures  
- Why agent evaluation differs from model evaluation  
- Component tests for tools, retrieval, memory, planning, and final answers  
- LangFuse tracing, cost tracking, latency, and failure analysis  
- Guardrails, human-in-the-loop approvals, monitoring, and improvement loops  

### 🧪 Hands-on Labs  
- Instrument an agent workflow with LangFuse traces  
- Create evaluation cases for hallucination, retrieval misses, and tool failures  
- Package the final app with FastAPI and a lightweight deployment checklist  
```


Yes. I did the same exercise for the **IIT Hyderabad AI Launchpad** program, but there is an important difference from the previous IISc course: **this one is much more focused on production-grade Agentic AI engineering** and less focused on general software development/SDD.

I checked the current official IIT Hyderabad program page. It is a **3-weekend program + guided practical work**, with one connected production-style agent application built throughout the program. The advertised stack includes **LangChain, LangGraph, Qdrant, LangFuse and MCP**. ([AI Launchpad][1])

And yes — we can map it almost one-to-one to **free resources**, just like we did for the previous course.

---

# IIT Hyderabad AI Launchpad → Free Learning Roadmap

## First: What this course actually covers

The official curriculum has **five technical modules**:

1. **Foundations of Reliable AI Agents**
2. **Knowledge, Memory and Production RAG**
3. **Project Development Week**
4. **Graph-Based Multi-Agent Systems**
5. **Evaluation, Observability and Launch Readiness**

Then there's a final project/demo weekend. ([AI Launchpad][1])

The program expects you to already know:

* Python
* REST APIs
* basic Generative AI/LLM concepts
* OpenAI-compatible APIs

It explicitly says prior LangChain/LangGraph experience is **not required**. ([AI Launchpad][1])

---

# 🟡 PREREQUISITES

Do these first if any of them are weak.

| Prerequisite           | What to learn                                          | Free resource                                                                                                                          |
| ---------------------- | ------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------- |
| Python                 | Functions, classes, packages, exceptions, async basics | [Python Official Tutorial](https://docs.python.org/3/tutorial/?utm_source=chatgpt.com)                                                 |
| REST APIs              | HTTP, GET/POST, JSON, request/response                 | [MDN HTTP Overview](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview?utm_source=chatgpt.com)                                 |
| LLM basics             | Tokens, context, prompting, API calls                  | [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/?utm_source=chatgpt.com)                                             |
| OpenAI-compatible APIs | API calls, messages, tools                             | [OpenAI Function Calling Guide](https://help.openai.com/en/articles/8555517-function-calling-in-the-openai-api?utm_source=chatgpt.com) |
| Git/GitHub             | clone, branch, commit, PR                              | [GitHub Skills](https://skills.github.com/?utm_source=chatgpt.com)                                                                     |

### For you

Because you already work in data engineering/AI, **don't spend weeks here**.

You should probably spend **2–4 days maximum** making sure these are comfortable.

---

# 🟢 MODULE 1 — Foundations of Reliable AI Agents

### IIT Hyderabad curriculum

The first weekend covers:

* How agentic systems differ from chatbots
* Model selection
* Context windows
* Tokens
* Sessions
* State
* Structured outputs
* Pydantic
* Schema validation
* Native tool calling
* Retries
* Rate limits
* Callbacks
* Failure recovery

The hands-on labs are:

* Raw Python LLM client
* Session state
* Convert business emails → typed JSON
* Tool-calling loop
* Exception handling
* Retry logic. ([AI Launchpad][1])

This is an **excellent curriculum** because it starts with the runtime mechanics rather than immediately jumping into LangChain.

---

## 1A. LLM runtime + API

### Resource

[OpenAI Function Calling Documentation](https://help.openai.com/en/articles/8555517-function-calling-in-the-openai-api?utm_source=chatgpt.com)

Learn:

* messages
* API requests
* tool definitions
* function calling
* structured outputs
* JSON schema
* tool arguments

OpenAI's documentation explains that function calling connects models to external tools/systems, while Structured Outputs can enforce the supplied JSON schema for tool arguments. ([OpenAI Help Center][2])

### Priority

⭐⭐⭐⭐⭐

---

# 1B. Structured Outputs + Pydantic

The course specifically mentions:

> Structured outputs with Pydantic and schema validation. ([AI Launchpad][1])

Learn:

```text
Unstructured LLM output
        ↓
     Pydantic
        ↓
Validated object
        ↓
Your application
```

This is **very important in production AI engineering**.

Use:

[Pydantic Documentation](https://docs.pydantic.dev/latest/?utm_source=chatgpt.com)

Then practice:

```python
class Customer(BaseModel):
    name: str
    email: str
    priority: str
```

Have the LLM convert messy text into this schema.

---

# 1C. Agent Fundamentals

### Best free course

[Hugging Face Agents Course](https://huggingface.co/agents-course?utm_source=chatgpt.com)

This is one of the strongest free resources available.

It covers:

* Tools
* Thoughts
* Actions
* Observations
* LLMs
* Agent loops
* Python implementation
* smolagents
* LangGraph
* LlamaIndex
* real-world agent use cases

The official syllabus explicitly includes agent fundamentals and implementation in popular frameworks. ([Hugging Face][3])

### Priority

⭐⭐⭐⭐⭐

---

# 1D. Tool Calling

The IIT Hyderabad course wants you to understand the mechanics **before** hiding everything behind frameworks.

That is exactly the right approach.

Learn:

```text
User
 ↓
LLM
 ↓
Decides tool
 ↓
Tool call
 ↓
Python function
 ↓
Result
 ↓
LLM
 ↓
Final answer
```

Use:

[OpenAI Function Calling](https://help.openai.com/en/articles/8555517-function-calling-in-the-openai-api?utm_source=chatgpt.com)

Then implement the loop yourself in Python.

---

# 1E. Retries + failure recovery

The IIT Hyderabad curriculum specifically mentions:

* retries
* rate limits
* callbacks
* exception handling
* failure recovery. ([AI Launchpad][1])

This is **not something you should learn from a generic Agent course alone**.

Use the documentation for the API/framework you're using and implement:

```text
LLM call
   ↓
Failure?
 ┌─┴─┐
No  Yes
│    ↓
│   Retry
│    ↓
│  Backoff
│    ↓
│  Retry limit?
│    ↓
└──→ Error handling
```

This is an engineering exercise more than a video-course topic.

---

# 🟢 MODULE 2 — Knowledge, Memory & Production RAG

This is where the IIT Hyderabad course becomes significantly different from the IISc course.

The curriculum includes:

* semantic search
* embeddings
* vector spaces
* similarity
* chunking
* metadata filtering
* reranking
* query expansion
* short-term memory
* long-term memory
* session continuity
* prompt injection in RAG
* defensive retrieval. ([AI Launchpad][1])

This is a **very good RAG curriculum**.

---

# 2A. RAG fundamentals

### Free resource

[DeepLearning.AI — Building Agentic RAG with LlamaIndex](https://www.deeplearning.ai/courses/building-agentic-rag-with-llamaindex/?utm_source=chatgpt.com)

It teaches:

* router agents
* Q&A
* summarization
* tool calling
* research agents
* multi-document agents
* debugging/control of agents

The current course is about **44 minutes**, with six lessons and four code examples. ([DeepLearning.ai][4])

### Priority

⭐⭐⭐⭐⭐

---

# 2B. Embeddings + Vector Search

You need to understand:

```text
Document
 ↓
Chunks
 ↓
Embedding model
 ↓
Vectors
 ↓
Vector DB
```

Then:

```text
Question
 ↓
Embedding
 ↓
Similarity search
 ↓
Top K documents
 ↓
LLM
```

---

# 2C. Qdrant

The IIT Hyderabad program specifically uses **Qdrant**. ([AI Launchpad][1])

So instead of learning five vector databases, learn Qdrant.

[Qdrant Documentation](https://qdrant.tech/documentation/?utm_source=chatgpt.com)

Learn:

* collections
* vectors
* payloads
* metadata filtering
* similarity search
* indexing
* hybrid search
* retrieval

The course specifically asks students to spin up Qdrant or Chroma locally and run metadata-filtered queries. ([AI Launchpad][1])

### Priority

⭐⭐⭐⭐⭐

---

# 2D. Chunking

Learn:

* fixed-size chunking
* recursive chunking
* semantic chunking
* overlap
* document-aware chunking

Understand the tradeoff:

```text
Too small
→ loses context

Too large
→ retrieval becomes noisy
```

This should be **hands-on**, not just theoretical.

---

# 2E. Metadata filtering

Example:

```text
Search:
"company leave policy"

Filter:
department = HR
country = India
year > 2025
```

This is very important for enterprise RAG.

Qdrant's payload filtering documentation is the resource I'd use.

---

# 2F. Reranking

Learn the difference between:

### Retrieval

Find 20 candidates.

### Reranking

Take those 20 and determine which 5 are actually most relevant.

```text
Query
 ↓
Vector Search
 ↓
20 documents
 ↓
Reranker
 ↓
Top 5
 ↓
LLM
```

This is a topic worth learning separately because the IIT Hyderabad curriculum explicitly mentions reranking. ([AI Launchpad][1])

---

# 2G. Query expansion

Learn:

```text
Original query
      ↓
Generate alternative queries
      ↓
Retrieve for each
      ↓
Merge
      ↓
Rerank
      ↓
Answer
```

This is particularly useful for enterprise knowledge systems.

---

# 2H. Memory

The course explicitly covers:

* short-term memory
* long-term memory
* session continuity. ([AI Launchpad][1])

You need to understand the distinction:

### Short-term

```text
Current conversation
```

### Long-term

```text
User preferences
Historical interactions
Persistent facts
```

### Session state

```text
Conversation/session ID
       ↓
State
       ↓
Resume later
```

This will become extremely important in the LangGraph module.

---

# 🟢 MODULE 3 — Project Development Week

The official curriculum doesn't introduce a new technical lecture topic here.

Instead:

> Guided online learning, project development and mentor support. ([AI Launchpad][1])

This means **you should build instead of consuming more courses.**

I'd recommend building:

## Enterprise Knowledge Agent

For example:

```text
                    User
                     ↓
                 FastAPI
                     ↓
               Agent Router
                     ↓
          ┌──────────┼──────────┐
          ↓          ↓          ↓
        RAG       SQL Tool    API Tool
          ↓          ↓          ↓
       Qdrant      DB       External API
          ↓
       Memory
          ↓
       Answer
```

Use your own domain if possible.

Given your data-engineering background, an **Enterprise Data/Knowledge Agent** would be much more valuable for your portfolio than a generic chatbot.

---

# 🟢 MODULE 4 — Graph-Based Multi-Agent Systems

The IIT Hyderabad curriculum covers:

* LangGraph
* one agent vs many
* supervisor
* choreography
* planner-executor
* reflection
* review
* state
* edges
* checkpoints
* breakpoints
* resumability
* MCP
* plugins
* skills
* enterprise tool integration. ([AI Launchpad][1])

This is probably the **most advanced part of the program**.

---

# 4A. LangGraph

### Best free course

[DeepLearning.AI — AI Agents in LangGraph](https://www.deeplearning.ai/courses/ai-agents-in-langgraph?utm_source=chatgpt.com)

It teaches you to first build an agent from scratch and then rebuild it with LangGraph, including its components and flow-based architecture. ([DeepLearning.ai][5])

### Priority

⭐⭐⭐⭐⭐

---

# 4B. LangGraph state

Understand:

```text
State
 ↓
Node
 ↓
Node
 ↓
Conditional edge
 ↓
Node
```

Unlike a simple loop:

```text
while True:
    agent()
```

LangGraph allows you to explicitly represent workflow/state.

---

# 4C. Checkpoints

This is particularly important.

Suppose:

```text
Agent
 ↓
Research
 ↓
Human approval
 ↓
Writing
 ↓
Review
```

If the human takes 5 hours to approve:

**the workflow should not disappear.**

Checkpointing lets you persist/resume state.

The IIT Hyderabad curriculum explicitly includes checkpoints, breakpoints and resumability. ([AI Launchpad][1])

---

# 4D. Multi-agent architectures

Learn these four architectures:

### Supervisor

```text
           Supervisor
          /    |     \
     Research Coding  Review
```

### Planner–Executor

```text
Planner
   ↓
Tasks
   ↓
Executor
```

### Reflection

```text
Agent
 ↓
Output
 ↓
Critic
 ↓
Agent
```

### Reviewer

```text
Researcher
     ↓
   Writer
     ↓
  Reviewer
     ↓
Approved?
 ┌───┴───┐
No      Yes
 ↓       ↓
Rewrite  Done
```

These are directly aligned with the curriculum's supervisor, choreography, planner-executor, reflection and review patterns. ([AI Launchpad][1])

---

# 4E. Deep Agents

I'd add this as an **advanced supplementary resource**.

LangChain's Deep Agents material focuses on:

* planning
* filesystem/context management
* subagents
* detailed prompting

These are useful extensions when tasks become longer and more complex. ([YouTube][6])

This isn't necessary before LangGraph; do it **after you understand basic LangGraph**.

---

# 4F. MCP

The IIT Hyderabad course explicitly includes MCP. ([AI Launchpad][1])

### Official resource

[Model Context Protocol Documentation](https://modelcontextprotocol.io/?utm_source=chatgpt.com)

Learn:

* MCP host
* MCP client
* MCP server
* tools
* resources
* prompts
* transports
* security
* external system integration

Think:

```text
             Agent
               ↓
           MCP Client
               ↓
       ┌───────┼────────┐
       ↓       ↓        ↓
    GitHub   Database   API
```

---

# 4G. MCP hands-on

Don't just read the specification.

Build:

### MCP server #1

A filesystem tool.

### MCP server #2

A database tool.

### MCP server #3

A simple business API.

Then connect them to your agent.

That will teach you much more than watching another 5-hour course.

---

# 🟢 MODULE 5 — Evaluation, Observability & Launch Readiness

This is another **excellent part of the IIT Hyderabad curriculum**.

It covers:

* agent evaluation
* tool evaluation
* retrieval evaluation
* memory evaluation
* planning evaluation
* final-answer evaluation
* LangFuse
* tracing
* cost
* latency
* failure analysis
* guardrails
* human-in-the-loop
* monitoring
* improvement loops. ([AI Launchpad][1])

---

# 5A. LangFuse

This is the exact tool used by the course.

### Free resource

[LangFuse Documentation](https://langfuse.com/docs?utm_source=chatgpt.com)

LangFuse provides tracing for:

* LLM calls
* retrieval
* embeddings
* APIs
* multi-turn sessions
* agent graphs

It also provides evaluation capabilities including:

* LLM-as-a-judge
* code evaluators
* human feedback
* datasets
* experiments
* production trace evaluation. ([Langfuse][7])

### Priority

⭐⭐⭐⭐⭐

---

# 5B. Agent Evaluation

Don't think only:

> "Did the answer look good?"

Evaluate:

```text
Agent
 │
 ├── Tool selection
 ├── Tool arguments
 ├── Retrieval
 ├── Memory
 ├── Planning
 ├── Final answer
 ├── Cost
 └── Latency
```

The IIT Hyderabad curriculum specifically says evaluation differs from model evaluation and calls for component-level testing of tools, retrieval, memory, planning and final answers. ([AI Launchpad][1])

---

# 5C. Observability

Learn to inspect:

```text
User request
 ↓
Agent
 ↓
LLM call
 ↓
Tool
 ↓
Retrieval
 ↓
LLM
 ↓
Final response
```

And determine:

* where it spent time
* where it failed
* how many tokens were used
* how much it cost
* which tool failed
* which retrieval failed

LangFuse is particularly well aligned with this module. ([Langfuse][7])

---

# 5D. Guardrails

Learn:

* input validation
* output validation
* tool permissioning
* human approval
* sensitive-data protection
* tool allowlists
* maximum iterations
* cost limits
* timeout limits

Example:

```text
Agent wants to:
DELETE customer records

        ↓

Human approval required
        ↓
      YES/NO
```

This is essential for production agents.

---

# 5E. Prompt Injection

The IIT Hyderabad course specifically includes **prompt-injection risk in RAG and defensive retrieval**. ([AI Launchpad][1])

This deserves its own study topic.

Learn:

### Direct injection

User tries to manipulate the agent.

### Indirect injection

Malicious instructions are hidden inside:

* documents
* websites
* emails
* search results

For agents, this is particularly serious because the model can potentially turn the injected instruction into a **tool action**.

Recent research continues to demonstrate that agentic systems remain vulnerable to indirect prompt injection, so this isn't merely a theoretical topic. ([arXiv][8])

---

# 🟢 FINAL WEEKEND — Project + Certification

The official program finishes with:

* project demonstration
* presentation
* feedback
* source-code submission
* assessment
* certificate. ([AI Launchpad][1])

We can reproduce the **technical portion** ourselves.

Your final project should contain:

```text
                 ┌──────────────────┐
                 │    React/UI      │
                 └────────┬─────────┘
                          ↓
                      FastAPI
                          ↓
                  Agent Orchestrator
                          ↓
          ┌───────────────┼───────────────┐
          ↓               ↓               ↓
       Research         SQL            Tools
        Agent           Agent             │
          ↓               ↓               ↓
       Qdrant            DB             MCP
          │
          ↓
       Memory
          │
          ↓
      LangGraph
          │
          ↓
     Human Approval
          │
          ↓
       LangFuse
          │
          ↓
      Evaluation
          │
          ↓
       Deployment
```

---

# 📚 COMPLETE IIT-HYDERABAD → FREE RESOURCE MAP

This is the table I'd actually keep beside you while studying.

| IIT Hyderabad Curriculum              | What you need to learn             | Best free resource                                                                                                                |
| ------------------------------------- | ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Foundations of Reliable AI Agents** | Agent fundamentals                 | [Hugging Face Agents Course](https://huggingface.co/agents-course?utm_source=chatgpt.com)                                         |
| LLM runtime                           | API, messages, context             | [OpenAI Function Calling](https://help.openai.com/en/articles/8555517-function-calling-in-the-openai-api?utm_source=chatgpt.com)  |
| Structured outputs                    | JSON schema, validation            | [Pydantic](https://docs.pydantic.dev/latest/?utm_source=chatgpt.com)                                                              |
| Tool calling                          | Function/tool calling              | [OpenAI Function Calling](https://help.openai.com/en/articles/8555517-function-calling-in-the-openai-api?utm_source=chatgpt.com)  |
| Retries                               | Retry/backoff/error handling       | API/framework docs + hands-on                                                                                                     |
| Rate limits                           | Production API handling            | API provider documentation                                                                                                        |
| Sessions/state                        | State management                   | LangGraph                                                                                                                         |
| **Production RAG**                    | RAG fundamentals                   | [Agentic RAG — DeepLearning.AI](https://www.deeplearning.ai/courses/building-agentic-rag-with-llamaindex/?utm_source=chatgpt.com) |
| Embeddings                            | Vector representation              | Qdrant docs                                                                                                                       |
| Vector DB                             | Qdrant                             | [Qdrant Documentation](https://qdrant.tech/documentation/?utm_source=chatgpt.com)                                                 |
| Chunking                              | Retrieval preparation              | Qdrant/LlamaIndex docs + implementation                                                                                           |
| Metadata filtering                    | Filtered retrieval                 | Qdrant docs                                                                                                                       |
| Reranking                             | Retrieval quality                  | LlamaIndex/LangChain docs                                                                                                         |
| Query expansion                       | Better retrieval                   | Agentic RAG course                                                                                                                |
| Short-term memory                     | Conversation state                 | LangGraph                                                                                                                         |
| Long-term memory                      | Persistent user/application memory | LangGraph/Deep Agents                                                                                                             |
| RAG security                          | Prompt injection                   | Security study + hands-on                                                                                                         |
| **Multi-Agent Systems**               | Agent architectures                | [AI Agents in LangGraph](https://www.deeplearning.ai/courses/ai-agents-in-langgraph?utm_source=chatgpt.com)                       |
| Supervisor                            | Multi-agent orchestration          | LangGraph                                                                                                                         |
| Planner-executor                      | Planning                           | LangGraph                                                                                                                         |
| Reflection                            | Critique/revision loops            | LangGraph                                                                                                                         |
| Review pattern                        | Human/agent review                 | LangGraph                                                                                                                         |
| State                                 | Graph state                        | LangGraph                                                                                                                         |
| Checkpoints                           | Persistence                        | LangGraph                                                                                                                         |
| Breakpoints                           | Human intervention                 | LangGraph                                                                                                                         |
| Resumability                          | Long-running workflows             | LangGraph                                                                                                                         |
| MCP                                   | Tool integration                   | [MCP Documentation](https://modelcontextprotocol.io/?utm_source=chatgpt.com)                                                      |
| Skills/plugins                        | Agent capabilities                 | LangChain/Deep Agents                                                                                                             |
| **Evaluation**                        | Agent evaluation                   | [LangFuse Documentation](https://langfuse.com/docs?utm_source=chatgpt.com)                                                        |
| Tracing                               | Agent observability                | LangFuse                                                                                                                          |
| Cost                                  | Token/cost tracking                | LangFuse                                                                                                                          |
| Latency                               | Performance                        | LangFuse                                                                                                                          |
| Failure analysis                      | Trace analysis                     | LangFuse                                                                                                                          |
| Guardrails                            | Safety/reliability                 | LangFuse + framework docs                                                                                                         |
| Human-in-loop                         | Approval workflows                 | LangGraph                                                                                                                         |
| Monitoring                            | Production observability           | LangFuse                                                                                                                          |
| Continuous improvement                | Evaluation → iteration             | LangFuse                                                                                                                          |
| FastAPI                               | Production API                     | [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/?utm_source=chatgpt.com)                                                 |
| Deployment                            | Production packaging               | FastAPI + Docker                                                                                                                  |
| **Final project**                     | End-to-end agent                   | Your own project                                                                                                                  |

---

# ⭐ The most important free resources

If the table looks overwhelming, **start with these six**:

### 1. Hugging Face Agents Course

[Hugging Face Agents Course](https://huggingface.co/agents-course?utm_source=chatgpt.com)

**Foundation**

### 2. DeepLearning.AI — AI Agents in LangGraph

[AI Agents in LangGraph](https://www.deeplearning.ai/courses/ai-agents-in-langgraph?utm_source=chatgpt.com)

**LangGraph + agents**

### 3. DeepLearning.AI — Agentic RAG

[Building Agentic RAG with LlamaIndex](https://www.deeplearning.ai/courses/building-agentic-rag-with-llamaindex/?utm_source=chatgpt.com)

**RAG + research agents**

### 4. Qdrant Documentation

[Qdrant Documentation](https://qdrant.tech/documentation/?utm_source=chatgpt.com)

**Vector DB**

### 5. MCP Documentation

[Model Context Protocol](https://modelcontextprotocol.io/?utm_source=chatgpt.com)

**Tools/integration**

### 6. LangFuse Documentation

[LangFuse Documentation](https://langfuse.com/docs?utm_source=chatgpt.com)

**Evaluation + observability**

---

# 🧭 How I'd organize your study

Unlike the previous IISc course, **I would not make this another 6–12 week generic curriculum**.

I'd follow the IIT-H course structure:

```text
PREREQUISITES
Python + APIs + LLM basics
        ↓
WEEKEND 1
Reliable Agent Foundations
        ↓
      BUILD
Raw LLM → Structured Output → Tools → Retry
        ↓
WEEKEND 2
RAG + Memory
        ↓
      BUILD
Qdrant → Retrieval → Reranking → Memory
        ↓
PROJECT WEEK
Combine everything
        ↓
WEEKEND 3
LangGraph + Multi-Agent + MCP
        ↓
      BUILD
Supervisor → Checkpoints → Human approval → MCP
        ↓
WEEKEND 4
Evaluation + Observability
        ↓
      BUILD
LangFuse → Evaluation → Guardrails
        ↓
FINAL
Deploy + Demonstrate
```

---



**Don't take the same topics twice.**

Use:

**IISc curriculum → SDD + Agentic Coding + Full-stack + CI/CD + System Design**

and

**IIT Hyderabad curriculum → Agent Runtime + RAG + Memory + LangGraph + Multi-agent + MCP + Evaluation + LangFuse + Guardrails**

That gives you a **much more complete Agentic AI engineering curriculum than either course individually**—while using free resources for the technical learning.

And given your existing data-engineering background, this combined route is actually a very strong fit: you can spend less time on basic Python/SQL and more time on **production agents, data/RAG, orchestration, evaluation and enterprise integration**.

[1]: https://ailaunchpad.cse.iith.ac.in/?utm_source=chatgpt.com "Applied AI Professional Certification Program"
[2]: https://help.openai.com/en/articles/8555517?utm_source=chatgpt.com "Function Calling in the OpenAI API | OpenAI Help Center"
[3]: https://huggingface.co/agents-course?utm_source=chatgpt.com "agents-course (Hugging Face Agents Course)"
[4]: https://www.deeplearning.ai/courses/building-agentic-rag-with-llamaindex?utm_source=chatgpt.com "Building Agentic RAG with Llamaindex - DeepLearning.AI"
[5]: https://www.deeplearning.ai/courses/ai-agents-in-langgraph?utm_source=chatgpt.com "AI Agents in LangGraph - DeepLearning.AI"
[6]: https://www.youtube.com/watch?v=EAwAJc0bD7o&utm_source=chatgpt.com "LangChain Academy New Course: Deep Agents - YouTube"
[7]: https://langfuse.com/docs?utm_source=chatgpt.com "Overview - Langfuse"
[8]: https://arxiv.org/abs/2504.18575?utm_source=chatgpt.com "WASP: Benchmarking Web Agent Security Against Prompt Injection Attacks"
