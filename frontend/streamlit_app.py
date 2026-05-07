import streamlit as st
import requests

st.title("Planet AI LLM Assistant")

query = st.text_input("Ask your question")

if st.button("Submit"):

    try:
        response = requests.post(
            "http://127.0.0.1:8000/ask",
            json={"question": query}
        )

        st.write("Status Code:", response.status_code)

        data = response.json()

        st.subheader("Answer")
        st.write(data["answer"])

    except Exception as e:
        st.error(str(e))