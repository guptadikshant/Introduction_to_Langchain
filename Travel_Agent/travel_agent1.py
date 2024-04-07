from langchain_openai import OpenAI
from langchain.memory.summary_buffer import ConversationSummaryBufferMemory
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

conv_mem = ConversationSummaryBufferMemory(llm=llm_model)

chat_prompt = PromptTemplate(
    input_variables=["history", "input"],
    template="""
You are travel agent which advises the customer how they plan their trip with details of transport and cities.
conversation history: {history}
human: {input}
AI: 
"""
)

# intialize the streamlit app
st.title("Travel Agent Advisor")
# input_text = st.text_input("Please Enter Your Queries.......")

# Session State Variable
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
else:
    # Save context based on the user/assistant role and their content
    for message in st.session_state.chat_history:
        conv_mem.save_context({"input": message["role"]}, {"output": message["content"]})
        # Display the content for whichever role
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


conv_chain = LLMChain(
    llm=llm_model,
    prompt=chat_prompt,
    memory=conv_mem,
    verbose=True
)

input_text = st.chat_input(placeholder="Ask me anything!")

if input_text:
    # displays the user's input 
    st.chat_message('user').markdown(input_text) 
    # save the user's input in the session and role will be user
    st.session_state.chat_history.append({"role": 'user', "content": input_text}) 
    with st.chat_message("assistant"):
        llm_response = conv_chain(input_text)["text"]
        # Save's the AI response and role will be of AI
        message = {'role': 'assistant', 'content': llm_response}
        # Save's its response in the session state
        st.session_state.chat_history.append(message)
        st.write(llm_response)
