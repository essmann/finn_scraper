from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
import threading
import time
import json
import time
from seleniumProject.test import queue
from seleniumProject.test import main
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#this one is gonna

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(self.path)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, World!')

    def do_POST(self):
       # read the content-length header
        content_length = int(self.headers.get("Content-Length"))
        # read that many bytes from the body of the request
        body = self.rfile.read(content_length)

        self.send_response(200)
        self.end_headers()
        # echo the body in the response
        self.wfile.write(body)
        data = body.decode('utf-8')
        data_dict = json.loads(data)
        try:
            message = data_dict["message"]
            print("server message: " + message)
            queue.put(message)
            
           
        except:
            pass
            print("no message found")

# Function to run the server
def run_server():
    host = '10.0.0.7'
    port = 8080
    server_address = (host, port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"Server running on {host}:{port}")
    httpd.serve_forever()


server_thread = threading.Thread(target=run_server)

server_thread.start()

jetpunk_thread = threading.Thread(target=main)

jetpunk_thread.start()





