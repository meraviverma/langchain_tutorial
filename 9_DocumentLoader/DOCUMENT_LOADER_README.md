
---
## 📋 PDF Use Cases and Recommended Loaders

| **Use Case**                | **Recommended Loader** |
|------------------------------|-------------------------|
| Simple, clean PDFs           | **PyPDFLoader** |
| PDFs with tables/columns     | **PDFPlumberLoader** |
| Scanned/image PDFs           | **UnstructuredPDFLoader** or **AmazonTextractPDFLoader** |
| Need layout and image data   | **PyMuPDFLoader** |
| Want best structure extraction | **UnstructuredPDFLoader** |

---

✨ This table is essentially a **decision guide** for choosing the right loader depending on the type of PDF you’re working with.  

- **PyPDFLoader** → Best for straightforward text-based PDFs.  
- **PDFPlumberLoader** → Handles structured PDFs with tables/columns.  
- **UnstructuredPDFLoader** → Flexible, works well for scanned/image PDFs and complex layouts.  
- **AmazonTextractPDFLoader** → Cloud-based option for OCR on scanned PDFs.  
- **PyMuPDFLoader** → Useful when you need both text and image/layout data.  

---

## 📋 Load vs Lazy Load in LangChain

### **load()**
- **Eager Loading** → loads everything at once.  
- **Returns**: A list of `Document` objects.  
- Loads all documents immediately into memory.  
- **Best when**:  
  - The number of documents is small.  
  - You want everything loaded upfront.  

---

### **lazy_load()**
- **Lazy Loading** → loads on demand.  
- **Returns**: A generator of `Document` objects.  
- Documents are not all loaded at once; they’re fetched one at a time as needed.  
- **Best when**:  
  - You’re dealing with large documents or lots of files.  
  - You want to stream processing (e.g., chunking, embedding) without using lots of memory.  

---

✨ In short:  
- `load()` → **eager**, good for small datasets.  
- `lazy_load()` → **lazy**, good for large datasets or streaming workflows.  

Here’s the text extracted from the image you uploaded:

---

## 📋 WebBaseLoader in LangChain

**WebBaseLoader**  
*(28 March 2025, 00:34)*  

- **Definition**: A document loader in LangChain used to **load** and **extract text content** from **web pages (URLs)**.  
- **How it works**: Uses **BeautifulSoup** under the hood to parse HTML and extract visible text.  

---

### ✅ When to Use
- Blogs  
- News articles  
- Public websites where the content is **text-based and static**  

---

### ⚠️ Limitations
- Doesn’t handle **JavaScript-heavy pages** well → use **SeleniumURLLoader** instead.  
- Loads only **static content** (HTML), not dynamic content rendered after page load.  

---

✨ In short:  
- **WebBaseLoader** is perfect for simple, static web pages.  
- For **dynamic or JS-heavy sites**, you’ll need loaders like **SeleniumURLLoader** or other specialized tools.  

# 📘 LangChain Web Loader + Google Gemini Chain

## 🔹 Function Details

1. **WebBaseLoader**
   - **Purpose**: Loads raw HTML content from a given URL (or list of URLs).
   - **Usage in Code**:  
     ```python
     loader = WebBaseLoader(url)
     docs = loader.load()
     ```
     This fetches the Flipkart product page and extracts its text content into `docs`.

2. **ChatGoogleGenerativeAI**
   - **Purpose**: Provides access to Google Gemini models through LangChain.
   - **Usage in Code**:  
     ```python
     model = ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite')
     ```
     This initializes the Gemini model for answering questions based on provided context.

3. **PromptTemplate**
   - **Purpose**: Defines a structured prompt with placeholders for dynamic input.
   - **Usage in Code**:  
     ```python
     prompt = PromptTemplate(
         template='Answer the following question \n {question} from the following text - \n {text}',
         input_variables=['question','text']
     )
     ```
     This ensures the model receives both the **question** and the **text** in a consistent format.

4. **StrOutputParser**
   - **Purpose**: Parses the model’s output into a plain string.
   - **Usage in Code**:  
     ```python
     parser = StrOutputParser()
     ```
     This strips away metadata and returns only the clean answer.

5. **Chain Composition (`|` operator)**
   - **Purpose**: Sequentially connects components (Prompt → Model → Parser).
   - **Usage in Code**:  
     ```python
     chain = prompt | model | parser
     ```
     This creates a pipeline where:
     - The **prompt** formats the input,
     - The **model** generates a response,
     - The **parser** extracts the final answer.

6. **Execution**
   - **Purpose**: Runs the chain with specific inputs.
   - **Usage in Code**:  
     ```python
     chain.invoke({'question':'What is the product that we are talking about?', 'text':docs[0].page_content})
     ```
     This passes the question and the document text into the chain, producing the answer.

---

## 🔹 Methodology Used

- **Environment Setup**:  
  `load_dotenv()` loads API keys and credentials from a `.env` file, ensuring secure configuration.

- **Document Loading**:  
  `WebBaseLoader` fetches and parses web content into structured `Document` objects.

- **Prompt Engineering**:  
  `PromptTemplate` ensures the model receives well-structured instructions with placeholders for dynamic inputs.

- **LLM Invocation**:  
  `ChatGoogleGenerativeAI` (Gemini) processes the prompt and generates a contextual answer.

- **Output Parsing**:  
  `StrOutputParser` cleans the raw model output, returning a simple string.

- **Pipeline Execution**:  
  The chain (`prompt | model | parser`) ensures modularity and readability, making it easy to extend or swap components.

---

✅ **Summary**:  
This code builds a **LangChain pipeline** that:
1. Loads product details from Flipkart,
2. Uses **Google Gemini** to answer a question about the product,
3. Returns a clean, human-readable answer.

