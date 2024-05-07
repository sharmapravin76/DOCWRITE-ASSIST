from dotenv import load_dotenv
load_dotenv() #loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("write the api key"))
which is AIzaSyBitsHhNAqI4OfMIyS-b1ZlYduK93iH9Zc
##Function to load gemini Pro model and get responses
model=genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
        response=model.generate_content(question) 
        return response.text

#initialize our streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM application")

input=st.text_input("input:",key="input")
submit=st.button("Ask the question")

#when submit is clicked

if submit:
    response=get_gemini_response(input)
    st.write(response)
