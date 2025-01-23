from socket import *
import datetime
import threading

PORT = 50000
BUF = 4096

def client_h(client,cliento_no,msg):
    data = client.recv(BUF)
    print(f"{cliento_no}:{data.decode('utf-8')}")
    client.sendall(msg.encode("UTF-8"))
    client.close()

server = socket(AF_INET,SOCK_STREAM)
server.bind(("",PORT))
server.listen()
client_no = 0

while True:
    client,addr = server.accept()
    client_no += 1
    msg = str(datetime.datetime.now())
    print(f"{msg}:接続要求あり :{client_no}")
    print(client)

    p = threading.Thread(target= client_h,args=(client,client_no,msg))
    p.start()
