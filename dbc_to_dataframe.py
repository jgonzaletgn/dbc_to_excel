# dbc_to_dataframe.py
import cantools
import pandas as pd

def dbc_to_dataframe(dbc_file):
    """
    Lee un archivo .dbc y extrae las señales en un DataFrame.
    """
    # Cargar el archivo DBC
    db = cantools.database.load_file(dbc_file)

    # Crear una lista para almacenar las señales
    signal_data = []

    # Iterar sobre los mensajes en la base de datos
    for message in db.messages:
        for signal in message.signals:
            # Almacenar la información relevante de cada señal, incluyendo el ID del mensaje
            signal_data.append({
                'Message ID': hex(message.frame_id),
                'Message': message.name,
                'Signal': signal.name,
                'Start Bit': signal.start,
                'Signal Length': signal.length,
                'Byte Order': signal.byte_order,
                'Scale': signal.scale,
                'Offset': signal.offset,
                'Min': signal.minimum,
                'Max': signal.maximum,
                'Unit': signal.unit,
            })

    # Convertir la lista de señales a un DataFrame de pandas
    df = pd.DataFrame(signal_data)
    return df
