from langchain import HuggingFaceHub

def getLLM():
    #подключение по API huggingface
    return HuggingFaceHub(repo_id='IlyaGusev/fred_t5_ru_turbo_alpaca',
                        huggingfacehub_api_token=os.environ["HUGGINGFACEHUB_API_TOKEN"],
                        model_kwargs={'temperature':0, 'max_length':128}
                        )

