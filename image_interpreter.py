from google.cloud import vision
from google.oauth2 import service_account

# Explicitly load the service account credentials
credentials_path = "/Users/sashaampuero/Desktop/Hackathon/DeltaHacks_2025/deltahack2025-5eb312c9eedd.json" # Change to your api key path
credentials = service_account.Credentials.from_service_account_file(credentials_path)

# Pass the credentials to the Vision API client
client = vision.ImageAnnotatorClient(credentials=credentials)

# Test the client with a simple image annotation request
file_path = "lion_test.jpg"
with open(file_path, "rb") as image_file:
    content = image_file.read()

image = vision.Image(content=content)
response = client.label_detection(image=image)

# Print the detected labels
for label in response.label_annotations:
    print(f"Label: {label.description}, Score: {label.score}")
