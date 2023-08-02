import streamlit as st
import os
from langchain import PromptTemplate, HuggingFaceHub, LLMChain
# pip install sentence_transformers
from langchain.embeddings import HuggingFaceEmbeddings

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

# def getEmbedding():
#     # Alternatively, open-source text embedding model hosted on Hugging Face
#     embeddings = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")
#     return embeddings
#
# def embeddingText(text = "Alice has a parrot. What animal is Alice's pet?"):
#     # The embeddings model takes a text as an input and outputs a list of floats
#     embeddings = getEmbedding()
#     return embeddings.embed_query(text)


def generate(text_input):
    prompt = promptTemplate()
    return prompt.format(question=text_input)

def main():
    # Set the HUGGINGFACEHUB_API_TOKEN environment variable
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"
    st.title("Simple LLM-powered App")
    text_input = st.text_input("Enter your text here:")
    if st.button("Generate"):
        response = generate(text_input)
        st.write(response)

if __name__ == "__main__":
    main()
