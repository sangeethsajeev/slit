import os
import streamlit as st
import pdfplumber
from langchain_openai import OpenAI
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS


# Initialize a session state variable called disabled to False
st.session_state["disabled"] = False


filename = st.file_uploader(label='Drag the PDF file here. Limit 200MB', type=['pdf'])

llm = OpenAI(temperature=0.7, openai_api_key='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')

# Initialize a session state variable called disabled to False
st.session_state["disabled"] = False


text = 'some text string'

if filename is not None:
    # Read the text from the PDF file
    with pdfplumber.open(filename) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()

text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150,
        length_function=len
    )


# Process the PDF text and create the documents list
documents = text_splitter.split_text(text=text)

# Vectorize the documents and create vectorstore
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_texts(documents, embedding=embeddings)

st.session_state.processed_data = {
    "document_chunks": documents,
    "vectorstore": vectorstore,
}
