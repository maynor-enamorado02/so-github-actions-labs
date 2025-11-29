
import os
import time
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

EXCHANGE_DIR = "/app/exchange"

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            payload = {
                "message": "Hola desde el contenedor",
                "container_hostname": os.uname().nodename,
                "timestamp": time.time()
            }
            os.makedirs(EXCHANGE_DIR, exist_ok=True)
            with open(os.path.join(EXCHANGE_DIR, "from-container.json"), "w") as f:
                json.dump(payload, f)

            try:
                with open("/proc/meminfo") as f:
                    meminfo = "".join(f.readlines()[:5])
                with open("/proc/cpuinfo") as f:
                    cpuinfo = "".join(f.readlines()[:10])
            except Exception as e:
                meminfo = f"Error leyendo /proc/meminfo: {e}"
                cpuinfo = f"Error leyendo /proc/cpuinfo: {e}"

            resp = {
                "status": "ok",
                "hostname": os.uname().nodename,
                "meminfo_head": meminfo,
                "cpuinfo_head": cpuinfo,
                "wrote_to": os.path.join(EXCHANGE_DIR, "from-container.json")
            }
            body = json.dumps(resp).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        else:
            self.send_response(404)
            self.end_headers()

def main():
    server = HTTPServer(("0.0.0.0", 8080), Handler)
    print("Servidor HTTP iniciado en :8080")
    server.serve_forever()

if __name__ == "__main__":
    main()
