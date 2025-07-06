import streamlit as st
import ollama 
import base64
from PIL import Image
from io import BytesIO
import os 
from pathlib import Path
import requests
 

def grade_math(uploaded_file_path):
    url = "http://localhost:11434/api/generate"
    data = {
            "model": "gemma3n:e4b",
            "prompt": f"What plant is this: {uploaded_file_path}",
            "stream": False,
            }
    # response = ollama.chat(
    #     model='gemma3n:e4b',
    #     messages=[
    #                 {
    #                 'role': 'user',
    #                 'content': 'What is in this image? Be concise.',
    #                 'images': [uploaded_file_path]  # Use the correct path here,
    #                 }
    #             ],  
    # )
    # print(response)
    response = requests.post(url, json=data)
    # Extract the caption from the response
    print(response.json())
    output= response.json().get('response')
    return output
        

st.set_page_config(
    page_title="Plant Identifier",
    page_icon="🌱",
)

st.title("Plant Identifier")

# File uploader for the math solution image
uploaded_file = st.file_uploader("Upload a picture of your mystery plant", type=["png", "jpg", "jpeg"])

# Grading button
if uploaded_file and st.button("Identify Plant"):
    # Placeholder for grading logic
    image = Image.open(uploaded_file)
    os.makedirs('./data/images', exist_ok=True)
    # Get the file extension and format
    filename = uploaded_file.name
    ext = filename.split('.')[-1].lower()
    valid_exts = ['jpg', 'jpeg', 'png']
    img_format = 'JPEG' if ext in ['jpg', 'jpeg'] else 'PNG'
    # Use appropriate extension if user uploads in jpg/jpeg/png
    if ext not in valid_exts:
        st.error("Unsupported file type. Please upload a PNG, JPG, or JPEG image.")
    else:
        filepath = f'./data/images/{filename}'
        image.save(filepath, format=img_format)
        st.image(image, caption="Uploaded Image")
        graded_output = grade_math(uploaded_file_path=filepath)
        # Display the graded output
        st.success("Your mystery plant has been identified!")
        st.markdown(f"**Plant Identification Result:** {graded_output}")
elif not uploaded_file:
    st.info("Please upload an image file of your mystery plant to get started.")