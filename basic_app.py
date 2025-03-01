import http.server
import socketserver

PORT = 8080

class SimpleHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello, Containerized World!")

with socketserver.TCPServer(("", PORT), SimpleHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
