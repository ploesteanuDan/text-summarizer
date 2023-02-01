import openai
import streamlit as st

test_data_base = {
    "pdf about elon husk": "elon husk is just the husk of the man he once was. he used to have a band and people say he once played a concert using only a tooth brush, for his mother.",
    # "pdf about cars": "cars do not exist yet. anyone saying otherwise is blatantly wrong."
}

test_knowledge_base = ' '.join(map(str, test_data_base.values()))

def summarize(prompt):
    augmented_prompt = f"as long as the answer is contained by this data: '{test_knowledge_base}', reply to '{prompt}', only using the information in the data."
    st.session_state["summary"] = openai.Completion.create(
        model="text-davinci-003",
        prompt=augmented_prompt,
        temperature=1, # from 0 to 1, less means more accure, more means more abstract 
        max_tokens=1000,
        presence_penalty=2
    )["choices"][0]["text"]

    # https://towardsdatascience.com/make-a-text-summarizer-with-gpt-3-f0917a07189e

    # asked who is mathew, with the database only containing "my mother has a fox",
    # it replied that mathew is my mother's fox

    #asked the same question, but told only to answer if the database contained the answer, 
    # it replied Mathew is not mentioned in the statement.

    #asked if sure, it said it's sure it doesnt know

        # o sa avem probleme mari daca taiem cartea in bucati si in proces, stricam frazele.