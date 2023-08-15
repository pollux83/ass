import random
import pandas as pd
from langchain.document_loaders import DataFrameLoader

def generate_documents():
    # Список вопросов пользователей
    user_questions = [
        "Каким образом я могу изменить свой пароль?",
        "Что делать, если у меня не работает интернет?",
        "Как добавить новый продукт в магазине?",
        "Как узнать статус моего заказа?",
        "Как настроить уведомления на почту?",
        "Какая версия ПО совместима с Windows 10?",
        "Как получить скидку на следующую покупку?",
        "Как пополнить баланс на мобильном телефоне?",
        "Как заблокировать свою учетную запись?",
        "Как связаться с технической поддержкой компании?"
    ]

    # Список ответов от службы поддержки
    support_answers = [
        "Для изменения пароля, перейдите в раздел 'Настройки аккаунта' и выберите 'Сменить пароль'.",
        "Пожалуйста, проверьте подключение к интернету и перезагрузите роутер.",
        "Чтобы добавить новый продукт, зайдите в административную панель магазина и выберите 'Добавить продукт'.",
        "Для проверки статуса заказа, перейдите в раздел 'Мои заказы' на сайте.",
        "Чтобы настроить уведомления, перейдите в настройки аккаунта и выберите 'Уведомления'.",
        "Для совместимости с Windows 10, установите последнюю версию программного обеспечения.",
        "Для получения скидки, воспользуйтесь промокодом при оформлении заказа.",
        "Чтобы пополнить баланс, выберите соответствующую опцию в личном кабинете.",
        "Чтобы заблокировать учетную запись, свяжитесь с нашей службой поддержки по телефону.",
        "Вы можете связаться с технической поддержкой через электронную почту support@example.com."
    ]

    # Список ссылок на источники информации
    urls = [
        "https://example.com/confluence/how-to-change-password",
        "https://example.com/confluence/troubleshooting-internet-issues",
        "https://example.com/confluence/add-new-product-admin-panel",
        "https://example.com/confluence/check-order-status",
        "https://example.com/confluence/email-notifications-setup",
        "https://example.com/confluence/software-compatibility-windows10",
        "https://example.com/confluence/get-next-purchase-discount",
        "https://example.com/confluence/top-up-mobile-balance",
        "https://example.com/confluence/account-blocking-instructions",
        "https://example.com/confluence/contact-technical-support"
    ]

    # Генерация 10 документов
    documents = []
    for i in range(1, 11):
        doc_id = i
        question = random.choice(user_questions)
        answer = random.choice(support_answers)
        url = random.choice(urls)

        document = {
            "id": doc_id,
            "question": question,
            "answer": answer,
            "url": url
        }
        documents.append(document)

    # создаем из наших документов датафрейм
    df = pd.DataFrame(documents)
    # грузим фрейм в лоадер, выделив колонку для векторизации (здесь может быть место для дискуссий)
    loader = DataFrameLoader(df, page_content_column='question')
    documents = loader.load()

    return documents
