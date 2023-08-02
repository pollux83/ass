# import spacy

# from flask import Flask, request
# pip install langchain
import streamlit as st
import langchain
# import os
# os.environ["OPENAI_API_KEY"] = ... # insert your API_TOKEN here
os.environ["HUGGINGFACEHUB_API_TOKEN"] = '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' # insert your API_TOKEN here

# app = Flask(__name__)

# @app.route('/test', methods=['POST'])
# def test():
#     print("test")

def getLlm(prompt = "Alice has a parrot. What animal is Alice's pet?"):
    # Proprietary LLM from e.g. OpenAI
    # pip install openai
    #     from langchain.llms import OpenAI
    #     llm = OpenAI(model_name="text-davinci-003")

    # Alternatively, open-source LLM hosted on Hugging Face
    # pip install huggingface_hub
    from langchain import HuggingFaceHub
    llm = HuggingFaceHub(repo_id = "google/flan-t5-xl")
    return llm


def completionLlm(prompt = "Alice has a parrot. What animal is Alice's pet?"):
    # The LLM takes a prompt as an input and outputs a completion
    completion = getLlm(prompt)
    return completion

def getEmbedding():
    # Proprietary text embedding model from e.g. OpenAI
    # pip install tiktoken
#     from langchain.embeddings import OpenAIEmbeddings
#     embeddings = OpenAIEmbeddings()

    # Alternatively, open-source text embedding model hosted on Hugging Face
    # pip install sentence_transformers
    from langchain.embeddings import HuggingFaceEmbeddings
    embeddings = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")
    return embeddings

def embeddingText(text = "Alice has a parrot. What animal is Alice's pet?"):
    # The embeddings model takes a text as an input and outputs a list of floats
    embeddings = getEmbedding()
    text_embedding = embeddings.embed_query(text)

def promptTemplate(input_variables=["company_name"], template = "Write a catchphrase for the following company: {company_name}"):
    from langchain import PromptTemplate
    prompt = PromptTemplate(
        input_variables=input_variables,
        template=template,
    )
#     prompt.format(product="colorful socks")
    return prompt

def chain():
    from langchain.chains import LLMChain, SimpleSequentialChain
    # Define the first chain as in the previous code example
    # ...
    # Create a second chain with a prompt template and an LLM
    second_prompt = promptTemplate(
        input_variables=["company_name"],
        template="Write a catchphrase for the following company: {company_name}",
    )
    llm = getLlm()
    chain_two = LLMChain(llm=llm, prompt=second_prompt)
    # Combine the first and the second chain
    overall_chain = SimpleSequentialChain(chains=[chain, chain_two], verbose=True)
    # Run the chain specifying only the input variable for the first chain.
    catchphrase = overall_chain.run("colorful socks")

def loadDocuments():
    # pip install youtube-transcript-api
    # pip install pytube
    from langchain.document_loaders import YoutubeLoader
    loader = YoutubeLoader.from_youtube_url("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    documents = loader.load()
    return documents

def createVectorestore():
    # pip install faiss-cpu
    from langchain.vectorstores import FAISS
    documents = loadDocuments()
    embeddings = getEmbedding()
    # create the vectorestore to use as the index
    db = FAISS.from_documents(documents, embeddings)

def getResult():
    from langchain.chains import RetrievalQA
    retriever = db.as_retriever()
    qa = RetrievalQA.from_chain_type(
        llm=llm,#???
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True)
    query = "What am I never going to do?"
    result = qa({"query": query})
    print(result['result'])

def app():
    st.title("Simple LLM-powered App")
    text_input = st.text_input("Enter your text here:")
    if st.button("Generate"):
        response = lc.generate(text_input)
        st.write(response)


if __name__ == '__main__':
#     app.run(debug=True)
       app()
