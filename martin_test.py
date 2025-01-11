import streamlit as st
import pandas as pd
import numpy as np

# Sidebar for user input
st.sidebar.header("User Input")
name = st.sidebar.text_input("What's your name?", "Guest")
age = st.sidebar.slider("How old are you?", 0, 100, 25)

# Title and Introduction
st.title(":deciduous_tree: Trash Map :deciduous_tree:")
st.markdown("""Welcome to Trash Map! This app demonstrates basic components like text, user inputs, and charts.""")

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
















# Display input
st.subheader(f"Hello, {name}!")
st.write(f"You are {age} years old.")

# Generating random data for visualization
st.subheader("Random Data Visualization")
chart_data = pd.DataFrame(
    np.random.randn(50, 3), 
    columns=['A', 'B', 'C']
)

# Line chart
st.line_chart(chart_data)

# Footer
st.markdown("Made with ❤️ using Streamlit.")
