import streamlit as st
from groq import Groq
st.set_page_config(page_title = 'AI assistant interview', layout='centered')
st.title("AI Interview Assistant")
st.caption("Practice and Prepare for your Placements here")
try:
  client = Groq(api_key = st.secrets["GROQ_API_KEY"])
except (KeyError, FileNotFound):
  st.error("API Key is missing. Add it in Advanced settings")
st.stop()
role = st.selectbox('Job Title', ['Machine Learning Engineer','Senior Software','DevOPs Engineer','Data Analyst','Other'])
if role == 'Other':
  st.text_input('Enter you Job Title','XXXXXXX')
model = st.selectbox('Model', ['openai/gpt-oss-120b','openai/gpt-oss-20b'])

