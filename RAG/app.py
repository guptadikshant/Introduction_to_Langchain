import os

import streamlit as st
from dotenv import find_dotenv, load_dotenv
from utils import extract_zip, rag_pipeline

load_dotenv(find_dotenv())

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "")

def get_extracted_file_path():
    pass

def main():
    extract_dir = "extracted_files"
    st.title("RAG Based Research QA Bot")
    uploaded_file = st.sidebar.file_uploader("Upload Research papers zip file", type="zip")
    submitted = st.sidebar.button(label="upload")
    
    

    if uploaded_file and submitted:
        st.sidebar.write("File uploaded")
        os.makedirs(extract_dir, exist_ok=True)
        extract_zip(uploaded_file, extract_dir)
        print(">>>>>> zip file extracted <<<<<<")
        chain = rag_pipeline(os.path.abspath(extract_dir))
        print(">>>>>> qa chain created <<<<<<")
        input_text = st.chat_input(placeholder="Please write your question here.")
        if input_text:
            if chain:
                print(chain)
                print(f"inside input text: {input_text}")
                llm_resp = chain.invoke({"query": input_text})
                st.write(llm_resp["result"])
            else:
                st.write("Please upload a research paper zip file to create the QA chain.")



if __name__ == "__main__":
    main()