import streamlit as st
from utils.data_loader import load_dataset
from utils.analysis import compute_basic_metrics

"""Главная функция запуска Streamlit-приложения."""
st.title("Physical and Chemical Properties Dashboard")

# Загрузка данных
df = load_dataset()

# Панель фильтров
st.sidebar.header("Фильтры")

# Фильтрация по типу соединения (kingdom)
unique_kingdoms = df["kingdom"].dropna().unique().tolist()
selected_kingdoms = st.sidebar.multiselect(
    "Тип соединения (kingdom)",
    options=unique_kingdoms,
    default=unique_kingdoms
)

min_temp = int(df["boiling_point_K"].min(skipna=True))
max_temp = int(df["boiling_point_K"].max(skipna=True))
boiling_range = st.sidebar.slider(
    "Температура кипения (K)",
    min_value=min_temp,
    max_value=max_temp,
    value=(min_temp, max_temp)
)

# Применение фильтров
df_filtered = df[
    df["kingdom"].isin(selected_kingdoms) &
    df["boiling_point_K"].between(boiling_range[0], boiling_range[1])
]

# Отображение базовых метрик
st.subheader("Основные статистики")
metrics = compute_basic_metrics(df_filtered)

col1, col2, col3 = st.columns(3)
col1.metric("Средняя молекулярная масса", f"{metrics['Средняя масса (g/mol)']} g/mol")
col2.metric("Средняя температура кипения", f"{metrics['Средняя t кипения (K)']} K")
col3.metric("Медианная температура плавления", f"{metrics['Медианная t плавления (K)']} K")

# Таблица с фильтрованными данными
st.subheader("Пример отфильтрованных данных")
st.dataframe(df_filtered.head(10))

# Визуализация гистограммы
import plotly.express as px
st.subheader("Распределение температуры кипения")
fig = px.histogram(
    df_filtered,
    x="boiling_point_K",
    nbins=30,
    title="Гистограмма температур кипения"
)
st.plotly_chart(fig, use_container_width=True)