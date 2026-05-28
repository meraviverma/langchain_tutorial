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

# # In LangChain, **`RunnableLambda`** is a powerful utility that allows you to wrap arbitrary Python functions into a `Runnable` object. This makes your custom code fully compatible with LangChain’s **LCEL (LangChain Expression Language)**, allowing it to participate in chains, benefit from batching, and integrate seamlessly with other LangChain components.

# ---

# ### Why use `RunnableLambda`?

# In complex chains, you often need to perform custom data transformations that standard LangChain components (like PromptTemplates or Models) don't handle natively. 

# While you *could* use a standard Python function, wrapping it in `RunnableLambda` provides:
# 1. **Pipelining:** Use the `|` operator to chain your function with other components.
# 2. **Automatic Async Support:** LangChain handles the `async` versions of your functions.
# 3. **Batching:** `RunnableLambda` provides built-in support for processing lists of inputs efficiently (`batch` and `abatch` methods).
# 4. **Tracing:** LangChain's observability tools (LangSmith) can track your function as a distinct step in the chain.

# ---

# ### Basic Implementation

# You can create a `RunnableLambda` in two main ways: using the constructor or the `@chain` decorator.

# #### 1. Using the Constructor
# ```python
# from langchain_core.runnables import RunnableLambda

# def say_hello(name: str):
#     return f"Hello, {name}!"

# # Wrap the function
# hello_runnable = RunnableLambda(say_hello)

# # Use it in a chain
# chain = hello_runnable | (lambda x: x.upper())

# print(chain.invoke("World"))  # Output: "HELLO, WORLD!"
# ```

# #### 2. Using the `@chain` Decorator (Recommended for complexity)
# If your custom logic is complex, the `@chain` decorator is often cleaner. It automatically converts the function into a `Runnable`.

# ```python
# from langchain_core.runnables import chain

# @chain
# def custom_logic(input_dict):
#     return input_dict["name"].upper()

# # This is effectively a RunnableLambda
# print(custom_logic.invoke({"name": "langchain"})) # Output: "LANGCHAIN"
# ```

# ---

# ### Advanced Features

# #### 1. Handling Input Dictionaries
# `RunnableLambda` is frequently used to transform input before passing it to a model. You can use it to extract values from a larger dictionary.

# ```python
# from langchain_core.runnables import RunnablePassthrough

# def get_length(text: str):
#     return len(text)

# # Example: Get length of a string passed through a chain
# chain = RunnablePassthrough() | RunnableLambda(get_length)
# print(chain.invoke("LangChain")) # Output: 9
# ```

# #### 2. Batching
# This is where `RunnableLambda` shines. If you have a function that processes one item, LangChain can automatically parallelize it if you define a batch function, or it will execute it sequentially if not.

# ```python
# def process_data(data):
#     return data * 2

# runnable = RunnableLambda(process_data)

# # Batch execution
# results = runnable.batch([1, 2, 3])
# print(results) # Output: [2, 4, 6]
# ```

# #### 3. Defining Async Functions
# If your custom logic involves I/O (like calling an API or a database), you can define an `async` function. LangChain will respect this when you use `.ainvoke()` or `.abatch()`.

# ```python
# import asyncio

# async def async_fetch(query):
#     await asyncio.sleep(1) # Simulate I/O
#     return f"Result for {query}"

# runnable = RunnableLambda(async_fetch)

# # Use in async context
# async def main():
#     res = await runnable.ainvoke("data")
#     print(res)
# ```

# ---

# ### Best Practices

# 1. **Keep it stateless:** `RunnableLambda` functions should be pure functions. They should not rely on external global state that might change between calls, as this complicates debugging and testing.
# 2. **Type Hinting:** Always use Python type hints. LangChain uses these internally to understand the input and output schemas of your chain.
# 3. **Use for Transformation, not Orchestration:** Use `RunnableLambda` for small data transformations (e.g., formatting strings, parsing JSON, arithmetic). For orchestration (calling LLMs, tools, or memory), use standard LCEL chains.
# 4. **Error Handling:** If your custom code is prone to failure (e.g., parsing an API response), wrap the logic inside the lambda in a `try-except` block to ensure your chain doesn't crash unexpectedly.

# ### Summary
# `RunnableLambda` is the "glue" of LangChain. It allows you to bridge the gap between structured AI components (models/retrievers) and your custom Python logic, turning your code into a first-class citizen within the LangChain ecosystem. 
#  word count - 603