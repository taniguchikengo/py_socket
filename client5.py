"""
UDP通信（クライアント）
コンソールアプリ
"""
from socket import *
import datetime
import threading
import sys

PORT = 50000
BUF = 4096

def server_h(client):
    while True:
        try:
            data = client.recv(BUF)
            print(data.decode("UTF-8"))
        except:
            sys.exit()
    client.close()

client = socket(AF_INET,SOCK_DGRAM)
host = input("接続先サーバ：")
if host == "":
    host = "localhost"
p = threading.Thread(target= server_h,args=(client,))
p.setDaemon(True)

while True:
    msg = input("")
    client.sendto(msg.encode("UTF-8"),(host,PORT))
    if msg == "0":
        break
    if not p.is_alive():
        p.start()
client.close()