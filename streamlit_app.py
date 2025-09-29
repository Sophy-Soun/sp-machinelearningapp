import streamlit as st
import pandas as pd



st.title('My Machine Learning App')

with st.expander("Data"):
  st.write('## Raw Data')
  st.write('This the machine learning app')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
  df
  st.write('**X**')
  X_raw = df.drop('species', axis=1)
  X_raw
  st.write('**y**')
  y_raw = df.species
  y_raw
with st.expander('Data Visulization'):
  # "bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g","sex"
  st.scatter_chart(data = df, x ='bill_length_mm', y = 'body_mass_g', color = 'species')

with st.sidebar:
  st.header('Input Features')
  island = st.selectbox('Island', ('Biscoe','Drean','Tergernson'))
  bill_length_mm = st.slider('Bill Length (mm)',32.1,59.6, 43.9)
  bill_dept_mm = st.slider('Bill Depth (mm)',13.1, 21.5, 17.2)
  flipper_mm = st.slider('Fipper Length (mm)', 172.0, 231.0, 201.0)
  body_mass_g = st.slider('Body Mass (g)', 2700.0, 6300.0, 4207.0)
  gender = st.selectbox('Gender', ('male', 'female'))

# Create the DataFrame for input features
data = {'island': island,
       'bill_length_mm': bill_length_mm,
       'bill_dept_mm':bill_dept_mm,
       'flipper_mm': flipper_mm,
       'body_mass_g':body_mass_g,
       'sex':gender}
input_df = pd.DataFrame(data, index = [0])
input_penguins = pd.concat([input_df, X_raw], axis = 0)

# Encoder X
encoder = ['island', 'sex']
df_penquins = pd.get_dummies(input_penguins, prefix = encoder)
input_row = df_penquins[:1]

# Encode y
target_mapper = {'Adelie': 0,
                'Chinstrap':1,
                'Gento':2}
def target_mapper(val):
  return target_mapper[val]
y = y_raw.apply(target_encode)
y
with st.expander('Input Features'):
  st.write('**Input Penquin**')
  input_df
  st.write('*Combined penquins data*')
  input_penguins
  st.write('Input Penguin Features')
  input_row























