import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(open('./saved_models/diabetes_model.sav', 'rb'))

with st.sidebar:
    menu =  option_menu('Diagnosis', ['Diabetes Diagnosis'], icons = ['activity'], default_index = 0)

if menu == 'Diabetes Diagnosis':

    st.title('Diabetes Diagnosis Using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        pregnancies = st.number_input("Number of Pregnancies")
    
    with col2:
        glucose = st.number_input("Glucose Level")

    with col3:
        bloodP = st.number_input("Blood Pressure")
    
    with col1:
        skinT = st.number_input("Skin Thickness")
    
    with col2:
        bmi = st.number_input("BMI value")

    with col3:
        diapedfn = st.number_input("Diabetes Pedigree Function")

    with col1:
        age = st.number_input("Age")

    with col2:
        insulin = st.number_input("Insulin Level")

    inputs = [pregnancies, glucose, bloodP, skinT, insulin, bmi, diapedfn, age]
    print(inputs)
    diabetes_res = ''

    if st.button("Check Diabetes"):
        prediction = diabetes_model.predict([inputs])

        if prediction == 1:
            diabetes_res = 'Positive- Patient has Diabetes'
        else:
            diabetes_res = 'Negative- Patient dosent have Diabetes'

    st.success(diabetes_res)


        
