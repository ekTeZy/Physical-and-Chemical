import pandas as pd
import kagglehub
from kagglehub import KaggleDatasetAdapter
import streamlit as st

@st.cache_data(show_spinner="Загружаем датасет с Kaggle...")
def load_dataset() -> pd.DataFrame:
    """
    Загружает датасет с физическими и химическими свойствами органических веществ из Kaggle.

    Эта функция использует библиотеку KaggleHub для загрузки датасета и возвращает его в виде DataFrame.
    Датасет содержит информацию о различных органических веществах и их свойствах.

    Возвращает:
        pd.DataFrame: DataFrame с данными о физических и химических свойствах органических веществ.
    """
    df = kagglehub.load_dataset(
        KaggleDatasetAdapter.PANDAS,
        "ivanyakovlevg/physical-and-chemical-properties-of-substances",
        path="physical_chemical_properties_of_organic_substances.csv"
    )
    return df
