import openai
import streamlit as st
import numpy as np
import os

filename = 'kb1.txt'
test_knowledge_base = np.loadtxt(filename, delimiter=',', skiprows=1, dtype=str)

def summarize(prompt):
    augmented_prompt = f"as long as the answer is contained by this data: '{test_knowledge_base}', reply to '{prompt}', only using the information in the data."
    resp = openai.Completion.create(
        model="text-davinci-003",
        prompt=augmented_prompt,
        temperature=0, # from 0 to 1, less means more accure, more means more abstract 
        max_tokens=1000,
        presence_penalty=-2
    )["choices"][0]["text"]
    st.session_state["summary"] = resp
    with open('output_log.txt', 'a') as output_log:
      output_log.write(f"IN: {prompt} \nOUT: {os.linesep.join([s for s in resp.splitlines() if s])} \n --- \n ")