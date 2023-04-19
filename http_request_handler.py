import http.server
import socketserver
import urllib.parse as urlparse
from io import BytesIO
import telebot
import json


class Http_request_handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)

        if self.path == '/':
            with open('index.html', 'r') as f:
                index = f.read()

            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(str(index).encode('utf8'))
            return

        self.send_error(404, "NOT FOUND")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        print(body)
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())
