import streamlit as st
 
import numpy as np
import pandas as pd
#import os


#accueil = "Bonjour " + os.environ["USERNAME"] 
#st.write(accueil)

st.markdown("""# Student Information
## The student's name
This is text""")
#pour recup du text
student = st.text_input('Name_student', 'your name')

st.write('Current student', student)

df = pd.DataFrame({
    'first column': list(range(1, 11)),
    'second column': np.arange(10, 101, 10)
})
 
# this slider allows the user to select a number of lines
# to display in the dataframe
# the selected value is returned by st.slider
line_count = st.slider('Select a line count', 1, 100, 50)

# and used to select the displayed lines
head_df = df.head(line_count)
 


#bouton
#Bouton
if st.button('display'):
    # print is visible in the server output, not in the page
    st.write('Current student', student)
    st.write('Age', line_count)
    head_df
    st.write('I was clicked 🎉')
    st.write('Further clicks are not visible but are executed')
else:
    st.write('I was not clicked 😞')