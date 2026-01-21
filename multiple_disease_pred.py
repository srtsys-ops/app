# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 15:17:35 2026

@author: Thilak
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# Loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav','rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))
parkinsons_model= pickle.load(open('parkinsons_model.sav','rb'))

with st.sidebar:
    selected = option_menu('Mutiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           icons = ['activity','heart','person'],
                           default_index = 0
                           )

#Diabetes Prediction Page

if (selected == 'Diabetes Prediction'):    
    
    #page title
    st.header('Diabetes Prediction using ML')


    # ---------- Initialize session state ----------
    # ---------- Initialize session state ----------
    defaults = {
        "Pregnancies": 0,
        "Glucose": 0,
        "BloodPressure": 0,
        "SkinThickness": 0,
        "Insulin": 0,
        "BMI": 0.0,
        "DPF": 0.0,
        "Age": 1
    }
    
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value
    
    
    def clear_form():
        for key, value in defaults.items():
            st.session_state[key] = value
    
    
    # ---------- Form ----------
    with st.form("diabetes_form"):
    
        col1, col2, col3 = st.columns(3)
        with col1:
            Pregnancies = st.number_input(
                "Number of Pregnancies", 0, 20, key="Pregnancies"
            )
        with col2:
            Glucose = st.number_input(
                "Glucose Level (mg/dL)", 0, 300, key="Glucose"
            )
        with col3:
            BloodPressure = st.number_input(
                "Blood Pressure (mm Hg)", 0, 200, key="BloodPressure"
            )
    
        col1, col2, col3 = st.columns(3)
        with col1:
            SkinThickness = st.number_input(
                "Skin Thickness (mm)", 0, 100, key="SkinThickness"
            )
        with col2:
            Insulin = st.number_input(
                "Insulin Level (µU/mL)", 0, 900, key="Insulin"
            )
        with col3:
            BMI = st.number_input(
                "BMI", 0.0, 70.0, format="%.2f", key="BMI"
            )
    
        col1, col2 = st.columns(2)
        with col1:
            DPF = st.number_input(
                "Diabetes Pedigree Function", 0.0, 3.0, format="%.3f", key="DPF"
            )
        with col2:
            Age = st.number_input(
                "Age", 1, 120, key="Age"
            )
    
        submitted = st.form_submit_button("Diabetes Test Result")
    
    
    # ---------- Clear Button (OUTSIDE FORM) ----------
    st.button("Clear Form", on_click=clear_form)
    
    
    # ---------- Prediction ----------
    if submitted:
    
        errors = []
    
        if Glucose < 70:
            errors.append("⚠️ Glucose level seems too low.")
        if BloodPressure < 40:
            errors.append("⚠️ Blood Pressure seems too low.")
        if BMI < 10:
            errors.append("⚠️ BMI value seems invalid.")
        if Age < 10:
            errors.append("⚠️ Age must be at least 10 years.")
    
        if errors:
            st.error("Please correct the following:")
            for err in errors:
                st.write(err)
        else:
            diab_prediction = diabetes_model.predict([[
                Pregnancies, Glucose, BloodPressure,
                SkinThickness, Insulin, BMI, DPF, Age
            ]])
    
            if diab_prediction[0] == 1:
                st.warning("The Person is Diabetic")
            else:
                st.success("The Person is not Diabetic")


       
    
        



            


   

    

















