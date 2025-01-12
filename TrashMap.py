import streamlit as st
from openai import OpenAI
from google.cloud import vision
from google.oauth2 import service_account
import json
import re
import pandas as pd
import numpy as np
import base64
import requests  # Import requests for making API calls
import googlemaps


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

# CHECK POSTAL CODE
def is_valid_postal_code(postal_code):
    pattern = r'^[A-Za-z]\d[A-Za-z][ -]?\d[A-Za-z]\d$' 
    return bool(re.match(pattern, postal_code))

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
def determine_category(pp, item, categories):
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
def no_category(pp, item, categories):
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
    instructions = response.choices[0].message.content
    cleaned_instructions = re.sub(r'[.*?]', '', instructions).strip()

    st.write(response.choices[0].message.content)

# DISPLAY INSTRUCTIONS
def display_instructions(pp, item_category, categories):
    user_query = f"Explain to me in 3 sentences or less, point form, how to dispose of an item with key {item_category} in {categories}. Start your answer with {item_category}.name: To dispose of an item in this category..."
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

# GOOGLE GEOCODING API: Convert postal code to latitude and longitude
def get_lat_lng(postal_code, api_key):
    # Base URL for Google Geocoding API
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    
    # Parameters for the API request
    params = {
        "address": postal_code,
        "key": api_key
    }
    
    # Send GET request to the API
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if len(data["results"]) > 0:
            # Extract latitude and longitude
            location = data["results"][0]["geometry"]["location"]
            return location["lat"], location["lng"]
        else:
            st.write("No results found for the provided postal code.")
            return None, None
    else:
        st.write(f"Error: {response.status_code}")
        return None, None

# MAIN FUNCTION
def main():
    # Title and Introduction
    st.title(":deciduous_tree: Trash Map :deciduous_tree:")
    st.divider()

    # Initialize keys
    gcv = init_google()
    pp = init_perplexity()
    
    # Get postal code
    st.header("1. Enter your postal code")
    postal_code = st.text_input("", label_visibility="collapsed")

    # Get image through either image or camera
    st.header("2. Take a photo or upload an image")
    camera_image = st.camera_input("", label_visibility="collapsed")
    img = st.file_uploader("", type=["jpg", "jpeg", "png"], label_visibility="collapsed")

    # Submit Button
    st.header("3. Get results")
    submit = st.button("Submit", use_container_width=True)
    
    # After Image Submission
    if submit and postal_code and (img or camera_image):
        # Get JSON contents
        with st.spinner("Analyzing image..."):
            with open('category.json') as f:
                categories = json.load(f)
            
            is_valid = is_valid_postal_code(postal_code)

            if not is_valid:
                st.error("Error with postal code")
                return

            # Get Item
            img_bytes = img.read() if img else base64.b64encode(camera_image.getvalue()).decode('utf-8')
            item = analyze_img(gcv, img_bytes)
            
            if item == False:
                st.error("Error detecting item")
                return
            
            with st.chat_message("user"):
                st.write(f"Detected Item: {item}")
            
            # Get Category
            item_category = determine_category(pp, item, categories)
            
            # No Category
            if item_category == False:
                st.header("Cannot be Recycled")
                no_category(pp, item, categories)
                return
            
            # Instructions for Disposal
            st.header("Recycling Instructions")
            display_instructions(pp, item_category, categories)

            # Mapping Code
            # Replace 'YOUR_API_KEY' with your actual API key for Google Geocoding
            API_KEY = 'AIzaSyAOCuaXG6CsoWpopF7nJQwV0gZMNVfgxnU'
            latitude, longitude = get_lat_lng(postal_code, API_KEY) # postal code lat and lon

            # Replace 'YOUR_API_KEY' with your actual API key for google places
            API_KEY = 'AIzaSyCbWRimxXzz13a-4Xmr_aeAK-EMBS0nFPQ'

            # Initialize the client
            gmaps = googlemaps.Client(key=API_KEY)

            # Example: Search for nearby places (e.g., restaurants within 1000 meters)
            places_result = gmaps.places_nearby(location=f"{latitude}, {longitude}", radius=10000, type=f'{item_category} waste disposal')
            # Extract latitude and longitude for each place
            if places_result["results"]:
                lat = places_result["results"][0]["geometry"]["location"]["lat"]
                lon = places_result["results"][0]["geometry"]["location"]["lng"]
            else:
                st.write("No results found.")

            if latitude and longitude:
                
                # Now create a DataFrame for plotting
                coordinates = {
                    'lat': [lat, lat - 0.01],  # Latitude values
                    'lon': [lon, lon - 0.01]  # Longitude values
                }
                # Create a DataFrame
                df = pd.DataFrame(coordinates)
                # Header
                st.header("Nearest Recycling Location")
                # Plot the coordinates on a map
                st.map(df)

if __name__ == "__main__":
    main()
