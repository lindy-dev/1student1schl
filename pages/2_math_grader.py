import streamlit as st
import ollama 
import base64
from PIL import Image
from io import BytesIO


def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
    

def grade_math(uploaded_file_path):
    # im_bytes = uploaded_file.read()
    # file_name = uploaded_file.name
    # # Base64 encode the bytes (must decode to pass as a string)
    # im_b64 = base64.b64encode(im_bytes).decode('utf-8')
    # with open(file_name, "wb") as f:
    #     f.write(im_bytes)
    # Use the correct approach as per Gemma 3 documentation - images at top level
    response = ollama.generate(
        model='gemma3n:e4b',
        prompt="What's this? ",
        images=[uploaded_file_path],  # Pass base64 encoded image data at top level
        options={"temperature": 0.1}  # Lower temperature for more consistent output
    )
    # print(response)
    # Extract the caption from the response
    caption = response['response'].strip()
    return caption
        

st.set_page_config(
    page_title="Math Grader",
    page_icon="🧮",
)

st.title("Math Grader")

# File uploader for the math solution image
uploaded_file = st.file_uploader("Upload a picture of your solved sum", type=["png", "jpg", "jpeg"])

# Grading button
if uploaded_file and st.button("Grade"):
    # Placeholder for grading logic
    image = Image.open(uploaded_file)
    file_name = uploaded_file.name
    file_path = "data/images/" + file_name
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    # im_file = BytesIO()
    # image.save(im_file, format="JPEG")
    # im_bytes = im_file.getvalue()  # im_bytes: image in binary format.
    # im_b64 = base64.b64encode(im_bytes)
    # Read bytes from the uploaded file
    

    st.image(image, caption="Uploaded Image")
    graded_output = grade_math(file_path)

    st.success("Your solution has been sent for grading!")
    st.text_area("Output", value=graded_output, height=120, disabled=True)
elif not uploaded_file:
    st.info("Please upload an image file to grade your solution.")