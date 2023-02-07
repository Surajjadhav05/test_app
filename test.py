import pandas as pd
import streamlit as st


st.title("Streamlit test Web app")

uploaded_file=st.file_uploader("Please Share Order Details Here", type=["csv","excel"])
if uploaded_file is not None: 
    df=pd.read_csv(uploaded_file)

    st.header("Uploaded File")
    st.dataframe(df)
else:
    st.header("Please upload file")