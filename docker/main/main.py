import streamlit as st
import os
from langchain import PromptTemplate, HuggingFaceHub, LLMChain
from langchain.vectorstores import FAISS
from document_generator import generate_documents
from splitter import getTextSplitter
from db import createDB
import alpaca_app as generateAlpaca

from llmHuggingFaceHub import getLLM
from promptTemplate import getPromptTemplate
# Set the HUGGINGFACEHUB_API_TOKEN environment variable
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"


def generate(text_input='не знаю как прикрепить сотрудника'):
    documents = generate_documents()
#     return documents[0]
    texts = getTextSplitter(documents)
    db = createDB(texts)
#     st.write(db.similarity_search_with_score(text_input)[0])
    # цепочка с кастомным промтом
    chain = LLMChain(
    llm=getLLM(),
    prompt=getPromptTemplate())
    relevants = db.similarity_search(text_input)
    doc = relevants[0].dict()['metadata']
    st.write(doc)
    return chain.run(doc)

def main():
    st.title("Simple LLM-powered App")
#     text_input = st.text_input("Enter your text here:")
    text_input = 'Что делать, если у меня не работает интернет?'
    if st.button("Generate"):
        st.write(text_input)
        st.write(generate(text_input))
        st.write('Завершено')
    elif st.button("Generate Alpaca"):
       text_input = 'What is the capital of England?'
       st.write(text_input)
       st.write(generateAlpaca(text_input))
       st.write('Завершено')

if __name__ == "__main__":
    main()
