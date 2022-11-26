#!/usr/bin/env python3
import http.server
import socketserver
import os
from urllib.parse import urlparse, unquote_plus
from datetime import datetime
#print('source code for "http.server":', http.server.__file__)

class web_server(http.server.SimpleHTTPRequestHandler):
    
    def do_GET(self):

   
        if self.path == '/':
            
            self.protocol_version = 'HTTP/1.1'
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=UTF-8")
            self.end_headers()
            self.wfile.write(b"Hello World!<br>\n")


        elif "?" in self.path:
            self.protocol_version = 'HTTP/1.1'
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=UTF-8")
            self.end_headers()
            parts = urlparse('http://localhost:4080'+self.path)
            qs = parts.query
            pairs = [p.split("=", 1) for p in qs.split("&")]
            decoded = [(unquote_plus(k), unquote_plus(v)) for (k, v) in pairs]
            self.wfile.write(str.encode(decoded[0][1]))

        else:
            super().do_GET()
    
# --- main ---

PORT = 4080

print(f'Starting: http://localhost:{PORT}')

tcp_server = socketserver.TCPServer(("",PORT), web_server)
tcp_server.serve_forever()
