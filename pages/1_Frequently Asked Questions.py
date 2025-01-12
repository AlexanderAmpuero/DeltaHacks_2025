import streamlit as st
import base64

st.title("Frequently Asked Questions")

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


# Expander for Frequently Asked Questions
with st.expander("What is Trash Map?"):
    st.subheader("The Web App")
    st.markdown(
        """
        Trash Map is a Streamlit-based web app that uses image recognition to identify trash, determine the correct disposal bin (e.g., recycling, compost, landfill), and show nearby bin locations on a university campus. It promotes proper waste segregation, reduces contamination, and supports sustainability efforts by simplifying responsible waste disposal for users. 
        """
    )
with st.expander("What's the point of Trash Map?"):
    st.subheader("Sustainable Waste Management")
    st.markdown(
        """
        Trash Map is important because it promotes sustainable waste management and environmental awareness. 
        By identifying trash through image recognition and directing users to the correct disposal bin, 
        it reduces contamination in recycling and compost streams, ensuring waste is properly processed. 
        Locating nearby bins simplifies responsible disposal, encouraging eco-friendly habits. 
        For universities, it minimizes landfill waste, lowers operational costs, and supports green initiatives, 
        fostering a cleaner campus. Additionally, it educates users on waste segregation, 
        empowering them to make environmentally conscious decisions. In the long term, 
        tools like Trash Map help combat pollution, conserve resources, and contribute to a sustainable future.
        """
    )
with st.expander("How does Trash Map work?"):
    st.subheader("Use Image and Find Disposal")
    st.markdown(
        """
        Trash Map works by combining image recognition and location mapping to simplify waste disposal:
        - Image Upload: Users upload a photo of trash through the app.
        - Trash Identification: A machine learning model analyzes the image to identify the type of trash (e.g., plastic, paper, organic).
        - Bin Recommendation: The app matches the trash type to the appropriate bin category (e.g., recycling, compost, landfill).
        - Bin Locations: It displays a map showing nearby garbage bins on the university campus for easy disposal.
        
        This process helps users dispose of waste correctly and sustainably.
        """
    )
with st.expander("Do I need to create an account to use Trash Map?"):
    st.subheader("No Need")
    st.markdown(
        """
        No, you don’t need to create an account to use Trash Map. The app is designed for quick and easy access, allowing anyone to upload an image, 
        identify trash, and find nearby bins without the need for registration or login.
        """
    )
with st.expander("Is my data (e.g., uploaded images) stored or shared?"):
    st.subheader("Not Stored or Shared")
    st.markdown(
        """
        No, your data is not stored or shared. Uploaded images are processed temporarily for trash identification and are not saved on the server or shared with third parties. 
        Trash Map prioritizes user privacy by handling data securely and ensuring that all processing happens in real-time without retaining any personal information or images.
        """
    )

with st.expander("What should I do if the app isn’t working properly?"):
    st.subheader("Follow the Steps")
    st.markdown(
        """
        If the app isn’t working properly, try the following steps:
        1. Refresh the Page: Reload the app to resolve temporary issues.
        2. Check Your Internet Connection: Ensure you’re connected to a stable network.
        3. Verify File Format: Make sure the uploaded image is in a supported format (e.g., JPG, PNG).
        4. Clear Cache: Clear your browser cache and try again.
        5. Report the Issue: Contact the support team with details about the problem on the report page and any error messages you see.
        """
    )
with st.expander("Who are we?"):
    st.subheader("Mutable Tuples")
    st.markdown(
        """
        Our names are Sasha, Martin, and Daniel and we call ourselves Mutable Tuples. They call it impossible, but we call it possible. 
        """
    )
