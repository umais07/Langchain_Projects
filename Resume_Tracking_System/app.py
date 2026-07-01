# Imports
from dotenv import load_dotenv
load_dotenv()

import prompts as pr
import os
import streamlit as st
import PyPDF2 as pdf

from langchain_core.messages import HumanMessage   
from langchain_google_genai import ChatGoogleGenerativeAI


def get_gemini_response(prompt, pdf_content, user_input):
    model = ChatGoogleGenerativeAI(model = 'gemini-3.5-flash', temperature = 0.7,
                            google_api_key = os.getenv('GOOGLE_API_KEY')) 
    
    message = HumanMessage(content=[
        {"type": "text", "text": prompt},
        {"type": "text", "text": user_input},
        {"type":"text", "text": pdf_content
        }
    ])

    response = model.invoke([message])
    
    if isinstance(response.content, list):
        return "\n".join(
            block.get("text", "") for block in response.content
            if isinstance(block, dict) and block.get("type") == "text"
        )

    return response.content

def input_pdf_setup(uploaded_file):
#convert the pdf to image
    if uploaded_file is not None:
        reader = pdf.PdfReader(uploaded_file)
        text = ''

        page = reader.pages[0]
        text+=str(page.extract_text())
        return text
    else:
        raise FileNotFoundError("No File Uploaded")


#system Prompt from the prompts.pt
prompts_improve = pr.PROMPT_IMPROVE_SKILLS
about_resume = pr.PROMPT_ABOUT_RESUME
miss_keywords = pr.PROMPT_MISSING_KEYWORDS
perct_match =  pr.PROMPT_PERCENTAGE_MATCH


# StreamLit App

st.set_page_config(page_title='Resume_Tracking System')
st.header('Resume_Tracking_system')

input_text = st.text_area("Job Description", key='input')
uploaded_file = st.file_uploader('Upload your Resume (PDF)')

if uploaded_file is not None:
    st.write("PDF uploaded Successfully")
else:
    st.write('Please Upload the Resume')

submit1 = st.button('How i improvise this skills')
submit2 = st.button('Tell me about the Resume')
submit3 = st.button('What are the keywords that are missing')
submit4 = st.button('Percentage Match')


def run_action(prompt):
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)

        with st.spinner("Analyzing"):
            response = get_gemini_response(prompt, pdf_content, input_text)

        st.subheader('The REsponse is')
        st.markdown(response)

    else: 
        st.warning("Please Upload the Resume")

if submit1:
    run_action(prompts_improve)
elif submit2:
    run_action(about_resume)
elif submit3:
    run_action(miss_keywords)
elif submit4:
    run_action(perct_match)
