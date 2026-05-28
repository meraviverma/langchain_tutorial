from langchain_experimental.text_splitter import SemanticChunker
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview")

text_splitter = SemanticChunker(
    embeddings,
    breakpoint_threshold_type="percentile",
    breakpoint_threshold_amount=80
)

sample = """
Farmers were working hard in the fields, preparing the soil and planting seeds for the next season. The sun was bright, and the air smelled of earth and fresh grass. The Indian Premier League (IPL) is the biggest cricket league in the world. People all over the world watch the matches and cheer for their favourite teams.


Terrorism is a big danger to peace and safety. It causes harm to people and creates fear in cities and villages. When such attacks happen, they leave behind pain and sadness. To fight terrorism, we need strong laws, alert security forces, and support from people who care about peace and safety.

API keys that are unrestricted are vulnerable to bad actors and unauthorized use. Starting June 19, 2026, to improve security, the Gemini API will discontinue support for unrestricted traffic keys.This means that your Gemini API requests will fail if you don't take action.To continue using the Gemini API without interruption, secure your traffic keys by adding
"""

docs = text_splitter.create_documents([sample])
print(len(docs))
for i, doc in enumerate(docs, 1):
    print(f"\nChunk {i}:\n{doc.page_content}")