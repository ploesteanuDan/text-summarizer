import streamlit as st
import openai
import os
from text_summarizer.functions import summarize

openai.api_key = os.getenv('OPENAI_KEY')

if "summary" not in st.session_state:
    st.session_state["summary"] = ""

st.title("Text Summarizer")

input_text = st.text_input(label="State your question:", value="")

st.button(
    "Submit",
    on_click=summarize,
    kwargs={"prompt": input_text},
)

output_text = st.text_area(label="Response based on knowledge base:", value=st.session_state["summary"], height=250)