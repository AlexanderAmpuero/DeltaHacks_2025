import streamlit as st
import base64

# Function to convert image to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

# Path to your logo image
logo_path = "UI_images/github.png"
base64_logo = get_base64_image(logo_path)

# Use HTML and CSS to display the logo at the top-right corner
st.markdown(
    f"""
    <style>
        .logo-container {{
            position: absolute;
            top: -40px;
            right: 0px;
            z-index: 1000; /* Ensures it stays on top */
        }}
        .logo {{
            width: 50px; /* Adjust the size of your logo */
            height: auto;
        }}
    </style>
    <div class="logo-container">
        <a href="https://github.com/AlexanderAmpuero/DeltaHacks_2025" target="_blank">
            <img class="logo" src="data:image/png;base64,{base64_logo}" alt="Logo">
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)

# Load the image
image_path = "UI_images/Mut_tup.png"
base64_image = get_base64_image(image_path)
# Use HTML and CSS to place the image at the top of the sidebar
st.sidebar.markdown(
    f"""
    <style>
        .sidebar-img-container {{
            display: flex;
            justify-content: center;
            margin-bottom: 20px;
        }}
        .sidebar-img {{
            width: 100%; /* Adjust size as needed */
            border-radius: 10px; /* Optional: Add rounded corners */
        }}
    </style>
    <div class="sidebar-img-container">
        <img class="sidebar-img" src="data:image/png;base64,{base64_image}" alt="Sidebar Image">
    </div>
    """,
    unsafe_allow_html=True,
)

st.title("Report!")
st.title("Trash Map - Report an Issue")
st.write("If you encounter any problems or have questions, please use the form below to report them.")

# Create a form for user input
with st.form(key="report_form"):
    # Email input
    user_email = st.text_input("Your Email (optional)", placeholder="you@example.com")
    
    # Problem/Question input
    user_problem = st.text_area("Your Question or Problem", placeholder="Describe your issue or question here...")
    
    # Submit button
    submit_button = st.form_submit_button("Submit")
    
    if submit_button:
        if user_problem.strip():  # Check if the question/problem is not empty
            st.success("Thank you for your report! We’ll get back to you soon.")
            # You can add code here to save the data or send an email
            # Example: save_report(user_email, user_problem)
        else:
            st.error("Please describe your question or problem before submitting.")