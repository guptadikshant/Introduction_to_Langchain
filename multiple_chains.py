from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain.chains.sequential import SimpleSequentialChain
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

st.title("Langchain Demo with LLMS")
input_text = st.text_input("Search the topic you want.....")

llm_model = OpenAI(
    temperature=0.8
)

## First Input Prompt

first_input_template = PromptTemplate(
    input_variables=["name"],
    template="Tell me about {name}"
)

chain_1 = LLMChain(
    llm=llm_model,
    prompt=first_input_template,
    verbose=True,
    output_key="person"
)

second_input_template = PromptTemplate(
    input_variables=["person"],
    template="when was this {person} born",
)

chain_2 = LLMChain(
    llm=llm_model,
    prompt=second_input_template,
    verbose=True,
    output_key="dob"
)

main_chain = SimpleSequentialChain(
    chains=[chain_1, chain_2],
    verbose=True
)

if input_text:
    st.write(main_chain.run(input_text))