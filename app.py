import pickle
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu
import tensorflow as tf
from PIL import Image

diabetes_model = pickle.load(open('./saved_models/diabetes_model.sav', 'rb'))
covid_model = pickle.load(open('saved_models\covid_model.sav', 'rb'))


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
    default_index = 1)

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
            diabetes_res = 'You might have Diabetes.'
            st.error(diabetes_res)

        else:
            diabetes_res = 'You are non-diabetics.'
            st.success(diabetes_res)

elif menu == "Covid-19":
    
    st.title("Covid-19")
    covid_img = Image.open("images\covid.jpg")
    st.image(covid_img, caption = 'covid-19 virus', width = 500)
    st.header("What is covid-19?")
    st.markdown("Coronavirus disease 2019 (COVID-19) is a contagious disease caused by a virus, the severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). The first known case was identified in Wuhan, China, in December 2019.[5] The disease quickly spread worldwide, resulting in the COVID-19 pandemic.")
    st.subheader("Pandemic Statistics")
    covid_stat_img = Image.open("images\covid-stat.png")
    st.image(covid_stat_img, width = 700)
    st.subheader("Symptoms of Covid-19-")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("-Fever or chills")
        st.markdown("-Cough")
        st.markdown("-Shortness of breath or difficulty breathing")
        st.markdown("-Fatigue")
        st.markdown("-Muscle or body aches")
        st.markdown("-Headache")
    with col2:
        st.markdown("-New loss of taste or smell")
        st.markdown("-Sore throat")
        st.markdown("-Congestion or runny nose")
        st.markdown("-Nausea or vomiting")
        st.markdown("-Diarrhea")

    st.header("Test for Covid-19")

    col1, col2, col3 = st.columns(3)
    dict = {"Yes": 1, "No": 0}
    with col1:
        breath_prob = st.radio("Do you have any problem in breathing?", ("Yes", "No"))
        sore_throat = st.radio("Do you have sore throat?", ("Yes", "No"))
        contact_patient = st.radio("Did you had any contact with covid positive patient?", ("Yes", "No"))
        family_public_place = st.radio("Does any family member work near public place?", ("Yes", "No"))

    with col2:
        fever = st.radio("Do you have fever?", ("Yes", "No"))
        hypertension = st.radio("Do you have hyper tension", ("Yes", "No"))
        large_gather = st.radio("Have you attended any large gathering in past 2 week?", ("Yes", "No"))

    with col3:
        dry_cough = st.radio("Do you have dry cough?", ("Yes", "No"))
        abroad = st.radio("Did you travel abroad in last 2 weeks?", ("Yes", "No"))
        public_place = st.radio("Do you visit public places?", ("Yes", "No"))

    inputs = [[dict[breath_prob], dict[fever], dict[dry_cough], dict[sore_throat], dict[hypertension], dict[abroad], dict[contact_patient], dict[large_gather], dict[public_place], dict[family_public_place]]]


    if st.button("Check Result"):
        prediction = covid_model.predict(inputs)

        if prediction == 1:
            covid_res = 'You might have Covid. Please get yourself diaognised properly'
            st.error(covid_res)

        else:
            covid_res = 'Congrats, you are Covid-Negative.'
            st.success(covid_res)


        

    
    


        
