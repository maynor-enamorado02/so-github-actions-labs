
import logging
import os
from datetime import datetime

# Configurar logging
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO').upper()
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL, logging.INFO),
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
)
logger = logging.getLogger('app')


def read_file(path: str) -> str:
    """Lee el contenido de un archivo y retorna su texto."""
    logger.debug(f"Intentando leer archivo: {path}")
    if not os.path.exists(path):
        logger.error("El archivo no existe: %s", path)
        raise FileNotFoundError(path)
    with open(path, 'r', encoding='utf-8') as f:
        data = f.read()
    logger.info("Archivo leído correctamente: %s (%d bytes)", path, len(data))
    return data


def write_log_file(dir_path: str, message: str) -> str:
    """Escribe un archivo con un log y devuelve la ruta generada."""
    os.makedirs(dir_path, exist_ok=True)
    filename = f"log_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.txt"
    full_path = os.path.join(dir_path, filename)
    with open(full_path, 'w', encoding='utf-8') as f:
        # ---> Aquí estaba el error: asegúrate de escribir una cadena válida
        f.write(message + "\n")
    logger.info("Log escrito en: %s", full_path)
    return full_path


def add(a: int, b: int) -> int:
    """Suma dos números (ejemplo para pruebas unitarias)."""
    logger.debug("Sumando %s + %s", a, b)
    return a + b


if __name__ == '__main__':
    # Interacción simple con el sistema de archivos
    demo_dir = os.getenv('APP_DATA_DIR', 'data')
    msg = os.getenv('APP_MESSAGE', 'Hola CI/CD multiplataforma!')
    path = write_log_file(demo_dir, msg)
    print(f"Archivo de log creado en: {path}")
