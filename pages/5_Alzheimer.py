import pickle
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu
import tensorflow as tf
from PIL import Image

alzheimer_model = tf.keras.models.load_model('saved_models/alzheimer_model.h5')
alz_img = Image.open('images/alzheimer.webp')
st.image(alz_img)
st.header("What is Alzheimer's Disease?")
st.markdown("Alzheimer’s disease is the most common type of dementia. It is a progressive disease beginning with mild memory loss and possibly leading to loss of the ability to carry on a conversation and respond to the environment. Alzheimer’s disease involves parts of the brain that control thought, memory, and language. It can seriously affect a person’s ability to carry out daily activities.")
st.subheader("Symptoms- ")
st.markdown("- Repeat statements and questions over and over.")
st.markdown("- Forget conversations, appointments or events.")
st.markdown("- Misplace items, often putting them in places that don't make sense.")
st.markdown("- Get lost in places they used to know well.")
st.markdown("- Eventually forget the names of family members and everyday objects")
st.markdown("- Have trouble finding the right words for objects, expressing thoughts or taking part in conversations.")

st.header("Test for Alzheimer")
st.markdown("Alzheimer's disease is thought to be caused by the abnormal build-up of proteins in and around brain cells.")
st.markdown("Upload photo of your brain MRI scan to test for alzheimer's disease")
mri_image = st.file_uploader("Upload Brain MRI Scan", type = ['jpg', 'png'])
dementia_dict = ['Mild Dementia', 'Morderate Dementia', 'no Dementia', 'Very Mild Dementia']
if st.button("Check Result"):
    if mri_image:
        st.image(mri_image)
        mri_image = tf.keras.preprocessing.image.load_img(mri_image, target_size= [176, 208])
        mri_image = tf.keras.preprocessing.image.img_to_array(mri_image)
        mri_image = np.array([mri_image])
        prediction = alzheimer_model.predict(mri_image)
        for i in range(len(prediction[0])):
            if prediction[0][i] == max(prediction[0]):
                st.info("You have " + dementia_dict[i])
        
    else:
        st.error("Please upload image")

