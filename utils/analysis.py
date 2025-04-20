import pandas as pd
from typing import Dict

def compute_basic_metrics(df: pd.DataFrame) -> Dict[str, float]:
    metrics: dict = {
        "Средняя масса (g/mol)": round(df["molecular_weight"].mean(), 2),
        "Средняя t кипения (K)": round(df["boiling_point_K"].mean(), 2),
        "Медианная t плавления (K)": round(df["melting_point_K"].median(), 2)
    }
    return metrics
