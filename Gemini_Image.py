from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyCPHAdaF1oDGq8AFb4NccNePz873SvUkH8")

# function to load gemini pro model
model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(query):
    response = model.generate_content(query)

    return response.text

## Initialize our streamlit app

st.set_page_config(page_title="Ai chat bot")
st.header("Chat BOT", divider=True)

input = st.text_input("Input: ", key="input")
submit = st.button("Generate")

# when submit is clicked

if submit and input:
    response = get_gemini_response(input)
    st.subheader("The Reponse is")
    st.write(response)

