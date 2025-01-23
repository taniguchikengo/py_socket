from socket import *
import datetime
import threading

PORT = 50000
BUF = 4096

def client_h(client,cliento_no,msg):
    flag = 1
    while flag:
        data = client.recv(BUF)
        if not data :
            flag = 0
        else:
            print(f"{cliento_no} : {data.decode('utf-8')}")
    print(f"client : {cliento_no} : 接続解除")
    client.close()


server = socket(AF_INET,SOCK_STREAM)
server.bind(("",PORT))
server.listen()
print("サーバ起動：待ち受け中")

while True:
    client,addr = server.accept()
    client_no = addr[0]
    msg = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
    print(f"{msg} : client接続 : {client_no}")
    msg += "---Connecting---"
    client.sendall(msg.encode("utf-8"))
    p = threading.Thread(target= client_h,args=(client,client_no,msg))
    p.start()


