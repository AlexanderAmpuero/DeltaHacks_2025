
import streamlit as st
from openai import OpenAI
from google.cloud import vision
from google.oauth2 import service_account
import json


# GOOGLE VISION CLIENT
def init_google():
    credentials_path = ".streamlit/googlekey.json"
    credentials = service_account.Credentials.from_service_account_file(credentials_path)
    client = vision.ImageAnnotatorClient(credentials=credentials)
    return client

# PERPLEXITY API
def init_perplexity():
    api_key = st.secrets['api_keys']['perplexity']
    if not api_key:
        st.error("Please set Pp api key")
        return None
    return OpenAI(api_key=api_key, base_url="https://api.perplexity.ai")

# ANALYZE IMAGE
def analyze_img(gcv, img):
    # Get GCV Response
    image=vision.Image(content=img)
    response=gcv.label_detection(image=image)
    
    return response.label_annotations[0].description

def determine_category(pp, item):
    with open('category.json') as f:
        categories = json.load(f)
    
    messages = [
        {
            "role": "user",
            "content": f"You are a waste sorting assistant that identifies an item based on established categories. Identify items precisely. If an item does not fit into any category, return 'False'. Item: {item}. Categories: {categories}. Return precisely the name of the category and nothing else."
        }
    ]
    
    response = pp.chat.completions.create(model="llama-3.1-sonar-large-128k-online", messages=messages)
    
    st.write("Response from Perplexity")
    st.write(response.choices[0])
    
    

# MAIN FUNCTION
def main():
    # Title
    st.title("Recycling App")
    
    # Initialize keys
    gcv = init_google()
    pp = init_perplexity()
    
    # Get Image
    img = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    
    if img:
        with st.spinner("Analyzing image..."):
            img_bytes = img.read()
            item = analyze_img(gcv, img_bytes)
            
            st.write(f"Detected Item: {item}")
            
            item_category = determine_category(pp, item)
            
            

            
            
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    main()

