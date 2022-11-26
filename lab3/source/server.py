#!/usr/bin/env python3
import http.server
import socketserver
import os
import re
import json
import io
from urllib.parse import urlparse, unquote_plus
from datetime import datetime
#print('source code for "http.server":', http.server.__file__)

class web_server(http.server.SimpleHTTPRequestHandler):
    
    def do_GET(self):

   
        
            
            self.protocol_version = 'HTTP/1.1'
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=UTF-8")
            self.end_headers()
            if self.path == '/':
                self.wfile.write(b"Hello World!\n")


            elif "?" in self.path:
                self.protocol_version = 'HTTP/1.1'
                self.send_response(200)
                self.send_header("Content-type", "text/html; charset=UTF-8")
                self.end_headers()
                parts = urlparse('http://localhost:4080'+self.path)
                qs = parts.query
                pairs = [p.split("=", 1) for p in qs.split("&")]
                decoded = [(unquote_plus(k), unquote_plus(v)) for (k, v) in pairs]
                for i in decoded:
                    if i[0] == "str":
                        lower = len(re.findall("[a-z]",i[1]))
                        upper= len(re.findall("[A-Z]",i[1]))
                        digits= len(re.findall("[0-9]",i[1]))
                        allNormal=lower+upper+digits
                        other = len(i[1])-allNormal
                        saveText = {"lowercase":lower, "uppercase":upper, "digits":digits,"special": other}
                        self.wfile.write(str.encode(json.dumps(saveText)))

            else:
                super().do_GET()
    
# --- main ---

PORT = 4080

print(f'Starting: http://localhost:{PORT}')

tcp_server = socketserver.TCPServer(("",PORT), web_server)
tcp_server.serve_forever()
