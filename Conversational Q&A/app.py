# Q&A 
from langchain_groq import ChatGroq
from langchain.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os

from dotenv import load_dotenv
load_dotenv()


if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages'] = [SystemMessage(content= 'You are Comedian Ai Assistant')]

# main page UI
st.set_page_config(page_title='Conversational Q&A chatbot')
st.header('hey lets chat')

def get_chatmodel_response(question:str):
    llm = ChatGroq(temperature = 0.5,
               model="meta-llama/llama-4-scout-17b-16e-instruct")
    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer = llm.invoke(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content= answer.content))

    return answer.content


input = st.text_input("Input: ",key='input')
response = get_chatmodel_response(input)

submit = st.button('Ask the Question')

# OnCLick
if submit:
    if input:
        st.subheader('The Response is')
        st.write(response)