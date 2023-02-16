import pickle
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu
import tensorflow as tf
from PIL import Image

lung_model = pickle.load(open('./saved_models/lung_cancer.sav', 'rb'))
lung_cancer_scaler = pickle.load(open('./saved_models/scaler_lung_cancer.pkl', 'rb'))

st.title("Lung Cancer")
lung_cancer_img = Image.open("./images/lung_cancer.jfif")
st.image(lung_cancer_img)
st.header("What is Lung Cancer?")
st.markdown("Cancer is a disease in which cells in the body grow out of control. When cancer starts in the lungs, it is called Lung Cancer. Lung cancer begins in the lungs and may spread to lymph nodes or other organs in the body, such as the brain. Cancer from other organs also may spread to the lungs. When cancer cells spread from one organ to another, they are called metastases.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Causes: ")
    st.markdown("- Smoking")
    st.markdown("- Exposure to secondhand smoke")
    st.markdown("- Previous radiation therapy")
    st.markdown("- Exposure to radon gas")   
    st.markdown("- Exposure to asbestos and other carcinogens")
    st.markdown("- Family history of lung cancer")

with col2:
    st.subheader("Symptoms: ")
    st.markdown("- A new cough that doesn't go away")
    st.markdown("- Coughing up blood, even a small amount")
    st.markdown("- Shortness of breath")
    st.markdown("- Chest pain")
    st.markdown("- Hoarseness")
    st.markdown("- Losing weight without trying")
    st.markdown("- Bone pain")
    st.markdown("- Headache")


st.header("Test for Lung Cancer")
col1, col2, col3 = st.columns(3)
dict = {"Yes": 1, "No": 0, "Male": 1, "Female": 0}
with col1:
    gender = st.radio("Sex:", ("Male", "Female"))
    anxiety = st.radio("Do you feel anxiety often?:", ("Yes", "No"))
    fatigue = st.radio("Do you feel fatigue?:", ("Yes", "No"))
    wheezing = st.radio("Do you feel like wheezing?:", ("Yes", "No"))
    swallow_diff = st.radio("Do you feel difficulty while swallowing?:", ("Yes", "No"))

with col2:
    smoke = st.radio("Do you Smoke?:", ("Yes", "No"))
    pp = st.radio("Do you feel peer pressure?:", ("Yes", "No"))
    drink = st.radio("Do you consume alcohol?:", ("Yes", "No"))
    cough = st.radio("Do you feel like coughing?:", ("Yes", "No"))
    chest_pain = st.radio("Do you have chest pain?:", ("Yes", "No"))

with col3:
    ylo_fng = st.radio("Are your fingers yellow?:", ("Yes", "No"))
    chronic_disease = st.radio("Do you have any chronic disease?:", ("Yes", "No"))
    allergy = st.radio("Do you have some kind of allergy?:", ("Yes", "No"))
    short_breath = st.radio("Are you experiancing shortness of breath?:", ("Yes", "No"))
    age = st.slider("Age", min_value = 0, max_value = 100, value = 50, step = 1)

if st.button("Check Result"):

    inputs = [[dict[gender], age, dict[smoke], dict[ylo_fng], dict[anxiety], dict[pp], dict[chronic_disease], dict[fatigue], dict[allergy], dict[wheezing], dict[drink], dict[cough], dict[short_breath], dict[swallow_diff], dict[chest_pain]]]

    
    inputs[0][1] = lung_cancer_scaler.transform([[inputs[0][1]]])[0][0]
    
    prediction = lung_model.predict(inputs)
    
    if prediction[0]:
        st.error("Alert! You might have Lung Cancer. Get yourself properly diagnosed")
    else:
        st.success("Congrats! You do not possess Lung Cancer")

