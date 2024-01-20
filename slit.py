
import streamlit as st
import pdfplumber
from langchain_openai import OpenAI


# Initialize a session state variable called disabled to False
st.session_state["disabled"] = False


filename = st.file_uploader(label='Drag the PDF file here. Limit 200MB', type=['pdf'])

llm = OpenAI(temperature=0.7, openai_api_key='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')

# Initialize a session state variable called disabled to False
st.session_state["disabled"] = False


filename = st.file_uploader(label='Drag the PDF file here. Limit 200MB', type=['pdf'])

text = 'some text string'

if filename is not None:
    # Read the text from the PDF file
    with pdfplumber.open(filename) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
