import pickle
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu
import tensorflow as tf
from PIL import Image

diabetes_model = pickle.load(open('./saved_models/diabetes_model.sav', 'rb'))
st.title('Diabetes')
st.header('What is Diabetes?')
st.markdown("Diabetes is a chronic (long-lasting) health condition that affects how your body turns food into energy. Your body breaks down most of the food you eat into sugar (glucose) and releases it into your bloodstream. When your blood sugar goes up, it signals your pancreas to release insulin. Insulin acts like a key to let the blood sugar into your body’s cells for use as energy.With diabetes, your body doesn’t make enough insulin or can’t use it as well as it should. When there isn’t enough insulin or cells stop responding to insulin, too much blood sugar stays in your bloodstream. Over time, that can cause serious health problems, such as heart disease, vision loss, and kidney disease.")
st.subheader("Symptoms")
st.markdown("If you have any of the following diabetes symptoms, see your doctor about getting your blood sugar tested:")
col1, col2 = st.columns(2)
with col1:
    st.markdown("-Urinate (pee) a lot, often at night")
    st.markdown("-Are very thirsty")
    st.markdown("-Lose weight without trying")
    st.markdown("-Are very Hungary")
    st.markdown("-Have blurry vivion")
    st.markdown("-Feel very Tired")
    st.header("Test for Diabetes")
with col2:
    dia_img = Image.open('images\diabetes.webp')
    st.image(dia_img, width = 250)

col1, col2, col3 = st.columns(3)


pregnancies = st.slider('Number of Pregnencies', min_value=0, max_value=10, value=1, step=1)
age = st.slider("Age", min_value = 0, max_value = 100, value = 50, step = 1)

with col1:
    skinT = st.number_input("Triceps Skin Thickness (mm)", value = 29)
    diapedfn = st.number_input("Diabetes Pedigree Function", value = 0.672) 

with col2:
    glucose = st.number_input("Glucose Level", value = 85)
    insulin = st.number_input("Insulin Level(mm U/ml)", value = 99)

with col3:
    bloodP = st.number_input("Blood Pressure(mm Hg)", value = 66)
    bmi = st.number_input("BMI value", value = 26.6)    

inputs = [[pregnancies, glucose, bloodP, skinT, insulin, bmi, diapedfn, age]]

if st.button("Check Result"):
    prediction = diabetes_model.predict(inputs)

    if prediction == 1:
        diabetes_res = 'Alert! You might have Diabetes.'
        st.error(diabetes_res)

    else:
        diabetes_res = 'Congrats! You are non-diabetics.'
        st.success(diabetes_res)