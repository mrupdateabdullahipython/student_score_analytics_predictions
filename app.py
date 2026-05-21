import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
import time
import base64

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Student Score Analytics Dashboard",
    page_icon="🎓",
    layout="wide"
)

# ---------------- BACKGROUND IMAGE ---------------- #

import streamlit as st
import base64

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_bg_local(main_bg):
    bin_str = get_base64(main_bg)
    page_bg_img = f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-attachment: fixed;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_bg_local('university_bg.jpg')

# ---------------- LOAD MODEL ---------------- #

model = joblib.load("student_score_model.pkl")

# ---------------- TITLE ---------------- #

st.markdown(
"""
<div class='main-title'>
🎓 STUDENT ANALYTICS DASHBOARD
</div>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<div class='sub-title'>
AI-Powered Student Performance Prediction System
</div>
""",
unsafe_allow_html=True
)
# University logo goes here
logo = st.sidebar.image('anotherlogo.jpg')
# ---------------- SIDEBAR ---------------- #

st.sidebar.title("📚 Student Inputs")

study_hours = st.sidebar.slider(
    "Study Hours",
    1,
    10,
    5
)

sleep_hours = st.sidebar.slider(
    "Sleep Hours",
    4,
    10,
    7
)

attendance = st.sidebar.slider(
    "Attendance (%)",
    50,
    100,
    80
)

assignment = st.sidebar.slider(
    "Assignments Completed",
    0,
    20,
    10
)

import streamlit as st
import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Replace 'your_image.png' with your actual file path
img_base64 = get_base64_image("another.jpg")

sidebar_style = f"""
<style>
    [data-testid="stSidebar"] {{
        background-image: url("data:image/png;base64,{img_base64}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
</style>
"""

st.markdown(sidebar_style, unsafe_allow_html=True)

# ---------------- PREDICTION ---------------- #

input_data = pd.DataFrame({

    'Study_Hours':[study_hours],
    'Sleep_Hours':[sleep_hours],
    'Attendance':[attendance],
    'Assignment':[assignment]

})

prediction = model.predict(input_data)[0]

prediction = round(prediction,2)

# ---------------- BUTTON ---------------- #

if st.button("🚀 Predict Student Score"):
    st.image('final_chart.png',width=500)

    with st.spinner("Analyzing Student Performance..."):

        time.sleep(2)

    st.markdown(
    f"""
    <div class='prediction-box'>
    Predicted Result <br>
    {prediction}%
    </div>
    """,
    unsafe_allow_html=True
    )

    # ---------------- PE
    if prediction >= 80:
        st.success("🌟 Excellent Performance")

    elif prediction >= 60:
        st.info("✅ Average Performance")

    else:
        st.warning("⚠ Needs Improvement")

# ---------------- METRICS ---------------- #

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
    """
    <div class='card'>
    <div class='metric'>95%</div>
    <div class='metric-label'>
    Prediction Accuracy
    </div>
    </div>
    """,
    unsafe_allow_html=True
    )

with col2:
    st.markdown(
    """
    <div class='card'>
    <div class='metric'>3000+</div>
    <div class='metric-label'>
    Student Records
    </div>
    </div>
    """,
    unsafe_allow_html=True
    )

with col3:
    st.markdown(
    """
    <div class='card'>
    <div class='metric'>AI ML</div>
    <div class='metric-label'>
    Linear Regression Model
    </div>
    </div>
    """,
    unsafe_allow_html=True
    )

# ---------------- CHART ---------------- #

st.markdown("## 📊 Performance Analytics")

chart_data = pd.DataFrame({

    'Features':[
        'Study',
        'Sleep',
        'Attendance',
        'Assignment'
    ],

    'Values':[
        study_hours,
        sleep_hours,
        attendance/10,
        assignment
    ]
})

fig, ax = plt.subplots(figsize=(4,4))

ax.bar(
    chart_data['Features'],
    chart_data['Values']
)

ax.set_title(
    'Student Performance Factors'
)

st.pyplot(fig)

# ---------------- PIE CHART ---------------- #

st.markdown("## 🥧 Student Activity Distribution")

fig2, ax2 = plt.subplots(figsize=(4,4))

ax2.pie(

    [
        study_hours,
        sleep_hours,
        assignment
    ],

    labels=[
        'Study',
        'Sleep',
        'Assignment'
    ],

    autopct='%1.1f%%'
)

st.pyplot(fig2)

# ---------------- FOOTER ---------------- #

st.markdown(
    "<p style='text-align: center;'>Avarage Student Score.</p>", 
    unsafe_allow_html=True
)
st.image('avarege.png',width=500)
st.sidebar.image('student_exam.jpg')

st.markdown(
"""
<center style='color:white;font-size:18px;'>

Developed with
Python, Scikit learn, Machine Learning & Streamlit

</center>
""",
unsafe_allow_html=True
)
import streamlit as st

# Centering a title
# Centering a paragraph
st.markdown("<div style='text-align: center;'>Project Designed by UpdateCodesML.</div>", unsafe_allow_html=True)

st.sidebar.markdown(
    "<p style='text-align: center;'>Project Created by @updateabdullahi.</p>", 
    unsafe_allow_html=True
)