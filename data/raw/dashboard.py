import pandas as pd
import streamlit as st

st.title("Smart Hospital Predictor Dashboard")

# Load CSV
file_path = r"C:\Users\vinot\smart-hospital-predictor\smart-hospital-predictor\data\processed\processed.csv"
df = pd.read_csv(file_path)

# Show data and summary
st.subheader("Hospital Data")
st.dataframe(df)

st.subheader("Summary Statistics")
st.write(df.describe())
