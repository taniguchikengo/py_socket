"""
基本的なソケットプログラム
IPv4,TCP
50000番ポートで待ち受け
双方向
複数クライアント可（同時処理不可）
クライアント複数メッセージ可能
"""
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
    client.sendall(f"{msg}:接続成功！".encode("utf-8"))
    print(msg,"接続要求あり")
    print(client)

    data = client.recv(BUF)
    print(data.decode("UTF-8"))


