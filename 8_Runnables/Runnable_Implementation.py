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


# Sequential Chain#

prompt1 = PromptTemplate(
    template= "Write a joke about {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template= "Explain the following joke - {text}",
    input_variables=['text']
)

chain = RunnableSequence(prompt1 , model , parser , prompt2, model ,parser)

result = chain.invoke({'topic' : 'Data Engineering'})


print(result)
# Parallel Runnable #

prompt1 = PromptTemplate(
    template= "Generate a tweet about {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template= "Generate a linkedin post about {topic}",
    input_variables=['topic']
)


parser = StrOutputParser()

parallel_chain = RunnableParallel({
        'tweet' : RunnableSequence(prompt1 , model , parser),
        'linkedin' : RunnableSequence(prompt2 , model , parser)
    }
)

result = parallel_chain.invoke({'topic' : 'Apache-Kafka'})

print(result)
# Runnable Branch with Runnable Passthrough and Runnable Lambda (word_count is used here as custom Python Function)#

def word_count(text) :
    return int(len(text.split()))

prompt1 = PromptTemplate(
    template= "Write a detailed report about {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template= "Summarize the following {text}",
    input_variables=['text']
)

model = ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite')

parser = StrOutputParser()

report_chain = RunnableSequence(prompt1 , model , parser)

branch_chain = RunnableBranch( 
    (lambda x : len(x.split()) > 300 , RunnableSequence(prompt2 , model , parser)),
    RunnablePassthrough()
 )

final_chain = RunnableSequence(report_chain , branch_chain)

result = final_chain.invoke({'topic' : 'Attention is all you need!'})

print(result)