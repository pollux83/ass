import streamlit as st

def generate(text_input):
    return text_input

def main():
#     st.title("My Streamlit App. Test")
#     st.write("Welcome to my first Streamlit app! Test")
    st.title("Simple LLM-powered App")
    text_input = st.text_input("Enter your text here:")
    if st.button("Generate"):
        response = generate(text_input)
        st.write(response)

if __name__ == "__main__":
    main()
