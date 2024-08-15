import os
import streamlit as st
from dotenv import find_dotenv, load_dotenv
from utils import rag_pipeline

load_dotenv(find_dotenv())

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "")

st.title("RAG Based Research QA Bot")
st.subheader("This is subheader heading")

input_text = st.text_input(label="Enter your questions here.")  



if input_text and "rag_qa_chain" not in st.session_state:
    st.session_state.rag_qa_chain = rag_pipeline(os.path.join(os.getcwd(), "RAG", "ml_research_papers"))
    print(">>>>>>> qa chain created <<<<<<<")

if "rag_qa_chain" in st.session_state:
    rag_chain = st.session_state.rag_qa_chain
    llm_response = rag_chain.invoke({"input": input_text})
    st.write(llm_response["answer"])