# 🧩 Detailed Walkthrough of  **RUNNABLE**

---

# 🔹 Why Runnables?
LangChain introduced **Runnables** to unify how all components (LLMs, prompts, retrievers, parsers, tools) are executed.  
Instead of each having different methods (`predict()`, `run()`, `parse()`), now everything shares **three core methods**:

- `invoke()` → single input → single output  
- `batch()` → multiple inputs → multiple outputs  
- `stream()` → stream chunks of output as they’re generated  

This consistency makes pipelines easier to build, debug, and extend.

---

# 🔹 Two Major Categories of Runnables

## 1. **Task-Specific Runnables**
These are the “do-something” units:
- Run LLM calls  
- Format prompts  
- Retrieve documents  
- Parse outputs  
- Call tools/functions  

👉 They perform the actual work inside your pipeline.

---

## 2. **Runnable Primitives**
These are the **control-flow building blocks**:
- **RunnableSequence** → Sequential execution (step by step).  
- **RunnableParallel** → Parallel execution (same input sent to multiple runnables).  
- **RunnableBranch** → Conditional routing (like if-else).  
- **RunnableLambda** → Wraps a Python function for custom logic.  
- **RunnablePassthrough** → Returns input unchanged (useful for defaults).  

👉 They orchestrate how multiple Runnables interact, just like control-flow statements in programming.

---

# 🔹 Example Implementations

### ✅ Sequential
```python
chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)
result = chain.invoke({'topic': 'Data Engineering'})
```
Runs step by step: generate joke → explain joke.

---

### ✅ Parallel
```python
parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1, model, parser),
    'linkedin': RunnableSequence(prompt2, model, parser)
})
result = parallel_chain.invoke({'topic': 'Apache-Kafka'})
```
Runs tweet + LinkedIn post generation simultaneously.

---

### ✅ Conditional (Branch)
```python
branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 300, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)
final_chain = RunnableSequence(report_chain, branch_chain)
result = final_chain.invoke({'topic': 'Attention is all you need!'})
```
If text length > 300 → summarize, else → return as-is.

---

# 🔹 Key Takeaways
- **Runnables unify execution** → one interface for everything.  
- **Task-specific runnables** → do the actual work.  
- **Runnable primitives** → control flow (sequence, parallel, branch, etc.).  
- **Backward compatibility** → old methods still exist, but Runnables are the recommended way forward.  

---

# 📋 Runnables in LangChain

## 🔹 Task Specific Runnables
- **Definition**: Core LangChain components converted into Runnables so they can be used in pipelines.  
- **Purpose**: Perform task-specific operations like LLM calls, prompting, retrieval, etc.  
- **Examples**:  
  - `ChatOpenAI` → Runs an LLM model  
  - `PromptTemplate` → Formats prompts dynamically  
  - `Retriever` → Retrieves relevant documents  

---

## 🔹 Runnable Primitives
- **Definition**: Fundamental building blocks for structuring execution logic in AI workflows.  
- **Purpose**: Orchestrate execution by defining how different Runnables interact (sequentially, in parallel, conditionally, etc.).  
- **Examples**:  
  - `RunnableSequence` → Runs steps in order (`|` operator)  
  - `RunnableParallel` → Runs multiple steps simultaneously  
  - `RunnableMap` → Maps the same input across multiple functions  
  - `RunnableBranch` → Implements conditional execution (if-else logic)  
  - `RunnableLambda` → Wraps custom Python functions into Runnables  
  - `RunnablePassthrough` → Forwards input as output (acts as a placeholder)  

---

✨ In short:  
- **Task Specific Runnables** = “do-something units” (LLM calls, prompt formatting, retrieval).  
- **Runnable Primitives** = “logic layer” (sequence, parallel, branch, lambda, passthrough).  

### 🔹 RunnablePassthrough in LangChain

**RunnablePassthrough** is one of the simplest **Runnable primitives** in LangChain.  
It doesn’t transform or process the input — it just **returns the input as the output**. Think of it as a “no-op” (no operation) step in your pipeline.

---

## ✅ Purpose
- Acts as a **placeholder** when you want to keep the input unchanged.  
- Useful as a **default branch** in conditional workflows.  
- Helps in debugging pipelines by letting you see raw inputs passed through.  

---

## 🔹 Example Usage

### 1. Basic Passthrough
```python
from langchain_core.runnables import RunnablePassthrough

passthrough = RunnablePassthrough()
print(passthrough.invoke("Hello World"))
# Output: "Hello World"
```
👉 Whatever you give it, it returns unchanged.

---

### 2. In a Branch Chain
```python
from langchain_core.runnables import RunnableBranch, RunnablePassthrough

branch_chain = RunnableBranch(
    (lambda x: "error" in x.lower(), RunnablePassthrough()),
    RunnablePassthrough()
)

print(branch_chain.invoke("This is fine"))
# Output: "This is fine"

print(branch_chain.invoke("Error occurred"))
# Output: "Error occurred"
```
👉 If condition matches, it passes input unchanged. Otherwise, fallback also returns input.

---

### 3. As a Debugging Tool
You can insert `RunnablePassthrough` in a sequence to check intermediate outputs:
```python
from langchain_core.runnables import RunnableSequence

chain = RunnableSequence(prompt1, model, RunnablePassthrough(), parser)
```
👉 Here, the passthrough lets you inspect what the model produced before parsing.

---

## 🔹 Key Takeaways
- **RunnablePassthrough = identity function** (input → output).  
- Often used as a **default branch** in `RunnableBranch`.  
- Handy for **debugging** or when you want to keep raw input/output unchanged.  

---

### 🔹 RunnableLambda in LangChain

**RunnableLambda** is a **Runnable primitive** that lets you wrap a normal Python function into the LangChain pipeline.  
It’s useful when you want to add **custom logic** (preprocessing, transformation, filtering, postprocessing, API calls, etc.) inside your workflow.

---

## ✅ Purpose
- Integrate **custom Python functions** into LangChain pipelines.  
- Acts like middleware between other Runnables.  
- Lets you apply logic that isn’t handled by LLMs or built-in components.  

---

## 🔹 Example 1: Simple Transformation
```python
from langchain_core.runnables import RunnableLambda

# Define a Python function
def word_count(text):
    return len(text.split())

# Wrap it as a Runnable
word_count_runnable = RunnableLambda(word_count)

print(word_count_runnable.invoke("AI makes life easier"))
# Output: 4
```
👉 Here, `RunnableLambda` counts words in the input text.

---

## 🔹 Example 2: Preprocessing Before LLM
```python
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableLambda

model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")
parser = StrOutputParser()

# Custom preprocessing: lowercase input
lowercase = RunnableLambda(lambda x: x.lower())

prompt = PromptTemplate(
    template="Write a poem about {topic}",
    input_variables=["topic"]
)

chain = RunnableSequence(lowercase, prompt, model, parser)

print(chain.invoke("AI Revolution"))
```
👉 Input `"AI Revolution"` is first converted to lowercase, then passed into the prompt → model → parser.

---

## 🔹 Example 3: Conditional Branch with Lambda
```python
from langchain_core.runnables import RunnableBranch, RunnablePassthrough

branch_chain = RunnableBranch(
    (lambda x: "error" in x.lower(), RunnableLambda(lambda x: "⚠️ Error detected")),
    RunnablePassthrough()
)

print(branch_chain.invoke("This is fine"))
# Output: "This is fine"

print(branch_chain.invoke("Error occurred"))
# Output: "⚠️ Error detected"
```
👉 `RunnableLambda` provides custom logic for handling error cases.

---

## 🔹 Key Takeaways
- **RunnableLambda = custom Python function inside LangChain pipeline.**  
- Perfect for **data preprocessing, transformation, filtering, or fallback logic.**  
- Works seamlessly with other primitives like **Sequence, Parallel, Branch, Passthrough.**

---

# 🔹 RunnableBranch in LangChain

**RunnableBranch** is a **control-flow primitive** in LangChain that lets you add **conditional logic** to your pipeline.  
It works like an **if-elif-else block**: you define conditions, and based on the input, the pipeline routes execution to the matching branch.

---

## ✅ Purpose
- Route inputs to different chains depending on conditions.  
- Useful when you want **different workflows for different types of data**.  
- Provides a **default branch** if no condition matches.  

---

## 🔹 Structure
```python
RunnableBranch(
    (condition_function, runnable_if_true),
    (condition_function, runnable_if_true),
    default_runnable
)
```

- Each branch has:
  - A **condition function** (lambda or custom function returning True/False).  
  - A **Runnable** to execute if the condition matches.  
- The **first matching condition** is executed.  
- If none match, the **default runnable** runs.

---

## 🔹 Example 1: Positive vs Negative Feedback
```python
from langchain_core.runnables import RunnableBranch, RunnableLambda, RunnablePassthrough

branch_chain = RunnableBranch(
    (lambda x: "good" in x.lower(), RunnableLambda(lambda x: "😊 Thanks for the positive feedback!")),
    (lambda x: "bad" in x.lower(), RunnableLambda(lambda x: "😟 Sorry to hear that, we’ll improve.")),
    RunnablePassthrough()
)

print(branch_chain.invoke("This product is good"))
# Output: 😊 Thanks for the positive feedback!

print(branch_chain.invoke("This product is bad"))
# Output: 😟 Sorry to hear that, we’ll improve.

print(branch_chain.invoke("This product is okay"))
# Output: This product is okay
```

---

## 🔹 Example 2: Length-Based Routing
```python
branch_chain = RunnableBranch(
    (lambda x: len(x) > 50, RunnableLambda(lambda x: "Long text detected")),
    (lambda x: len(x) <= 50, RunnableLambda(lambda x: "Short text detected")),
    RunnablePassthrough()
)

print(branch_chain.invoke("AI is amazing"))
# Output: Short text detected
```

---

## 🔹 Example 3: With LLMs
```python
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")
parser = StrOutputParser()

positive_prompt = PromptTemplate(
    template="Write a cheerful response to: {feedback}",
    input_variables=["feedback"]
)

negative_prompt = PromptTemplate(
    template="Write a constructive response to: {feedback}",
    input_variables=["feedback"]
)

branch_chain = RunnableBranch(
    (lambda x: "love" in x["feedback"].lower(), positive_prompt | model | parser),
    (lambda x: "hate" in x["feedback"].lower(), negative_prompt | model | parser),
    RunnableLambda(lambda x: "Neutral feedback detected")
)

print(branch_chain.invoke({"feedback": "I love this phone"}))
# Output: Cheerful response from Gemini
```

---

## 🔹 Key Takeaways
- **RunnableBranch = conditional routing** in LangChain pipelines.  
- Works like **if-else logic** for AI workflows.  
- Often combined with **RunnableLambda** (custom logic) and **RunnablePassthrough** (default fallback).  
- Enables **dynamic, flexible pipelines** that adapt to input.

---

✨ In your **feedback classifier project**, you already used `RunnableBranch` to route **positive vs negative sentiment**. You can extend it further:
- Add a **neutral branch**.  
- Use **RunnableLambda** for keyword-based rules.  
- Use **RunnablePassthrough** as a fallback when sentiment isn’t detected.  