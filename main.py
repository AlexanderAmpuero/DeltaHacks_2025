import streamlit as st
from openai import OpenAI
from google.cloud import vision
from google.oauth2 import service_account
import json
import re


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
    
    try:
        # Get GCV Response
        image=vision.Image(content=img)
        response=gcv.label_detection(image=image)
        
        return response.label_annotations[0].description
    except:
        return False

# DETERMINE CATEGORY
def determine_category(pp, item):
    with open('category.json') as f:
        categories = json.load(f)
    
    messages = [
        {
            "role": "user",
            "content": f"You are a waste sorting assistant that identifies an item based on established categories. Identify items precisely. If an item does not fit into any category, return 'False'. Item: {item}. Categories: {categories}. You must respond with precisely the key of the category and nothing else."
        }
    ]
    
    response = pp.chat.completions.create(model="llama-3.1-sonar-large-128k-online", messages=messages)
    category = response.choices[0].message.content
    cleaned_category = re.sub(r'\[.*?\]', '', category).strip()

    if cleaned_category in categories:
        return cleaned_category
    else:
        return False
    
# NO CATEGORY
def no_category(pp, item):
    with open('category.json') as f:
        categories = json.load(f)
    
    user_query = f"Explain to me why in 3 sentences or less, point form, why {item} is not in {categories}. You are a waste sorting algorithm"
    messages = [
        {
            "role": "user",
            "content": user_query
        }
    ]
    
    response = pp.chat.completions.create(model="llama-3.1-sonar-large-128k-online", messages=messages)
    st.write(response.choices[0].message.content)
    
# DISPLAY INSTRUCTIONS
def display_instructions(pp, item_category):
    with open('category.json') as f:
        categories = json.load(f)
    
    user_query = f"Explain to me in 3 sentences or less, point form, how to dispose of an item with key {item_category} in {categories}. Avoid using headings."
    messages = [
        {
            "role": "user",
            "content": user_query
        }
    ]
    
    response = pp.chat.completions.create(model="llama-3.1-sonar-large-128k-online", messages=messages)
    instructions = response.choices[0].message.content
    cleaned_instructions = re.sub(r'\[.*?\]', '', instructions).strip()
    
    st.write(cleaned_instructions)

# MAIN FUNCTION
def main():
    # Title
    st.title("Recycling App")
    
    # Initialize keys
    gcv = init_google()
    pp = init_perplexity()
    
    # Get Image
    img = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    
    # After Image Submission
    if img:
        with st.spinner("Analyzing image..."):
            # Get Item
            img_bytes = img.read()
            item = analyze_img(gcv, img_bytes)
            
            if item == False:
                st.write("Error detecting item")
                return
            
            st.write(f"Detected Item: {item}")
            
            # Get Category
            item_category = determine_category(pp, item)
            
            # No Category
            if item_category == False:
                no_category(pp, item)
                return
            
            # Instructions for Disposal
            st.write(f"Item Category: {item_category}")
            display_instructions(pp, item_category)
            
            
            

            
            
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    main()

