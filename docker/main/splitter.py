from langchain.text_splitter import RecursiveCharacterTextSplitter

def getTextSplitter(documents):
     # создаем сплиттер документов, чтобы уложиться в лимит по токенам, в нашем случае это не очень полезный шаг
     text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
     return text_splitter.split_documents(documents)


