import socket

port = 5555
address = ('10.10.21.117', 2500)
BUFSIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)

while True:
    msg = input("Message to send: ")
    s.send(msg.encode())
