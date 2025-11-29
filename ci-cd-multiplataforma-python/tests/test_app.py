
import os
import tempfile
from app.main import add, write_log_file, read_file


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_write_and_read_file(tmp_path):
    # Escribir log
    p = write_log_file(tmp_path.as_posix(), 'mensaje de prueba')
    # Leer log
    contenido = read_file(p)
    assert 'mensaje de prueba' in contenido
    # Validar que el archivo existe
    assert os.path.exists(p)
