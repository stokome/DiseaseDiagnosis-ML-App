import pickle
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu
import tensorflow as tf
from PIL import Image

cvd_model = tf.keras.models.load_model('./saved_models/cvd_model.h5')

st.title("Cardiovascular Disease")
st.header("What is Cardiovascular Disease?")
col1, col2 = st.columns(2)
with col1:
    st.markdown("Cardiovascular diseases (CVDs) are a group of disorders of the heart and blood vessels. They include:")
    st.markdown("1. Coronary heart disease: a disease of the blood vessels supplying the heart muscle")
    st.markdown("2. Cerebrovascular disease: a disease of the blood vessels supplying the brain")
    st.markdown("3. Peripheral arterial disease: a disease of blood vessels supplying the arms and legs")
    st.markdown("4. Congenital heart disease: birth defects that affect the normal development and functioning of the heart caused by malformations of the heart structure from birth")
    st.markdown("5. Deep vein thrombosis and pulmonary embolism: blood clots in the leg veins, which can dislodge and move to the heart and lungs")

with col2:
    cvd_image = Image.open('./images/cvd.png')
    st.image(cvd_image, width = 500)

st.subheader("Symptoms: ")
st.markdown("Heart disease describes a range of conditions that affect the heart. Heart diseases include:")
st.markdown("- Blood vessel disease, such as coronary artery disease")
st.markdown("- Irregular heartbeats (arrhythmias)")
st.markdown("- Heart problems you're born with (congenital heart defects)")
st.markdown("- Disease of the heart muscle")
st.markdown("- Heart valve disease")
st.header("Test for CVDs:")

col1, col2 = st.columns(2)
dict = {"Yes": 1, "No": 0, "Male": 1, "Female": 0}
with col1:
    age = st.slider("Age:", min_value = 0, max_value = 100, value = 50, step = 1)
    ap_high = st.slider("Systolic BP:", min_value = 40, max_value = 300, value = 120, step = 1)
    gender = st.radio("Sex:", ("Male", "Female"))
    drink = st.radio("Do you consume alcohol?", ("Yes", "No"))
    chol = st.radio("What is your cholesterol level:", ("High", "Low", "Normal"))

with col2:
    bmi = st.slider("BMI:", min_value = 10.0, max_value = 100.0, value = 20.0, step = 0.1)
    ap_low = st.slider("Distolic BP:", min_value = 40, max_value = 300, value = 80, step = 1)
    smoke = st.radio("Do you Smoke?:", ("Yes", "No"))
    active = st.radio("Are you physically active:", ("Yes", "No"))
    gluc = st.radio("What is your glucose level:", ("High", "Low", "Normal"))

if st.button("Check Result"):
    chol_nor, chol_abv, gluc_nor, gluc_abv = None, None, None, None
    if chol == "High":
        chol_nor = 0
        chol_abv = 1
    elif chol == "Low":
        chol_nor = 0
        chol_abv = 0
    else:
        chol_nor = 1
        chol_abv = 0

    if gluc == "High":
        gluc_nor = 0
        gluc_abv = 1
    elif gluc == "Low":
        gluc_nor = 0
        gluc_abv = 0
    else:
        gluc_nor = 1
        gluc_abv = 0

    inputs = [[age, dict[gender], ap_high, ap_low, dict[smoke], dict[drink], dict[active], bmi, chol_nor, gluc_nor, chol_abv, gluc_abv]]
    
    prediction = cvd_model.predict(inputs)
    if prediction > 0.98:
        st.error("Alert! You might have Cardiovascular Disease")
    else:
        st.success("Congrats! You do not have Cardiovascular Disease")

