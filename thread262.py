from socket import *
import _thread

BUFFSIZE = 1024
host_addr = '10.10.21.117'
port = 5555


def response(key):
    return '서버 응답 메시지'

def handler(clientsock, addr):
    while True:
        data = clientsock.recv(BUFFSIZE)
        print('got:' + repr(response('')))
        if not data: break
        clientsock.send(response('').encode())
        print('sent:' + repr(response('')))

if __name__=='__main__':
    ADDR = ('10.10.21.117', 5555)
    serversock = socket(AF_INET, SOCK_STREAM)
    serversock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serversock.bind(ADDR)
    serversock.listen(100)

    while True:
        print('waiting for connection...')
        clientsock, addr = serversock.accept()
        print('...connected from:', addr)

        _thread.start_new_thread(handler, (clientsock, addr))