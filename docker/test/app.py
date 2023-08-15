import main as generate
import alpaca_app as generateAlpaca
import streamlit as st

def app():
    st.title("Simple LLM-powered App")
#     text_input = st.text_input("Enter your text here:")
    if st.button("Generate"):
        text_input = 'Что делать, если у меня не работает интернет?'
        st.write(text_input)
        st.write(generate(text_input))
        st.write('Завершено')
    elif st.button("Generate Alpaca"):
       text_input = 'What is the capital of England?'
       st.write(text_input)
       st.write(generateAlpaca(text_input))
       st.write('Завершено')

if __name__ == "__main__":
    app()
