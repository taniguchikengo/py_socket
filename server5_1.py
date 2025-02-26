"""
UDP通信（サーバ）
コンソールアプリ
"""
from socket import *
import datetime

PORT = 50000
BUF = 4096

server = socket(AF_INET,SOCK_DGRAM)
server.bind(("",PORT))
print("待ち受け開始")
c_lis =[]

while True:
    data,client = server.recvfrom(BUF)
    if not (client in c_lis):
        c_lis.append(client)
    if data.decode("UTF-8") == "0":
        c_lis.remove(client)
    else:
        ti = datetime.datetime.now().strftime("%H:%M:%S")
        msg = f"{ti} [{client[0]}] > {data.decode('UTF-8')}"
        print(msg)
    for c in c_lis:
        server.sendto(msg.encode("utf-8"),c)

