import openai
import streamlit as st

def summarize(prompt):
    augmented_prompt = f"as long as the answer is contained by 'my mother has a fox', reply to {prompt}"
    st.session_state["summary"] = openai.Completion.create(
        model="text-davinci-003",
        prompt=augmented_prompt,
        temperature=.5,
        max_tokens=1000,
    )["choices"][0]["text"]


    # https://towardsdatascience.com/make-a-text-summarizer-with-gpt-3-f0917a07189e

    # asked who is mathew, with the database only containing "my mother has a fox",
    # it replied that mathew is my mother's fox

    #asked the same question, but told only to answer if the database contained the answer, 
    # it replied Mathew is not mentioned in the statement.

    #asked if sure, it said it's sure it doesnt know