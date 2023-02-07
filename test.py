import pandas as pd
import streamlit as st


st.title("Streamlit test Web app")

uploaded_file=st.file_uploader("Please Share Order Details Here", type=["csv","excel"])

df=pd.read_csv(uploaded_file)

st.header("Uploaded File")
st.dataframe(df)