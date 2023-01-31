import socket

port = 5555
address = ('10.10.21.117', 5555)
BUFSIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)

while True:
    msg = input("Mossage to send: ")
    s.send(msg.encode())
    r_msg = s.recv(BUFSIZE)
    if not r_msg: break
    print("Received message: %s" %r_msg.decode())