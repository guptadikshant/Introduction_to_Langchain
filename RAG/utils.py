import os
import zipfile

from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.chroma import Chroma
from langchain_community.document_loaders.pdf import PyPDFDirectoryLoader
from langchain_openai import OpenAI, OpenAIEmbeddings
from langchain.memory.buffer import ConversationBufferMemory


def extract_zip(zip_file_path, extract_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)


def read_pdfs(dir_path):
    loader = PyPDFDirectoryLoader(dir_path)
    docs = loader.load()
    return docs


def convert_docs_into_chunks(documents):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splitted_docs = text_splitter.split_documents(documents)
    return splitted_docs

def create_embeddings_and_store_vectordb(texts):
    persist_dir = "db"
    openai_embedding = OpenAIEmbeddings()
    vectordb = Chroma(
    persist_directory=os.path.abspath(persist_dir), 
    embedding_function=openai_embedding
)
    
    if vectordb._collection.count() == 0:
        vectordb = Chroma.from_documents(
            documents=texts,
            embedding=openai_embedding,
            persist_directory=persist_dir,
            collection_name="RAG"
        )

        vectordb.persist()
    
    
    retriever = vectordb.as_retriever()

    return retriever

def create_qa_chain(retriever):    
    qa_chain = RetrievalQA.from_chain_type(
        llm=OpenAI(temperature=0.4),
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True
)
    return qa_chain
    
def rag_pipeline(dir_path):
    docs = read_pdfs(dir_path)
    splitted_docs = convert_docs_into_chunks(docs)
    retriver = create_embeddings_and_store_vectordb(splitted_docs)
    rag_qa_chain = create_qa_chain(retriver)

    return rag_qa_chain

