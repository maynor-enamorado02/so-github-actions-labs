
from pathlib import Path

def write_file(filename, content):
    p = Path(filename)
    p.write_text(content, encoding='utf-8')


def read_file(filename):
    p = Path(filename)
    return p.read_text(encoding='utf-8')
