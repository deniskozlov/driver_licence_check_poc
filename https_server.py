import http.server
import ssl

server_address = ('0.0.0.0', 8443)  # Using port 8443 for HTTPS
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)

# Create SSL context
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')

# Wrap the socket with SSL
httpd.socket = ssl_context.wrap_socket(httpd.socket, server_side=True)

print(f"Serving HTTPS on {server_address[0]} port {server_address[1]} (https://0.0.0.0:8443/) ...")
httpd.serve_forever() 