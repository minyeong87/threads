import socket
import select
import pymysql
from datetime import datetime

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((IP, PORT))

server_socket.listen()

sockets_list = [server_socket]

clients = {}

con = pymysql.connect(host='localhost', user='root', password='0000', db='newschema', charset='utf8')  # 한글처리 (charset = 'utf8')

cur = con.cursor()

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

def receive_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGTH)

        if not len(message_header):
            return False

        message_length = int(message_header.decode("utf-8").strip())
        return {"header": message_length, "data": client_socket.recv(message_length)}



    except:
        return False

n = 1
while True:
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()

            user = receive_message(client_socket)
            if user is False:
                continue

            sockets_list.append(client_socket)
            clients[client_socket] = user
            print(client_address, 'what') #########
            print(f"Accepted new connection from {client_address[0]}:{client_address[1]} username:{user['data'].decode('utf-8')}")
        else:
            message = receive_message(notified_socket)

            if message == False:
                print("Closed connection from {clients[notified_socket]['data'].decode(utf-8')}")
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue

            user = clients[notified_socket]
            username = user['data'].decode('utf-8')
            gotmessage = message['data'].decode('utf-8')
            print(f"Received message from {username}: {gotmessage}")
            print(f"{username} {gotmessage}")
            # dbinput = f"insert into newschema.chatting1(user_id, message) values('{username}', '{gotmessage}')"
            print(n, dt_string)
            dbinput = f"insert into newschema.chatting1(user_id, message, ip_address, port_number, time) values('{username}', '{gotmessage}', '{client_address[0]}', '{client_address[1]}', '{str(dt_string)}')"
            idon = f"select * from newschema.chatting1"
            n += 1
            cur.execute(dbinput)

            avg = cur.fetchall()
            con.commit()

            print(avg)


            # print(notified_socket, 'noti')
            # print(clients, 'cli')

            # for client_socket in clients:
            #     if client_socket != notified_socket:
            #         client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])

    for notified_socket in exception_sockets:
        sockets_list.remove(notified_socket)
        del clients[notified_socket]