# main.py
from dbc_to_dataframe import dbc_to_dataframe
from save_to_excel import save_to_excel

def main():
    # Ruta del archivo .dbc
    dbc_file = 'your_dictionary.dbc' 

    # Verifica que el archivo .dbc exista
    try:
        with open(dbc_file, 'r') as f:
            pass
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {dbc_file}")
        return

    # Ruta del archivo Excel de salida
    output_file = 'outputfile_name.xlsx'    # Nombre del archivo Excel de salida

    # Crear el DataFrame a partir del archivo .dbc
    print("Leyendo el archivo .dbc...")
    df = dbc_to_dataframe(dbc_file)
    print("DataFrame creado con éxito.")

    # Verifica si el DataFrame no está vacío
    if df.empty:
        print("Error: El DataFrame está vacío. Verifica el archivo .dbc.")
        return

    # Guardar el DataFrame en un archivo Excel
    print(f"Guardando el archivo Excel como {output_file}...")
    save_to_excel(df, output_file)
    print(f"El archivo Excel se ha guardado como {output_file}")

if __name__ == '__main__':
    main()
