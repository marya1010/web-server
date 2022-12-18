#запустить веб-сервер
from http.server import HTTPServer, CGIHTTPRequestHandler
server_address = ("", 8000) #('Host', Port) Host Пустой - localhost
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
httpd.serve_forever()
