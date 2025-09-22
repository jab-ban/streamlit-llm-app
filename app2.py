# -*- coding: utf-8 -*-
"""app.py


"""



import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv("envi")  
api_key = os.getenv("GROQ_API_KEY")
llm = Groq(api_key=api_key)
messages = [
    {"role": "system", "content": "i am a helpful assistant"},
]
st.sidebar.title("⚙️ Settings")
temperature = st.sidebar.slider(
    "Model Temperature (0 = ثابت / 1 = عشوائي):", 
    0.0, 1.0, 0.3, 0.1
)
max_tokens = st.sidebar.slider(
    "Max Tokens:", 
    100, 2000, 500, 100
)
def run_llm(prompt):
    messages.append({"role": "user", "content": prompt})

    LLM = llm.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        max_tokens=100000,
        temperature=0.3
    )

    reply = LLM.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    return reply

"""**Streamlit UI**


"""

st.title('My llm app')
st.header('ask the assistant:')
st.write('welcome to my first llm app!')
user_input=st.text_input('enter your question here:')
if st.button('Try to click me to get the answer!'):
  if user_input.strip() !="":
    reply=run_llm(user_input)
    st.success(reply)
  else:
    st.warning('please enter your question!')
