import streamlit as st
from pathlib import Path
import pandas as pd

# Définir le répertoire de sortie
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"

# Fonction pour charger les données avec cache
@st.cache_data
def load_csv_data(file_name):
    file_path = OUTPUT_DIR / file_name
    return pd.read_csv(file_path)