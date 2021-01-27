import http.server

SERVER_ADDRESS = ('', 7999)

http = http.server.HTTPServer(SERVER_ADDRESS, http.server.CGIHTTPRequestHandler)
http.serve_forever()