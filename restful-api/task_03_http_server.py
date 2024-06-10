#!/usr/bin/python3
"""This module contians a subclass of BaseHTTPRequestHandler"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import socketserver
import requests


data_set = {"name": "John", "age": 30,
            "city": "New York"}
info_set = {"version": "1.0", "description":
            "A simple API built with http.server"}
json_data = json.dumps(data_set)
json_data_2 = json.dumps(info_set)


class MyHandler(BaseHTTPRequestHandler):
    """Sublass that inherits methods to handle HTTP requests."""
    def do_GET(self):
        """Handles get requests"""
        if self.path == "/data":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(bytes(json_data, "utf-8"))
        elif self.path == "/status":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes("OK", "utf-8"))

        elif self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes("Hello, this is a simple API!", "utf-8"))

        elif self.path == "/info":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(bytes(json_data_2, "utf-8"))

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes("Endpoint not found", "utf-8"))


PORT = 8000


with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
