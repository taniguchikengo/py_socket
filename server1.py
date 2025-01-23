from socket import *
import datetime

PORT = 50000
server = socket(AF_INET,SOCK_STREAM)

server.bind(("",PORT))

server.listen()
while True:
    client,addr = server.accept()
    msg = str(datetime.datetime.now())
    client.sendall(msg.encode("UTF-8"))
    print(msg,"接続要求あり")
    client.close()
    server.close()