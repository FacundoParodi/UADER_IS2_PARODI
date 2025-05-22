# ------------------------------------------
# Descripción: Recupera el valor de una clave desde un archivo JSON.
# Permite indicar el nombre del archivo y la clave a buscar.
# Si no se especifica clave, se asume 'token1' por defecto.
# ------------------------------------------

import json
import sys


def obtener_valor(archivo_json, clave="token1"):
    try:
        # Abrir y leer el contenido del archivo JSON
        with open(archivo_json, 'r') as archivo:
            contenido = archivo.read()
        datos = json.loads(contenido)

        # Buscar la clave en el diccionario
        if clave in datos:
            print(f"Valor de '{clave}': {datos[clave]}")
        else:
            print(f"Clave '{clave}' no encontrada en el archivo.")
    except FileNotFoundError:
        print(f"Archivo '{archivo_json}' no encontrado.")
    except json.JSONDecodeError:
        print("El archivo no contiene un JSON válido.")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    # Verifica los argumentos y usa 'token1' como valor por defecto si no se indica
    if len(sys.argv) < 2:
        print("Uso: python getJason.py archivo.json [clave]")
    else:
        archivo = sys.argv[1]
        clave = sys.argv[2] if len(sys.argv) >= 3 else "token1"
        obtener_valor(archivo, clave)
