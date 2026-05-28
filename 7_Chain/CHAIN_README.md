
# 🧩 Detailed Walkthrough of  **SIMPLE** Chain
---

## 🔹 1. Model Setup
```python
model = ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite')
```
- You’re connecting to Google’s Gemini model via LangChain’s `ChatGoogleGenerativeAI`.

---

## 🔹 2. Prompt Template
```python
prompt = PromptTemplate(
    template='Generate 5 interesting facts about {topic}',
    input_variables=['topic']
)
```
- This defines a reusable template where `{topic}` can be replaced dynamically (here: `"cricket"`).

---

## 🔹 3. Output Parser
```python
parser = StrOutputParser()
```
- Ensures the model’s output is returned as a **plain string**.  
- Useful when you just want text without enforcing JSON or schema.

---

## 🔹 4. Chain Definition
```python
chain = prompt | model | parser
```
This pipeline means:
1. **PromptTemplate** → Generates the final text prompt.  
2. **Model** → Produces the response.  
3. **StrOutputParser** → Converts the response into a string.

---

## 🔹 5. Execution
```python
result = chain.invoke({'topic':'cricket'})
print(result)
```
- Input: `{'topic': 'cricket'}`  
- Output: A string with 5 interesting facts about cricket.

---

## 🔹 6. Chain Graph Visualization
```python
chain.get_graph().print_ascii()
```
This prints an ASCII diagram of your chain, showing the flow:

```
PromptTemplate --> ChatGoogleGenerativeAI --> StrOutputParser
```

It’s a quick way to **debug and visualize** how data flows through your pipeline.

---

## 🔹 Why This is Useful
- **Clarity** → You can see exactly how prompts, models, and parsers connect.  
- **Debugging** → If something breaks, the graph shows where.  
- **Scalability** → As you add more steps (e.g., summaries, validators), the graph helps track complexity.

---

✅ **Key Takeaway**:  
Chain is a **simple linear pipeline**: prompt → model → parser.  
The ASCII graph confirms the structure, making it easy to reason about and extend.

---

# 🧩 Detailed Walkthrough of  **Sequential Chain**

This chain is a great example of **multi‑stage prompt chaining** in LangChain. Let’s break it down clearly:

---

## 🔹 1. Model Setup
```python
model = ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite')
```
- You’re using Google’s Gemini model wrapped in LangChain’s `ChatGoogleGenerativeAI`.

---

## 🔹 2. Prompt Templates
You defined two prompts:

1. **Detailed Report Prompt**
```python
prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)
```
- Takes a `topic` (here: `"Unemployment in India"`) and asks for a long, detailed report.

2. **Summary Prompt**
```python
prompt2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)
```
- Takes the detailed report as input and asks for a concise 5‑point summary.

---

## 🔹 3. Output Parser
```python
parser = StrOutputParser()
```
- Ensures the model’s output is returned as plain text.  
- No JSON or schema enforcement here — just raw strings.

---

## 🔹 4. Chain Definition
```python
chain = prompt1 | model | parser | prompt2 | model | parser
```
This pipeline flows like this:

1. **PromptTemplate1** → Generates the detailed report request.  
2. **Model** → Produces the detailed report.  
3. **StrOutputParser** → Converts the report into a string.  
4. **PromptTemplate2** → Takes that string and asks for a 5‑point summary.  
5. **Model** → Produces the summary.  
6. **StrOutputParser** → Converts the summary into a string.

---

## 🔹 5. Execution
```python
result = chain.invoke({'topic': 'Unemployment in India'})
print(result)
```
- Input: `{'topic': 'Unemployment in India'}`  
- Output: A **5‑point summary** of the detailed report on unemployment in India.

---

## 🔹 6. Graph Visualization
```python
chain.get_graph().print_ascii()
```
This prints an ASCII diagram of the chain:

```
PromptTemplate --> ChatGoogleGenerativeAI --> StrOutputParser --> PromptTemplate --> ChatGoogleGenerativeAI --> StrOutputParser
```

It shows the **linear flow** of your pipeline: report → summary.

---

## 🔹 Why This is Powerful
- **Automation** → You don’t need to manually call each step; the chain handles it.  
- **Reusability** → Swap out prompts or parsers easily.  
- **Scalability** → Add more stages (e.g., sentiment analysis, bullet points, JSON parsing).  
- **Debugging** → The ASCII graph makes it easy to see how data flows.

---

✅ **Key Takeaway**:  
Your chain is a **two‑stage workflow**:  
1. Generate a detailed report.  
2. Summarize it into 5 points.  

This is a classic **prompt chaining pattern** in LangChain — turning raw LLM outputs into structured, multi‑step results.

---
# 🧩 Detailed Walkthrough of  **Parallel Chain**


---

## 🔹 1. Two Models
- **Model 1** → `ChatGoogleGenerativeAI` (Gemini 3.1 flash‑lite).  
- **Model 2** → `ChatHuggingFace` (DeepSeek‑V4‑Pro).  
You’re using them side‑by‑side to process the same input text differently.

---

## 🔹 2. Prompts
- **Prompt 1** → Generates short notes from the text.  
- **Prompt 2** → Generates 5 short Q&A quiz items from the text.  
- **Prompt 3** → Merges notes and quiz into a single document.

---

## 🔹 3. RunnableParallel
```python
parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})
```
- Runs **both prompts in parallel**.  
- Produces two outputs: `"notes"` and `"quiz"`.  
- Each branch uses its own model and parser.

---

## 🔹 4. Merge Chain
```python
merge_chain = prompt3 | model1 | parser
```
- Takes the parallel outputs (`notes`, `quiz`).  
- Asks the model to merge them into one coherent document.

---

## 🔹 5. Final Chain
```python
chain = parallel_chain | merge_chain
```
- First step: run notes + quiz generation in parallel.  
- Second step: merge them into a single result.

---

## 🔹 6. Execution
```python
result = chain.invoke({'text': text})
print(result)
```
- Input: the SVM explanation text.  
- Output: a merged document containing both **short notes** and a **quiz**.

---

## 🔹 7. Graph Visualization
```python
chain.get_graph().print_ascii()
```
This prints an ASCII diagram showing the flow:

```
          ┌───────────────┐
          │ RunnableParallel│
          └───────┬────────┘
                  │
   ┌──────────────┴──────────────┐
   │ notes: Prompt1 → Model1 → Parser
   │ quiz:  Prompt2 → Model2 → Parser
   └──────────────┬──────────────┘
                  │
         Prompt3 → Model1 → Parser
```

---

## 🔹 Why This is Powerful
- **Parallelism** → You can generate multiple perspectives (notes + quiz) at once.  
- **Merging** → Combine outputs into a single coherent artifact.  
- **Flexibility** → Different models can handle different tasks (Gemini for summarization, DeepSeek for Q&A).  
- **Scalability** → Add more branches (e.g., sentiment analysis, flashcards) and merge them.

---

✅ **Key Takeaway**:  
This is a **multi‑model, multi‑prompt pipeline**:  
1. Generate notes and quiz in parallel.  
2. Merge them into one document.  
3. Visualize the workflow with `print_ascii()`.

---

# 🧩 Detailed Walkthrough of  **Conditional Chain**

## 🔹 Overview
This project uses **LangChain**, **Google Gemini**, and **HuggingFace models** to:
1. **Classify feedback sentiment** (positive or negative).
2. **Generate appropriate responses** based on the sentiment.
3. **Visualize the execution chain** using ASCII graphs.

---

## 🔹 Libraries & Methods Used

### 1. **dotenv**
```python
from dotenv import load_dotenv
```
- Loads environment variables from a `.env` file.
- Used here to securely manage API keys and credentials.

---

### 2. **LangChain Models**
```python
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
```
- **ChatGoogleGenerativeAI** → Connects to Google Gemini models.
- **ChatHuggingFace** → Connects to HuggingFace models (optional in this project).

---

### 3. **Pydantic**
```python
from pydantic import BaseModel, EmailStr, Field
```
- Provides **data validation** and **structured outputs**.
- Used to define a `Feedback` schema for sentiment classification.

---

### 4. **PromptTemplate**
```python
from langchain_core.prompts import PromptTemplate
```
- Defines structured prompts for the model.
- Ensures consistent input formatting.

---

### 5. **Output Parsers**
```python
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
```
- **StrOutputParser** → Converts model output into plain text.
- **PydanticOutputParser** → Converts model output into structured `Feedback` objects.

---

### 6. **Runnable Chains**
```python
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
```
- **RunnableBranch** → Executes different chains depending on conditions (positive/negative sentiment).
- **RunnableLambda** → Provides fallback logic if sentiment is not detected.

---

### 7. **Typing**
```python
from typing import Literal
```
- Used to restrict sentiment values to only `"positive"` or `"negative"`.

---

## 🔹 Code Explanation

### Step 1: Load Environment Variables
```python
load_dotenv()
```
Ensures API keys (Google Gemini, HuggingFace) are available for authentication.

---

### Step 2: Initialize Model
```python
model = ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite')
```
- Loads **Google Gemini 3.1 Flash Lite** model for fast inference.

---

### Step 3: Define Output Parsers
```python
parser = StrOutputParser()
```
- Converts raw model output into text.

```python
class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description='Give the sentiment of the feedback')
```
- Defines a schema for feedback sentiment.

```python
parser2 = PydanticOutputParser(pydantic_object=Feedback)
```
- Ensures model output matches the `Feedback` schema.

---

### Step 4: Create Sentiment Classification Prompt
```python
prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback text into postive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)
```
- Asks the model to classify feedback into **positive** or **negative**.
- Includes format instructions from `parser2`.

---

### Step 5: Build Classification Chain
```python
classifier_chain = prompt1 | model | parser2
```
- Combines prompt → model → parser into a pipeline.
- Ensures structured sentiment output.

---

### Step 6: Define Response Prompts
```python
prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)
```
- Separate prompts for **positive** and **negative** feedback.

---

### Step 7: Create Branching Logic
```python
branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt2 | model | parser),
    (lambda x:x.sentiment == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x: "could not find sentiment")
)
```
- If sentiment is **positive** → use `prompt2`.
- If sentiment is **negative** → use `prompt3`.
- If sentiment is missing → fallback message.

---

### Step 8: Combine Chains
```python
chain = classifier_chain | branch_chain
```
- First classify sentiment.
- Then generate appropriate response.

---

### Step 9: Run Example
```python
print(chain.invoke({'feedback': 'This is a beautiful phone'}))
```
- Input: `"This is a beautiful phone"`
- Output: Positive sentiment → Generates a positive response.

---

### Step 10: Visualize Chain
```python
chain.get_graph().print_ascii()
```
- Prints ASCII graph of the chain execution.
- Helps in debugging and understanding workflow.

---

## 🔹 Execution Flow Diagram (Simplified)

```
Feedback Text
     |
     v
 Sentiment Classifier (Gemini)
     |
     v
 Structured Sentiment (positive/negative)
     |
     v
 Branch Logic
   ├── Positive → Response Generator (Gemini)
   ├── Negative → Response Generator (Gemini)
   └── Fallback → "could not find sentiment"
```

---

## 🔹 Example Run

### Input:
```text
"This is a beautiful phone"
```

### Output:
```text
"Thank you for your wonderful feedback! We're glad you love the phone."
```

---

## 🔹 Key Takeaways
- **Modular design**: Each step (classification, branching, response) is independent.
- **Structured outputs**: Pydantic ensures reliable parsing.
- **Scalable workflow**: Runnable chains allow easy extension (e.g., neutral sentiment).
- **Visualization**: ASCII graphs make debugging easier.

---

# 🔹 Sequential vs Parallel vs Conditional Chains

## 1. **Sequential Chains**
- **Definition**: Tasks are executed **one after another** in a pipeline.
- **Flow**: Output of one step becomes the input of the next.
- **Use Case**: When steps depend on each other.
- **Example**:
```python
chain = step1 | step2 | step3
```
Here:
- `step1` → processes input
- `step2` → takes `step1` output
- `step3` → takes `step2` output

✅ Best for workflows like **classification → summarization → formatting**.

---

## 2. **Parallel Chains**
- **Definition**: Multiple tasks run **simultaneously** on the same input.
- **Flow**: Input is broadcast to all chains, and outputs are collected together.
- **Use Case**: When tasks are independent and don’t rely on each other.
- **Example**:
```python
from langchain_core.runnables import RunnableParallel

parallel_chain = RunnableParallel({
    "summary": summarizer_chain,
    "keywords": keyword_extractor_chain,
    "sentiment": sentiment_chain
})
```
Here:
- Input text is sent to **all three chains at once**.
- Output is a dictionary with results from each chain.

✅ Best for workflows like **summarize + extract keywords + classify sentiment** simultaneously.

---

## 3. **Conditional (Branching) Chains**
- **Definition**: Execution path depends on a **condition** (like an if-else).
- **Flow**: Input is classified, then routed to the appropriate chain.
- **Use Case**: When different logic is needed based on input type/value.
- **Example** (from your code):
```python
branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt2 | model | parser),
    (lambda x:x.sentiment == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x: "could not find sentiment")
)
```
Here:
- If sentiment = **positive** → run `prompt2`.
- If sentiment = **negative** → run `prompt3`.
- Else → fallback message.

✅ Best for workflows like **routing customer feedback** to different response generators.

---

# 🔹 Comparison Table

| Type          | Execution Style | Dependency | Example Use Case |
|---------------|-----------------|------------|------------------|
| Sequential    | Step-by-step    | Each step depends on previous | Translate → Summarize → Format |
| Parallel      | Simultaneous    | Independent tasks | Summarize + Extract keywords + Classify sentiment |
| Conditional   | Branching logic | Depends on condition | Positive vs Negative feedback responses |

---

# 🔹 Key Takeaway
- Use **Sequential** when tasks build on each other.
- Use **Parallel** when tasks are independent but need to run together.
- Use **Conditional** when input determines which path to follow.

---
Here’s the text extracted from the image you uploaded:

---

## 📋 Chain Types Table

**Chain Name | Description**

1. **LLMChain**  
   Basic chain that calls an LLM with a prompt template.  

2. **SequentialChain**  
   Chains multiple LLM calls in a specific sequence.  

3. **SimpleSequentialChain**  
   A simplified version of SequentialChain for easier use.  

4. **ConversationalRetrievalChain**  
   Handles conversational Q&A with memory and retrieval.  

5. **RetrievalQA**  
   Fetches relevant documents and uses an LLM for question-answering.  

6. **RouterChain**  
   Directs user queries to different chains based on intent.  

7. **MultiPromptChain**  
   Uses different prompts for different user intents dynamically.  

8. **HydeChain (Hypothetical Document Embeddings)**  
   Generates hypothetical answers to improve document retrieval.  

9. **AgentExecutorChain**  
   Orchestrates different tools and actions dynamically using an agent.  

10. **SQLDatabaseChain**  
   Connects to SQL databases and answers natural language queries.  

---