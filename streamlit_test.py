import streamlit as st

st.title("Sasha Ampuero was here!")
uploaded_file = st.file_uploader("Choose a PDF file: ", type="pdf")

if uploaded_file is not None:
    st.write("File Uploaded...")

