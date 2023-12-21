import streamlit as st
import eda
import prediction_model

navigation = st.sidebar.selectbox('Pilih halaman', ('EDA', 'Predict Player Rating'))

if navigation== 'EDA':
    eda.run()
else :
    prediction_model.run()