import streamlit as st
import numpy as np
import pandas as pd # used for data like graphs and tables

st.title("Sasha Ampuero was here!")
uploaded_file = st.file_uploader("Choose a PDF file: ", type="pdf") # give a pdf

if uploaded_file is not None:
    st.write("File Uploaded...")

x = st.slider('x')  # 👈 this is a widget slider
st.write(x, 'squared is', x * x)

st.write("Here's our first attempt at using data to create a table:") # data table
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

if st.checkbox('Show dataframe'): # Togglable data frame
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data
