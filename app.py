import streamlit as st
from utils.data_loader import load_dataset
from utils.analysis import compute_basic_metrics

st.title("Physical and Chemical Properties Dashboard")

df = load_dataset()

st.subheader("Пример данных")
st.dataframe(df.head(10))

st.subheader("Основные статистики")
metrics = compute_basic_metrics(df)

col1, col2, col3 = st.columns(3)
col1.metric("Средняя молекулярная масса", f"{metrics['Средняя масса (g/mol)']} g/mol")
col2.metric("Средняя температура кипения", f"{metrics['Средняя t кипения (K)']} K")
col3.metric("Медианная температура плавления", f"{metrics['Медианная t плавления (K)']} K")
