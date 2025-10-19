import pandas as pd
from pathlib import Path

def load_data():
    """
    Cargar y preprocesar los datos del dataset de terremotos.
    
    Returns:
        pd.DataFrame: Dataset procesado
    """
    DATA_PATH = Path(__file__).parent.parent.parent / "data" / "earthquake_data_tsunami.csv"

    # Cargar datos
    df = pd.read_csv(DATA_PATH)

    # Asegurar tipos de datos correctos
    numeric_columns = ['magnitude', 'depth', 'sig', 'nst', 'dmin', 'gap', 'cdi', 'mmi']
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    
    return df
