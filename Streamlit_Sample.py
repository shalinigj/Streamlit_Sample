import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.title("Penguins")
st.markdown('For scatterplot')
selected_species = st.selectbox('Please choose the species',['Adelie', 'Gentoo', 'Chinstrap'])
x_var = st.selectbox('Please choose x variable ',['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm','body_mass_g'])
y_var = st.selectbox('Please choose y',['bill_depth_mm', 'bill_length_mm', 'flipper_length_mm','body_mass_g'])
df = pd.read_csv('penguins.csv')
df = df[df['species'] == selected_species]
fig, ax = plt.subplots()
ax = sns.scatterplot(x = df[x_var],y = df[y_var])
plt.xlabel(x_var)
plt.ylabel(y_var)
plt.title('Scatterplot of {} Penguins'.format(selected_species))
st.pyplot(fig)