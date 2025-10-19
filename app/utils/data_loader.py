import pandas as pd

def load_data():
    """
    Cargar y preprocesar los datos del dataset de terremotos.
    
    Returns:
        pd.DataFrame: Dataset procesado
    """
    # Cargar datos
    df = pd.read_csv('C:\\Users\\u179376\\Documents\\GitHub\\Vulcans\\data\\earthquake_data_tsunami.csv')
    
    # Asegurar tipos de datos correctos
    numeric_columns = ['magnitude', 'depth', 'sig', 'nst', 'dmin', 'gap', 'cdi', 'mmi']
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    
    return df
