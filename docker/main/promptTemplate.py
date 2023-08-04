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
