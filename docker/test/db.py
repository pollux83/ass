from embedding import getEmbedding
from langchain.vectorstores import FAISS


def createDB(texts):
    # задаем векторайзер
    embeddings = getEmbedding()

    # создаем хранилище
    db = FAISS.from_documents(texts, embeddings)
    db.as_retriever()

    # также можно сохранить хранилище локально
#     db.save_local('faiss_index')

    # тестируем ретривер
#     db.similarity_search_with_score('не знаю как прикрепить сотрудника')

    return db
