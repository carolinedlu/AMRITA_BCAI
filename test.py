# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 20:09:40 2023
@author: RATUL BHOWMIK
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models
cancer_first_model = pickle.load(open('Random_forest_v1.pkl', 'rb'))
cancer_second_model = pickle.load(open('Random_forest_v2.pkl', 'rb'))
cancer_third_model = pickle.load(open('Random_forest_v3.pkl', 'rb'))

# Page expands to full width
st.set_page_config(page_title='AMRITA-BCAI', page_icon='🌐', layout="wide")

# For hiding streamlite messages
st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_option('deprecation.showfileUploaderEncoding', False)

# Create title and subtitle
html_temp = """
		<div style="background-color:teal">
		<h1 style="font-family:arial;color:white;text-align:center;">AMRITA-BCAI</h1>
		<h4 style="font-family:arial;color:white;text-align:center;">Artificial Intelligence Based Breast-Cancer-Prediction Web-App</h4>
		</div>
		<br>
		"""
st.markdown(html_temp, unsafe_allow_html=True)

st.sidebar.title("AMRITA-BCAI")
st.sidebar.header("Menu")
CB = st.sidebar.checkbox("Web Application Information")

if CB:
    st.title('Application Description')
    st.success(
        "This module of [**AMRITA-BCAI](https://github.com/MohanChemoinformaticsLab) helps to predict nodal stages based on users clinical data."
        " It also helps to predict sentinal node status using robust machine learning algorithm.")

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Artificial Intelligence assisted Machine Learning Breast Cancer Prediction Models',
                           ['Cancer nodal stages prediction N0 and N1',
                            'Cancer nodal stages prediction N2 and N3',
                            'Cancer multiple nodal stages prediction N0, N1, N2, and N3'],
                           icons=['activity', 'person', 'activity'],
                           default_index=0)

# Cancer Nodal Stages N0 and N1 prediction
if selected == 'Cancer nodal stages prediction N0 and N1':
    # page title
    st.title('Nodal Stages N0 and N1 prediction using AI/ML')

    # Get input from the user using selectbox for categorical options
    menopause_options = {"1": "Pre", "2": "Post", "3": "Peri"}
    menopaus_stat = st.selectbox("Select your menopause status", list(menopause_options.keys()), format_func=lambda x: menopause_options[x], key="menopause_n1")

    ptnm_tstage_options = {"0": "T0", "1": "T1", "2": "T2", "3": "T3", "4": "T4"}
    ptnm_tstage = st.selectbox("Select your clinically tested Tumor Stage", list(ptnm_tstage_options.keys()), format_func=lambda x: ptnm_tstage_options[x], key="tumor_stage_n1")

    ihc_options = {"1": "Strong", "2": "Weak", "3": "Negative"}
    ihc_er = st.selectbox("Select your clinically tested estrogen status", list(ihc_options.keys()), format_func=lambda x: ihc_options[x], key="estrogen_n1")

    ihc_pr = st.selectbox("Select your clinically tested progesterone status", list(ihc_options.keys()), format_func=lambda x: ihc_options[x], key="progesterone_n1")

    ihc_her2neu = st.selectbox("Select your clinically tested HER2 status", ["0", "1", "2", "3"], key="her2_n1")
    ki67 = st.text_input("Enter your clinically tested KI67 status", key="ki67_n1")

    # Creation of a button for prediction
    if st.button('Nodal Stages N0 and N1 diagnosis'):
        nodal_initial_stages_pred = cancer_first_model.predict([[menopaus_stat, ptnm_tstage, ihc_er, ihc_pr, ihc_her2neu, ki67]])

        if nodal_initial_stages_pred[0] == 1:
            nodal_initial_stages_diag = 'The predicted nodal stage is N1'
        elif nodal_initial_stages_pred[0] == 0:
            nodal_initial_stages_diag = 'The predicted nodal stage is N0.'
        else:
            nodal_initial_stages_diag = 'Nodal stage prediction not available'

        st.success(nodal_initial_stages_diag)

# Cancer Nodal Stages N2 and N3 prediction
if selected == 'Cancer nodal stages prediction N2 and N3':
    # page title
    st.title('Nodal Stages N2 and N3 prediction using AI/ML')

    # ... (your imports and initial code)

# Get input from the user using selectbox for categorical options
    menopause_options = {"1": "Pre", "2": "Post", "3": "Peri"}
    menopaus_stat = st.selectbox("Select your menopause status", list(menopause_options.keys()), format_func=lambda x: menopause_options[x], key="menopause_n2")

    ptnm_tstage_options = {"0": "T0", "1": "T1", "2": "T2", "3": "T3", "4": "T4"}
    ptnm_tstage = st.selectbox("Select your clinically tested Tumor Stage", list(ptnm_tstage_options.keys()), format_func=lambda x: ptnm_tstage_options[x], key="tumor_stage_n2")

    ihc_options = {"1": "Strong", "2": "Weak", "3": "Negative"}
    ihc_er = st.selectbox("Select your clinically tested estrogen status", list(ihc_options.keys()), format_func=lambda x: ihc_options[x], key="estrogen_n2")

    ihc_pr = st.selectbox("Select your clinically tested progesterone status", list(ihc_options.keys()), format_func=lambda x: ihc_options[x], key="progesterone_n2")

    ihc_her2neu = st.selectbox("Select your clinically tested HER2 status", ["0", "1", "2", "3"], key="her2_n2")
    ki67 = st.text_input("Enter your clinically tested KI67 status", key="ki67_n2")

    # Creation of a button for prediction
    if st.button('Nodal Stages N2 and N3 diagnosis'):
        nodal_initial_stages_2_pred = cancer_second_model.predict([[menopaus_stat, ptnm_tstage, ihc_er, ihc_pr, ihc_her2neu, ki67]])

        if nodal_initial_stages_2_pred[0] == 2:
            nodal_initial_stages_2_diag = 'The predicted nodal stage is N2'
        elif nodal_initial_stages_2_pred[0] == 3:
            nodal_initial_stages_2_diag = 'The predicted nodal stage is N3'
        else:
            nodal_initial_stages_2_diag = 'Nodal stage prediction not available'

        st.success(nodal_initial_stages_2_diag)

# Cancer Multiple Nodal Stages prediction
if selected == 'Cancer multiple nodal stages prediction N0, N1, N2, and N3':
    # page title
    st.title('Multiple Nodal Stages N0, N1, N2 and N3 prediction using AI/ML')

    menopause_options = {"1": "Pre", "2": "Post", "3": "Peri"}
    menopaus_stat = st.selectbox("Select your menopause status", list(menopause_options.keys()), format_func=lambda x: menopause_options[x], key="menopause_n3")

    ptnm_tstage_options = {"0": "T0", "1": "T1", "2": "T2", "3": "T3", "4": "T4"}
    ptnm_tstage = st.selectbox("Select your clinically tested Tumor Stage", list(ptnm_tstage_options.keys()), format_func=lambda x: ptnm_tstage_options[x], key="tumor_stage_n3")

    ihc_options = {"1": "Strong", "2": "Weak", "3": "Negative"}
    ihc_er = st.selectbox("Select your clinically tested estrogen status", list(ihc_options.keys()), format_func=lambda x: ihc_options[x], key="estrogen_n3")

    ihc_pr = st.selectbox("Select your clinically tested progesterone status", list(ihc_options.keys()), format_func=lambda x: ihc_options[x], key="progesterone_n3")

    ihc_her2neu = st.selectbox("Select your clinically tested HER2 status", ["0", "1", "2", "3"], key="her2_n3")
    ki67 = st.text_input("Enter your clinically tested KI67 status", key="ki67_n3")

    # Creation of a button for prediction
    if st.button('Multiple Nodal stages diagnosis'):
        nodal_initial_stages_3_pred = cancer_third_model.predict([[menopaus_stat, ptnm_tstage, ihc_er, ihc_pr, ihc_her2neu, ki67]])

        if nodal_initial_stages_3_pred[0] == 0:
            nodal_initial_stages_3_diag = 'The predicted nodal stage is N0'
        elif nodal_initial_stages_3_pred[0] == 1:
            nodal_initial_stages_3_diag = 'The predicted nodal stage is N1'
        elif nodal_initial_stages_3_pred[0] == 2:
            nodal_initial_stages_3_diag = 'The predicted nodal stage is N2'
        elif nodal_initial_stages_3_pred[0] == 3:
            nodal_initial_stages_3_diag = 'The predicted nodal stage is N3'
        else:
            nodal_initial_stages_3_diag = 'Nodal stage prediction not available'

        st.success(nodal_initial_stages_3_diag)

