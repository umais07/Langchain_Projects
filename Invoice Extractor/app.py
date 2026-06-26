# Imports
import os
import base64
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from PIL import Image
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage   

model = ChatGroq(
    model='meta-llama/llama-4-scout-17b-16e-instruct',
    temperature=0.7,
    api_key=os.getenv('GOOGLE_API_KEY')     
)

def get_gemini_response(user_input, image_parts, prompt):
    message = HumanMessage(content=[
        {"type": "text", "text": prompt},
        {"type": "text", "text": user_input},
        {
            "type": "image_url",                   
            "image_url": {
                "url": f"data:{image_parts[0]['mime_type']};base64,{image_parts[0]['data']}"
            }
        }
    ])
    response = model.invoke([message])
    return response.content                        

#Converting the image to machine Code
def image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                'mime_type': uploaded_file.type,
                'data': base64.b64encode(bytes_data).decode('utf-8')  
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError('No File Uploaded')

st.set_page_config(page_title='Multi Invoice Extractor')
st.header(' Multi-Language Invoice Extractor')

user_input = st.text_input("Input Prompt:", key='input')  

uploaded_file = st.file_uploader(
    "Choose an Image of the invoice...",
    type=['jpeg', 'png', 'jpg']
)

image = ''
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Invoice', use_column_width=True)

submit = st.button('Extract Invoice Data')

input_prompt = """
You are an expert invoice extractor that supports multiple languages.
Extract all relevant information from the invoice image and return:
- Invoice Number
- Invoice Date
- Vendor / Seller Name
- Buyer Name
- Line Items (description, qty, unit price, total)
- Subtotal, Tax, Grand Total
- Currency
- Language detected

If a field is not found, write 'N/A'.
"""

if submit:
    if uploaded_file is None:
        st.warning("Please upload an invoice image first!")
    else:
        with st.spinner("Extracting invoice details..."):
            image_data = image_details(uploaded_file)
            response = get_gemini_response(input_prompt, image_data, user_input)
        st.subheader(' The Response is')
        st.write(response)