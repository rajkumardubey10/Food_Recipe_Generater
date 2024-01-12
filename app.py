from dotenv import load_dotenv

load_dotenv() # loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Google Geminipro Vision API and get respose

def get_gemini_response(input,image,prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response= model.generate_content([input,image[0],prompt])
    return response.text


def input_image_setup(uploaded_file):
    # check if a file has been uploaded
    if uploaded_file is not None:
        #read the file into bytes
        bytes_data= uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("File not uploaded or No file uploaded")
    

# initialize our streamlit app
    
st.set_page_config(page_title="Foods Recipe Generater App")

st.header("Upload Any Dish Photo And Get Recipe")
input=st.text_input("Input Prompt: ",key= "input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg","jpeg","png"])
image= ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption = "Uploaded Image.", use_column_width=True)

submit = st.button("Generate the Recipe")

input_prompt ="""

You are an expert Chef where you need to see the dish from the image and
Generate a detailed recipe based on the uploaded photo of the dish.
Describe the ingredients and provide step-by-step instructions for recreating this delicious dish.
Be specific about quantities, cooking methods, and any unique elements that make this recipe stand out. 
The goal is to provide a comprehensive and easy-to-follow recipe based on the visual representation of the dish.

"""

## we are creating the submit button so that as soon as we click the button we get the results

if submit:
    image_data= input_image_setup(uploaded_file)
    response= get_gemini_response(input_prompt,image_data,input)
    st.subheader("The Recipe Is Here")
    st.write(response)
    

