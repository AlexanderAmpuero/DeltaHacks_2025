from google.cloud import vision
from google.cloud.vision import types
import io

# Path to your Google Cloud credentials file (JSON)
# If you're using an API Key, you won't need this line
# Set your GOOGLE_APPLICATION_CREDENTIALS environment variable to the path of your credentials file
# Example: export GOOGLE_APPLICATION_CREDENTIALS='/path/to/your/credentials.json'

# Initialize the Vision API client
client = vision.ImageAnnotatorClient()

# Open the image file you want to test (replace 'your_image.jpg' with your image path)
with io.open('lion_test.jpg', 'rb') as image_file:
    content = image_file.read()

# Create an image instance from the content
image = types.Image(content=content)

# Use the Vision API to analyze the image
response = client.label_detection(image=image)

# Get the labels returned by the Vision API
labels = response.label_annotations

# Print out the labels detected in the image
print("Labels found in image:")
for label in labels:
    print(label.description)

# Check for errors in the API response
if response.error.message:
    print(f"Error: {response.error.message}")
