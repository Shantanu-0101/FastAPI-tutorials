import streamlit as st
import requests

API_URL="http://localhost:8000/predict"

st.title('Insurance Premium Category Predictor')

st.markdown('Enter your details below')

#Input Fields

age = st.number_input('Age', min_value=1, max_value=120, value=20)
weight=st.number_input('Weight (Kg)', min_value=1, value=50)
height=st.number_input('Height (Meter)', min_value=0.5, max_value=2.5, value=1.7)
income_lpa=st.number_input('Annual Salary (LPA)', min_value=1.0, max_value=10.0, value=10.0)
smoker=st.selectbox("Are you a smoker?", options=[True, False])
city=st.text_input('City', value='Mumbai')
occupation=st.selectbox(
    "Occupation",
    ['retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job']
)

if st.button('Predict Premium Category'):
    input_data={
        "age":age,
        "weight":weight,
        "height":height,
        "income_lpa":income_lpa,
        "smoker":smoker,
        "city":city,
        "occupation":occupation
    }


    try:
        response=requests.post(API_URL, json=input_data )
        if response.status_code==200:
            result=response.json()
            st.success(f"Predicted Insurance Premium Category: **{result['predicted_category']}**")
        else:
            st.error(f"API error: {response.status_code} - {response.text}")
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the FastAPI server. Make sure its running on 8000.")