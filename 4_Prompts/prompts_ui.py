from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()
#model = ChatOpenAI()
model = ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite')


st.header('Reasearch Tool')

user_input = st.text_input("Enter your prompt here")

if st.button('Submit'):
    result = model.invoke(user_input)
    st.write(result.content)
