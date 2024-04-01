from langchain_openai import OpenAI


from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

st.title("Langchain Demo with LLMS")
input_text = st.text_input("Search the topic you want.....")

llm_model = OpenAI(
    temperature=0.8
)

if input_text:
    st.write(llm_model(input_text))