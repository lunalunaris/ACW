#!/usr/bin/env python3
import http.server
import socketserver
import os
import urlparse
from datetime import datetime
#print('source code for "http.server":', http.server.__file__)

class web_server(http.server.SimpleHTTPRequestHandler):
    
    def do_GET(self):

    
        if self.path == '/':
            
            self.protocol_version = 'HTTP/1.1'
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=UTF-8")
            self.end_headers()
            if params==None:
                self.wfile.write(b"Hello World!<br>\n")


        elif "?" in self.path:
            self.protocol_version = 'HTTP/1.1'
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=UTF-8")
            self.end_headers()
            pathTemp, tmp = self.path.split('?', 1)
            now = datetime.now()
            cur_time = now.strftime("%H:%M:%S")
            self.wfile.write(str.encode(""+cur_time+"\n"))
            self.wfile.write(str.encode(tmp))
        else:
            super().do_GET()
    
# --- main ---

PORT = 4080

print(f'Starting: http://localhost:{PORT}')

tcp_server = socketserver.TCPServer(("",PORT), web_server)
tcp_server.serve_forever()
