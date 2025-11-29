
def write_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)

def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()

