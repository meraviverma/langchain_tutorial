from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",   # pick the Gemini model
    temperature=1.0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

result = llm.invoke("What is the capital of India")

# Gemini sometimes returns structured parts, so safest is:
def get_text(result):
    if isinstance(result, list):
        # handle list of dicts
        return " ".join([part["text"] for part in result if part.get("type") == "text"])
    elif hasattr(result, "content"):
        # handle AIMessage
        return result.content
    return str(result)

print(get_text(result))
