import http_request_handler
import socketserver

with socketserver.ForkingTCPServer(("", 8000), http_request_handler.Http_request_handler) as httpd:
    print("Resender server starting at 8000")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Closing server")
        httpd.socket.close()