import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image
# !pip install plotly
#set page cofig
st.set_page_config(
    page_title= 'FIFA_2022_EDA',
    layout='wide',
    initial_sidebar_state='expanded'
)

#create function for eda
def run():
    #create title/membuat judul
    st.title('FIFA 2022 Player Rating Prediction')

    #create sub header/membuat sub judul
    st.subheader('EDA untuk Analisis Dataset FIFA 2033')

    #menambahkan gambar
    st.image('https://media.bleacherreport.com/image/upload/x_11,y_11,w_1780,h_1188,c_crop/c_fill,g_faces,w_3800,h_2000,q_95/v1678812368/cnlukxiel3sx0308ys4d.jpg',
             caption='Argetina Juara')
    
    #membuat deskripsi
    st.write('Page ini dibuat oleh Riefqi')
    st.write('# Deskripsi 1')
    st.write('## Deskripsi 1')
    st.write('### Deskripsi 1')

    #Magic syintax
    '''
    Pada page kali ini,penulism akan melakukan eksplorasi sedrhana,
    Dataset yang digunakan adalah FIFA 2022.
    Dataset ini berasal dari web sofifa.com
    '''

    #create straight line
    st.markdown('---')

    # show dataframe
    df=pd.read_csv('https://raw.githubusercontent.com/FTDS-learning-materials/phase-1/master/w1/P1W1D1PM%20-%20Machine%20Learning%20Problem%20Framing.csv')
    st.dataframe(df)

    # create barplot
    st.write('### Plot AttackingWorkRate')
    fig = plt.figure(figsize=(15,5))
    sns.countplot(x='AttackingWorkRate',data=df)
    st.pyplot(fig)
    
    #statement Barachart using magic syntax
    '''
    Medium ada xxx Low ad xxx High xxx...
    '''

    
    #create histogram based on input user
    st.write('### Histogram Berdasarkan Input User')
    pilihan= st.selectbox('Pilihan:',('Age', 'Weight', 'ShootingTotal'))
    fig = plt.figure(figsize=(15,5))
    sns.histplot(df[pilihan], bins=30)
    st.pyplot(fig)

    
    #statement
    st.write('Age normal distribusi....bla bla bla')
    

    
    #create plotly plot
    '''
    Objective 3:
    
    **Saya mempunyai hipotesis bahwa korelasi mereka positif dan rating dipengaruhi oleh harga pemain dipasar,lets prove it!**
    '''
    st.write('### Plotly Plot - ValueEur vs Overall')
    fig = px.scatter(df,x='ValueEUR', y='Overall',
                     hover_data=['Name','Age'])
    st.plotly_chart(fig)
    '''
    Berarti tidak selalu price menjadi faktor penentu Rating
    contohnya messi,ronaldo dan neuer.
    Bisa jadi ada faktor lain yaitu faktor usia
    '''














if __name__=='__main__':
    run()



