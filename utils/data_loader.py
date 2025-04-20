import pandas as pd
import kagglehub
from kagglehub import KaggleDatasetAdapter
import streamlit as st
import os

@st.cache_data(show_spinner="Загружаем датасет с Kaggle...")
def load_dataset() -> pd.DataFrame:
    df = kagglehub.load_dataset(
        KaggleDatasetAdapter.PANDAS,
        "ivanyakovlevg/physical-and-chemical-properties-of-substances",
        path="physical_chemical_properties_of_organic_substances.csv"
    )
    return df
