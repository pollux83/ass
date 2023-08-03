# pip install sentence_transformers
from langchain.embeddings import HuggingFaceEmbeddings


def getEmbedding():
    # Alternatively, open-source text embedding model hosted on Hugging Face
    return HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")

# def embeddingText(text = "Alice has a parrot. What animal is Alice's pet?"):
#     # The embeddings model takes a text as an input and outputs a list of floats
#     embeddings = getEmbedding()
#     return embeddings.embed_query(text)
