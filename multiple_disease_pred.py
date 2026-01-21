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
    
    
    with st.form("diabetes_form"):
    
        # ---------- Row 1 ----------
        col1, col2, col3 = st.columns(3)
        with col1:
            Pregnancies = st.number_input(
                "Number of Pregnancies",
                min_value=0, max_value=20, step=1,
                key="Pregnancies"
            )
        with col2:
            Glucose = st.number_input(
                "Glucose Level (mg/dL)",
                min_value=0, max_value=300,
                key="Glucose"
            )
        with col3:
            BloodPressure = st.number_input(
                "Blood Pressure (mm Hg)",
                min_value=0, max_value=200,
                key="BloodPressure"
            )
    
        # ---------- Row 2 ----------
        col1, col2, col3 = st.columns(3)
        with col1:
            SkinThickness = st.number_input(
                "Skin Thickness (mm)",
                min_value=0, max_value=100,
                key="SkinThickness"
            )
        with col2:
            Insulin = st.number_input(
                "Insulin Level (µU/mL)",
                min_value=0, max_value=900,
                key="Insulin"
            )
        with col3:
            BMI = st.number_input(
                "BMI",
                min_value=0.0, max_value=70.0, format="%.2f",
                key="BMI"
            )
    
        # ---------- Row 3 ----------
        col1, col2, col3 = st.columns(3)
        with col1:
            DiabetesPedigreeFunction = st.number_input(
                "Diabetes Pedigree Function",
                min_value=0.0, max_value=3.0, format="%.3f",
                key="DPF"
            )
        with col2:
            Age = st.number_input(
                "Age",
                min_value=1, max_value=120, step=1,
                key="Age"
            )
    
        # ---------- Buttons ----------
        col1, col2 = st.columns(2)
        with col1:
            submitted = st.form_submit_button("Diabetes Test Result")
        with col2:
            clear = st.form_submit_button("Clear")
    
        
        
   
    # Code for Pediction    
   
    #Creating a button for Predicition

    # ---------- Validation ----------
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
            # 🔸 Process data here
            
            diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
           
            if (diab_prediction[0]==1):
                st.warning('The Person is Diabetic')            
            else: 
                st.success('The Person is not Diabetic ')

       
    if clear:
        for key, value in defaults.items():
            st.session_state[key] = value
        st.experimental_rerun()


            
if (selected == 'Heart Disease Prediction'):
    
    #page title
    st.title('Heart Prediction using ML')
    
    
    #getting the input data from the user
   
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    col1, col2, col3 = st.columns(3)
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    col1, col2, col3 = st.columns(3)
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    col1, col2, col3 = st.columns(3)
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    col1, col2, col3 = st.columns(3)
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
   
    # code for Prediction
     
    #Creating a button for Predicition
   
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
       
        if heart_prediction[0] == 1:
            st.warning('The person is having heart disease')  
        else:
            st.success('The person does not have any heart disease')
           
    
    

if (selected == 'Parkinsons Prediction'):
    
    #page title
    st.title('Parkinsons Prediction using ML')
    
    #getting the input data from the user
   
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

   
    # Code for Pediction
 
   
    #Creating a button for Predicition
   
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
       
        if parkinsons_prediction[0] == 1:
            st.warning("The person has Parkinson's disease")
        else:
            st.success("The person does not have Parkinson's disease")

   

    













