import socketserver

class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            self.data = self.request.recv(1024).strip()
            print(("{} wrote:".format(self.client_address[0])))
            print((self.data))

            self.request.sendall(self.data.lower())

if __name__=="__main__":
    host, port = '10.10.21.117', 2500

    server = socketserver.TCPServer((host, port), TCPHandler)
    server.serve_forever()