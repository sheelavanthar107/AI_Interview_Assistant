import streamlit as st
from groq import Groq
st.set_page_config(page_title = 'AI assistant interview', layout='centered')
st.title("AI Interview Assistant")
st.caption("Launched By Harshitha")
try:
  client = Groq(api_key = st.secrets["GROQ_API_KEY"])
except (KeyError, FileNotFound):
  st.error("API Key is missing. Add it in Advanced settings")
  st.stop()
role = st.selectbox('Job Title', ['Machine Learning Engineer','Senior Software','DevOPs Engineer','Data Analyst','Other'])
if role == 'Other':
  st.text_input('Enter you Job Title','XXXXXXX')
model = st.selectbox('Model', ['openai/gpt-oss-120b','openai/gpt-oss-20b'])
level = st.selectbox('Difficulty',['Beginner', 'Intermediate', 'Adavanced'])
mode = st.radio('Activity', ['Generate Questions','Generate Code Questions','Evaluate Answers','Improve Answers'])
if mode == 'Generate Questions':
  count = st.slider(1,10,5)
elif mode == 'Generate Code Questions':
  topic = st.selectbox('Topics', ['SQL', 'AIML', 'Python', 'DSA', 'Java', 'c/c++'])
  count = st.slider("Number of Questions",1,10,5)
else:
  questions = st.text_area('Enter Interview Questions here')
  answer = st.text_area('Enter your answer', height =160)
if st.button("Generate AI Response", type = "primary"):
  if mode == (['Evaluate Answers']) and (not question.strip()) or (not answer.strip()) :
             st.warning("Please enter a valid Question and Answer")
  st.stop()
topics = "Topics is" + topic + "Difficulty is" + level
if mode = "Generate Questions":
  task = "Generate" + str(count) + "Frequently asked Interview Questions 3 theory and 2 scenario questions.Do not give answer"."Give Hints"
elif mode == "Generate code questions"
