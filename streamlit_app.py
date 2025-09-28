import streamlit as st
import pandas as pd



st.title('My Machine Learning App')

with st.expander("Data"):
  st.write('## Raw Data')
  st.write('This the machine learning app')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
  df
