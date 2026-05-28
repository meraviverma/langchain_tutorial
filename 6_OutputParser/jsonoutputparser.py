from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

# Define the model
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Pro",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template = PromptTemplate(
    #template='Give me 5 facts about {topic} \n {format_instruction}',
    template='Give me the name , age and city of a fictional person \n {format_instruction}',
    #input_variables=['topic'],
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser

result_chain = chain.invoke({})


# One approach is to do it step by step
prompt=template.format()
print(prompt)

result=model.invoke(prompt)

print(result)

final_result=parser.parse(result.content)

print(final_result)

print("Name:",final_result['name'])
print("Age:",final_result['age'])
print("City:",final_result['city'])
#print(parser.parse(result.content))

print("---------Result Chain----------------")
print(result_chain)

#Can't enforce schema in json output parser but we can parse the output to get the required information.