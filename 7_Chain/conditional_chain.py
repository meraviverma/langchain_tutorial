from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, EmailStr, Field
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.runnables import RunnableParallel
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda
from typing import Literal

load_dotenv()

#Model 1
model = ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite')

parser = StrOutputParser()

class Feedback(BaseModel):

    sentiment: Literal['positive', 'negative'] = Field(description='Give the sentiment of the feedback')

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback text into postive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt2 | model | parser),
    (lambda x:x.sentiment == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x: "could not find sentiment")
)

chain = classifier_chain | branch_chain

print(chain.invoke({'feedback': 'This is a beautiful phone'}))

chain.get_graph().print_ascii()

#################### OUTPUT ##############################

# To provide the best response, it helps to know the context (e.g., a customer review, an email from a boss, or a message from a client). Here are a few options based on the situation:

# ### Option 1: Professional (Best for clients or business partners)
# > "Thank you so much for your kind words! It has been a pleasure working with you, and I’m thrilled to hear that you’re happy with the results. We truly value your support and look forward to our continued partnership."

# ### Option 2: Customer-Facing (Best for reviews or feedback on a product)
# > "Thank you for the wonderful feedback! We are so glad to hear you’re enjoying [Product/Service Name]. Our team works hard to provide the best experience possible, and it’s always rewarding to hear from happy customers like you."

# ### Option 3: Internal (Best for a manager or colleague)
# > "Thank you so much for the feedback! I really appreciate you taking the time to share your thoughts. It’s been a great experience working on this project, and I’m glad we were able to achieve such a positive outcome together."

# ### Option 4: Short & Casual (Best for social media or quick messages)
# > "Thanks so much for the kind words! It’s great to hear that you had a positive experience. We really appreciate your support!"

# ---

# **A few tips for customizing these:**
# *   **Be specific:** If they mentioned a specific feature or team member, acknowledge it (e.g., *"I'll be sure to pass your praise along to Sarah, she'll be thrilled to hear it!"*).
# *   **Keep it prompt:** Sending a thank-you response shortly after receiving the feedback shows that you genuinely value their opinion.
# *   **Personalize it:** Using the sender’s name makes the response feel much more sincere.
#       +-------------+      
#       | PromptInput |      
#       +-------------+      
#              *             
#              *             
#              *             
#     +----------------+     
#     | PromptTemplate |     
#     +----------------+     
#              *             
#              *             
#              *             
# +------------------------+ 
# | ChatGoogleGenerativeAI | 
# +------------------------+ 
#              *             
#              *             
#              *             
#  +----------------------+  
#  | PydanticOutputParser |  
#  +----------------------+  
#              *             
#              *             
#              *             
#         +--------+         
#         | Branch |         
#         +--------+         
#              *             
#              *             
#              *             
#      +--------------+      
#      | BranchOutput |      
#      +--------------+ 