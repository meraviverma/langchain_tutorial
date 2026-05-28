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
    template= "Write a joke about {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template= "Explain the following joke - {text}",
    input_variables=['text']
)

chain = RunnableSequence(prompt1 , model , parser , prompt2, model ,parser)

print(chain.invoke({'topic' : 'AI'}))