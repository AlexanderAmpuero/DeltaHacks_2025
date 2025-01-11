
import streamlit as st
from openai import OpenAI
from google.cloud import vision
from google.oauth2 import service_account



def init_google():
    credentials_path = ".streamlit/googlekey.json"
    credentials = service_account.Credentials.from_service_account_file(credentials_path)
    client = vision.ImageAnnotatorClient(credentials=credentials)
    return client

def init_perplexity():
    api_key = st.secrets['api_keys']['perplexity']
    if not api_key:
        st.error("Please set Pp api key")
        return None
    return OpenAI(api_key=api_key, base_url="https://api.perplexity.ai")

def main():
    # Title
    st.title("Recycling App")
    
    # Initialize keys
    google_client = init_google()
    pp = init_perplexity()
    
    if pp is None:
        return
    
    user_query = st.text_input("Enter your query:")
    
    messages = [
    {
        "role": "user",
        "content": user_query
    }
    ]
    
    if user_query:
        response = pp.chat.completions.create(model="llama-3.1-sonar-large-128k-online", messages=messages)
        
        st.write("Response from Perplexity:")
        st.write(response)
    
    
    
    
    
    
    
if __name__ == "__main__":
    main()

