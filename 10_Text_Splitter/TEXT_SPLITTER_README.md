# 📘 Text Splitting in LLM Workflows

https://chunkviz.up.railway.app/


## 🔹 Definition
Text Splitting is the process of breaking large chunks of text (such as articles, PDFs, HTML pages, or books) into smaller, manageable pieces (chunks) that a large language model (LLM) can handle effectively.

---

## 🔹 Why Text Splitting Matters

1. **Overcoming Model Limitations**
   - Many embedding models and LLMs have maximum input size constraints.
   - Splitting allows processing of documents that would otherwise exceed these limits.

2. **Improving Downstream Tasks**
   Text splitting enhances nearly every LLM-powered task:
   | Task            | Why Splitting Helps                          |
   |-----------------|----------------------------------------------|
   | **Embedding**   | Short chunks yield more accurate vectors     |
   | **Semantic Search** | Search results point to focused info, not noise |
   | **Summarization**   | Prevents hallucination and topic drift    |

3. **Optimizing Computational Resources**
   - Smaller chunks are more memory-efficient.
   - Enables better parallelization of processing tasks.

---
# 📘 Types of Text Splitters

## 🔹 Overview
Text splitters are strategies used to break large documents into smaller, manageable chunks so that language models (LLMs) can process them effectively. Different splitting methods are chosen depending on the structure, size, and purpose of the text.


---

## 🔹 Types of Text Splitters

1. **Length Based**
   - Splits text purely by character or token count.
   - Ensures each chunk fits within the LLM’s maximum input size.
   - Useful for raw text without clear structure.

2. **Text Structure Based**
   - Splits text according to natural language structure (sentences, paragraphs).
   - Preserves readability and semantic flow.
   - Ideal for articles, essays, or conversational transcripts.

3. **Document Structure Based**
   - Splits text using document-specific markers (headings, sections, chapters).
   - Maintains logical organization of content.
   - Best for structured documents like PDFs, reports, or books.

4. **Semantic Meaning Based**
   - Splits text by semantic similarity or meaning.
   - Uses embeddings or clustering to group related content.
   - Powerful for tasks like semantic search, summarization, or topic modeling.

---

# 📘 Length-Based Text Splitting

## 🔹 Definition
Length-based text splitting is the process of dividing a large block of text into smaller chunks based on **character count** or **token count**. Each chunk is limited to a predefined size (e.g., 100 characters or a fixed number of tokens) so that it can fit within the input constraints of a language model (LLM).

It also cuts words in middle. Suppose "exploring" will get cut into explo 
---

## 🔹 How It Works
- The text is scanned sequentially.
- A chunk is created once the specified length threshold is reached.
- The process continues until the entire text is divided into manageable segments.

Where:
- **c1, c2, c3, ...** represent chunks split by length.
- Each chunk contains ~100 characters (or tokens).

---

## 🔹 Benefits
1. **Handles Large Inputs**
   - Prevents exceeding LLM maximum input size.
   - Ensures long documents can be processed without truncation.

2. **Consistency**
   - Provides uniform chunk sizes, making downstream tasks predictable.

3. **Efficiency**
   - Smaller chunks reduce memory usage.
   - Enables parallel processing of text segments.

---

## 🔹 Use Cases
- **Embedding**: Short, consistent chunks yield more accurate vector representations.
- **Semantic Search**: Queries return focused results tied to specific text segments.
- **Summarization**: Prevents hallucination and topic drift by limiting context size.

---

✅ **Summary**:  
Length-based text splitting is a straightforward method to divide large text into fixed-size chunks, ensuring compatibility with LLMs and improving efficiency in tasks like embedding, search, and summarization.

# 📘 PDF Loading and Recursive Text Splitting

## 🔹 Function Details

1. **PyPDFLoader**
   - **Purpose**: Loads PDF documents into LangChain as `Document` objects.
   - **Usage in Code**:  
     ```python
     loader = PyPDFLoader('D:\\langchain_models\\10_Text_Splitter\\DA_2026_Syllabus.pdf')
     docs = loader.load()
     ```
     This reads the syllabus PDF and stores its content in `docs`.

2. **RecursiveCharacterTextSplitter**
   - **Purpose**: Splits text into smaller chunks based on character length, while recursively applying multiple separators (e.g., newline, space, punctuation).
   - **Usage in Code**:  
     ```python
     text_splitter = RecursiveCharacterTextSplitter(
         chunk_size=100,
         chunk_overlap=0,
         separators="\n"
     )
     texts = text_splitter.split_text(docs[0].page_content)
     ```
     This divides the PDF text into chunks of 100 characters, with no overlap, using newline as the primary separator.
     This ensures text is divided into chunks of 100 characters, with no overlap, using a hierarchy of separators:
     - Double newline (`\n\n`)
     - Single newline (`\n`)
     - Space (` `)
     - Empty string (`''` → raw character split)

# 📘 Text Splitter Separators

## 🔹 Definition
Separators are **characters or sequences of characters** used to divide text into smaller chunks. They define the logical boundaries for splitting, ensuring that the text is segmented in a meaningful way for processing by language models (LLMs).

---

## 🔹 Common Separator Strategies

1. **Paragraphs**
   - Separator: `"\n\n"`
   - Splits text into **paragraphs** based on double newline characters.

2. **Lines**
   - Separator: `"\n"`
   - Splits text into **lines** based on single newline characters.

3. **Sentences**
   - Separator: `[".", "!", "?"]`
   - Splits text into **sentences** using common punctuation marks.

4. **Words**
   - Separator: `" "`
   - Splits text into **words** based on spaces.

5. **Characters**
   - Separator: `""`
   - Splits text into **individual characters**.

6. **Mixed Separators**
   - Example: `["\n", " ", ",", ".", "!", "?"]`
   - Splits text into **sentences or phrases** using multiple punctuation marks and spaces.

---

## 🔹 Methodology Used

- **Hierarchy of Separators**:  
  Recursive splitters often apply separators in order:
  1. Try larger boundaries (paragraphs).
  2. Fall back to smaller boundaries (lines, sentences).
  3. Finally split by words or characters if chunks are still too large.

- **Chunk Size Control**:  
  Separators work in combination with `chunk_size` and `chunk_overlap` to ensure chunks fit within LLM input limits while preserving context.

---

3. **Chunk Parameters**
   - **chunk_size**: Maximum size of each chunk (here, 100 characters).
   - **chunk_overlap**: Number of overlapping characters between consecutive chunks (here, 0).
   - **separators**: Defines how text is split (here, newline `\n`).

4. **Iteration and Printing**
   - **Purpose**: Loops through the generated chunks and prints their length and content.
   - **Usage in Code**:  
     ```python
     for text in texts[2:]:
         print(len(text))
         print(text)
         print('------------------')
     ```
     This displays each chunk’s size and text content for inspection.

---

## 🔹 Methodology Used

- **Document Loading**:  
  `PyPDFLoader` extracts raw text from the syllabus PDF.

- **Text Splitting Strategy**:  
  `RecursiveCharacterTextSplitter` ensures text is split into manageable pieces by recursively applying separators until the chunk size constraint is satisfied.

- **Chunk Management**:  
  - Smaller chunks prevent exceeding LLM input limits.  
  - No overlap ensures efficiency, but overlap can be added if context continuity is required.  
  - Using newline as a separator preserves logical text boundaries.

- **Inspection**:  
  Printing chunk lengths and content helps verify that splitting is working as expected.

---

