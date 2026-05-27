# Integrate code with the GroqAi
from langchain_core.globals import set_debug
set_debug(True)

from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import MessagesPlaceholder, ChatPromptTemplate

import os
from dotenv import load_dotenv

load_dotenv()
groq_key = os.getenv("groq_key")

from langchain_groq import ChatGroq

# Custom-Search
import streamlit as st

#Streamlit interface
st.title('Langchain Demo with Groq')
input_text = st.text_input('Search the topic')

# Prompt Template with memory
first_input_Template = ChatPromptTemplate.from_messages([
    ('system','you are a helpful Ai Assistant'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','tell me about {name}')
])

second_prompt_template = ChatPromptTemplate.from_template(
    'when was {person} born'
)

third_prompt_template = ChatPromptTemplate.from_template(
    'Mention Global Events around that {dob}'
)

#Groq LLm model
llm = ChatGroq(
    temperature = 0.8,
    api_key=groq_key,
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    max_tokens=1024,
)

# Persistent Memory
msgs = StreamlitChatMessageHistory(key = 'langchain_messages')

# Chain
chain1 = first_input_Template | llm

chain1_with_memory = RunnableWithMessageHistory(
    chain1,
    lambda session_id: msgs,
    input_messages_key='name',
    output_messages_key='person',
    history_messages_key='chat_history'
)

chain2 = {"person": chain1_with_memory} | second_prompt_template | llm

full_chain = (
    {"dob": chain2} 
    | third_prompt_template 
    | llm
)

# Running
if input_text:
    config = {'configurable':{'session_id':'default_session'}}
    response = full_chain.invoke({"name":input_text}, config=config)
    st.write(response.content)