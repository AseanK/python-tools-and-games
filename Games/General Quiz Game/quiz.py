'''
Project 1: Web Based Game
Author: Ruchit Tripathi
'''

import random
import time
import numpy as np
import json as js
import requests as rq
from datetime import datetime, timedelta

from utils import package_installer
package_installer.install_dependencies()

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import altair as alt

# Logic to add background images (Future Enhancement)
# def set_bg_hack_url():
#     '''
#     A function to unpack an image from url and set as bg.
#     Returns
#     -------
#     The background.
#     '''
        
#     st.markdown(
#          f"""
#          <style>
#          .stApp {{
#              background: url("https://www.clemson.edu/brand/resources/logos/paw/orange.png");
#              background-size: cover
#          }}
#          </style>
#          """,
#          unsafe_allow_html=True
#      )

def get_category():
    category_dict = dict()
    category_json_list = rq.get("https://opentdb.com/api_category.php").json()
    for item in category_json_list['trivia_categories']:
        category_dict[item['name']] = item['id']
    return category_dict

@st.cache_data(ttl= 75, max_entries=1)
def get_question(category,difficulty):
    questions = rq.get("https://opentdb.com/api.php?amount=10"+"&category="+str(category)+"&difficulty="+str(difficulty)).json()["results"]
    return questions

def initialize_session_state():
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
        # st.snow()
    if 'player_score' not in st.session_state:
        st.session_state.player_score = 0

def update_score(player_choice, correct_answer):
    if str(player_choice) == str(correct_answer):
        st.success("It was a correct answer! Great Job! 😁✌")
        st.session_state.player_score += 1
        st.balloons()
    else:
        st.error("It was an incorrect answer! 😕")

if "page" not in st.session_state:
    st.session_state.page = 0
if "submit_key" in st.session_state and st.session_state.submit_key == True:
    st.session_state.running = True
else:
    st.session_state.running = False

if "running" not in st.session_state:
    st.session_state.running = False

def nextpage(): st.session_state.page += 1
def restart(): st.session_state.page = 0

# set_bg_hack_url()
st.markdown("<style>description {color: Green;}</style>",unsafe_allow_html = True)
st.title(":orange[Welcome to the] :violet[QuizMaster!] 🧩")
st.subheader("_Engage, Entertain, and Educate with QuizMaster - Where Knowledge Meets Fun!_", divider= 'rainbow')
st.sidebar.title("Tune the Options to Play the Game")
st.sidebar.markdown("---")
initialize_session_state()

def calculate_score(player_choice):
    correct_answer = quiz_questions[st.session_state.current_question]["answer"]
    # st.write("inside calculate_score" + str(correct_answer))
    update_score(player_choice, correct_answer)
    st.session_state.current_question += 1

categories_option = get_category()
category = st.sidebar.selectbox("Category: ", list(categories_option.keys()), index= None, placeholder= "Select one: ", disabled=(st.session_state.running))
# st.session_state.disable_opt = True
# category = st.sidebar.selectbox("Category: ", list(categories_option.keys()), index= None, placeholder= "Select one: ", disabled=(st.session_state.running))
if category is None:
    st.warning('Please select one category to start the game', icon="⚠️")
else:
    levels = st.sidebar.selectbox("Difficulty Level: ", ['Easy', 'Medium', 'Hard'], disabled=(st.session_state.running))
    QuestionList = get_question(categories_option[category], levels.lower())
    # st.write(QuestionList)
    len_response = len(QuestionList)
    if len_response == 0:
        st.error("This Category has no question for the given difficulty mode at the source side! Please select another difficulty level or category to start the game! 😕😔")
        st.stop()
    quiz_questions = []
    for item in range(len_response):
        temp_dict = dict()
        temp_dict['text'] = QuestionList[item].get("question")
        temp_dict['options'] = tuple(QuestionList[item].get("incorrect_answers") + [QuestionList[item].get("correct_answer")])
        temp_dict['answer'] = QuestionList[item].get("correct_answer")
        quiz_questions.append(temp_dict)
    placeholder = st.empty()
    ind = st.session_state.current_question
    if ind > len(quiz_questions):
        st.stop()
    else:
        current_question = quiz_questions[ind]
        st.subheader(quiz_questions[ind]["text"])
        player_choice = st.radio("Select your answer:",
                                 options= current_question["options"],
                                 key=f"question_{ind}",  disabled=(st.session_state.running))
        submitted =  st.button("Submit", key="submit_key", disabled=(st.session_state.running))
        if submitted:           
            calculate_score(player_choice)
            st.markdown("Correct Answer: "+ current_question["answer"])
        # st.empty()
            if st.button("Next",on_click=nextpage,disabled=(st.session_state.page >= 9)):
                if st.session_state.current_question < len(quiz_questions):
                    st.rerun()  
            if st.session_state.current_question >= len(quiz_questions):
            # st.session_state.clear
                st.empty()
                st.success("Quiz Finished!")
                st.subheader(f"_Your_ _Score_: :blue[{st.session_state.player_score}] :sunglasses:")
                st.snow()

st.markdown("---")
st.info("Reload the page or press F5 to restart the game!")
st.sidebar.markdown("---")
st.sidebar.markdown("### About Developer", unsafe_allow_html=True)
st.sidebar.markdown("Visit <a href='https://www.linkedin.com/in/ruchit-tripathi/'>Ruchit's LinkedIn</a> and <a href='https://www.github.com/ruchit-t/'>Github</a> profiles for more information & updates.", unsafe_allow_html=True)
st.sidebar.markdown("### About Contributors", unsafe_allow_html=True)
st.sidebar.markdown("<a href='https://www.linkedin.com/in/stephanie-damas7213/'>Stephanie's LinkedIn</a>", unsafe_allow_html=True)
st.sidebar.markdown("<a href='https://www.linkedin.com/in/gayatri-tatineni-0a939a20b/'>Gayatri's LinkedIn</a>", unsafe_allow_html=True)
st.sidebar.markdown("Thanks for visiting the site! 😃 Have Fun 😉")