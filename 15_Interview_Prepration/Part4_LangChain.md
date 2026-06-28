# Q) What are LangChain Componenets

## 🧩 Core LangChain Components

![alt text](components.png)

### 1. **Models**
- **LLMs** → Large language models (OpenAI, Azure, Anthropic, etc.).
- **Chat Models** → Conversational variants of LLMs.
- **Embeddings** → Convert text into numerical vectors for similarity search.

---

### 2. **Data Connectors**
- **Document Loaders** → Import data from PDFs, web pages, SQL, APIs, etc.
- **Text Splitters** → Chunk large documents into smaller pieces for embedding.
- **Vector Stores** → Databases for embeddings (Chroma, FAISS, Pinecone, Weaviate).

---

### 3. **Retrievers**
- **VectorStoreRetriever** → Fetches relevant chunks from embeddings.
- **BM25Retriever** → Keyword‑based retrieval.
- **Advanced retrievers** → MultiQuery, ContextualCompression, ParentDocument, TimeWeighted, etc.

👉 These are the backbone of **RAG**.

---

### 4. **Chains**
- **LLMChain** → Simple prompt + LLM.
- **RetrievalQAChain** → Classic RAG pipeline (retriever + LLM).
- **ConversationalRetrievalChain** → RAG with chat history.
- **Custom Chains** → Combine multiple steps (summarization, filtering, etc.).

---

### 5. **Agents**
- **Tools** → External functions/APIs (search, calculator, SQL, calendar).
- **Agent Executors** → Decide which tool to call, in what order.
- **Planning & Memory** → Break tasks into steps, remember context.

👉 This is where **Agentic AI** comes in — RAG can be one tool inside an agent.

---

### 6. **Memory**
- **ConversationBufferMemory** → Stores past dialogue.
- **VectorStoreRetrieverMemory** → Uses embeddings for long‑term recall.
- **Combined Memory** → Mixes short‑term and long‑term memory.

---

### 7. **Evaluation & Monitoring**
- **LangSmith / DeepEval** → Debugging, tracing, and evaluating LLM outputs.
- **Callbacks** → Hook into execution for logging/monitoring.

---

## 📊 Quick Map

| Component | Role | Example |
|-----------|------|---------|
| **Models** | Generate text/embeddings | `OpenAI`, `GoogleGenerativeAIEmbeddings` |
| **Data Connectors** | Load + chunk data | `PyPDFLoader`, `RecursiveTextSplitter` |
| **Vector Stores** | Store embeddings | `Chroma`, `FAISS` |
| **Retrievers** | Fetch relevant docs | `VectorStoreRetriever` |
| **Chains** | Orchestrate steps | `RetrievalQA` |
| **Agents** | Plan + act | `AgentExecutor` with tools |
| **Memory** | Maintain context | `ConversationBufferMemory` |

---

# Q) Models in LangChain
---

In LangChain, **Models** are one of the core building blocks — they’re the engines that actually generate text or embeddings. Let’s break them down clearly:

![alt text](models.png)
---

Language Model

![alt text](Language_Model.png)
## 🧩 Types of Models in LangChain

### 1. **LLMs (Large Language Models)**
- General text generation models.
- Examples: `OpenAI`, `Anthropic`, `Cohere`, `AzureOpenAI`.
- Used for tasks like summarization, Q&A, reasoning, creative writing.

---

### 2. **Chat Models**
- Specialized LLMs designed for conversational interactions.
- Examples: `ChatOpenAI`, `ChatAnthropic`.
- Handle multi‑turn dialogue with structured input/output.

```python
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite')

result = model.invoke('What is the capital of India')

print(result.content)
```
Hugging Face

```python
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Pro",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India")

print(result.content)

```
---

### 3. **Embeddings Models**
- Convert text into numerical vectors for similarity search.
- Examples: `OpenAIEmbeddings`, `GoogleGenerativeAIEmbeddings`, `HuggingFaceEmbeddings`.
- Used in **RAG pipelines** with vector stores (Chroma, FAISS, Pinecone).

```python
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = HuggingFaceEndpointEmbeddings(repo_id='sentence-transformers/all-MiniLM-L6-v2')

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = 'tell me about msdhoni'

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embeddings)[0]

index, score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print("similarity score is:", score)

```
---

### 4. **Other Specialized Models**
- **Text-to-Image / Multimodal** (via integrations, though less common in LangChain core).
- **Function Calling Models** → LLMs that can call tools or APIs.
- **Custom Models** → Wrap any API or local model into LangChain’s `LLM` interface.

---

## 📊 Quick Table

| Model Type | Purpose | Example |
|------------|---------|---------|
| **LLM** | General text generation | `OpenAI`, `Cohere` |
| **Chat Model** | Dialogue, multi‑turn | `ChatOpenAI`, `ChatAnthropic` |
| **Embeddings** | Vector representation for retrieval | `OpenAIEmbeddings`, `FAISS` |
| **Custom/Other** | Specialized tasks | HuggingFace models, local LLMs |

---

## 🎯 Key Insight
- **LLMs** → Generate answers.  
- **Embeddings** → Enable retrieval (RAG).  
- **Chat Models** → Handle conversations.  
- Together, they form the **foundation of LangChain pipelines** — whether you’re building a simple RAG system or a full Agentic AI.

In LangChain, **prompts** are the structured instructions you give to a model — they define *what the model should do* and *how it should respond*. Think of them as the **bridge between your intent and the LLM’s output**.

---

## 🧩 Prompt Components in LangChain

### 1. **PromptTemplate** or **Dynamic & Reusable Prompts**
- A reusable template for prompts with placeholders.  
- Example:  
  ```python
  from langchain.prompts import PromptTemplate

  template = "Translate the following text to French: {text}"
  prompt = PromptTemplate.from_template(template)
  prompt.format(text="Hello, how are you?")
  ```
- Output: `"Translate the following text to French: Hello, how are you?"`

---

### 2. **ChatPromptTemplate** / **Role Based Prompts**
- Designed for **multi‑turn conversations**.  
- Lets you structure prompts as a sequence of messages (system, human, AI).  
- Example:  
  ```python
  from langchain.prompts import ChatPromptTemplate

  chat_prompt = ChatPromptTemplate.from_messages([
      ("system", "You are a helpful assistant."),
      ("human", "Summarize this text: {text}")
  ])
  ```
- Output: A structured chat prompt ready for a chat model.

---

### 3. **Few‑Shot Prompting**
- You can embed **examples** in the prompt to guide the model.  
- Example:  
  ```python
  from langchain.prompts import FewShotPromptTemplate

  examples = [
      {"word": "happy", "antonym": "sad"},
      {"word": "tall", "antonym": "short"},
  ]

  example_prompt = PromptTemplate(
      input_variables=["word", "antonym"],
      template="Word: {word}, Antonym: {antonym}"
  )

  few_shot_prompt = FewShotPromptTemplate(
      examples=examples,
      example_prompt=example_prompt,
      prefix="Give antonyms for the following words.",
      suffix="Word: {input}, Antonym:",
      input_variables=["input"]
  )
  ```
- This teaches the model by showing patterns.

---

### 4. **Output Parsers**
- Define how the model’s response should be structured (JSON, list, etc.).  
- Example: `StructuredOutputParser` ensures the model outputs valid JSON.

---

## 📊 Summary Table

| Prompt Type | Purpose | Example Use |
|-------------|---------|-------------|
| **PromptTemplate** | Single‑shot template | Translation, summarization |
| **ChatPromptTemplate** | Multi‑turn dialogue | Chatbots, assistants |
| **FewShotPromptTemplate** | Guide with examples | Classification, Q&A |
| **Output Parsers** | Control response format | JSON, tables, lists |

---

## 🎯 Key Insight
- Prompts in LangChain aren’t just text — they’re **structured, reusable, and composable**.  
- They let you **control the behavior of LLMs** in RAG pipelines or Agentic AI workflows.  

---

# 🧩 Types of Chains in LangChain
---

## 1. 🔹 **LLMChain**
Simplest chain: prompt + LLM.

```python
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI

prompt = PromptTemplate.from_template("Translate this text to French: {text}")
llm = OpenAI()
chain = LLMChain(llm=llm, prompt=prompt)

result = chain.run(text="Hello, how are you?")
print(result)  # → "Bonjour, comment ça va?"
```

---

## 2. 🔹 **SequentialChain**
Runs multiple chains one after another.

```python
from langchain.chains import SequentialChain

# Chain 1: Summarize
summarize_prompt = PromptTemplate.from_template("Summarize: {text}")
summarize_chain = LLMChain(llm=OpenAI(), prompt=summarize_prompt)

# Chain 2: Translate
translate_prompt = PromptTemplate.from_template("Translate to Spanish: {summary}")
translate_chain = LLMChain(llm=OpenAI(), prompt=translate_prompt)

# Sequential pipeline
overall_chain = SequentialChain(
    chains=[summarize_chain, translate_chain],
    input_variables=["text"],
    output_variables=["summary", "translation"]
)

result = overall_chain.run(text="LangChain helps build LLM-powered apps.")
print(result["translation"])
```

---

## 3.🔹 ParallelChain Overview
- **SequentialChain** → runs one chain after another (step‑by‑step).  
- **ParallelChain** → runs multiple chains simultaneously (side‑by‑side).  
- **Use case:** When you want multiple independent outputs from the same input, without waiting for one to finish before starting the next.

---

## 🧩 Example: ParallelChain

```python
from langchain.chains import LLMChain, ParallelChain
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI

llm = OpenAI()

# Chain 1: Summarize
summarize_prompt = PromptTemplate.from_template("Summarize this text: {text}")
summarize_chain = LLMChain(llm=llm, prompt=summarize_prompt)

# Chain 2: Translate
translate_prompt = PromptTemplate.from_template("Translate this text to Spanish: {text}")
translate_chain = LLMChain(llm=llm, prompt=translate_prompt)

# Run both chains in parallel
parallel_chain = ParallelChain(
    chains={
        "summary": summarize_chain,
        "translation": translate_chain
    }
)

result = parallel_chain.run(text="LangChain helps build LLM-powered applications.")
print(result["summary"])      # → "LangChain builds apps with LLMs."
print(result["translation"])  # → "LangChain ayuda a crear aplicaciones con LLMs."
```

Hands-On Exmaple

```python
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, EmailStr, Field
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.runnables import RunnableParallel

load_dotenv()

#Model 1
model1 = ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite')

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Pro",
    task="text-generation"
)

#Model 2
model2 = ChatHuggingFace(llm=llm)

#Prompts and parser
prompt1 = PromptTemplate(
    template='Generate short and simple notes from the following text \n {text}',
    input_variables=['text']
)

# quiz generation prompt
prompt2 = PromptTemplate(
    template='Generate 5 short question answers from the following text \n {text}',
    input_variables=['text']
)

# merge prompt
prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}',
    input_variables=['notes', 'quiz']
)

parser = StrOutputParser()

# parallel chain
parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

# Merge chain
merge_chain = prompt3 | model1 | parser

# Final chain
chain = parallel_chain | merge_chain

text = """
Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.

The advantages of support vector machines are:

Effective in high dimensional spaces.

Still effective in cases where number of dimensions is greater than the number of samples.

Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.

Versatile: different Kernel functions can be specified for the decision function. Common kernels are provided, but it is also possible to specify custom kernels.

The disadvantages of support vector machines include:

If the number of features is much greater than the number of samples, avoid over-fitting in choosing Kernel functions and regularization term is crucial.

SVMs do not directly provide probability estimates, these are calculated using an expensive five-fold cross-validation (see Scores and probabilities, below).

The support vector machines in scikit-learn support both dense (numpy.ndarray and convertible to that by numpy.asarray) and sparse (any scipy.sparse) sample vectors as input. However, to use an SVM to make predictions for sparse data, it must have been fit on such data. For optimal performance, use C-ordered numpy.ndarray (dense) or scipy.sparse.csr_matrix (sparse) with dtype=float64.
"""


result = chain.invoke({'text':text})

print(result)

chain.get_graph().print_ascii()

#  +---------------------------+                 
#                    | Parallel<notes,quiz>Input |                 
#                    +---------------------------+                 
#                       ***                 ****                   
#                   ****                        ***                
#                 **                               **              
#     +----------------+                      +----------------+   
#     | PromptTemplate |                      | PromptTemplate |   
#     +----------------+                      +----------------+   
#              *                                        *          
#              *                                        *          
#              *                                        *          
# +------------------------+                  +-----------------+  
# | ChatGoogleGenerativeAI |                  | ChatHuggingFace |  
# +------------------------+                  +-----------------+  
#              *                                        *          
#              *                                        *          
#              *                                        *          
#     +-----------------+                     +-----------------+  
#     | StrOutputParser |                     | StrOutputParser |  
#     +-----------------+                     +-----------------+  
#                       ***                 ****                   
#                          ****          ***                       
#                              **      **                          
#                   +----------------------------+                 
#                   | Parallel<notes,quiz>Output |                 
#                   +----------------------------+                 
#                                  *                               
#                                  *                               
#                                  *                               
#                         +----------------+                       
#                         | PromptTemplate |                       
#                         +----------------+                       
#                                  *                               
#                                  *                               
#                                  *                               
#                     +------------------------+                   
#                     | ChatGoogleGenerativeAI |                   
#                     +------------------------+                   
#                                  *                               
#                                  *                               
#                                  *                               
#                         +-----------------+                      
#                         | StrOutputParser |                      
#                         +-----------------+                      
#                                  *                               
#                                  *                               
#                                  *                               
#                      +-----------------------+                   
#                      | StrOutputParserOutput |                   
#                      +-----------------------+                   

```
---

## 📊 When to Use ParallelChain
- ✅ Multiple independent tasks on the same input (summarize + sentiment analysis + translation).  
- ✅ Speed: avoids waiting for sequential execution.  
- ✅ Aggregating diverse outputs for richer pipelines.  

---

## 🎯 Key Insight
- **SequentialChain** = step‑by‑step pipeline.  
- **ParallelChain** = simultaneous tasks.  
- Both are orchestration tools, but **ParallelChain shines when tasks don’t depend on each other**.

---

## 4. 🔹 **RouterChain** or **Conditional Chain**
- Routes input to different chains depending on conditions.
- Dynamically route input to different chains depending on conditions.
- Example: If input is a math problem → send to calculator chain; if it’s a Q&A → send to RAG chain.

```python
from langchain.chains.router import MultiPromptChain

prompts = {
    "math": PromptTemplate.from_template("Solve this math problem: {input}"),
    "qa": PromptTemplate.from_template("Answer this question: {input}")
}

chain = MultiPromptChain.from_prompts(prompts, default_chain=LLMChain(llm=OpenAI(), prompt=prompts["qa"]))

print(chain.run("2+2"))       # → "4"
print(chain.run("Who is Einstein?"))  # → factual answer
```

```python
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, EmailStr, Field
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.runnables import RunnableParallel
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda
from typing import Literal

load_dotenv()

#Model 1
model = ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite')

parser = StrOutputParser()

class Feedback(BaseModel):

    sentiment: Literal['positive', 'negative'] = Field(description='Give the sentiment of the feedback')

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback text into postive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt2 | model | parser),
    (lambda x:x.sentiment == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x: "could not find sentiment")
)

chain = classifier_chain | branch_chain

print(chain.invoke({'feedback': 'This is a beautiful phone'}))

chain.get_graph().print_ascii()
```

---

## 5. 🔹 **RetrievalQAChain**
Classic **RAG pipeline**.

```python
from langchain.chains import RetrievalQA

qa_chain = RetrievalQA.from_chain_type(
    llm=OpenAI(),
    retriever=vectorstore.as_retriever()
)

result = qa_chain.run("What are LangChain components?")
print(result)
```

---

## 6. 🔹 **ConversationalRetrievalChain**
RAG + chat history (memory).

```python
from langchain.chains import ConversationalRetrievalChain

chat_chain = ConversationalRetrievalChain.from_llm(
    llm=OpenAI(),
    retriever=vectorstore.as_retriever()
)

chat_history = []
query = "Explain LangChain agents."
result = chat_chain({"question": query, "chat_history": chat_history})
print(result["answer"])
```

---

## 🎯 Takeaway
- **LLMChain** → single prompt + LLM.  
- **SequentialChain** → multi‑step pipeline.  
- **RouterChain** → conditional routing.  
- **RetrievalQAChain** → RAG pipeline.  
- **ConversationalRetrievalChain** → RAG + memory for chatbots.  

---

# 🧩 What is Runnables

Runnables are the new unified abstraction that power chains, agents, and pipelines. Instead of having separate classes for everything, LangChain now treats most components as Runnables — meaning they can be executed, composed, and connected in flexible ways.

### 🧩 Runnables Types

Got it — let’s go through **each type of Runnable in LangChain with concrete examples** so you can see how they work in practice.  

---

## 1. 🔹 **RunnableSequence**
Runs tasks **step by step** (like a pipeline).

```python
from langchain.schema import RunnableSequence
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI

llm = OpenAI()

# Step 1: Summarize
summarize_prompt = PromptTemplate.from_template("Summarize: {text}")
summarize = summarize_prompt | llm

# Step 2: Translate
translate_prompt = PromptTemplate.from_template("Translate to Spanish: {summary}")
translate = translate_prompt | llm

# Sequence pipeline
sequence = RunnableSequence(first=summarize, last=translate)

result = sequence.invoke({"text": "LangChain helps build LLM-powered applications."})
print(result)
```

---

## 2. 🔹 **RunnableParallel**
Runs tasks **simultaneously** and returns a dictionary of outputs.

```python
from langchain.schema import RunnableParallel

llm = OpenAI()

summarize_prompt = PromptTemplate.from_template("Summarize: {text}")
translate_prompt = PromptTemplate.from_template("Translate to Spanish: {text}")

parallel = RunnableParallel({
    "summary": summarize_prompt | llm,
    "translation": translate_prompt | llm
})

result = parallel.invoke({"text": "LangChain helps build LLM-powered applications."})
print(result["summary"])
print(result["translation"])
```
Hand-On Exmaple

```python
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, EmailStr, Field
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.runnables import RunnableBranch, RunnableParallel, RunnablePassthrough, RunnableSequence

load_dotenv()

#Model
model = ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite')

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Generate a tweet about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a Linkedin post about {topic}',
    input_variables=['topic']
)

parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1, model, parser),
    'linkedin': RunnableSequence(prompt2, model, parser)
})

result = parallel_chain.invoke({'topic':'AI'})

print(result['tweet'])
print(result['linkedin'])

```
---

## 3. 🔹 **RunnableBranch**
Routes input to different pipelines depending on conditions.

- RunnableBranchis a control flow componentin LangChain that allows you to conditionally route input data to different chains or runnablesbased on custom logic.
- It functions like an if/elif/elseblock for chains —where you define a set of condition functions, each associated with a runnable (e.g., LLM call, prompt chain, or tool). The first matching condition is executed.
- If no condition matches ,a default runnable is used (if provided)

```python
from langchain.schema import RunnableBranch

llm = OpenAI()

math_prompt = PromptTemplate.from_template("Solve: {input}") | llm
qa_prompt = PromptTemplate.from_template("Answer: {input}") | llm

branch = RunnableBranch(
    branches=[
        (lambda x: x["input"].isdigit(), math_prompt),
        (lambda x: True, qa_prompt)  # default
    ]
)

print(branch.invoke({"input": "2+2"}))       # → "4"
print(branch.invoke({"input": "Who is Einstein?"}))  # → factual answer
```

- It’s a **conditional pipeline**: you define multiple branches, each with a condition and a runnable.  
- When invoked, the input is tested against each condition in order.  
- The first condition that evaluates to `True` determines which runnable executes.  
- If none match, you can set a **default branch**.

Think of it like an **if/elif/else** statement, but inside LangChain’s runnable ecosystem.

---

## 🧩 Example 2: Sentiment Routing
```python
from langchain.schema import RunnableBranch, RunnableLambda

llm = OpenAI()

positive_chain = PromptTemplate.from_template("Write a happy poem about: {input}") | llm
negative_chain = PromptTemplate.from_template("Write a motivational message for: {input}") | llm

branch = RunnableBranch(
    branches=[
        (lambda x: "good" in x["input"].lower(), positive_chain),
        (lambda x: "bad" in x["input"].lower(), negative_chain),
        (lambda x: True, llm)  # fallback
    ]
)

print(branch.invoke({"input": "I had a good day"}))  
print(branch.invoke({"input": "I had a bad day"}))  
```

---

## 📊 When to Use `RunnableBranch`
- ✅ **Routing tasks** → Different prompts/models depending on input type.  
- ✅ **Multi‑modal workflows** → Text vs image vs structured data.  
- ✅ **Fallback logic** → Default runnable if no condition matches.  

---

## 🎯 Key Insight
- `RunnableBranch` = **conditional routing** in LangChain pipelines.  
- It’s the equivalent of an **if/else decision tree**, but integrated with LLMs, retrievers, and other runnables.  
- This makes it powerful for building **adaptive workflows** where the system decides how to process input dynamically.

---

## 4. 🔹 **RunnableLambda**
Wraps a Python function as a runnable.

```python
from langchain.schema import RunnableLambda

def clean_text(x):
    return x["text"].lower()

clean_runnable = RunnableLambda(clean_text)

print(clean_runnable.invoke({"text": "HELLO WORLD"}))  # → "hello world"
```

In LangChain, **`RunnableLambda`** is a way to wrap a **custom Python function** into the runnable ecosystem. It lets you insert your own logic into a pipeline — so you can preprocess inputs, transform outputs, or add custom steps alongside LLMs, retrievers, and other components.

---

## 🔹 What `RunnableLambda` Does
- Takes a Python function (`lambda` or normal function).  
- Expects the function to accept a dictionary (the input) and return a value.  
- Can be composed with other runnables using the `|` operator.  
- Useful for **custom transformations** like cleaning text, formatting JSON, or applying business rules.

---

## 🧩 Example 1: Simple Transformation
```python
from langchain.schema import RunnableLambda

# Define a custom function
def clean_text(x):
    return {"cleaned": x["text"].lower()}

# Wrap it as a runnable
clean_runnable = RunnableLambda(clean_text)

result = clean_runnable.invoke({"text": "HELLO WORLD"})
print(result)  # → {"cleaned": "hello world"}
```

---

## 🧩 Example 2: Combine with LLM
```python
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI

llm = OpenAI()

# Custom preprocessing step
preprocess = RunnableLambda(lambda x: {"text": x["text"].strip()})

# Prompt + LLM
prompt = PromptTemplate.from_template("Translate to French: {text}")
translation = prompt | llm

# Pipeline: preprocess → translate
pipeline = preprocess | translation

result = pipeline.invoke({"text": "   Hello, how are you?   "})
print(result)  # → "Bonjour, comment ça va?"
```

Hand-On Example

```python
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, EmailStr, Field
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.runnables import RunnableBranch, RunnableLambda, RunnableParallel, RunnablePassthrough, RunnableSequence

load_dotenv()

#Model
model = ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite')

parser = StrOutputParser()

def word_count(text):
    return len(text.split())

prompt = PromptTemplate(
    template='Write in detail about {topic}',
    input_variables=['topic']
)

joke_gen_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count': RunnableLambda(word_count)
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({'topic':'RunnableLambda langchain'})

final_result = """{} \n word count - {}""".format(result['joke'], result['word_count'])

print(final_result)
# ### Summary
# `RunnableLambda` is the "glue" of LangChain. It allows you to bridge the gap between structured AI components (models/retrievers) and your custom Python logic, turning your code into a first-class citizen within the LangChain ecosystem. 
#  word count - 603
```
---

## 🧩 Example 3: Post‑processing
```python
# Add a post-processing step
postprocess = RunnableLambda(lambda x: {"length": len(x)})

pipeline = translation | postprocess

result = pipeline.invoke({"text": "Hello world"})
print(result)  # → {"length": 23}  (length of translated string)
```

---

## 📊 When to Use `RunnableLambda`
- ✅ Preprocessing inputs (cleaning, normalizing, formatting).  
- ✅ Postprocessing outputs (extracting values, enforcing structure).  
- ✅ Injecting custom logic into a chain without writing a new class.  

---

## 🎯 Key Insight
`RunnableLambda` is the **glue** that lets you mix your own Python logic with LangChain’s built‑in components. It’s lightweight, flexible, and perfect for tailoring pipelines to your exact needs.

---

## 5. 🔹 **RunnableMap**
Applies the same runnable to multiple inputs.

```python
from langchain.schema import RunnableMap

llm = OpenAI()
summarize_prompt = PromptTemplate.from_template("Summarize: {doc}") | llm

map_runnable = RunnableMap({"summary": summarize_prompt})

docs = [{"doc": "LangChain helps build LLM-powered apps."},
        {"doc": "RAG improves factual accuracy."}]

results = [map_runnable.invoke(doc) for doc in docs]
print(results)
```

---

## 🔹 RunnableMap in LangChain
- Think of it as a **fan‑out operator**: it applies one or more runnables to the input(s) and returns a dictionary of results.  
- Each key in the map corresponds to a runnable.  
- It’s great for **multi‑tasking** (run different tasks on the same input) or **batching** (apply the same task to multiple inputs).

---

## 🧩 Example 1: Multi‑Tasking on Same Input
```python
from langchain.schema import RunnableMap
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI

llm = OpenAI()

# Define tasks
summarize_prompt = PromptTemplate.from_template("Summarize: {text}") | llm
translate_prompt = PromptTemplate.from_template("Translate to Spanish: {text}") | llm

# Map both tasks
map_runnable = RunnableMap({
    "summary": summarize_prompt,
    "translation": translate_prompt
})

result = map_runnable.invoke({"text": "LangChain helps build LLM-powered applications."})
print(result["summary"])      # → "LangChain builds apps with LLMs."
print(result["translation"])  # → "LangChain ayuda a crear aplicaciones con LLMs."
```

---

## 🧩 Example 2: Batch Processing Multiple Docs
```python
from langchain.schema import RunnableMap

llm = OpenAI()
summarize_prompt = PromptTemplate.from_template("Summarize: {doc}") | llm

# Map summarization
map_runnable = RunnableMap({"summary": summarize_prompt})

docs = [
    {"doc": "LangChain helps build LLM-powered applications."},
    {"doc": "RAG improves factual accuracy in AI systems."}
]

results = [map_runnable.invoke(doc) for doc in docs]
print(results)
# → [{'summary': 'LangChain builds apps with LLMs.'}, 
#    {'summary': 'RAG makes AI answers more accurate.'}]
```

---

## 📊 When to Use RunnableMap
- ✅ **Multi‑tasking** → Run multiple independent tasks on the same input.  
- ✅ **Batching** → Apply the same task to a list of inputs.  
- ✅ **Parallel pipelines** → Collect diverse outputs at once.  

---

## 🎯 Key Insight
- `RunnableMap` is like saying: *“Take this input, run it through multiple tasks, and give me all the results together.”*  
- It complements `RunnableSequence` (step‑by‑step) and `RunnableParallel` (side‑by‑side) by focusing on **mapping tasks to keys or inputs**.

---

## 🧩 RunnableParallel
👉 **One input → many tasks at the same time.**

**Example:**  
You give me **one sentence**:  
`"LangChain helps build LLM-powered apps."`

- Task 1: Summarize it.  
- Task 2: Translate it.  
- Task 3: Check sentiment.  

All three tasks run **side‑by‑side** on the **same sentence**.  
Result:  
```json
{
  "summary": "LangChain builds apps with LLMs.",
  "translation": "LangChain ayuda a crear aplicaciones con LLMs.",
  "sentiment": "Positive"
}
```

---

## 🧩 RunnableMap
👉 **Many inputs → each gets processed by the same task(s).**

**Example:**  
You give me **two sentences**:  
1. `"LangChain helps build LLM-powered apps."`  
2. `"RAG improves factual accuracy."`

- Task: Summarize each sentence.  

Result:  
```json
[
  {"summary": "LangChain builds apps with LLMs."},
  {"summary": "RAG makes AI answers more accurate."}
]
```

---

## 📊 Quick Analogy
- **Parallel** = One essay, three reviewers working at the same time (different tasks on the same essay).  
- **Map** = A stack of essays, one reviewer summarizes each essay (same task applied to multiple inputs).  

---

## 🎯 Takeaway
- Use **Parallel** when you want **different tasks on one input**.  
- Use **Map** when you want to **apply tasks across multiple inputs**.  

---

## 6. 🔹 **RunnablePassthrough**
Passes input through unchanged (useful for debugging or merging).

```python
from langchain.schema import RunnablePassthrough

passthrough = RunnablePassthrough()
print(passthrough.invoke({"text": "Keep this as is"}))
# → {"text": "Keep this as is"}
```
In LangChain, **`RunnablePassthrough`** is the simplest runnable — it just **returns whatever input you give it, unchanged**. Think of it as a “do nothing” step in a pipeline. It’s mainly useful for debugging, merging raw inputs with processed outputs, or when you want to keep the original data alongside transformed results.

---

## 🔹 How `RunnablePassthrough` Works
- **Input → Output** (no modification).  
- Often combined with other runnables to preserve the original input while also generating something new.  
- Helpful when you want both the **raw input** and the **LLM output** in the same result.

---

## 🧩 Example

```python
from langchain.schema import RunnablePassthrough
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain.schema import RunnableParallel

llm = OpenAI()

# Create a summarization runnable
summarize_prompt = PromptTemplate.from_template("Summarize: {text}")
summarize = summarize_prompt | llm

# Passthrough keeps the original input
passthrough = RunnablePassthrough()

# Run both in parallel
parallel = RunnableParallel({
    "original": passthrough,
    "summary": summarize
})

result = parallel.invoke({"text": "LangChain helps build LLM-powered applications."})
print(result["original"])   # → {"text": "LangChain helps build LLM-powered applications."}
print(result["summary"])    # → "LangChain builds apps with LLMs."
```

---

## 📊 When to Use
- ✅ **Debugging** → See both raw input and processed output.  
- ✅ **Merging** → Keep original data alongside transformations.  
- ✅ **Pipelines** → Pass through values unchanged while other runnables act on them.  

---

## 🎯 Key Insight
`RunnablePassthrough` is like a transparent pipe — it doesn’t alter the data but ensures you can **carry the original input forward** in complex workflows.  

---

## 📊 Summary

| Runnable Type       | Purpose | Example |
|---------------------|---------|---------|
| **Sequence**        | Step‑by‑step pipeline | Summarize → Translate |
| **Parallel**        | Run tasks simultaneously | Summary + Translation |
| **Branch**          | Conditional routing | Math vs Q&A |
| **Lambda**          | Custom Python function | Clean text |
| **Map**             | Apply to multiple inputs | Summarize docs list |
| **Passthrough**     | Keep input unchanged | Debugging |

---

## 🎯 Key Insight
- **Runnables unify chains, agents, and pipelines.**  
- You can compose them like Lego blocks: **Sequence for workflows, Parallel for multi‑outputs, Branch for routing, Lambda for custom logic, Map for batch processing, Passthrough for debugging.**

---
