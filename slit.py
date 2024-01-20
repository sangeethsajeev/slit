import os
import streamlit as st
import pdfplumber
from langchain_openai import OpenAI
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain


# Initialize a session state variable called disabled to False
st.session_state["disabled"] = False


filename = st.file_uploader(label='Drag the PDF file here. Limit 200MB', type=['pdf'])
key = os.getenv('openai_api_key')
print(key)
llm = OpenAI(temperature=0.7, openai_api_key=st.secrets["openai_api_key"])

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



# Load the Langchain chatbot
llm = ChatOpenAI(temperature=0, max_tokens=1000, model_name="gpt-3.5-turbo")
qa = ConversationalRetrievalChain.from_llm(llm, vectorstore.as_retriever())

# Initialize Streamlit chat UI
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask your questions from PDF "):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
            st.markdown(prompt)
if prompt:
    result = qa({"question": prompt, "chat_history": [(message["role"], message["content"]) for message in st.session_state.messages]})
    print(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = result["answer"]
        message_placeholder.markdown(full_response + "|")
        message_placeholder.markdown(full_response)
        print(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})
