import pickle
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu
import tensorflow as tf

diabetes_model = pickle.load(open('./saved_models/diabetes_model.sav', 'rb'))


with st.sidebar:
    menu =  option_menu('Diagnosis', ['Diabetes', 
    'Covid-19', 
    'Heart', 
    "Lungs's Cancer", 
    'Alzheimer'], 
    icons = ['activity', 
    'activity', 
    'activity', 
    'activity', 
    'activity'], 
    default_index = 0)

if menu == 'Diabetes':

    st.title('Diabetes')
    st.header('What is Diabetes?')
    st.markdown("Diabetes is a chronic (long-lasting) health condition that affects how your body turns food into energy. Your body breaks down most of the food you eat into sugar (glucose) and releases it into your bloodstream. When your blood sugar goes up, it signals your pancreas to release insulin. Insulin acts like a key to let the blood sugar into your body’s cells for use as energy.With diabetes, your body doesn’t make enough insulin or can’t use it as well as it should. When there isn’t enough insulin or cells stop responding to insulin, too much blood sugar stays in your bloodstream. Over time, that can cause serious health problems, such as heart disease, vision loss, and kidney disease.")
    st.subheader("Symptoms")
    st.markdown("If you have any of the following diabetes symptoms, see your doctor about getting your blood sugar tested:")
    st.markdown("-Urinate (pee) a lot, often at night")
    st.markdown("-Are very thirsty")
    st.markdown("-Lose weight without trying")
    st.markdown("-Are very Hungary")
    st.markdown("-Have blurry vivion")
    st.markdown("-Feel very Tired")
    st.header("Test for Diabetes")
    
    col1, col2, col3 = st.columns(3)


    pregnancies = st.slider('Number of Pregnencies', min_value=0, max_value=10, value=1, step=1)
    
    with col2:
        glucose = st.number_input("Glucose Level", value = 85)

    with col3:
        bloodP = st.number_input("Blood Pressure(mm Hg)", value = 66)
    
    with col1:
        skinT = st.number_input("Triceps Skin Thickness (mm)", value = 29)

    with col2:
        insulin = st.number_input("Insulin Level(mm U/ml)", value = 99)
    
    with col3:
        bmi = st.number_input("BMI value", value = 26.6)

    with col1:
        diapedfn = st.number_input("Diabetes Pedigree Function", value = 0.672)

    age = st.slider("Age", min_value = 0, max_value = 100, value = 50, step = 1)

    

    inputs = [[pregnancies, glucose, bloodP, skinT, insulin, bmi, diapedfn, age]]
    diabetes_res = ''

    if st.button("Check Diabetes"):
        prediction = diabetes_model.predict(inputs)

        if prediction == 1:
            diabetes_res = 'You might have Diabetes.'
            st.error(diabetes_res)

        else:
            diabetes_res = 'You are non-diabetics.'
            st.success(diabetes_res)

    


        
