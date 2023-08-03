from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


def getPromptTemplate():
    # создаем шаблон для промта
    prompt_template = """Используй контекст для ответа на вопрос, пользуясь следующими правилами:

    Не изменяй текст, который находится в кавычках.
    В конце обязательно добавь ссылку на полный документ
    {answer}
    url: {url}
    """

    PROMPT = PromptTemplate(
    template=prompt_template, input_variables=['answer', 'url']
    )

    return PROMPT
    llm = getLLM()
    # цепочка с кастомным промтом
    chain = LLMChain(
    llm=llm,
    prompt=PROMPT)

    relevants = db.similarity_search('не знаю как прикрепить сотрудника')
    doc = relevants[0].dict()['metadata']

    chain.run(doc)
