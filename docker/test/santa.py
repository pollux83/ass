from transformers import AutoModelForCausalLM, AutoTokenizer
import streamlit as st

# os.environ["HUGGINGFACEHUB_API_TOKEN"] = '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' #
checkpoint = "bigcode/santacoder"
device = "cuda" # for GPU usage or "cpu" for CPU usage

def loadModel():
    # load model
    return AutoModelForCausalLM.from_pretrained(checkpoint, trust_remote_code=True).to(device)

def generateCode(model):
    tokenizer = AutoTokenizer.from_pretrained(checkpoint)
    model = loadModel()

    inputs = tokenizer.encode("def print_hello_world():", return_tensors="pt").to(device)
    outputs = model.generate(inputs)
    return tokenizer.decode(outputs[0])


def app():
    st.title("Test")
    if st.button("Run"):
        model = loadModel()
        st.write(generate(model))


if __name__ == '__main__':
       app()
