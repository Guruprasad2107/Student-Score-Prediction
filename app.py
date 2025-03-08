#streamlit code for GUI implementation
#save the streamlit code in the same folder in which model was saved
#run this streamlit code using command prompt.
#pip install streamlit(if streamlit is not installed in your device) 
import streamlit as st
import numpy as np
import joblib  # Save/load model

# Load the pre-trained model
model = joblib.load('student_performance_model.joblib')

# App UI
st.title("Student Performance Prediction")
studytime = st.number_input("Study Time (hours/week)", min_value=1, max_value=10)
absences = st.number_input("Number of Absences", min_value=0)
G1 = st.number_input("First Period Grade", min_value=0, max_value=20)
G2 = st.number_input("Second Period Grade", min_value=0, max_value=20)
failures = st.number_input("Past Failures", min_value=0, max_value=5)
freetime = st.slider("Free Time (scale 1-5)", 1, 5)

if st.button("Predict"):
    inputs = np.array([[studytime, absences, G1, G2, failures, freetime]])
    prediction = model.predict(inputs)
    st.write(f"Predicted Final Grade: {prediction[0]:.2f}")
