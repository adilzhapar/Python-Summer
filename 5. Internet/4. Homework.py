import http.server

SERVER_ADDRESS = ('', 12113)
http = http.server.HTTPServer(SERVER_ADDRESS, http.server.CGIHTTPRequestHandler)
http.serve_forever()