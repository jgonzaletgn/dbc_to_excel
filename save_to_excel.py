# save_to_excel.py
import pandas as pd

def save_to_excel(df, output_file):
    """
    Guarda el DataFrame en un archivo Excel.
    """
    try:
        df.to_excel(output_file, index=False)  # index=False para evitar que se guarde el índice como columna
        print(f"Archivo Excel guardado exitosamente: {output_file}")
    except Exception as e:
        print(f"Error al guardar el archivo Excel: {e}")
