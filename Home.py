import streamlit as st
import pandas as pd
import numpy as np

# Sidebar for user input
st.sidebar.header("User Input")
name = st.sidebar.text_input("What's your name?", "Guest")
age = st.sidebar.slider("How old are you?", 0, 100, 25)

# Title and Introduction
st.title(":deciduous_tree: Trash Map :deciduous_tree:")
st.markdown("""Welcome to Trash Map! This web app demonstrates basic components like text, user inputs, and charts.""")

st.divider()

# Camera Testing
st.subheader("Garbage Identifier")
enable = st.button("Enable/Reset Camera")
picture = st.camera_input("Hey Garbage! Say Cheese!", disabled=not enable)
if picture:
    trash_pic = st.image(picture)

# Data upload and display
uploaded_file = st.file_uploader("Choose picture", type=["jpg"])
if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("Preview of your data:")
    st.dataframe(data)
    st.bar_chart(data.select_dtypes(include=[np.number]))

# Expander
with st.expander("What's the point of Trash Map?"):
    st.subheader("DeltaHacks 2024")
    st.markdown(
        """
        This project is a submission for the [Streamlit Connections Hackathon 2023](https://discuss.streamlit.io/t/connections-hackathon/47574).
        It delivers a Streamlit connector for the open-source vector database, [Weaviate](https://weaviate.io/). 
        Magic Chat uses the Weaviate connector to search through [Magic The Gathering](https://magic.wizards.com/en) cards with various search options, such as BM25, Semantic Search, Hybrid Search and Generative Search. 
        You can find the submission in this [GitHub repo](https://github.com/weaviate/st-weaviate-connection/tree/main)
        """
    )
7
