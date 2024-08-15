import os
from langchain_openai import OpenAI, ChatOpenAI
from langchain.memory.buffer import ConversationBufferMemory
from langchain.prompts import PromptTemplate, FewShotPromptTemplate
from langchain.chains.llm import LLMChain
import streamlit as st
from dotenv import load_dotenv, find_dotenv

from constants import FEW_SHOT_EXAMPLE
import warnings
warnings.filterwarnings("ignore")


load_dotenv(r"F:\PlayGround\GEN_AI\Introduction_to_Langchain\.env")

# load the API Key
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "")

# initialize the model
llm_model = ChatOpenAI(
    model="gpt-4o",
    temperature=0.4,
    max_tokens=1500,
)

# initialize the Memory
memory = ConversationBufferMemory()

# Initialize the Prompt example
example_travel_prompt = PromptTemplate(
    input_variables=["travel_query", "travel_response"],
    template="""
    Role: You are an intelligent Travel Agent Advisor whose job is to plan a trip based on the source and 
    destination provided by the customer query. 
    Instruction: First completely analyse the request step by step and 
    then provide your response in accurate, precise and point wise manner so that a customer easily understands the 
    mode of transportation, fare for each mode of transportation, flight number, cab number, buses number. Also, 
    suggest the alternate route/mode of transportation if not present directly from source and destination. Make sure 
    not to provide any incorrect or unfeasible information that is not useful to the customer. 
    Query: {travel_query} 
    Response: {travel_response}
    """
)

# Initialize few short template with examples
few_shot_prompt = FewShotPromptTemplate(
    examples=FEW_SHOT_EXAMPLE,
    example_prompt=example_travel_prompt,
    suffix="Travel Query: {travel_query}",
    input_variables=["travel_query"]
)

# Created a LLM chain to run the model
travel_chain = LLMChain(
    llm=llm_model,
    memory=memory,
    prompt=few_shot_prompt
)

# Set the page name
st.set_page_config(page_title="Gen AI based Travel Advisor")
# initialize the streamlit app
st.title("Travel Advisor ✈️🧳")


# Session state variables
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
else:
    # Save context based on user/assistant role and their content
    for message in st.session_state.chat_history:
        memory.save_context({"input": message["role"]}, {"output": message["content"]})
        # Displays the content for whichever role
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


input_text = st.chat_input(placeholder="Plan your Trip!!!!")

if input_text:
    # display's the user's input
    st.chat_message("user").markdown(input_text)
    # saves the user's input in the session and role will be of user
    st.session_state.chat_history.append({"role": "user", "content": input_text})
    with st.chat_message("assistant"):
        llm_response = travel_chain.invoke({"travel_query": input_text})["text"]
        # Save's the LLM response and role will be of assistant (AI)
        st.session_state.chat_history.append({"role": "assistant", "content": llm_response})
        st.markdown(llm_response)
