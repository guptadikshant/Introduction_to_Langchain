import os
import zipfile
import streamlit as st


def extract_zip(zip_file_path, extract_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)


def main():
    st.title("RAG Based Research QA Bot")
    uploaded_file = st.sidebar.file_uploader("Upload Research papers zip file", type="zip")

    submitted = st.sidebar.button(label="upload")

    if uploaded_file and submitted:
        st.sidebar.write("File uploaded")
        extract_dir = "extracted_files"
        os.makedirs(extract_dir, exist_ok=True)
        

        extract_zip(uploaded_file, extract_dir)


if __name__ == "__main__":
    main()