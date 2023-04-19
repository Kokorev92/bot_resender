import http.server
import socketserver
import urllib.parse as urlparse

class Http_request_handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)

        if(self.path == '/'):
            with open('index.html', 'r') as f:
                index = f.read()

            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(str(index).encode('utf8'))
            return

        self.send_error(404, "NOT FOUND")

