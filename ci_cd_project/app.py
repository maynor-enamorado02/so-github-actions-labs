
import logging
import os
from utils import read_file, write_file

# Configuración básica de logs
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def main():
    logging.info("Aplicación iniciada")
    file_name = "data.txt"

    # Escribe un archivo de texto
    write_file(file_name, "Hola, este es un archivo generado por la app.")
    logging.info(f"Archivo {file_name} creado.")

    # Lee el archivo y lo muestra
    content = read_file(file_name)
    logging.info(f"Contenido leído: {content}")

    print("Proceso completado. Revisa app.log para detalles.")


if __name__ == "__main__":
    main()
