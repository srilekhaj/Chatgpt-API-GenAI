#first creating text related data
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai 

genai.configure(api_key = os.getenv('GOOGLE_API_KEY'))

model = genai.GenerativeModel("gemini-2.5-flash")

def get_model_response(input):
    if input!="":
        response = model.generate_content(input)
        return response.text


st.set_page_config(page_title="llm app")
st.header("GEMINI APPLICATION")
input = st.text_input("Enter the question")
submit = st.button("Submit")

if submit:
    st.subheader("The Response is")
    response = get_model_response(input)
    st.write(response)
