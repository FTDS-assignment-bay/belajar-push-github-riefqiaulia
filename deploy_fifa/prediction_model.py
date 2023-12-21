import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import json
import streamlit as st

with open('model_lin_reg.pkl', 'rb') as file_1:
  model_lin = pickle.load(file_1)

with open('model_scaler.pkl', 'rb') as file_2:
  model_scaler = pickle.load(file_2)

with open('model_encoder.pkl', 'rb') as file_3:
  model_encoder = pickle.load(file_3)

with open('list_num_cols.txt', 'r') as file_4:
  num_col = json.load(file_4)

with open('list_cat_cols.txt', 'r') as file_5:
  cat_col = json.load(file_5)


def run():
#load file
   
    with st.form(key ='fifa form'):

      name= st.text_input('Name Of Player', value='Riefqi Ronaldo')
      age = st.number_input('Age', min_value=0, max_value=60, value=0, step=1,help='Usia Pemain')
      Height = st.number_input('Height', min_value=150, max_value=300, value=150,step=1,help='Tinggi Pemain')
      Weight = st.number_input('Weight', min_value=50, max_value=150)
      Price = st.number_input('Price', min_value=0, value=0,help='Harga Pemain')
      st.markdown('---')
      AttackingWorkRate= st.radio('AttackingWorkRate', ('Low', 'Medium', 'High'), index=1)
      DefensiveWorkRate= st.radio('DefensiveWorkRate', ('Low', 'Medium', 'High'), index=1)
      st.markdown('---')
      Pace = st.slider('PaceTotal', min_value=0, max_value=100)
      Shooting= st.slider('ShootingTotal', min_value=0, max_value=100)
      Passing = st.slider('PassingTotal', min_value=0, max_value=100)
      Dribbling = st.slider('DribblingTotal', min_value=0, max_value=100)
      Defending = st.slider('DefendingTotal', min_value=0, max_value=100)
      Physicality = st.slider('Pace Total', min_value=0, max_value=100)
      submitted = st.form_submit_button('Predict')

#create new data
    df_inf={
    'Name': name,
    'Age':age,
    'Height':Height,
    'Weight':Weight,
    'Price':Price,
    'AttackingWorkRate':AttackingWorkRate,
    'DefensiveWorkRate':DefensiveWorkRate,
    'PaceTotal':Pace,
    'ShootingTotal':Shooting,
    'PassingTotal':Passing,
    'DribblingTotal':Dribbling,
    'DefendingTotal':Defending,
    'PhysicalityTotal':Physicality,
}
    df_inf = pd.DataFrame([df_inf])
    df_inf

    if submitted:
      df_inf_num = df_inf[num_col]
      df_inf_cat = df_inf[cat_col]
      # Feature scaling and encoding
      df_inf_num_scaled = model_scaler.transform(df_inf_num)
      df_inf_cat_encoded = model_encoder.transform(df_inf_cat)

    # Concat
      df_inf_final = np.concatenate([df_inf_num_scaled,df_inf_cat_encoded],axis=1)
      y_pred_inf = model_lin.predict(df_inf_final)
      st.write(f'Rating {name}:', round(y_pred_inf[0],2))

if __name__=='__main__':
    run()
