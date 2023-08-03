import streamlit as st
import os
from langchain import PromptTemplate, HuggingFaceHub, LLMChain
from langchain.vectorstores import FAISS
from document_generator import generate_documents
from splitter import getTextSplitter
from db import createDB

from llmHuggingFaceHub import getLLM
from promptTemplate import getPromptTemplate
# Set the HUGGINGFACEHUB_API_TOKEN environment variable
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

def getLlm():
    # Alternatively, open-source LLM hosted on Hugging Face
    # pip install huggingface_hub
    llm = HuggingFaceHub(repo_id = "google/flan-t5-xl", model_kwargs={"temperature":1e-10})
    return llm

def promptTemplate(input_variables=["question"]):
    template = """Question: {question}

    Answer: Let's think step by step."""
    prompt = PromptTemplate(template=template, input_variables=input_variables)

    return prompt


def generate(text_input='не знаю как прикрепить сотрудника'):
    documents = generate_documents()
#     st.write(documents[0])
    texts = getTextSplitter(documents)
    db = createDB(texts)
#     st.write(db.similarity_search_with_score(text_input))
    # цепочка с кастомным промтом
    chain = LLMChain(
    llm=getLlm(),
    prompt=getPromptTemplate())
    relevants = db.similarity_search(text_input)
    doc = relevants[0].dict()['metadata']
    return chain.run(doc)
#
#     prompt = promptTemplate()
#     return prompt.format(question=text_input)

def main():
    st.title("Simple LLM-powered App")
    text_input = st.text_input("Enter your text here:")
    if st.button("Generate"):
        response = generate(text_input)
        st.write(response)

if __name__ == "__main__":
    main()
