from socket import *
import datetime

PORT = 50000
BUF = 4096
server = socket(AF_INET,SOCK_STREAM)

server.bind(("",PORT))

server.listen()
while True:
    client,addr = server.accept()
    msg = str(datetime.datetime.now())
    print(msg,"接続要求あり")
    print(client)

    data = client.recv(BUF)
    print(data.decode("UTF-8"))

    client.sendall(msg.encode("utf-8"))

    client.close()
