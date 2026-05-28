# langchain_tutorial

1) python -m venv venv
2) venv\scripts\Activate
3) pip install -r requirements.txt

# Embedding HF API

# Temperature

Temperature parameter sets the randomness between multiple outputs on invoking the same input, like if the temperature is 0 then on an input the output will always be same no matter how many times we invoke the model, while if temperature is high then on every call it will be random and completely different from the previous response on the same input.

Temperature is not meant to retain the same output. That job is for the "seed" attribute that OpenAI introduced last year I believe. 

Temperature 0 makes LLM obey the prompt strictly meanwhile higher temperature gives LLM more freedom/creativity. 

The reason you're seeing same output at Temperature 0 is because of Cached Tokens. OpenAI skips the calculation and uses cached Tokens to save computation. You can get different results at Temperature 0 by turning off Cache.

Temperature basically make the difference in the probability of the words, if you know that mathematical aspect how a word is chosen next in the output sequence, these models use softmax function for this, and temperature is the denominator for each probability in that function, so a lower temperature makes the high probabilities even higher making it seem like the output is the same, rather it is generated the same because of these higher probabilities becoming even more high making the model choose them over and over again, and with higher temperature it makes the gap between high and low probabilities less making the model choose words which it wouldn't choose in a natural state.

The higher the temperature, rarer tokens get more prone to selection, whereas lower the temperature common tokens get more prone to selection.

# 📘 LangChain Hugging Face Embeddings Example

https://github.com/meraviverma/langchain_tutorial/blob/main/2_ChatModels/chatmodel_hf_api.py

This script demonstrates how to generate **text embeddings** using Hugging Face models through the `langchain-huggingface` integration.  
Embeddings are numerical vector representations of text, enabling tasks like semantic search, clustering, and retrieval-augmented generation (RAG).

---

## 🔑 Key Components

### 1. `dotenv.load_dotenv()`
- Loads environment variables from a `.env` file.
- Required here to securely access your Hugging Face API token (`HUGGINGFACEHUB_API_TOKEN`).
- Prevents hardcoding sensitive credentials in the script.

---

### 2. `HuggingFaceEndpointEmbeddings`
- Imported from `langchain_huggingface`.
- Provides an interface to Hugging Face’s **Inference API** for embedding models.
- Replaces the deprecated `HuggingFaceHubEmbeddings`.
- Usage:
  ```python
  from langchain_huggingface import HuggingFaceEndpointEmbeddings
  embedding = HuggingFaceEndpointEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")
  ```
- Parameter:
  - `model`: Hugging Face model ID (e.g., `"sentence-transformers/all-MiniLM-L6-v2"`).
    - This model produces **384-dimensional embeddings** optimized for sentence similarity.

---

### 3. `embed_documents(documents: List[str])`
- Converts a list of text documents into embeddings.
- Each document is transformed into a dense vector of floats.
- Example:
  ```python
  documents = [
      "Delhi is the capital of India",
      "Kolkata is the capital of West Bengal",
      "Paris is the capital of France"
  ]
  vector = embedding.embed_documents(documents)
  ```
- Output:
  - A list of vectors, one per document.
  - Each vector has 384 dimensions (for MiniLM).

---

### 4. `embed_query(query: str)`
- Converts a single query string into an embedding.
- Useful for comparing queries against stored document embeddings.
- Example:
  ```python
  result = embedding.embed_query("Delhi is the capital of India")
  ```

---

## ⚡ Typical Workflow

1. **Embed documents** → Store vectors in a vector database (e.g., FAISS, Pinecone).
2. **Embed query** → Convert user input into a vector.
3. **Similarity search** → Compare query vector with document vectors using cosine similarity.
4. **Retrieve best match** → Return the most relevant document(s).

---

## 📊 Example: Cosine Similarity

```python
from sklearn.metrics.pairwise import cosine_similarity

query = "Which city is the capital of France?"
query_vector = embedding.embed_query(query)

similarities = cosine_similarity([query_vector], vector)
print(similarities)
```

- Produces similarity scores between the query and each document.
- The highest score corresponds to the most relevant document (`"Paris is the capital of France"`).

---

## ✅ Use Cases
- Semantic search engines
- Question answering systems
- Document clustering
- Recommendation systems
- Retrieval-Augmented Generation (RAG) pipelines

# Embedding Document Similarity
https://github.com/meraviverma/langchain_tutorial/blob/main/3_EmbeddedModels/embedding_document_similarity.py
# 📘 Semantic Search with Hugging Face Embeddings

This script demonstrates how to perform **semantic similarity search** using Hugging Face embeddings in LangChain.  
It embeds both documents and queries into dense vectors, then applies **cosine similarity** to find the closest match.

---

## 🔑 Key Components

### 1. `HuggingFaceEndpointEmbeddings`
- **Source:** `langchain-huggingface` package.
- **Purpose:** Provides access to Hugging Face’s **Inference API** for embedding models.
- **Parameter:**
  - `repo_id`: Hugging Face model ID (e.g., `"sentence-transformers/all-MiniLM-L6-v2"`).
    - This model generates **384-dimensional sentence embeddings** optimized for semantic similarity.
- **Docs:** Hugging Face [Sentence Transformers](https://www.sbert.net/) library powers these embeddings.

---

### 2. `embed_documents(documents: List[str])`
- **Definition:** Converts a list of text strings into embeddings.
- **Return:** A list of vectors (each vector is a list of floats).
- **Usage:**
  ```python
  doc_embeddings = embedding.embed_documents(documents)


### 3. `embed_query(query: str)`
- **Definition:** Converts a single query string into an embedding.
- **Return:** A single vector (list of floats).
- **Usage:**
  ```python
  query_embedding = embedding.embed_query("tell me about msdhoni")
  ```
- **Purpose:** Represent user queries in the same vector space as documents, enabling semantic search.

---

### 4. `cosine_similarity`
- **Source:** `sklearn.metrics.pairwise.cosine_similarity`
- **Definition:** Measures similarity between two sets of vectors by computing the cosine of the angle between them.
- **Formula:**
  \[
  \text{cosine similarity}(A, B) = \frac{A \cdot B}{||A|| \cdot ||B||}
  \]
- **Return:** A similarity score between -1 and 1.
- **Usage:**
  ```python
  scores = cosine_similarity([query_embedding], doc_embeddings)[0]
  ```
- **Purpose:** Identify which document is closest in meaning to the query.
- **Docs:** scikit-learn cosine_similarity [(scikit-learn.org in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fscikit-learn.org%2Fstable%2Fmodules%2Fgenerated%2Fsklearn.metrics.pairwise.cosine_similarity.html")

---

## ⚡ Workflow in This Script

1. **Embed documents** → Each cricket player description becomes a vector.
2. **Embed query** → `"tell me about msdhoni"` becomes a vector.
3. **Cosine similarity** → Compare query vector with all document vectors.
4. **Retrieve best match** → Highest similarity score corresponds to the MS Dhoni document.

---

## 📊 Example Output

```
Query: tell me about msdhoni
Best Match: MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.
Similarity Score: 0.89
```

---

## ✅ Use Cases
- Semantic search engines
- Question answering systems
- Document clustering
- Recommendation systems
- Retrieval-Augmented Generation (RAG) pipelines

---

# Prompts

Prompts are the input instruction or queries given to model to guide its output

Stremlit

streamlit run prompts_ui.py 

Here’s a clean, well‑structured **Markdown documentation** for your code. It explains the logic, methods, and functions so you (or anyone else) can refer back later.

---

# 📘 Research Tool with LangChain + Streamlit + Google Gemini

https://github.com/meraviverma/langchain_tutorial/blob/main/4_Prompts/prompts_ui_dynamic.py

## 🔹 Code

```python
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

# Load environment variables (e.g., API keys)
load_dotenv()

# Initialize Gemini model via LangChain wrapper
# model = ChatOpenAI()   # Example if using OpenAI
model = ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite')

# Streamlit UI
st.header('Research Tool')

# Input field for user prompt
user_input = st.text_input("Enter your prompt here")

# Submit button triggers model invocation
if st.button('Submit'):
    result = model.invoke(user_input)
    st.write(result.content)
```

---

## 🔹 Explanation of Components

### 1. **Imports**
- `ChatGoogleGenerativeAI`  
  - LangChain wrapper for Google Gemini models.  
  - Provides `.invoke()` method to send prompts and receive responses.

- `load_dotenv` (from `dotenv`)  
  - Loads environment variables from a `.env` file.  
  - Useful for securely storing API keys (`GOOGLE_API_KEY`).

- `streamlit as st`  
  - Streamlit library for building interactive web apps.  
  - Provides UI elements like `st.header`, `st.text_input`, `st.button`, `st.write`.

- `PromptTemplate`, `load_prompt` (from `langchain_core.prompts`)  
  - Tools for creating structured prompts.  
  - Not directly used in this snippet, but helpful for reusable/custom prompt design.

---

### 2. **Environment Setup**
```python
load_dotenv()
```
- Loads `.env` file variables into the environment.  
- Example `.env` file:
  ```
  GOOGLE_API_KEY=your_api_key_here
  ```

---

### 3. **Model Initialization**
```python
model = ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite')
```
- Creates a Gemini model instance.  
- `gemini-3.1-flash-lite` → lightweight, fast inference model.  
- Alternative: `ChatOpenAI()` for OpenAI models.

---

### 4. **Streamlit UI**
```python
st.header('Research Tool')
```
- Displays a header at the top of the app.

```python
user_input = st.text_input("Enter your prompt here")
```
- Creates a text input box for user queries.

```python
if st.button('Submit'):
    result = model.invoke(user_input)
    st.write(result.content)
```
- **Button**: Executes only when clicked.  
- **`model.invoke(user_input)`**: Sends the user’s text to Gemini model.  
- **`result.content`**: Extracts the model’s response.  
- **`st.write()`**: Displays the output in the app.

---

## 🔹 Methods & Functions Used

| Function / Method | Library | Purpose |
|-------------------|---------|---------|
| `load_dotenv()` | `dotenv` | Loads environment variables (API keys, secrets). |
| `ChatGoogleGenerativeAI()` | `langchain_google_genai` | Initializes Gemini model wrapper. |
| `.invoke(prompt)` | LangChain | Sends prompt to model and returns response object. |
| `st.header()` | Streamlit | Adds a header to the app UI. |
| `st.text_input()` | Streamlit | Creates an input box for user text. |
| `st.button()` | Streamlit | Adds a clickable button to trigger actions. |
| `st.write()` | Streamlit | Displays text, data, or objects in the app. |

---

## 🔹 Workflow Summary
1. Load environment variables (API key).  
2. Initialize Gemini model via LangChain.  
3. Build Streamlit UI with input + button.  
4. On button click → send user input to Gemini.  
5. Display model’s response in the app.

---

# 📝 Prompt Template (LangChain)

## 🔹 What is a PromptTemplate?

A **PromptTemplate** in LangChain is a structured way to create prompts dynamically by inserting variables into a predefined template.

- Unlike hardcoded prompts, PromptTemplate allows defining **placeholders** that can be filled at runtime with different inputs.  
- This makes prompts **reusable, flexible, and easy to manage**, especially when working with dynamic user inputs or automated workflows.

---

## 🔹 Why use PromptTemplate over `f-strings`?

1. **Default validation** – Ensures placeholders are correctly filled.  
2. **Reusable** – Templates can be applied across multiple tasks without rewriting.  
3. **LangChain Ecosystem** – Seamlessly integrates with LangChain’s tools and workflows.

---

## 🔹 Key Benefits

- ✅ **Dynamic input handling**  
- ✅ **Cleaner code management**  
- ✅ **Scalable for complex workflows**  

---

# 📘 Research Tool – Detailed Explanation

## 🔹 Purpose
This Streamlit app integrates **LangChain** with **Google Gemini** to create a research assistant.  
It allows users to:
- Select a **research paper** from a predefined list.  
- Choose an **explanation style** (e.g., beginner-friendly, technical).  
- Decide on the **length of explanation** (short, medium, long).  
- Generate a structured summary using a **prompt template**.

---

## 🔹 Key Components

### 1. **Environment Setup**
- **`load_dotenv()`**  
  Loads environment variables (like API keys) from a `.env` file.  
  This keeps sensitive credentials secure and separate from the code.

---

### 2. **Model Initialization**
- **`ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite')`**  
  Initializes the Gemini model via LangChain.  
  - `gemini-3.1-flash-lite` → lightweight, fast inference model.  
  - Provides `.invoke()` method to send structured prompts and receive responses.

---

### 3. **Streamlit UI Elements**
- **`st.header()`** → Displays the app title.  
- **`st.selectbox()`** → Dropdown menus for user input:
  - **Research Paper Name** → Predefined list of famous papers (e.g., *Attention Is All You Need*).  
  - **Explanation Style** → Options like beginner-friendly, technical, code-oriented, mathematical.  
  - **Explanation Length** → Short, medium, or long summaries.

- **`st.button('Summarize')`** → Executes the summarization workflow when clicked.  
- **`st.write()`** → Displays the generated explanation in the app.

---

### 4. **Prompt Template**
- **`load_prompt('template.json')`**  
  Loads a reusable JSON prompt template.  
  - Templates define placeholders (`paper_input`, `style_input`, `length_input`).  
  - At runtime, these placeholders are filled with user selections.  
  - Ensures **validation, reusability, and integration** with LangChain ecosystem.

---

### 5. **Execution Flow**
1. User selects paper, style, and length.  
2. Button click triggers the chain:  
   - `template | model` → Combines structured prompt with Gemini model.  
3. `.invoke()` sends the filled template to Gemini.  
4. Model generates explanation tailored to user’s choices.  
5. Output is displayed in the Streamlit app.

---

## 🔹 Definitions & Usage

| Concept | Definition | Usage in Code |
|---------|------------|---------------|
| **Environment Variables** | Secure storage for API keys and secrets. | Loaded via `load_dotenv()`. |
| **LangChain Model Wrapper** | Abstraction layer for AI models. | `ChatGoogleGenerativeAI` wraps Gemini. |
| **Prompt Template** | Structured prompt with placeholders. | Loaded from `template.json` and filled dynamically. |
| **Chain (`template | model`)** | Pipeline combining prompt + model. | Ensures structured input before sending to Gemini. |
| **Streamlit UI** | Interactive web interface. | Dropdowns, buttons, and output display. |

---

Perfect — let’s focus on explaining the **chain** concept in detail, since that’s central to how your code works. I’ll remove the Edge browser metadata and give you a clear, structured Markdown reference.

---

# 🔗 Understanding Chains in LangChain

## 🔹 What is a Chain?
A **Chain** in LangChain is a pipeline that connects multiple components together — typically **prompts** and **models** — so that data flows seamlessly from one step to the next.

Instead of manually formatting prompts and passing them to the model, a chain lets you:
- Define a **prompt template** with placeholders.
- Fill those placeholders dynamically with user input.
- Send the structured prompt to the model.
- Get back a response in a single, streamlined call.

---

## 🔹 How Chains Work in Your Code
In your script, the chain is created like this:

```python
chain = template | model
```

This means:
1. **`template`** → A `PromptTemplate` loaded from `template.json`.  
   - Contains placeholders: `paper_input`, `style_input`, `length_input`.  
   - Ensures inputs are validated and structured before reaching the model.

2. **`| model`** → The Gemini model (`ChatGoogleGenerativeAI`).  
   - Receives the filled prompt.  
   - Generates the explanation based on paper, style, and length.

3. **Execution** →  
   ```python
   result = chain.invoke({
       'paper_input': paper_input,
       'style_input': style_input,
       'length_input': length_input
   })
   ```
   - User selections are passed into the chain.  
   - The chain fills the template and sends it to Gemini.  
   - The model returns a response, which is displayed in Streamlit.

---

## 🔹 Why Use Chains?
Chains provide several advantages over manually coding prompt + model calls:

- **Validation** → Ensures required inputs are provided.  
- **Reusability** → Templates can be reused across different tasks.  
- **Flexibility** → Easy to swap models or prompts without rewriting logic.  
- **Integration** → Fits naturally into LangChain’s ecosystem (agents, tools, workflows).  
- **Cleaner Code** → Reduces boilerplate and keeps logic modular.

---

## 🔹 Example Workflow (Conceptual)
1. User selects:
   - Paper → *“Attention Is All You Need”*  
   - Style → *“Beginner-Friendly”*  
   - Length → *“Medium”*  

2. Chain fills the template:
   ```
   Summarize the paper "Attention Is All You Need"
   in a Beginner-Friendly style,
   with a Medium length explanation.
   ```

3. Model processes the structured prompt.  
4. Output is returned and displayed in the app.

---

## 🔹 Key Takeaway
Think of a **chain** as a **bridge**:
- On one side → user inputs (paper, style, length).  
- On the other side → model output (summary).  
- The chain ensures the inputs are correctly formatted and validated before reaching the model, making the workflow **robust, reusable, and scalable**.

---

---

# 📝 Prompts in LangChain

## 🔹 What is a Prompt?
A **prompt** is the input you give to a language model.  
It defines *what* the model should do — for example, summarize a paper, explain a concept, or generate code.

In LangChain, prompts are often managed using **PromptTemplate**, which allows you to structure prompts with placeholders that can be filled at runtime.

---

## 🔹 Static Prompt
A **static prompt** is hardcoded — it never changes unless you manually edit the code.

### Example
```python
prompt = "Summarize the paper Attention Is All You Need in a beginner-friendly style."
```

- **Characteristics:**
  - Fixed wording.
  - No flexibility for different inputs.
  - Good for quick tests or one-off tasks.

- **Limitations:**
  - Cannot adapt to user input.
  - Requires rewriting code for every new variation.

---

## 🔹 Dynamic Prompt
A **dynamic prompt** uses placeholders that are filled with values at runtime.  
This makes prompts flexible, reusable, and adaptable to different contexts.

### Example with PromptTemplate
```python
from langchain_core.prompts import PromptTemplate

template = PromptTemplate.from_template(
    "Summarize the paper {paper_input} in a {style_input} style with {length_input} length."
)
```

- **Characteristics:**
  - Placeholders (`{paper_input}`, `{style_input}`, `{length_input}`) are replaced with user selections.
  - Works seamlessly with LangChain chains.
  - Enables validation and integration with workflows.

- **Advantages:**
  - Reusable across multiple tasks.
  - Easy to adapt to different user inputs.
  - Cleaner and more scalable code.

---

## 🔹 Static vs Dynamic Prompt Comparison

| Aspect | Static Prompt | Dynamic Prompt |
|--------|---------------|----------------|
| **Flexibility** | Fixed, hardcoded | Adaptable with placeholders |
| **Reusability** | Low | High |
| **User Input** | Not supported | Supported |
| **Best Use Case** | Quick tests, prototypes | Production apps, interactive tools |

---

## 🔹 Why Dynamic Prompts Matter in Your Code
In your **Research Tool app**:
- You let users select:
  - Paper name  
  - Explanation style  
  - Explanation length  
- These values are injected into the **PromptTemplate** dynamically.  
- The chain (`template | model`) ensures the prompt is correctly structured before sending it to Gemini.

This makes your app:
- **Interactive** → Users control the output style and length.  
- **Reusable** → Same template works for multiple papers.  
- **Scalable** → Easy to add new papers, styles, or lengths without rewriting logic.

---

✅ **Key Takeaway:**  
- **Static prompts** are simple but rigid.  
- **Dynamic prompts** (via PromptTemplate) are powerful, reusable, and essential for building interactive AI applications like your research tool.

---

# 💬 Understanding Chat Chains with History

---

## 🔹 Purpose of the Script
This program builds a **command-line chatbot** using:
- **LangChain’s message objects** (`SystemMessage`, `HumanMessage`, `AIMessage`)  
- **Google Gemini model** (`ChatGoogleGenerativeAI`)  
- A simple **loop** to maintain conversation history  

It allows you to chat with the AI, keep track of past exchanges, and exit when you type `"exit"`.

---

## 🔹 Key Components

### 1. **SystemMessage**
- Sets the initial context for the model.  
- Example: `"You are a helpful AI assistant"`.  
- This acts like a permanent instruction guiding the AI’s behavior throughout the session.

---

### 2. **HumanMessage**
- Represents user input.  
- Every time you type something, it’s wrapped in a `HumanMessage` object and added to `chat_history`.

---

### 3. **AIMessage**
- Represents the AI’s response.  
- After the model generates output, it’s stored as an `AIMessage` in `chat_history`.

---

### 4. **Chat History**
- A list that stores all messages (`SystemMessage`, `HumanMessage`, `AIMessage`).  
- Passed to the model each time so it has **full context** of the conversation.  
- This is what makes the chatbot **stateful** — it remembers what was said earlier.

---

### 5. **Loop Logic**
- **`while True`** → Keeps the chatbot running until you type `"exit"`.  
- Each cycle:
  1. User enters input.  
  2. Input is added to `chat_history`.  
  3. Model is invoked with the entire history.  
  4. AI response is appended to `chat_history`.  
  5. Response is printed.  
- When `"exit"` is typed, the loop breaks and prints the full conversation history.

---

## 🔹 Why Use This Approach?

- **Context Retention** → The model sees the entire conversation, not just the latest message.  
- **Structured Messages** → Using `SystemMessage`, `HumanMessage`, and `AIMessage` makes the dialogue explicit and organized.  
- **Flexibility** → You can add more system instructions (e.g., “Always answer in JSON”) or preprocess user input before sending.  
- **Debugging** → Printing `chat_history` at the end shows exactly what was exchanged.

---

## 🔹 Example Flow

1. **SystemMessage**: “You are a helpful AI assistant.”  
2. **HumanMessage**: “Explain transformers in simple terms.”  
3. **AIMessage**: “Transformers are models that…”  
4. **HumanMessage**: “Make it more technical.”  
5. **AIMessage**: “Technically, transformers use self-attention…”  

👉 Each step is stored in `chat_history`, so the model knows you first asked for a simple explanation, then requested a technical one.

---

## 🔹 Key Takeaway
This script demonstrates a **basic conversational chain**:
- **SystemMessage** sets the role.  
- **HumanMessage** captures user input.  
- **AIMessage** stores responses.  
- **Chat history** ensures continuity.  
---

# 💬 Messages and Their Types in LLMs

When working with **Large Language Models (LLMs)**, especially in frameworks like **LangChain**, communication is structured using **message objects**. These messages define *who is speaking* and *what role the content plays* in the conversation.  

---

## 🔹 What is a Message?
A **message** is a structured unit of text passed between the user, system, and AI model.  
Instead of just raw strings, messages carry **roles** (system, human, AI) that help the model understand context and maintain conversation history.

---

## 🔹 Types of Messages in LLMs

### 1. **SystemMessage**
- **Definition**: Sets the overall context, rules, or persona for the AI.  
- **Usage**: Acts like an instruction manual for the model.  
- **Example**:  
  - `"You are a helpful AI assistant."`  
  - `"Always answer in JSON format."`  

👉 This message is usually given once at the start and persists throughout the conversation.

---

### 2. **HumanMessage**
- **Definition**: Represents the user’s input.  
- **Usage**: Captures what the user types or asks.  
- **Example**:  
  - `"Explain transformers in simple terms."`  
  - `"Summarize the paper Attention Is All You Need."`  

👉 Every time the user interacts, a new `HumanMessage` is added to the chat history.

---

### 3. **AIMessage**
- **Definition**: Represents the model’s response.  
- **Usage**: Stores the output generated by the LLM.  
- **Example**:  
  - `"Transformers are models that use self-attention..."`  
  - `"Here’s a beginner-friendly summary of GPT-3..."`  

👉 This ensures the conversation history includes both sides of the dialogue.

---

## 🔹 Why Use Structured Messages?
- **Context Retention** → The model sees the entire conversation, not just the latest input.  
- **Role Awareness** → The AI knows which text is instruction, which is user input, and which is its own response.  
- **Flexibility** → You can add multiple system messages (e.g., “Be concise” + “Use bullet points”).  
- **Debugging** → Easy to track who said what in the conversation history.

---

## 🔹 Example Conversation Flow

1. **SystemMessage**: `"You are a helpful AI assistant."`  
2. **HumanMessage**: `"Explain BERT in beginner-friendly terms."`  
3. **AIMessage**: `"BERT is a language model that reads text in both directions..."`  
4. **HumanMessage**: `"Make it more technical."`  
5. **AIMessage**: `"Technically, BERT uses bidirectional transformers with masked language modeling..."`  

👉 Each step is stored in `chat_history`, so the model adapts based on prior exchanges.

---

## 🔹 Key Takeaway
Messages in LLMs are **role-based containers**:
- **SystemMessage** → Instructions / context.  
- **HumanMessage** → User input.  
- **AIMessage** → Model output.  

Together, they form a **conversation chain** that keeps interactions coherent, contextual, and reusable.

---

# 🧩 ChatPromptTemplate and MessagesPlaceholder Explained

https://github.com/meraviverma/langchain_tutorial/blob/main/4_Prompts/message_placeholder.py

Script demonstrates how to build a **structured chat prompt** in LangChain. Let’s break it down carefully so you can use this as a reference.

---

## 🔹 ChatPromptTemplate
- **Definition**: A `ChatPromptTemplate` is a way to define a structured conversation prompt for LLMs.  
- **Usage**: It allows you to specify different roles (`system`, `human`, `ai`) and placeholders for dynamic content.  
- **Benefit**: Keeps prompts organized, reusable, and adaptable to different contexts.

### In your code:
```python
chat_template = ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])
```

- **System role**: Sets the AI’s persona → *“You are a helpful customer support agent.”*  
- **MessagesPlaceholder**: A placeholder for past conversation history.  
- **Human role**: Accepts a dynamic `{query}` from the user.

---

## 🔹 MessagesPlaceholder
- **Definition**: A special placeholder that represents a list of messages (conversation history).  
- **Usage**: Lets you inject previous exchanges (`HumanMessage`, `AIMessage`) into the prompt dynamically.  
- **Benefit**: Ensures the model has context of the entire conversation, not just the latest query.

### In your code:
```python
MessagesPlaceholder(variable_name='chat_history')
```
- This means when you invoke the template, you pass in a list of messages under the key `chat_history`.  
- The template will insert them in the right place before the new query.

---

## 🔹 Chat History
- **Purpose**: Keeps track of all past exchanges.  
- **Implementation**: You load it from a file (`chat_history.txt`) and extend the list.  
- **Benefit**: The AI can respond with awareness of prior context (e.g., refund discussions, previous questions).

---

## 🔹 Prompt Creation
```python
prompt = chat_template.invoke({'chat_history': chat_history, 'query': 'Where is my refund'})
```

- **Invoke**: Fills the template with actual values.  
- **chat_history**: Injects past conversation.  
- **query**: The new user question.  
- **Result**: A fully structured prompt that combines system instructions, past history, and the new query.

---

## 🔹 Why This Matters
- **Dynamic Context** → The AI doesn’t forget past exchanges.  
- **Role Awareness** → System vs human vs AI messages are clearly separated.  
- **Scalability** → You can reuse the same template for multiple queries.  
- **Customer Support Use Case** → Perfect for building assistants that need memory of ongoing issues (like refunds, troubleshooting).

---

## 🔹 Key Takeaway
- **ChatPromptTemplate** = Blueprint for structured conversations.  
- **MessagesPlaceholder** = Slot for injecting chat history.  
- **Invoke** = Fills the template with actual values (history + query).  

Together, they make your chatbot **context-aware, reusable, and professional**.

---

# 🎯 Structured Output with `TypedDict` in LangChain

Script is a great example of combining **LangChain’s structured output feature** with Python’s `TypedDict`. Let’s break it down so you can use this as a reference.

https://github.com/meraviverma/langchain_tutorial/blob/main/5_StructuredOutput/with_structuredoutput_typedict.py
---

## 🔹 What’s Happening in the Code

1. **Environment Setup**
   - `load_dotenv()` loads your API keys from `.env`.
   - `ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite')` initializes the Gemini model.

2. **Define a Schema with `TypedDict`**
   ```python
   class Review(TypedDict):
       summary: str
       sentiment: str
       rating: int
   ```
   - This defines the **expected structure** of the model’s output:
     - `summary` → A short text summary.
     - `sentiment` → Positive / Negative / Neutral.
     - `rating` → Numeric score (e.g., 1–10).

3. **Structured Output**
   ```python
   structured_model = model.with_structured_output(Review)
   ```
   - This tells LangChain: *“Always return results that fit the `Review` schema.”*
   - The model output is automatically parsed into a dictionary with the correct keys.

4. **Invoking the Model**
   - Example 1: `"What do you think of the movie 3 idiots?"`
   - Example 2: A detailed product review of the Samsung Galaxy S24 Ultra.

   Each invocation returns a dictionary like:
   ```python
   {
       "summary": "...",
       "sentiment": "...",
       "rating": ...
   }
   ```

5. **Accessing Results**
   ```python
   print(result['summary'])
   print(result['sentiment'])
   print(result['rating'])
   ```
   - You can directly access structured fields instead of parsing raw text.

---

## 🔹 Why This Matters

- **Consistency** → The model always returns the same structure.  
- **Reliability** → Easier to integrate into apps (no messy string parsing).  
- **Validation** → Type checkers (like `mypy`) ensure correct usage.  
- **Automation** → Perfect for pipelines where AI outputs feed into databases, dashboards, or APIs.

---

## 🔹 Example Outputs (Conceptual)

- **Movie Review (3 Idiots)**  
  ```json
  {
    "summary": "A heartwarming comedy-drama about friendship and education.",
    "sentiment": "Positive",
    "rating": 9
  }
  ```

- **Product Review (Samsung Galaxy S24 Ultra)**  
  ```json
  {
    "summary": "Powerful phone with excellent camera and battery, but heavy and pricey.",
    "sentiment": "Mixed",
    "rating": 8
  }
  ```

---

## 🔹 Key Takeaway
Using `TypedDict` with `with_structured_output` transforms AI responses from **free-form text** into **structured, predictable data**. This makes your AI assistant’s outputs **production-ready** and easy to consume in downstream applications.


---
# 🧩 Deep Dive: `with_structured_output` in LangChain

## 🔹 What is `with_structured_output`?
`with_structured_output` is a **LangChain method** that transforms a language model into one that **always returns data in a structured format**.  
Instead of free‑form text, the model’s output is parsed into a schema you define (using `TypedDict`, `Pydantic`, or similar).

Think of it as telling the model:  
👉 *“Don’t just give me text — give me a dictionary with specific keys and types.”*

---

## 🔹 Why Use It?
Normally, LLMs return plain text. That’s fine for human reading, but messy for automation.  
With `with_structured_output`, you get:
- **Predictable structure** → No need to parse text manually.  
- **Type safety** → Keys and value types are enforced by your schema.  
- **Integration ready** → Outputs can flow directly into databases, APIs, or dashboards.  
- **Reduced hallucination risk** → The model is guided to fit the schema, limiting irrelevant text.

---

## 🔹 How It Works in Your Code
1. **Define a Schema**
   ```python
   class Review(TypedDict):
       summary: str
       sentiment: str
       rating: int
   ```
   - This schema says: every output must have `summary`, `sentiment`, and `rating`.

2. **Wrap the Model**
   ```python
   structured_model = model.with_structured_output(Review)
   ```
   - Now, whenever you call `structured_model.invoke(...)`, the result is guaranteed to fit the `Review` schema.

3. **Invoke with Input**
   ```python
   result = structured_model.invoke("What do you think of the movie 3 idiots?")
   ```
   - Instead of free text, you get:
     ```json
     {
       "summary": "A heartwarming comedy-drama about friendship and education.",
       "sentiment": "Positive",
       "rating": 9
     }
     ```

---

## 🔹 Benefits Over Plain Output
| Aspect | Normal Model Output | With `with_structured_output` |
|--------|---------------------|-------------------------------|
| Format | Free text | Dictionary with keys |
| Parsing | Manual string parsing | Direct field access (`result['summary']`) |
| Reliability | May vary each run | Consistent schema |
| Use Case | Human reading | Automation, pipelines, APIs |

---

## 🔹 Example Use Cases
- **Product Reviews** → Extract `summary`, `sentiment`, `rating`.  
- **Customer Support** → Return `issue_type`, `priority`, `resolution_steps`.  
- **Healthcare** → Return `symptoms`, `diagnosis`, `recommendation`.  
- **Education** → Return `topic`, `difficulty_level`, `explanation`.

---

## 🔹 Key Takeaway
`with_structured_output` is the bridge between **LLM creativity** and **software reliability**.  
It ensures that AI responses are **machine‑friendly, predictable, and safe to use in production workflows**.

---

✨ It turns subjective reviews (movies, phones) into structured data with **summary, sentiment, and rating** — making them instantly usable for analytics or dashboards.

# 🧩 Deep Dive into `BaseModel`, `EmailStr`, and `Field` (Pydantic)

Example is a great showcase of **Pydantic**, which is widely used for **data validation and parsing** in Python. Let’s break it down step by step.

https://github.com/meraviverma/langchain_tutorial/blob/main/5_StructuredOutput/pydantic_demo.py
---

## 🔹 1. `BaseModel`
- **Definition**: The core class in Pydantic.  
- **Purpose**: Provides automatic validation, parsing, and serialization of data.  
- **Usage**: You define your schema by subclassing `BaseModel`.  

### Key Features:
- **Validation at runtime** → Ensures inputs match expected types.  
- **Parsing** → Converts compatible types automatically (e.g., `"32"` → `32` for an `int`).  
- **Serialization** → Easily convert to dict or JSON (`.model_dump()`, `.model_dump_json()`).  
- **Defaults** → Supports default values for fields.  

👉 In code:
```python
class Student(BaseModel):
    name: str = 'Ravi'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, default=5, description='A decimal value representing the cgpa of the student')
```
This defines a **Student schema** with strict rules.

---

## 🔹 2. `EmailStr`
- **Definition**: A special type from Pydantic that validates email addresses.  
- **Purpose**: Ensures the string is a valid email format.  
- **Usage**: If you pass `"abc@gmail.com"`, it’s valid. If you pass `"abc"`, validation fails.  

👉 In  code:
```python
email: EmailStr
```
This guarantees that only proper email addresses are accepted.

---

## 🔹 3. `Field`
- **Definition**: Used to add extra constraints, metadata, or defaults to a field.  
- **Purpose**: Fine‑tunes validation rules.  
- **Common Parameters**:
  - `default` → Default value.  
  - `gt` / `lt` → Greater than / less than constraints.  
  - `description` → Adds documentation.  
  - `regex` → Pattern matching.  

👉 In  code:
```python
cgpa: float = Field(gt=0, lt=10, default=5, description='A decimal value representing the cgpa of the student')
```
- Must be a float.  
- Must be greater than 0 and less than 10.  
- Defaults to 5 if not provided.  
- Has a description for clarity.

---

## 🔹 4. Runtime Behavior in Your Example
```python
new_student = {'age':'32', 'email':'abc@gmail.com'}
student = Student(**new_student)
```

- **Age**: Passed as a string `"32"`.  
  - Pydantic **parses it into an integer** automatically → `32`.  
- **Email**: `"abc@gmail.com"` → Validated as a proper email.  
- **Name**: Not provided → Defaults to `"Ravi"`.  
- **CGPA**: Not provided → Defaults to `5`.

---

## 🔹 5. Serialization
```python
student_dict = dict(student)
print(student_dict['age'])   # 32

student_json = student.model_dump_json()
print(student_json)
```

- `.model_dump()` → Converts to a Python dict.  
- `.model_dump_json()` → Converts to JSON string.  

👉 Example Output:
```json
{"name": "Ravi", "age": 32, "email": "abc@gmail.com", "cgpa": 5.0}
```

---

## 🔹 Key Takeaways
- **`BaseModel`** → Defines schema + runtime validation.  
- **`EmailStr`** → Ensures valid email format.  
- **`Field`** → Adds constraints (like ranges, defaults, descriptions).  
- **Automatic Parsing** → `"32"` (string) becomes `32` (int).  
- **Serialization** → Easy conversion to dict/JSON for APIs or storage.  

---

✅ In short: Pydantic makes your data **safe, clean, and predictable** — perfect for production systems where inputs can be messy (like user forms, API payloads, or external data sources).

---

# 🧩 Deep Dive: Using `with_structured_output` with **JSON Schema**

Latest example shows how you can guide an LLM to return **structured data** using a **JSON Schema** instead of `TypedDict` or `Pydantic`. Let’s unpack this carefully.

https://github.com/meraviverma/langchain_tutorial/blob/main/5_StructuredOutput/with_structured_output_json.py

---

## 🔹 What’s Happening in  Code

1. **Define a JSON Schema**
   ```python
   json_schema = {
     "title": "Review",
     "type": "object",
     "properties": {
       "key_themes": {"type": "array", "items": {"type": "string"}},
       "summary": {"type": "string"},
       "sentiment": {"type": "string", "enum": ["pos", "neg"]},
       "pros": {"type": ["array", "null"], "items": {"type": "string"}},
       "cons": {"type": ["array", "null"], "items": {"type": "string"}},
       "name": {"type": ["string", "null"]}
     },
     "required": ["key_themes", "summary", "sentiment"]
   }
   ```
   - This schema defines the **shape of the output**:
     - `key_themes` → list of strings.
     - `summary` → string.
     - `sentiment` → must be `"pos"` or `"neg"`.
     - `pros` / `cons` → optional lists of strings.
     - `name` → optional string (reviewer’s name).
   - `"required"` ensures those fields must always be present.

2. **Wrap the Model**
   ```python
   structured_model = model.with_structured_output(json_schema)
   ```
   - This tells LangChain: *“Always return results that fit this JSON Schema.”*

3. **Invoke the Model**
   ```python
   result = structured_model.invoke(review_text)
   ```
   - Instead of free text, the model returns a **JSON object** that matches the schema.

---

## 🔹 Why JSON Schema?
- **Language‑agnostic** → Works across Python, JavaScript, Go, etc.  
- **Validation** → Ensures outputs conform to rules (types, enums, required fields).  
- **Standardized** → JSON Schema is widely used in APIs and contracts.  
- **No extra libraries** → Unlike Pydantic, you don’t need to install anything.

---

## 🔹 Example Output (Conceptual)
For your Samsung Galaxy S24 Ultra review, the model might return:

```json
{
  "key_themes": [
    "Performance",
    "Battery life",
    "Camera quality",
    "S-Pen integration",
    "Price",
    "Bloatware"
  ],
  "summary": "A powerful phone with excellent performance and camera, but heavy, pricey, and bloated with apps.",
  "sentiment": "pos",
  "pros": [
    "Snapdragon 8 Gen 3 processor",
    "200MP camera with zoom",
    "Long battery life",
    "S-Pen support"
  ],
  "cons": [
    "Heavy and large",
    "Bloatware in One UI",
    "High price"
  ],
  "name": "Ravi Verma"
}
```

---

## 🔹 Comparison to Other Approaches

| Feature                  | TypedDict | Pydantic | JSON Schema |
|---------------------------|-----------|----------|-------------|
| **Basic structure**       | ✅        | ✅       | ✅          |
| **Runtime validation**    | ❌        | ✅       | ✅          |
| **Default values**        | ❌        | ✅       | ❌          |
| **Automatic conversion**  | ❌        | ✅       | ❌          |
| **Cross‑language use**    | ❌        | ❌       | ✅          |

---

## 🔹 Key Takeaway
- **TypedDict** → lightweight type hints, no runtime checks.  
- **Pydantic** → Python‑centric, with validation, defaults, and conversions.  
- **JSON Schema** → universal, cross‑language, perfect for APIs and contracts.  

In this case, using **JSON Schema with `with_structured_output`** ensures the LLM’s review analysis is **consistent, validated, and portable** across systems.

---


# 🧩 TypedDict vs Pydantic vs JSON Schema — When to Use What

Summary of the trade‑offs between these three approaches. Let’s expand on it with more detailed explanations so you can decide which fits best in different scenarios.

---

## 🔹 1. **TypedDict**
- **What it is**: A Python typing construct that defines the expected keys and value types in a dictionary.  
- **Strengths**:
  - Lightweight — no extra libraries needed.  
  - Great for **static type checking** with tools like `mypy`.  
  - Useful when you trust the data source (e.g., an LLM or API that reliably returns the right structure).  
- **Limitations**:
  - No runtime validation — Python will happily accept wrong types.  
  - No defaults — missing keys cause issues unless you handle them manually.  
  - Only works inside Python (not cross‑language).  

👉 Best for **simple schemas** where you just want type hints.

---

## 🔹 2. **Pydantic**
- **What it is**: A powerful Python library for **data validation and parsing**.  
- **Strengths**:
  - Validates data at runtime (e.g., ensures `age` is an `int`, `email` is valid).  
  - Provides **default values** if fields are missing.  
  - Automatically converts compatible types (e.g., `"32"` → `32`).  
  - Rich constraints via `Field` (ranges, regex, descriptions).  
  - Easy serialization (`.model_dump()`, `.model_dump_json()`).  
- **Limitations**:
  - Requires installing Pydantic.  
  - Python‑specific (not cross‑language).  

👉 Best for **production systems** where data comes from external sources and must be validated.

---

## 🔹 3. **JSON Schema**
- **What it is**: A standardized way to describe data structures in JSON.  
- **Strengths**:
  - Language‑agnostic — works across Python, JavaScript, Go, etc.  
  - Provides validation rules (types, required fields, ranges).  
  - Ideal for APIs and contracts between services.  
- **Limitations**:
  - No Python object integration (you just validate JSON).  
  - No defaults or automatic type conversion.  
  - More verbose to write compared to Pydantic.  

👉 Best for **cross‑language projects** or when you want a universal schema definition.

---

## 🔹 Comparison Table

| Feature                  | TypedDict ✅ | Pydantic 🖋️ | JSON Schema 🌐 |
|---------------------------|--------------|--------------|----------------|
| Basic structure           | ✅           | ✅           | ✅             |
| Type enforcement          | ❌ (static only) | ✅ (runtime) | ✅ (runtime)   |
| Data validation           | ❌           | ✅           | ✅             |
| Default values            | ❌           | ✅           | ❌             |
| Automatic conversion      | ❌           | ✅           | ❌             |
| Cross‑language compatibility | ❌        | ❌           | ✅             |

---

## 🔹 Key Takeaway
- Use **TypedDict** → when you just need type hints and trust the data.  
- Use **Pydantic** → when you need runtime validation, defaults, and conversions in Python.  
- Use **JSON Schema** → when you need a universal schema across multiple languages or systems.  

---

✨ In practice:  
- For your **LLM structured outputs**, `TypedDict` is fine if you trust the model.  
- For **user input or API payloads**, Pydantic is safer because it validates and converts.  
- For **cross‑service contracts**, JSON Schema is the standard.

---

# 🧩 Output Parser
-----------------------

# 🧩 Detailed Explanation of Your HuggingFace + LangChain Workflow

Script demonstrates how to build a **two‑stage pipeline** using HuggingFace models inside LangChain. Let’s break it down step by step.

https://github.com/meraviverma/langchain_tutorial/blob/main/6_OutputParser/stroutputparser.py

---

## 🔹 1. Model Setup
```python
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Pro",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)
```
- **`HuggingFaceEndpoint`** → Connects to a HuggingFace model (`DeepSeek-V4-Pro`) for text generation.  
- **`ChatHuggingFace`** → Wraps the endpoint so you can interact with it in a conversational style (like a chatbot).

---

## 🔹 2. Prompt Templates
You define **two different prompt templates**:

1. **Detailed Report Prompt**
   ```python
   template1 = PromptTemplate(
       template='Write a detailed report on {topic}',
       input_variables=['topic']
   )
   ```
   - Accepts a `topic` variable.  
   - Produces a long, detailed response.

2. **Summary Prompt**
   ```python
   template2 = PromptTemplate(
       template='Write a 5 line summary on the following text. /n {text}',
       input_variables=['text']
   )
   ```
   - Accepts a `text` variable.  
   - Produces a concise summary (5 lines).

---

## 🔹 3. Workflow Execution
1. **Stage 1: Generate Report**
   ```python
   prompt1 = template1.invoke({'topic':'black hole'})
   result = model.invoke(prompt1)
   ```
   - The first template is filled with `"black hole"`.  
   - The model generates a **detailed report** on black holes.

2. **Stage 2: Summarize Report**
   ```python
   prompt2 = template2.invoke({'text':result.content})
   result1 = model.invoke(prompt2)
   ```
   - The second template takes the **full report** as input.  
   - The model generates a **5‑line summary** of that report.

---

## 🔹 4. Output
```python
print(result1.content)
```
- Prints the final summary.  
- The workflow ensures you get both a **long form explanation** and a **short summary**.

---

## 🔹 Why This Approach is Powerful
- **Modularity** → You can chain multiple prompts together.  
- **Reusability** → Each prompt template can be reused for different topics.  
- **Control** → You decide the style (detailed vs summary).  
- **Scalability** → You can extend this pipeline (e.g., add a third step for bullet points or sentiment analysis).

---

## 🔹 Key Takeaway
Your script shows a **prompt chaining workflow**:
1. Generate a **detailed report**.  
2. Feed that into another prompt to produce a **summary**.  

This is a classic **multi‑step LLM pipeline** — useful for research, content generation, or customer support where you need both depth and brevity.

---

# 🧩 Breaking Down Your HuggingFace + LangChain Chain

Script is a **multi‑step chain** that combines prompts, models, and parsers into one pipeline. Let’s walk through it carefully.

https://github.com/meraviverma/langchain_tutorial/blob/main/6_OutputParser/stroutputparserchain.py

---

## 🔹 1. Model Setup
```python
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Pro",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)
```
- Connects to the HuggingFace model `DeepSeek-V4-Pro` for text generation.  
- Wrapped with `ChatHuggingFace` so it behaves like a conversational model.

---

## 🔹 2. Prompt Templates
You define two templates:

1. **Detailed Report Prompt**
   ```python
   template1 = PromptTemplate(
       template='Write a detailed report on {topic}',
       input_variables=['topic']
   )
   ```
   - Takes a `topic` (e.g., `"black hole"`) and asks for a detailed report.

2. **Summary Prompt**
   ```python
   template2 = PromptTemplate(
       template='Write a 5 line summary on the following text. /n {text}',
       input_variables=['text']
   )
   ```
   - Takes a block of text and asks for a 5‑line summary.

---

## 🔹 3. Output Parser
```python
parser = StrOutputParser()
```
- Ensures the model’s output is parsed into a **plain string**.  
- Useful because HuggingFace models may return structured objects; this strips it down to text.

---

## 🔹 4. The Chain
```python
chain = template1 | model | parser | template2 | model | parser
```
This is a **pipeline** using the `|` operator:

1. **template1** → Fills in the topic (`black hole`).  
2. **model** → Generates a detailed report.  
3. **parser** → Converts the report into plain text.  
4. **template2** → Takes that text and asks for a summary.  
5. **model** → Generates the summary.  
6. **parser** → Converts the summary into plain text.

---

## 🔹 5. Execution
```python
result = chain.invoke({'topic':'black hole'})
print(result)
```
- Input: `{'topic': 'black hole'}`  
- Output: A **5‑line summary** of the detailed report on black holes.  
- The chain automatically handles both steps (report → summary) in one call.

---

## 🔹 Why This is Powerful
- **Chaining** → You don’t need to manually call each step; the pipeline flows automatically.  
- **Reusability** → You can swap templates or parsers easily.  
- **Scalability** → Add more steps (e.g., sentiment analysis, bullet points).  
- **Cleaner Code** → Instead of writing multiple `invoke` calls, you define the workflow once.

---

## 🔹 Key Takeaway
Your chain is a **two‑stage workflow**:
1. Generate a **detailed report** on a topic.  
2. Summarize that report into **five lines**.  

This is a classic example of **prompt chaining** in LangChain — turning raw LLM outputs into structured, multi‑step results.

---

# 🧩 Detailed Walkthrough of  `JsonOutputParser` Chain

Script is a great demonstration of how to **guide an LLM to return JSON‑structured data** using LangChain’s `JsonOutputParser`. Let’s break it down step by step.

---

## 🔹 1. Model Setup
```python
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Pro",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)
```
- Connects to HuggingFace’s `DeepSeek-V4-Pro` model for text generation.  
- Wrapped with `ChatHuggingFace` so you can interact with it in a conversational style.

---

## 🔹 2. JSON Output Parser
```python
parser = JsonOutputParser()
```
- This parser expects the model’s output to be **valid JSON**.  
- It provides helper instructions (`parser.get_format_instructions()`) that you can inject into your prompt so the model knows how to format its response.

---

## 🔹 3. Prompt Template
```python
template = PromptTemplate(
    template='Give me the name , age and city of a fictional person \n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)
```
- The prompt asks for **structured information** (name, age, city).  
- `{format_instruction}` is replaced with the parser’s formatting guide (e.g., “Return output as JSON with keys: name, age, city”).  
- This ensures the model outputs JSON instead of free text.

---

## 🔹 4. Chain Definition
```python
chain = template | model | parser
```
This pipeline means:
1. **PromptTemplate** → Generates the instruction text.  
2. **Model** → Produces the response.  
3. **JsonOutputParser** → Parses the response into a Python dictionary.

---

## 🔹 5. Running the Chain
```python
result_chain = chain.invoke({})
```
- Executes the full pipeline in one go.  
- Returns a parsed dictionary, e.g.:
  ```python
  {'name': 'John Doe', 'age': 32, 'city': 'New York'}
  ```

---

## 🔹 6. Step‑by‑Step Approach
You also show how to do it manually:

```python
prompt = template.format()
print(prompt)  # Shows the final prompt with format instructions

result = model.invoke(prompt)
print(result)  # Raw model output (likely JSON text)

final_result = parser.parse(result.content)
print(final_result)  # Parsed dict
```

Then you can access fields directly:
```python
print("Name:", final_result['name'])
print("Age:", final_result['age'])
print("City:", final_result['city'])
```

---

## 🔹 7. Important Note
As you correctly mention:
```python
# Can't enforce schema in json output parser but we can parse the output to get the required information.
```
- `JsonOutputParser` **cannot enforce a schema** (like Pydantic or JSON Schema).  
- It only parses whatever JSON the model produces.  
- If the model misses a field or outputs invalid JSON, parsing may fail.  
- For stricter enforcement, you’d use **Pydantic models** or **JSON Schema** with `with_structured_output`.

---

## 🔹 Key Takeaway
- **JsonOutputParser** → Simple way to parse JSON responses.  
- **PromptTemplate + format_instructions** → Guides the model to output valid JSON.  
- **Chain** → Automates prompt → model → parse in one pipeline.  
- **Limitation** → No schema enforcement; parsing works only if the model follows instructions.

---