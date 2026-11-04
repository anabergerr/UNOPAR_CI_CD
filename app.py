"""Aplicacao de exemplo para o pipeline CI/CD (UNOPAR_CI_CD)."""


def soma(a, b):
    """Soma dois numeros. Funcao isolada para testar sem subir o servidor."""
    return a + b


def _handler():
    from http.server import BaseHTTPRequestHandler

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):  # noqa: N802 - nome exigido pelo BaseHTTPRequestHandler
            if self.path == "/health":
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(b'{"status":"ok"}')
            else:
                self.send_response(404)
                self.end_headers()

    return Handler


if __name__ == "__main__":
    from http.server import HTTPServer

    HTTPServer(("", 8000), _handler()).serve_forever()
