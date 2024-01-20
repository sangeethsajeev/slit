
import streamlit as st



# Initialize a session state variable called disabled to False
st.session_state["disabled"] = False


filename = st.file_uploader(label='Drag the PDF file here. Limit 200MB', type=['pdf'])
