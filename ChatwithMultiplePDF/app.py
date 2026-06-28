#Imports
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

import faiss
from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

#read the pdf
def get_pdf_text(pdf_docs):
    text = ''

    for pdf in pdf_docs:
        pdfreader = PdfReader(pdf)
        for page in pdfreader.pages:
            text += page.extract_text()
    return text

#making chunks of the text
def pdf_text_chunks(text):

    textspliter = RecursiveCharacterTextSplitter(chunk_size = 10000, chunk_overlap = 1000)
    chunks  = textspliter.split_text(text)
    return chunks


def get_vector_store(text_chunks):

    embeddings = GoogleGenerativeAIEmbeddings(model = 'gemini-embedding-2-preview')
    vector_store = FAISS.from_texts(text_chunks, embeddings)
    vector_store.save_local('faiss-index')

def conversational_chain():
    prompt_template = ChatPromptTemplate.from_template("""You are a helpful assistant that answers questions based on the provided document context.
    Use the context below to answer the user's question. 
    If the answer is not in the context, say "I don't have enough information to answer that."
    Do not make up answers.

    Context: {context}

    Human: {question}
    Assistant:""")


    llm = GoogleGenerativeAI(model = 'gemini-3.5-flash', temperature = 0.7,
                            google_api_key = os.getenv('GOOGLE_API_KEY'))  

    chain = prompt_template | llm | StrOutputParser()
    return chain

def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model= 'gemini-embedding-2-preview')
    new_db = FAISS.load_local('faiss-index' ,embeddings, allow_dangerous_deserialization=True )
    docs = new_db.similarity_search(user_question)

    context = "\n\n".join([doc.page_content for doc in docs])
    chain = conversational_chain()

    response = chain.invoke({
        'context': context,
        'question': user_question
    })

    print(response)
    st.write("reply: ", response)
    return response


def main():
    st.set_page_config(page_title="Chat with PDFs")
    st.header("Chat with your PDFs 💬")

    user_question = st.text_input("Ask a question from your PDF files")
    if user_question:
        user_input(user_question)

    with st.sidebar:
        st.title("Upload PDFs")
        pdf_docs = st.file_uploader(
            "Upload your PDF files and click Process",
            accept_multiple_files=True
        )
        if st.button("Process"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = pdf_text_chunks(raw_text)
                get_vector_store(text_chunks)
                st.success("Done! You can now ask questions.")


if __name__ == "__main__":
    main()