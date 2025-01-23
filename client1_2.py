from socket import *
from socket import *
import sys

"""
基本的なソケットプログラム
IPv4
50000番ポートでサーバー接続
双方向(送受信)
"""

PORT = 50000
BUF = 4096

#ソケットの作成
client = socket(AF_INET,SOCK_STREAM)
#サーバー接続
# host = input("接続先サーバ：")
# try:
#     client.connect((host,PORT))
# except:
#     print("接続できません")
#     sys.exit()
client.connect(("192.168.10.21",PORT))
print(("接続先サーバ：192.168.10.21"))
data = client.recv(BUF)
print(data)
#メッセージ送信
flag = 1
while flag:
    msg = input("メッセージ入力：")
    if msg == "0":
        flag = 0
    else:
        client.sendall(msg.encode("utf-8"))


client.close()
