# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 15:17:35 2026

@author: Thilak
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.markdown(
    """
    <style>
    /* Hide Manage app button */
    button[data-testid="stAppSettingsButton"] {
        display: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
   

    button[data-testid="stAppSettingsButton"] {
        display: none;
    }

    footer {
        display: none;
    }

    .block-container {
        padding-top: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)






st.markdown(
    """
    <style>
    h1, h2, h3, h4, h5, h6, p, label, span {
        color: white !important;
    }

    div[data-testid="stForm"] {
        background: rgba(255,255,255,0.08);
        backdrop-filter: blur(10px);
        border-radius: 14px;
        padding: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav','rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))
parkinsons_model= pickle.load(open('parkinsons_model.sav','rb'))

def set_bg(color1, color2):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: linear-gradient(135deg, {color1}, {color2});
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


with st.sidebar:
    st.markdown(
        """
        <style>
        /* Sidebar container */
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #0d47a1, #1976d2);            
            color: white;
        }
    
        /* Sidebar title text */
        section[data-testid="stSidebar"] h1,
        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3,
        section[data-testid="stSidebar"] p {
            color: white;
        }
    
        /* Sidebar menu items */
        section[data-testid="stSidebar"] .nav-link {
            color: #e3f2fd !important;
            font-size: 15px;
            padding: 8px;
            border-radius: 8px;
            margin-bottom: 5px;
        }
    
        /* Selected menu item */
        section[data-testid="stSidebar"] .nav-link-selected {
            background-color: #ffffff !important;
            color: #0d47a1 !important;
            font-weight: 700;
        }
    
        /* Sidebar icons */
        section[data-testid="stSidebar"] svg {
            fill: #bbdefb !important;
        }
    
        /* Divider */
        section[data-testid="stSidebar"] hr {
            border-color: rgba(255,255,255,0.3);
        }
    
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="
            background: rgba(255,255,255,0.15);
            padding: 15px;
            border-radius: 12px;
            text-align: center;">
            <h2>🩺 Health Predictor</h2>
            <p>AI-powered disease detection</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.divider()    
   

    selected = option_menu(
        "Select Prediction",
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
        icons=['activity', 'heart-pulse', 'person-lines-fill'],
        default_index=0,
        styles={
            "container": {"padding": "5px"},
            "icon": {"font-size": "18px"},
            "nav-link": {"font-size": "15px", "text-align": "left"},
            "nav-link-selected": {"background-color": "#0d6efd"}
        }
    )

    st.markdown(
        """
        <div style="position: fixed; bottom: 20px; color: #bbdefb;">
            <small>© 2026 Health AI</small>
        </div>
        """,
        unsafe_allow_html=True
    )

if selected == 'Diabetes Prediction':
    set_bg("#0b132b", "#1c2541")

elif selected == 'Heart Disease Prediction':
    set_bg("#4a0404", "#8b0000")

elif selected == 'Parkinsons Prediction':
    set_bg("#1f1147", "#5b2c83")

#Diabetes Prediction Page

if (selected == 'Diabetes Prediction'):  

    #set_bg("#7f0000", "#b71c1c")
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
    
    #page title
    #st.header('Diabetes Prediction using ML')

    col_title, col_btn = st.columns([4, 1])

    with col_title:
        st.header("🩸 Diabetes Prediction", divider="blue")
    
    with col_btn:
        st.markdown("<br>", unsafe_allow_html=True)  # vertical alignment
        st.button("🧹 Clear Form", type="secondary", on_click=clear_form)
        
    
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
    
        # ---------- Buttons ----------
        col1, col2 = st.columns(2)
        with col1:
            predict_btn = st.form_submit_button("🔍 Diabetes Test Result", type="primary")
        

    
    # ---------- Clear Button (OUTSIDE FORM) ----------
    #st.button("Clear Form", on_click=clear_form)

       
    # ---------- Prediction ----------
    if predict_btn:

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
                st.error("🔴 High Risk: The person is Diabetic")
            else:
                st.success("🟢 Low Risk: The person is not Diabetic")

                

#------------Heart Disease Prediction Page-------------------------
if (selected == 'Heart Disease Prediction'):
    #set_bg("#311b92", "#512da8")

    heart_defaults = {
        "age": 1,
        "sex": 0,
        "cp": 0,
        "trestbps": 80,
        "chol": 100,
        "fbs": 0,
        "restecg": 0,
        "thalach": 60,
        "exang": 0,
        "oldpeak": 0.0,
        "slope": 0,
        "ca": 0,
        "thal": 0
    }

    for key, val in heart_defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val

    def clear_heart_form():
        for key, val in heart_defaults.items():
            st.session_state[key] = val


    col_title, col_btn = st.columns([4, 1])

    with col_title:
        st.header("❤️ Heart Disease Prediction", divider="red")

    with col_btn:
        st.markdown("<br>", unsafe_allow_html=True)
        st.button("Clear Form", on_click=clear_heart_form)

    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input('Age', 1, 120, key="age")
    with col2:
        sex = st.number_input('Sex (1 = Male, 0 = Female)', 0, 1, key="sex")
    with col3:
        cp = st.number_input('Chest Pain Type (0–3)', 0, 3, key="cp")

    col1, col2, col3 = st.columns(3)
    with col1:
        trestbps = st.number_input('Resting Blood Pressure', 80, 200, key="trestbps")
    with col2:
        chol = st.number_input('Serum Cholesterol', 100, 600, key="chol")
    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120', 0, 1, key="fbs")

    col1, col2, col3 = st.columns(3)
    with col1:
        restecg = st.number_input('Resting ECG (0–2)', 0, 2, key="restecg")
    with col2:
        thalach = st.number_input('Max Heart Rate', 60, 250, key="thalach")
    with col3:
        exang = st.number_input('Exercise Induced Angina', 0, 1, key="exang")

    col1, col2, col3 = st.columns(3)
    with col1:
        oldpeak = st.number_input('ST Depression', 0.0, 10.0, key="oldpeak")
    with col2:
        slope = st.number_input('Slope (0–2)', 0, 2, key="slope")
    with col3:
        ca = st.number_input('Major Vessels', 0, 4, key="ca")

    thal = st.number_input('Thal (0–2)', 0, 2, key="thal")


    if st.button('Heart Disease Test Result'):

        errors = []
    
        # ---------- Input Validation ----------
        if age < 10:
            errors.append("⚠️ Age must be at least 10 years.")
    
        if trestbps < 80 or trestbps > 200:
            errors.append("⚠️ Resting blood pressure should be between 80 and 200 mm Hg.")
    
        if chol < 100 or chol > 600:
            errors.append("⚠️ Cholesterol value seems invalid (100–600).")
    
        if thalach < 60 or thalach > 250:
            errors.append("⚠️ Max heart rate should be between 60 and 250.")
    
        if oldpeak < 0:
            errors.append("⚠️ ST Depression cannot be negative.")
    
        if ca < 0 or ca > 4:
            errors.append("⚠️ Number of major vessels must be between 0 and 4.")
    
        if sex not in [0, 1]:
            errors.append("⚠️ Sex must be 0 (Female) or 1 (Male).")
    
        if cp not in [0, 1, 2, 3]:
            errors.append("⚠️ Chest pain type must be between 0 and 3.")
    
        if fbs not in [0, 1] or exang not in [0, 1]:
            errors.append("⚠️ Binary fields must be 0 or 1.")
    
        # ---------- Show Errors ----------
        if errors:
            st.error("Please correct the following before prediction:")
            for err in errors:
                st.write(err)
    
        # ---------- Prediction ----------
        else:
            heart_prediction = heart_disease_model.predict([[ 
                age, sex, cp, trestbps, chol, fbs,
                restecg, thalach, exang, oldpeak,
                slope, ca, thal
            ]])
    
            
            if heart_prediction[0] == 1:
                st.error("🔴 High Risk of Heart Disease")
            else:
                st.success("🟢 No Significant Risk Detected")




#------------Parkinsons Prediction Page-------------------------           
if (selected == 'Parkinsons Prediction'):
    #set_bg("#FF0000", "#ffe0b2")
    #set_bg("#0f2027", "#2c5364")

    # ---------- Defaults ----------
    parkinsons_defaults = {
        "fo": 0.0, "fhi": 0.0, "flo": 0.0,
        "Jitter_percent": 0.0, "Jitter_Abs": 0.0,
        "RAP": 0.0, "PPQ": 0.0, "DDP": 0.0,
        "Shimmer": 0.0, "Shimmer_dB": 0.0,
        "APQ3": 0.0, "APQ5": 0.0, "APQ": 0.0, "DDA": 0.0,
        "NHR": 0.0, "HNR": 0.0,
        "RPDE": 0.0, "DFA": 0.0,
        "spread1": 0.0, "spread2": 0.0,
        "D2": 0.0, "PPE": 0.0
    }

    for key, val in parkinsons_defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val

    def clear_parkinsons_form():
        for key, val in parkinsons_defaults.items():
            st.session_state[key] = val

    # ---------- Title + Clear Button ----------
    col_title, col_btn = st.columns([4, 1])

    with col_title:
        st.header("🧠 Parkinson’s Prediction", divider="violet")

    with col_btn:
        st.markdown("<br>", unsafe_allow_html=True)
        st.button("🧹 Clear Form", type="secondary", on_click=clear_parkinsons_form)

    # ---------- Input Form ----------
    with st.form("parkinsons_form"):

        cols = st.columns(5)
        with cols[0]: fo = st.number_input("MDVP:Fo(Hz)", key="fo")
        with cols[1]: fhi = st.number_input("MDVP:Fhi(Hz)", key="fhi")
        with cols[2]: flo = st.number_input("MDVP:Flo(Hz)", key="flo")
        with cols[3]: Jitter_percent = st.number_input("MDVP:Jitter(%)", key="Jitter_percent")
        with cols[4]: Jitter_Abs = st.number_input("MDVP:Jitter(Abs)", key="Jitter_Abs")

        cols = st.columns(5)
        with cols[0]: RAP = st.number_input("MDVP:RAP", key="RAP")
        with cols[1]: PPQ = st.number_input("MDVP:PPQ", key="PPQ")
        with cols[2]: DDP = st.number_input("Jitter:DDP", key="DDP")
        with cols[3]: Shimmer = st.number_input("MDVP:Shimmer", key="Shimmer")
        with cols[4]: Shimmer_dB = st.number_input("MDVP:Shimmer(dB)", key="Shimmer_dB")

        cols = st.columns(5)
        with cols[0]: APQ3 = st.number_input("Shimmer:APQ3", key="APQ3")
        with cols[1]: APQ5 = st.number_input("Shimmer:APQ5", key="APQ5")
        with cols[2]: APQ = st.number_input("MDVP:APQ", key="APQ")
        with cols[3]: DDA = st.number_input("Shimmer:DDA", key="DDA")
        with cols[4]: NHR = st.number_input("NHR", key="NHR")

        cols = st.columns(5)
        with cols[0]: HNR = st.number_input("HNR", key="HNR")
        with cols[1]: RPDE = st.number_input("RPDE", key="RPDE")
        with cols[2]: DFA = st.number_input("DFA", key="DFA")
        with cols[3]: spread1 = st.number_input("spread1", key="spread1")
        with cols[4]: spread2 = st.number_input("spread2", key="spread2")

        cols = st.columns(2)
        with cols[0]: D2 = st.number_input("D2", key="D2")
        with cols[1]: PPE = st.number_input("PPE", key="PPE")

        predict_btn = st.form_submit_button("🔍 Parkinson's Test Result", type="primary")

    # ---------- Prediction ----------
    if predict_btn:

        errors = []
    
        # --------- Basic Validations ----------
        if fo <= 0 or fhi <= 0 or flo <= 0:
            errors.append("⚠️ Frequency values (Fo, Fhi, Flo) must be greater than 0.")
    
        if Jitter_percent < 0 or Shimmer < 0:
            errors.append("⚠️ Jitter and Shimmer values cannot be negative.")
    
        if HNR <= 0:
            errors.append("⚠️ HNR must be greater than 0.")
    
        if D2 <= 0 or PPE <= 0:
            errors.append("⚠️ D2 and PPE must be greater than 0.")
    
        # Check if all inputs are zero
        all_inputs = [
            fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP,
            Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA,
            NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE
        ]
    
        if all(value == 0 for value in all_inputs):
            errors.append("⚠️ Please enter valid data. All values cannot be zero.")
    
        # --------- Show Errors ----------
        if errors:
            st.error("Please fix the following issues before prediction:")
            for err in errors:
                st.write(err)
    
        # --------- Prediction ----------
        else:
            input_data = [[
                fo, fhi, flo, Jitter_percent, Jitter_Abs,
                RAP, PPQ, DDP, Shimmer, Shimmer_dB,
                APQ3, APQ5, APQ, DDA, NHR, HNR,
                RPDE, DFA, spread1, spread2, D2, PPE
            ]]
    
            prediction = parkinsons_model.predict(input_data)
    
            if prediction[0] == 1:
                st.error("🔴 Parkinson’s Disease Detected")
            else:
                st.success("🟢 No Parkinson’s Disease Detected")

    





































































