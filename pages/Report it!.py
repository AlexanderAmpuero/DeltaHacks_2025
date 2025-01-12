import streamlit as st

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