from flask import Flask, jsonify
import socket
import time
import os

app = Flask(__name__)

@app.route('/')
def hello():
    hostname = socket.gethostname()
    return jsonify({
        'message': 'Hola desde el contenedor Docker!',
        'hostname': hostname,
        'timestamp': time.time(),
        'environment': dict(os.environ)
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'timestamp': time.time()})

@app.route('/info')
def info():
    return jsonify({
        'container_id': socket.gethostname(),
        'python_version': os.environ.get('PYTHON_VERSION', 'N/A')
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
