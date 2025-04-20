import streamlit as st
from utils.data_loader import load_dataset

st.title("🚀 Physical & Chemical Properties")

df = load_dataset()
st.write("📄 Загружен датасет:")
st.dataframe(df.head())
