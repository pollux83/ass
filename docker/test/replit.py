from transformers import AutoModelForCausalLM
from transformers import AutoTokenizer
import streamlit as st

# os.environ["HUGGINGFACEHUB_API_TOKEN"] = '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' #

def loadModel():
    # load model
    return AutoModelForCausalLM.from_pretrained('replit/replit-code-v1-3b', trust_remote_code=True,device_map="auto",load_in_4bit=True)

def generateCode(model):
    # load tokenizer
    tokenizer = AutoTokenizer.from_pretrained('replit/replit-code-v1-3b', trust_remote_code=True)

    # single input encoding + generation
    x = tokenizer.encode('def hello():\n  print("hello world")\n', return_tensors='pt')
    y = model.generate(x)

    # decoding, clean_up_tokenization_spaces=False to ensure syntactical correctness
    generated_code = tokenizer.decode(y[0], skip_special_tokens=True, clean_up_tokenization_spaces=False)
    return generated_code


def app():
    st.title("Test replit")
    if st.button("Run"):
        model = loadModel()
        st.write(generate(model))


if __name__ == '__main__':
#     app.run(debug=True)
       app()
