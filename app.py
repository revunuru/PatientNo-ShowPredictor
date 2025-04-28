import streamlit as st
import pandas as pd
import joblib

# Load the trained Random Forest model
model = joblib.load('best_rf_model.pkl')

# Streamlit App
st.set_page_config(page_title="Patient No-Show Predictor", page_icon="🩺")
st.title('🩺 Patient No-Show Predictor')

st.write('''
Welcome! This app predicts whether a patient is likely to miss their medical appointment based on simple inputs.
Fill in the patient details below and hit **Predict**!
''')

# Sidebar for input
st.sidebar.header('Patient Details')

gender = st.sidebar.selectbox('Gender', ['Male', 'Female'])
age = st.sidebar.slider('Age', 0, 100, 30)
lead_time = st.sidebar.slider('Lead Time (days between scheduling and appointment)', 0, 100, 10)
scholarship = st.sidebar.selectbox('Scholarship Support', ['No', 'Yes'])
hipertension = st.sidebar.selectbox('Hypertension', ['No', 'Yes'])
diabetes = st.sidebar.selectbox('Diabetes', ['No', 'Yes'])
alcoholism = st.sidebar.selectbox('Alcoholism', ['No', 'Yes'])
handcap = st.sidebar.selectbox('Disability', ['No', 'Yes'])
sms_received = st.sidebar.selectbox('Received SMS Reminder?', ['No', 'Yes'])

# Prepare input for prediction
input_data = {
    'Age': age,
    'LeadTime': lead_time,
    'Scholarship': 1 if scholarship == 'Yes' else 0,
    'Hipertension': 1 if hipertension == 'Yes' else 0,
    'Diabetes': 1 if diabetes == 'Yes' else 0,
    'Alcoholism': 1 if alcoholism == 'Yes' else 0,
    'Handcap': 1 if handcap == 'Yes' else 0,
    'SMS_received': 1 if sms_received == 'Yes' else 0,
    'Gender_M': 1 if gender == 'Male' else 0
}

# Convert to DataFrame
input_df = pd.DataFrame([input_data])

# Prediction button
if st.button('Predict No-Show'):
    prediction = model.predict(input_df)
    if prediction[0] == 1:
        st.error('⚠️ The patient is likely to MISS the appointment.')
    else:
        st.success('✅ The patient is likely to ATTEND the appointment.')