#https://medium.com/artificialis/crafting-an-engaging-chatbot-harnessing-the-power-of-alpaca-and-langchain-66a51cc9d6de
from transformers import LlamaTokenizer, LlamaForCausalLM, GenerationConfig, pipeline
from langchain.llms import HuggingFacePipeline
from langchain import PromptTemplate, LLMChain

import torch

def generateAlpaca(question = "What is the capital of England?"):
    tokenizer = LlamaTokenizer.from_pretrained("chavinlo/alpaca-native")
    base_model = LlamaForCausalLM.from_pretrained(
        "chavinlo/alpaca-native",
        load_in_8bit=True,
        device_map='auto',
    )

    pipe = pipeline(
        "text-generation",
        model=base_model,
        tokenizer=tokenizer,
        max_length=256,
        temperature=0.6,
        top_p=0.95,
        repetition_penalty=1.2
    )
    local_llm = HuggingFacePipeline(pipeline=pipe)

    from langchain import PromptTemplate, LLMChain
    template = """Below is an instruction that describes a task. Write a response that appropriately completes the request.

    ### Instruction:
    {instruction}

    Answer:"""
    prompt = PromptTemplate(template=template, input_variables=["instruction"])

    llm_chain = LLMChain(prompt=prompt,llm=local_llm)
    return llm_chain.run(question)



