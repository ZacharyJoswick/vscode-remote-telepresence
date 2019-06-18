#!/usr/bin/env python3

# Taken from the telepresence "Rapid development with Kubernetes" page
# https://www.telepresence.io/tutorials/kubernetes-rapid

from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Hello, world!\n")
        return

httpd = HTTPServer(('', 8080), RequestHandler)
httpd.serve_forever()