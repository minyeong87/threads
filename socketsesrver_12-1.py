import socketserver

class TCPHandler(socketserver.BaseRequestHandler):
    def setup(self):
        print('연결되었습니다.')

if __name__=="__main__":
    host, port = '10.10.21.117', 2500

    server = socketserver.TCPServer((host, port), TCPHandler)
    server.serve_forever()