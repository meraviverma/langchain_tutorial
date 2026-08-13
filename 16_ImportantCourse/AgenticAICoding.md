Yes — **this format is much better for actually following the course week by week.** I’ll keep the **IISc PDF curriculum as the master structure**, and underneath each week I’ll map the best free resources to the exact topics they cover.

The PDF is a **6-weekend program**, with Week 1 covering Agentic AI fundamentals, Week 2 specification-driven development, Week 3 full-stack application development, Week 4 testing/CI-CD/deployment, Week 5 evaluation, and Week 6 system design. 

I've also rechecked the major free resources against their current official pages, rather than just giving you generic YouTube recommendations.

---

# First: Prerequisites — do these BEFORE Week 1

You don't need to become an expert in these. The goal is simply to be comfortable enough that the Agentic AI material doesn't feel difficult.

| Prerequisite           | What you need to know                                           | Free resource                                                                                          |
| ---------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| **Python**             | Functions, classes, modules, exceptions, packages, async basics | [Python Official Tutorial](https://docs.python.org/3/tutorial/?utm_source=chatgpt.com)                 |
| **Git/GitHub**         | clone, commit, branch, merge, PR, basic GitHub workflow         | [GitHub Skills](https://skills.github.com/?utm_source=chatgpt.com)                                     |
| **REST/API**           | HTTP, GET/POST, JSON, request/response                          | [MDN HTTP Overview](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview?utm_source=chatgpt.com) |
| **SQL**                | SELECT, JOIN, GROUP BY, INSERT/UPDATE, basic DB design          | [SQLBolt](https://sqlbolt.com/?utm_source=chatgpt.com)                                                 |
| **Basic LLM concepts** | tokens, context window, prompting, structured output            | [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/?utm_source=chatgpt.com)             |

### For you specifically

Because you already have a **data-engineering background**, I wouldn't spend much time on Python, SQL or basic APIs.

I'd treat them as **2–3 days of revision**, not as separate courses.

---

# Now the actual IISc curriculum → FREE resources

## 🟢 WEEK 1 — What is Agentic AI?

### PDF curriculum

The PDF says Week 1 covers:

> What is Agentic AI?
> Levels of autonomy of AI agents
> Augmented LLM calls
> Agentic workflows
> Single-agent systems
> Multi-agent systems
> Fully autonomous agents. 

### What you should actually learn

Break Week 1 into:

1. LLM vs AI agent
2. Tool/function calling
3. Agent loop
4. ReAct
5. Planning
6. Agentic workflows
7. Human-in-the-loop
8. Single-agent architecture
9. Multi-agent architecture
10. Autonomous agents
11. Agent memory/state
12. Agent reliability

### Best free resources

#### 1️⃣ Hugging Face — Agents Course

[Hugging Face Agents Course](https://huggingface.co/agents-course?utm_source=chatgpt.com)

**Covers:**

* Agent fundamentals
* Tools
* Thoughts/actions/observations
* LLMs
* Agent architecture
* Python implementation
* smolagents
* LangGraph
* LlamaIndex
* real-world agent use cases

The current syllabus explicitly has Agent Fundamentals, frameworks and real-world use cases. ([Hugging Face][1])

**This should be your primary Week 1 course.**

---

#### 2️⃣ DeepLearning.AI — AI Agents in LangGraph

[AI Agents in LangGraph](https://www.deeplearning.ai/courses/ai-agents-in-langgraph?utm_source=chatgpt.com)

**Use it for:**

* agent architecture
* agent loop
* tools
* building an agent from scratch
* LangGraph fundamentals
* agentic search

It's currently a 1h32m course with nine lessons and six coding examples. ([DeepLearning.AI][2])

### Week 1 outcome

By the end of Week 1, you should be able to explain:

```text
LLM
 ↓
Tool Calling
 ↓
Agent Loop
 ↓
Planning
 ↓
Tools
 ↓
Observation
 ↓
Next Action
 ↓
Final Answer
```

And you should be able to build a **basic tool-using agent in Python**.

---

# 🟢 WEEK 2 — Agentic Coding + Specification-Driven Development

### PDF curriculum

The PDF says:

> Agentic coding harness & specification-driven development
> writing high-quality specs
> vibe coding vs SDD
> writing correct tests. 

This is one of the most important weeks.

---

## Topic A — AI coding agents

Learn:

* coding agents
* repository understanding
* context management
* planning
* code generation
* debugging
* testing
* agent instructions
* skills
* MCP integration

### Free resource

[Claude Code Documentation](https://docs.anthropic.com/en/docs/claude-code?utm_source=chatgpt.com)

Use this primarily as **documentation + hands-on practice**, rather than trying to finish every page.

---

## Topic B — Vibe Coding vs SDD

### Best resource

[Spec-Driven Development with Coding Agents — DeepLearning.AI](https://www.deeplearning.ai/courses/spec-driven-development-with-coding-agents?utm_source=chatgpt.com)

This is almost a direct match to the PDF.

It teaches:

* vibe coding vs SDD
* project constitution
* feature specifications
* preserving context
* planning
* implementation
* verification
* human-in-the-loop
* custom agent skills

The current course has 15 lessons. ([DeepLearning.AI][3])

### Topic C — GitHub Spec Kit

[GitHub Spec Kit](https://github.com/github/spec-kit?utm_source=chatgpt.com)

Use this **after** the DeepLearning.AI course.

Your workflow becomes:

```text
Business requirement
        ↓
Project Constitution
        ↓
Feature Specification
        ↓
Technical Plan
        ↓
Tasks
        ↓
AI Coding Agent
        ↓
Implementation
        ↓
Tests
        ↓
Verification
```

This is the practical implementation of SDD.

---

### Week 2 outcome

You should be able to take:

> "Build an AI-powered expense tracker."

and NOT immediately tell the coding agent:

> "Build it."

Instead:

```text
Requirement
   ↓
Specification
   ↓
Architecture
   ↓
Implementation plan
   ↓
Tasks
   ↓
Coding agent
   ↓
Tests
```

That is exactly the mindset this week is trying to teach.

---

# 🟢 WEEK 3 — Build an End-to-End Full-Stack Application

### PDF curriculum

The PDF says:

> Building an end-to-end full-stack web application with agentic coding — front end & back end specs. Self-project begins. 

This week combines **software engineering + Agentic AI**.

---

## Topic A — Backend

### FastAPI

[FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/?utm_source=chatgpt.com)

Learn:

* REST APIs
* endpoints
* request/response
* Pydantic
* authentication basics
* async
* database integration
* API testing

---

## Topic B — Frontend

### React

[React Learn](https://react.dev/learn?utm_source=chatgpt.com)

Only learn:

* components
* props
* state
* hooks
* forms
* API calls
* basic routing

Don't spend months learning React.

---

## Topic C — Database

### SQL

[SQLBolt](https://sqlbolt.com/?utm_source=chatgpt.com)

Learn:

* SELECT
* JOIN
* GROUP BY
* CRUD
* indexes
* schema design

Then use PostgreSQL for the project.

---

## Topic D — Full-stack practice

### University of Helsinki Full Stack Open

[Full Stack Open](https://fullstackopen.com/en/?utm_source=chatgpt.com)

This is a **large free course**, but don't do the entire thing.

Use the relevant sections for:

* React
* REST APIs
* databases
* testing
* full-stack development

---

### Week 3 architecture

Your project should start looking like:

```text
              ┌──────────────┐
              │   React UI   │
              └──────┬───────┘
                     ↓
              ┌──────────────┐
              │   FastAPI    │
              └──────┬───────┘
                     ↓
              ┌──────────────┐
              │ AI Agent     │
              └──────┬───────┘
                     ↓
          ┌──────────┼──────────┐
          ↓          ↓          ↓
        LLM        Tools       DB
```

### Week 3 outcome

A working full-stack AI application.

Not just a notebook.

---

# 🟢 WEEK 4 — Testing + CI/CD + Cloud Deployment

### PDF curriculum

The PDF says:

> Writing full unit tests, CI/CD and cloud deployment of the application built in Week 3. 

This week has three major areas.

---

## Topic A — Testing

Learn:

* unit testing
* integration testing
* API testing
* end-to-end testing
* mocking
* regression testing
* testing AI components

### Python

[pytest Documentation](https://docs.pytest.org/en/stable/?utm_source=chatgpt.com)

---

## Topic B — Docker

[Docker Get Started](https://docs.docker.com/get-started/?utm_source=chatgpt.com)

Learn:

* Dockerfile
* image
* container
* volumes
* networks
* Docker Compose

Your application should become:

```text
React
 ↓
Docker
 ↓
FastAPI
 ↓
Docker
 ↓
PostgreSQL
 ↓
Docker
```

---

## Topic C — CI/CD

### GitHub Actions

[GitHub Actions Documentation](https://docs.github.com/en/actions?utm_source=chatgpt.com)

Build:

```text
git push
   ↓
GitHub Actions
   ↓
Run tests
   ↓
Build
   ↓
Docker
   ↓
Deploy
```

---

## Topic D — Deployment

### Frontend

[Vercel Documentation](https://vercel.com/docs?utm_source=chatgpt.com)

### Cloud

Pick **one**:

[AWS Free Tier](https://aws.amazon.com/free/?utm_source=chatgpt.com)

Don't learn AWS + Azure + GCP simultaneously.

---

### Week 4 outcome

You should have:

```text
GitHub
   ↓
CI/CD
   ↓
Tests
   ↓
Docker
   ↓
Cloud
   ↓
Live application
```

---

# 🟢 WEEK 5 — Evaluation of Agentic Coding

### PDF curriculum

The PDF says:

> Principled evaluation of the agentic coding lifecycle — the AI-driven software development lifecycle. 

This is where we go beyond:

> "The application works."

We ask:

> "How do I know the AI agent works reliably?"

---

## What you need to learn

### Traditional software evaluation

* unit tests
* integration tests
* regression tests

### Agent evaluation

* output quality
* trajectory evaluation
* tool selection
* tool arguments
* hallucination
* task completion
* LLM-as-judge
* evaluation datasets
* regression evaluation
* latency
* cost
* reliability

---

## Best free resource

[LangChain Academy — Agent Observability & Evaluation](https://academy.langchain.com/courses/building-reliable-agents?utm_source=chatgpt.com)

This is particularly relevant because the LangChain ecosystem has dedicated material around observing and evaluating agent behavior.

Also keep an eye on LangChain Academy's newer production monitoring material; its current material covers production traces, cost, quality, latency and issues such as prompt injection and PII leakage. ([YouTube][4])

### Week 5 outcome

You should be able to create something like:

```text
                    Agent
                      ↓
              ┌───────────────┐
              │ Evaluation    │
              └───────┬───────┘
                      ↓
          ┌───────────┼───────────┐
          ↓           ↓           ↓
       Quality      Cost       Latency
          ↓           ↓           ↓
       Accuracy    Tokens     Response
```

And answer:

**"Why is version 2 of my agent better than version 1?"**

---

# 🟢 WEEK 6 — System Design + Final Project

### PDF curriculum

The PDF says:

> High-level system design for new software applications. Final project presentations. 

This is where everything comes together.

---

# What you should learn in Week 6

## Traditional system design

* scalability
* load balancing
* caching
* databases
* queues
* APIs
* microservices
* fault tolerance
* monitoring

## Agentic system design

Add:

* LLM gateway
* model routing
* agent orchestration
* tool layer
* memory
* vector database
* MCP
* guardrails
* human approval
* evaluation
* observability

Your architecture should eventually look something like:

```text
                         USER
                           │
                           ↓
                      React UI
                           │
                           ↓
                       API Layer
                           │
                           ↓
                 ┌──────────────────┐
                 │ Agent Orchestrator│
                 └────────┬─────────┘
                          │
          ┌───────────────┼────────────────┐
          ↓               ↓                ↓
       Planner         Research         Coding
        Agent           Agent            Agent
          │               │                │
          └───────────────┼────────────────┘
                          ↓
                    Tool / MCP Layer
                          │
          ┌───────────────┼───────────────┐
          ↓               ↓               ↓
        APIs            Database        Search
          │
          ↓
       Vector DB
          │
          ↓
        Redis
          │
          ↓
      Observability
          │
          ↓
      Evaluation
```

---

# But there is ONE thing I would add to Week 6

## MCP

The PDF mentions MCP in its tools list. 

Use:

[Official Model Context Protocol Documentation](https://modelcontextprotocol.io/?utm_source=chatgpt.com)

And, for a more guided learning experience:

[LangChain Academy Deep Agents](https://academy.langchain.com/courses/foundation-introduction-to-deepagents?utm_source=chatgpt.com)

The current free Deep Agents course has 38 lessons covering tools, MCP, threads/checkpoints, human-in-the-loop, execution environments, context management, skills, memory, delegation and subagents. ([LangChain Academy][5])

That makes it an **excellent bridge between Weeks 1, 5 and 6**.

---

# 📚 So here is your COMPLETE week-by-week map

This is the table I would actually save/bookmark.

| IISc Week        | PDF Curriculum         | Free resource                                                                                                                       | What it covers                   |
| ---------------- | ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| **Prerequisite** | Programming foundation | [Python Tutorial](https://docs.python.org/3/tutorial/?utm_source=chatgpt.com)                                                       | Python                           |
|                  | Git/GitHub             | [GitHub Skills](https://skills.github.com/?utm_source=chatgpt.com)                                                                  | Git/GitHub                       |
|                  | SQL                    | [SQLBolt](https://sqlbolt.com/?utm_source=chatgpt.com)                                                                              | SQL                              |
|                  | LLM basics             | [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/?utm_source=chatgpt.com)                                          | LLM fundamentals                 |
| **Week 1**       | What is Agentic AI?    | [Hugging Face Agents Course](https://huggingface.co/agents-course?utm_source=chatgpt.com)                                           | Agent fundamentals               |
|                  | Agent autonomy         | [AI Agents in LangGraph](https://www.deeplearning.ai/courses/ai-agents-in-langgraph?utm_source=chatgpt.com)                         | Agent architecture               |
|                  | Augmented LLM calls    | Hugging Face Agents                                                                                                                 | Tools/actions                    |
|                  | Agentic workflows      | LangGraph                                                                                                                           | Workflows                        |
|                  | Single-agent           | LangGraph                                                                                                                           | Agents                           |
|                  | Multi-agent            | LangChain Deep Agents                                                                                                               | Delegation/subagents             |
|                  | Autonomous agents      | Hugging Face + Deep Agents                                                                                                          | Long-running agents              |
| **Week 2**       | Agentic coding         | [Claude Code Docs](https://docs.anthropic.com/en/docs/claude-code?utm_source=chatgpt.com)                                           | Coding agents                    |
|                  | SDD                    | [DeepLearning.AI SDD Course](https://www.deeplearning.ai/courses/spec-driven-development-with-coding-agents?utm_source=chatgpt.com) | Specification-driven development |
|                  | Vibe coding vs SDD     | Same SDD course                                                                                                                     | Development methodology          |
|                  | High-quality specs     | Same SDD course                                                                                                                     | Requirements/specs               |
|                  | Tests                  | [pytest](https://docs.pytest.org/en/stable/?utm_source=chatgpt.com)                                                                 | Testing                          |
|                  | SDD implementation     | [GitHub Spec Kit](https://github.com/github/spec-kit?utm_source=chatgpt.com)                                                        | Practical SDD                    |
| **Week 3**       | Full-stack application | [FastAPI](https://fastapi.tiangolo.com/tutorial/?utm_source=chatgpt.com)                                                            | Backend                          |
|                  | Frontend               | [React Learn](https://react.dev/learn?utm_source=chatgpt.com)                                                                       | React                            |
|                  | Database               | [SQLBolt](https://sqlbolt.com/?utm_source=chatgpt.com)                                                                              | SQL                              |
|                  | Full-stack             | [Full Stack Open](https://fullstackopen.com/en/?utm_source=chatgpt.com)                                                             | Full-stack practice              |
|                  | Agent development      | [LangGraph Course](https://www.deeplearning.ai/courses/ai-agents-in-langgraph?utm_source=chatgpt.com)                               | Agent integration                |
| **Week 4**       | Unit testing           | [pytest](https://docs.pytest.org/en/stable/?utm_source=chatgpt.com)                                                                 | Testing                          |
|                  | Docker                 | [Docker Getting Started](https://docs.docker.com/get-started/?utm_source=chatgpt.com)                                               | Containerization                 |
|                  | CI/CD                  | [GitHub Actions](https://docs.github.com/en/actions?utm_source=chatgpt.com)                                                         | Automation                       |
|                  | Cloud                  | [AWS Free Tier](https://aws.amazon.com/free/?utm_source=chatgpt.com)                                                                | Cloud                            |
|                  | Hosting                | [Vercel Docs](https://vercel.com/docs?utm_source=chatgpt.com)                                                                       | Deployment                       |
| **Week 5**       | Agent evaluation       | [LangChain Academy Evaluation](https://academy.langchain.com/courses/building-reliable-agents?utm_source=chatgpt.com)               | Agent evaluation                 |
|                  | Observability          | Same                                                                                                                                | Tracing/monitoring               |
|                  | Quality                | Same                                                                                                                                | Evaluation                       |
|                  | Reliability            | Same                                                                                                                                | Production agents                |
|                  | AI SDLC                | SDD + Evaluation                                                                                                                    | AI-driven development            |
| **Week 6**       | System design          | [Full Stack Open](https://fullstackopen.com/en/?utm_source=chatgpt.com)                                                             | Software architecture            |
|                  | Agent architecture     | [LangChain Deep Agents](https://academy.langchain.com/courses/foundation-introduction-to-deepagents?utm_source=chatgpt.com)         | Agent architecture               |
|                  | MCP                    | [MCP Documentation](https://modelcontextprotocol.io/?utm_source=chatgpt.com)                                                        | Tool/data integration            |
|                  | Multi-agent design     | [LangChain Deep Agents](https://academy.langchain.com/courses/foundation-introduction-to-deepagents?utm_source=chatgpt.com)         | Delegation/subagents             |
|                  | Final project          | **Your own project**                                                                                                                | End-to-end implementation        |

---

# ⭐ The 7 resources I'd prioritize

Don't get overwhelmed by the table.

If you asked me:

> **"Which seven should I actually start with?"**

I'd say:

### 1. 🥇 Hugging Face Agents Course

[Start here — Hugging Face Agents Course](https://huggingface.co/agents-course?utm_source=chatgpt.com)

**Week 1**

---

### 2. 🥈 DeepLearning.AI — AI Agents in LangGraph

[AI Agents in LangGraph](https://www.deeplearning.ai/courses/ai-agents-in-langgraph?utm_source=chatgpt.com)

**Week 1**

---

### 3. 🥉 DeepLearning.AI — Spec-Driven Development

[Spec-Driven Development with Coding Agents](https://www.deeplearning.ai/courses/spec-driven-development-with-coding-agents?utm_source=chatgpt.com)

**Week 2**

---

### 4. GitHub Spec Kit

[GitHub Spec Kit](https://github.com/github/spec-kit?utm_source=chatgpt.com)

**Week 2 practical implementation**

---

### 5. LangChain Academy — Deep Agents

[LangChain Deep Agents](https://academy.langchain.com/courses/foundation-introduction-to-deepagents?utm_source=chatgpt.com)

**Weeks 1–2 + MCP + multi-agent + memory**

---

### 6. LangChain Academy — Evaluation

[Agent Observability & Evaluation](https://academy.langchain.com/courses/building-reliable-agents?utm_source=chatgpt.com)

**Week 5**

---

### 7. MCP Official Documentation

[Model Context Protocol](https://modelcontextprotocol.io/?utm_source=chatgpt.com)

**Week 6 / after you understand agents**

---

# 🎯 Your learning path should therefore look like this

```text
PREREQUISITES
Python + Git + SQL + APIs
              │
              ↓
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WEEK 1
AGENTIC AI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Hugging Face Agents
        +
LangGraph
        +
Deep Agents
              │
              ↓
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WEEK 2
AGENTIC CODING + SDD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SDD Course
        +
GitHub Spec Kit
        +
Claude Code
              │
              ↓
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WEEK 3
FULL-STACK APPLICATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FastAPI
        +
React
        +
SQL
        +
Agent
              │
              ↓
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WEEK 4
TEST + DEPLOY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
pytest
        +
Docker
        +
GitHub Actions
        +
AWS/Vercel
              │
              ↓
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WEEK 5
EVALUATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Agent evaluation
        +
Tracing
        +
Observability
        +
Reliability
              │
              ↓
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WEEK 6
SYSTEM DESIGN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MCP
        +
Multi-agent architecture
        +
Memory
        +
Production architecture
              │
              ↓
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FINAL PROJECT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SPEC
 ↓
PLAN
 ↓
AI CODING AGENT
 ↓
FULL STACK
 ↓
AGENTS
 ↓
MCP
 ↓
TESTS
 ↓
EVALUATION
 ↓
DOCKER
 ↓
CI/CD
 ↓
CLOUD
 ↓
SYSTEM DESIGN
```

**This is the version I would follow.** It keeps the original IISc curriculum intact rather than replacing it with a generic Agentic AI roadmap, while adding the free resources needed to actually cover each component.

And importantly, you can keep the **PDF open beside this roadmap**: go to **Week 1 in the PDF → come here → open only the Week 1 resources**; then Week 2, Week 3, and so on. That removes the confusion of "which course should I watch for which topic?"

[1]: https://huggingface.co/agents-course?utm_source=chatgpt.com "agents-course (Hugging Face Agents Course)"
[2]: https://www.deeplearning.ai/courses/ai-agents-in-langgraph?utm_source=chatgpt.com "AI Agents in LangGraph - DeepLearning.AI"
[3]: https://www.deeplearning.ai/courses/spec-driven-development-with-coding-agents?utm_source=chatgpt.com "Spec-Driven Development with Coding Agents - DeepLearning.AI"
[4]: https://www.youtube.com/watch?v=efVSns9DAmo&utm_source=chatgpt.com "LangChain Academy New Course: Monitoring Production Agents - YouTube"
[5]: https://academy.langchain.com/courses/foundation-introduction-to-deepagents?utm_source=chatgpt.com "LangChain Deep Agents Course | Build Long-Running AI Agents"
