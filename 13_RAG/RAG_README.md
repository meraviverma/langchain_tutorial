# LangChain Tools and Toolkits: A Comprehensive Guide

## Installation of Libraries
This section demonstrates the installation of necessary Python libraries. `langchain`, `langchain-core`, `langchain-community`, `pydantic`, `duckduckgo-search`, and `langchain_experimental` are installed to provide functionalities for building language model applications, defining data models, performing searches, and experimenting with LangChain features. The `!pip install` command is a shell command executed within the Colab environment.

## Built-in Tool - DuckDuckGo Search

### `DuckDuckGoSearchRun`

`DuckDuckGoSearchRun` is a powerful built-in tool provided by `langchain_community.tools` that allows your language model agents to perform real-time web searches using DuckDuckGo. This is particularly useful for tasks requiring up-to-date information, current events, or general knowledge retrieval that might not be available in the model's training data.

**How it works:**
1.  **Instantiation:** You create an instance of `DuckDuckGoSearchRun()`. This object represents the tool itself.
2.  **`invoke()` method:** To use the tool, you call its `invoke()` method, passing a dictionary with a `query` key. The value associated with `query` is the search string you want to execute.
3.  **Output:** The `invoke()` method returns the search results as a string, which can then be parsed or summarized by the language model.

In this example, it's used to fetch 'top news in india today', demonstrating its capability to access current information.

The `name`, `description`, and `args` attributes are standard properties for LangChain tools:
-   **`name`**: A unique identifier for the tool, typically a concise string.
-   **`description`**: A human-readable explanation of what the tool does. This is crucial for language models to understand when to use the tool and what task it can perform.
-   **`args`**: A dictionary specifying the input arguments the tool expects. For `DuckDuckGoSearchRun`, it expects a `query` argument of type `string` with a description of its purpose. This structure helps in defining the schema for the tool's inputs, making it easier for agents to correctly format their requests when using the tool.

## Built-in Tool - Shell Tool

### `ShellTool`

`ShellTool` is another built-in tool from `langchain_community.tools` that enables a language model to execute shell commands directly on the host system. This tool is extremely powerful for interacting with the operating system, performing file operations, running scripts, or any task that can be accomplished via the command line.

**Important Considerations:**
-   **Security Warning:** As noted in the output, `ShellTool` has no safeguards by default. This means any command the language model generates and invokes will be executed. **It should be used with extreme caution**, especially in environments where security is a concern, or with untrusted inputs.
-   **`invoke()` method:** Similar to other tools, `invoke()` is used to pass the shell command as a string argument.

In this example, `shell_tool.invoke('ls')` lists the contents of the current directory (`sample_data` is a common directory in Colab environments), demonstrating a basic interaction with the file system.

## Custom Tools

### `@tool` Decorator

LangChain provides a convenient `@tool` decorator (`from langchain_core.tools import tool`) that simplifies the process of converting a regular Python function into a LangChain tool. This method is highly recommended for its conciseness and ease of use, especially when the tool's input schema is straightforward.

**Steps to create a tool with `@tool`:**
1.  **Define a Python function:** Create a standard Python function that performs the desired operation.
2.  **Add type hints:** Crucially, add type hints to the function parameters. These type hints are automatically used by the `@tool` decorator to infer the tool's input schema (its `args`).
3.  **Add a docstring:** Provide a clear docstring for the function. This docstring will automatically become the tool's `description`.
4.  **Decorate with `@tool`:** Place `@tool` directly above the function definition.

**Example (`multiply` function):**
-   The function `multiply(a: int, b: int) -> int` takes two integers `a` and `b` and returns their product.
-   The docstring `"""Multiply two numbers"""` becomes the tool's description.
-   The type hints `a: int` and `b: int` inform LangChain that the tool expects two integer arguments named `a` and `b`.

The `invoke()` method is the standard way to call a LangChain tool. When using a tool created with the `@tool` decorator, `invoke()` expects a dictionary where keys match the function's parameter names and values are the corresponding inputs. Here, `multiply.invoke({"a":3, "b":5})` calls the `multiply` tool with `a=3` and `b=5`.

As demonstrated previously, tools created with `@tool` automatically expose `name`, `description`, and `args` attributes derived from the function's name, docstring, and type hints, respectively. The `args` attribute presents the inferred input schema, detailing the expected arguments, their types, and whether they are required.

### `args_schema`

The `args_schema` attribute provides a more detailed, Pydantic-driven representation of the tool's input schema. Calling `.model_json_schema()` on `multiply.args_schema` outputs a JSON schema compliant dictionary. This schema is critical for advanced agent frameworks as it allows for rigorous validation of inputs and provides a machine-readable format for describing tool arguments, including their types, titles, and descriptions. This ensures that the agent provides valid inputs to the tool.

### `StructuredTool.from_function`

`StructuredTool.from_function` is a flexible method for creating LangChain tools, offering more control over the input schema compared to the `@tool` decorator. It's particularly useful when you need to define a more complex or custom input validation using Pydantic models.

**Key components:**
1.  **`BaseModel` and `Field` (Pydantic):** These are used to define a custom input schema. `BaseModel` creates the structure, and `Field` allows for detailed specifications like `required=True`, `description`, etc.
2.  **`MultiplyInput` (Pydantic model):** This class defines the expected input structure for our `multiply_func`. Each field (`a`, `b`) is an integer, marked as required, and includes a description. This enforces strict validation on the inputs.
3.  **`multiply_func` (Python function):** This is the core logic of the tool, taking `a` and `b` as arguments and returning their product.
4.  **`StructuredTool.from_function()`:** This static method binds the function (`func`), provides a `name` and `description`, and, most importantly, accepts `args_schema` as the Pydantic model (`MultiplyInput`). This explicitly links the tool's input requirements to our custom Pydantic schema.

This method allows for robust input validation and clearer definition of tool interfaces, making it easier for agents to understand and correctly utilize the tool.

Calling `invoke()` on `multiply_tool` with a dictionary `{'a':3, 'b':3}` demonstrates that the `StructuredTool` instance works as expected, returning the product. The output also confirms that the `name`, `description`, and `args` (derived from `args_schema`) are correctly configured for the tool.

### `BaseTool` Class

Creating a custom tool by inheriting from `BaseTool` offers the highest degree of customization and control. This method is suitable when you have complex tool logic, specific error handling, or need to encapsulate tool-specific state. It requires more boilerplate code but provides maximum flexibility.

**Key components:**
1.  **`BaseTool` (Abstract Base Class):** You inherit from `langchain.tools.BaseTool`.
2.  **`args_schema` (Pydantic model):** Similar to `StructuredTool.from_function`, a Pydantic `BaseModel` defines the input schema. This ensures strong typing and validation.
3.  **`name` and `description`:** These are defined as class attributes.
4.  **`_run()` method:** This is the core method where the tool's logic resides. It takes the arguments defined in `args_schema` and performs the operation. **Crucially, `_run` should not be called directly by the agent; `invoke()` handles calling it safely.**

**Example (`MultiplyTool`):**
-   The `MultiplyInput` Pydantic model is reused to define the input structure.
-   `MultiplyTool` inherits from `BaseTool` and explicitly sets `name`, `description`, and `args_schema`.
-   The `_run` method contains the multiplication logic.

This approach is ideal for tools that need more sophisticated internal mechanisms or when integrating with external systems that require specific setup or teardown procedures within the tool itself.

Executing `multiply_tool.invoke({'a':3, 'b':3})` for the `BaseTool` implementation shows identical behavior to the previous methods. This consistency across different tool creation methods is a hallmark of LangChain's design. The output verifies that the tool correctly performs its function and exposes its metadata (`name`, `description`, `args`) as expected.

## Toolkits

### Toolkits

Toolkits are collections of related tools, often grouped together for a specific domain or purpose. They simplify the management and provision of multiple tools to an agent. Instead of individually passing each tool, you can pass an entire toolkit, allowing the agent to dynamically discover and use the available tools within that kit.

**Key concept:**
-   **`get_tools()` method:** A common pattern for toolkits is to have a method (e.g., `get_tools()`) that returns a list of all tools included in the toolkit.

**Example (`MathToolkit`):**
-   Two custom tools, `add` and `multiply`, are defined using the `@tool` decorator.
-   The `MathToolkit` class encapsulates these tools. Its `get_tools()` method simply returns a list containing both the `add` and `multiply` tool instances.

This modular approach makes it easier to organize and scale the number of tools available to an agent, promoting reusability and maintainability of your LangChain applications.


## RAG USING LANGCHAIN

## Methods and Functions Used: A Deep Dive

This section provides a detailed breakdown of the libraries, methods, and functions employed in constructing this Retrieval-Augmented Generation (RAG) pipeline. The goal is to establish a robust framework for extracting insights from YouTube video transcripts using advanced NLP techniques.

### 1. Document Ingestion and Preprocessing

#### `youtube-transcript-api`

This indispensable library facilitates the programmatic retrieval of YouTube video transcripts. Given a `video_id`, its `YouTubeTranscriptApi().fetch(video_id)` method returns a `FetchedTranscript` object. This object is not merely a string but a structured representation, being both iterable and indexable. Each element within this collection is a snippet containing the spoken `text`, its `start` timestamp, and `duration`.

*   **`fetched_transcript.to_raw_data()`**: This method is critical for transforming the `FetchedTranscript` object into a more manageable list of dictionaries. Each dictionary corresponds to a transcript snippet, allowing for straightforward extraction and manipulation of the textual content, which is essential for subsequent processing steps.

#### `langchain-text-splitters`

Effective information retrieval hinges on managing the size of text segments. Large documents can overwhelm Language Models (LLMs) due to token limitations, while overly small segments may lack sufficient context. `langchain-text-splitters` addresses this challenge.

*   **`RecursiveCharacterTextSplitter`**: This class is designed for the intelligent segmentation of extensive text documents, such as full video transcripts. It employs a recursive strategy, attempting to split text first by large separators (e.g., `\n\n`), then by smaller ones (e.g., `\n`), and finally by individual characters if necessary. This hierarchical approach ensures that semantic units are preserved as much as possible.
    *   **`chunk_size`**: This parameter dictates the maximum character length for each generated text chunk. Careful selection is crucial; a size too small might fragment coherent ideas, while one too large could exceed an LLM's context window.
    *   **`chunk_overlap`**: This parameter specifies the number of characters that consecutive chunks will share. Overlapping chunks are vital for maintaining contextual continuity across split boundaries, preventing loss of information that might occur at the edges of a chunk.
*   **`splitter.create_documents([transcript_text])`**: This method takes a list of raw text strings and applies the configured splitting logic. The output is a list of `Document` objects, where each `Document` encapsulates a text chunk, ready for embedding and indexing.

### 2. Embedding Generation and Vector Store

To enable semantic search, text must be transformed into a numerical representation that captures its meaning. This is achieved through embeddings, and these embeddings are then stored in a specialized database for efficient retrieval.

#### `langchain-huggingface`

This library provides seamless integration with Hugging Face models, particularly for tasks like embedding generation.

*   **`HuggingFaceEndpointEmbeddings`**: This class serves as an interface to embedding models hosted on the Hugging Face Inference API. By specifying a `repo_id` (e.g., `'sentence-transformers/all-MiniLM-L6-v2'`), it leverages pre-trained models to convert textual data into dense numerical vectors (embeddings). These embeddings are high-dimensional representations where semantically similar texts are mapped to geometrically closer points in the vector space, a fundamental concept for vector search.

#### `langchain-community.vectorstores`

Vector stores are specialized databases optimized for storing and querying vector embeddings based on similarity.

*   **`FAISS`**: Developed by Facebook AI, FAISS (Facebook AI Similarity Search) is an open-source library renowned for its efficiency in similarity search and clustering of dense vectors. In this pipeline, `FAISS` is chosen as the vector store to index and store the embeddings of the text chunks. Its optimized algorithms allow for very fast nearest-neighbor searches, even with extremely large datasets.
*   **`FAISS.from_documents(chunks, embedding)`**: This static method is instrumental in populating the `FAISS` index. It takes a list of `Document` objects (our text chunks) and an `embedding` function (our `HuggingFaceEndpointEmbeddings` instance). For each document, it generates its embedding using the provided function and then stores this vector representation within the `FAISS` index. This process effectively creates a searchable semantic map of the entire transcript.

### 3. Retrieval

Once the embeddings are indexed, the next step is to retrieve relevant information given a query.

*   **`vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})`**: This method converts the initialized `FAISS` vector store into a retriever object. Retrievers are a core component of RAG, responsible for fetching relevant documents based on a query.
    *   **`search_type="similarity"`**: This specifies that the retrieval mechanism should be based on computing the similarity between the query's embedding and the stored document embeddings. Typically, cosine similarity is used for this purpose.
    *   **`search_kwargs={"k": 4}`**: This dictionary provides additional arguments to the search function. Here, `"k": 4` indicates that the retriever should return the top 4 most similar documents (chunks) to the given query. This ensures that the LLM receives a focused set of relevant contexts rather than the entire transcript.
