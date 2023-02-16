import pickle
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu
import tensorflow as tf
from PIL import Image

st.title("Welcome to Disease Diagnosis App")
st.markdown("As a passionate advocate for health and wellness, I, Yatharth Anand, developed a ML based web app for disease diagnosis as a personal project. This tool is designed to detect symptoms and risk factors for several prevalent diseases, including COVID-19, diabetes, cardiovascular disease, Alzheimer's, and lung cancer.")
st.header("Diseases")

col1, col2 = st.columns(2)
with col1:
    st.subheader("- Diabetes")
    st.subheader("- Covid-19")
    st.subheader("- Alzheimer's")

with col2:
    st.subheader("- Cardiovascular Diseases")
    st.subheader("- Lung Cancer")
    
st.info("Nagivate the sidebar on the left to visit different diseases and its diagnosis. This is just a personal project so I would suggest not to rely on it")
st.markdown("Using this app is simple. Just answer a few questions about your health history, symptoms, and lifestyle habits, and we'll provide you with your potential health concerns")


