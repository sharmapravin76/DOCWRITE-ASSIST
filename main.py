from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
from PIL import Image

import google.generativeai as genai

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("AIzaSyBitsHhNAqI4OfMIyS-b1ZlYduK93iH9Zc"))

# Function to load OpenAI model and get responses

def get_gemini_response(input, image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if input != "":
       response = model.generate_content([input, image])
    else:
       response = model.generate_content(image)
    return response.text

# Initialize our Streamlit app

st.set_page_config(page_title="Gemini Image Demo")

st.markdown(
    """
    <style>
        .header {
            font-size: 36px;
            font-weight: bold;
            color: #3D5A80; /* Dark Blue */
            text-align: center;
            margin-bottom: 30px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }
        .input-container {
            margin-bottom: 30px;
        }
        .image-caption {
            font-style: italic;
            text-align: center;
            margin-top: 20px;
            color: #628395; /* Light Blue */
        }
        .response-container {
            margin-top: 40px;
            padding: 20px;
            background-color: #F8EDD3; /* Light Yellow */
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .response {
            font-size: 18px;
            color: #3D5A80; /* Dark Blue */
            margin-top: 20px;
        }
        .button {
            background-color: #E76F51; /* Salmon */
            border: none;
            color: white;
            padding: 12px 24px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 18px;
            margin-top: 30px;
            cursor: pointer;
            border-radius: 5px;
            transition: background-color 0.3s;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .button:hover {
            background-color: #CC4E41; /* Dark Salmon */
        }
        /* Customizing file uploader */
        .stFileUploader > div {
            background-color: #F4A261; /* Light Orange */
            border-radius: 5px;
            padding: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        /* Customizing button */
        .stButton > button {
            background-color: #3D5A80; /* Dark Blue */
            border: none;
            color: white;
            padding: 12px 24px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 18px;
            margin-top: 30px;
            cursor: pointer;
            border-radius: 5px;
            transition: background-color 0.3s;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .stButton > button:hover {
            background-color: #2C436D; /* Darker Blue */
        }
    </style>
    """,
    unsafe_allow_html=True
)



# App layout

st.markdown('<p class="header">DOCTOR DECIPHER AI </p>', unsafe_allow_html=True)

input = st.text_input("Input Prompt:", key="input")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)
    
submit = st.button("Tell me about the image")

if submit:
    response = get_gemini_response(input, image)
    st.markdown('<p class="response-container">The Response is:</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="response">{response}</p>', unsafe_allow_html=True)

#  to run use command -->streamlit run c:\Users\KIIT\OneDrive\Desktop\Prescription-Ai\Prescription-Ai-\main.py