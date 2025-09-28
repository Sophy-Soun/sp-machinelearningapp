import streamlit as st
import pandas as pd



st.title('My Machine Learning App')

with st.expander("Data"):
  st.write('## Raw Data')
  st.write('This the machine learning app')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
  df
  st.write('## X')
  X = df.drop('species', axis=1)
  X
  st.write('## y')
  y = df.species
  y
with st.expander('Data Visulization'):
  # "bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g","sex"
  st.scatter_chart(data = df, x ='bill_length_mm', y = 'body_mass_g', color = 'species')

with st.sidebar:
  st.header('Input Features')
