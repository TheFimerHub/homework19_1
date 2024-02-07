from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from urllib.parse import urlparse, parse_qs

hostName = "localhost" # Network access address
serverPort = 8080 # Port for network access
htmlFilePath = "index.html"

class MyServer(BaseHTTPRequestHandler):


    def do_GET(self):
        """ Method for processing incoming GET requests """
        query_components = parse_qs(urlparse(self.path).query)
        print(query_components)
        self.send_response(200) # Sending a response status code
        self.send_header("Content-type", "text/html")
        self.end_headers() # Completing response headers

        with open(htmlFilePath, "rb") as file:
            htmlContent = file.read()

        self.wfile.write(htmlContent)

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    # The correct way to stop the server currently using the address and port on the network
    webServer.server_close()
    print("Server stopped.")