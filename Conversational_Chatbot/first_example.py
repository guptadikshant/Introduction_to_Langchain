from langchain_openai import OpenAI
from langchain.memory.buffer import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
import streamlit as st
from dotenv import load_dotenv

load_dotenv(".env")

# intialize the LLM Model
llm_model = OpenAI(
    model="gpt-3.5-turbo-instruct",
    temperature=0.6,
    verbose=True
)

conv_mem = ConversationBufferMemory()

chat_prompt = PromptTemplate(
    input_variables=["history", "input"],
    template="""
You are a conversational Chatbot which helps to resolve people queries.
conversation history: {history}
human: {input}
AI: 
"""
)

# intialize the streamlit app
st.title("Simple ChatBot Demo")
# input_text = st.text_input("Please Enter Your Queries.......")

# Session State Variable
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
else:
    for message in st.session_state.chat_history:
        conv_mem.save_context({"input": message["human"]}, {"output": message["AI"]})


conv_chain = LLMChain(
    llm=llm_model,
    prompt=chat_prompt,
    memory=conv_mem,
    verbose=True
)

input_text = st.chat_input(placeholder="Ask me anything!")

if input_text:
    st.chat_message('human').write(input_text)
    with st.chat_message("assistant")   :
        llm_response = conv_chain(input_text)["text"]
        message = {'human': input_text, 'AI': llm_response}
        st.session_state.chat_history.append(message)
        st.write(llm_response)

