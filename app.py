import requests
import streamlit as st

API_URL = "https://api-inference.huggingface.co/models/distilbert-base-cased-distilled-squad"
headers = {"Authorization": "Bearer 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"}

st.title("distilbert-demo")

text_input = st.text_area(
    "Enter some context👇",
)
text_question = st.text_input(
    "Enter a question regarding that context👇",
)


def query(payload):
    retries = 0
    while True:
        response = requests.post(API_URL, headers=headers, json=payload)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 429:
            retries += 1
            wait_time = 2 ** retries
            print(f"Too many requests. Retrying in {wait_time} seconds...")
            time.sleep(wait_time)
        else:
            print(f"Request failed with status code {response.status_code}.")
            return None


if st.button("Send"):
    output = query(
        {
            "inputs": {"question": text_question, "context": text_input}
        }
    )
    if output:
        st.write(output)
else:
    st.write(" ")

