from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain

from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

st.title("Langchain Demo with LLMS")
input_text = st.text_input("Search the topic you want.....")

## First Input Prompt

first_input_template = PromptTemplate(
    input_variables=["name"],
    template="Tell me about {name}"
)


llm_model = OpenAI(
    temperature=0.8
)

chain = LLMChain(
    llm=llm_model,
    prompt=first_input_template,
    verbose=True
)

if input_text:
    st.write(chain.run(input_text))