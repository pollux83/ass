from langchain import HuggingFaceHub
import os

def getLLM():
    #подключение по API huggingface
    return HuggingFaceHub(repo_id='IlyaGusev/fred_t5_ru_turbo_alpaca',
                        huggingfacehub_api_token=os.environ["HUGGINGFACEHUB_API_TOKEN"],
                        model_kwargs={'temperature':0, 'max_length':128}
                        )

#         # Alternatively, open-source LLM hosted on Hugging Face
#         # pip install huggingface_hub
#         llm = HuggingFaceHub(repo_id = "google/flan-t5-xl", model_kwargs={"temperature":1e-10})
#         return llm

