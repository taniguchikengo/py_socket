"""
基本的なソケットプログラム
IPv4
50000番ポートでサーバー接続
双方向(送受信)
複数回
"""

from socket import *
from socket import *
import sys

PORT = 50000
BUF = 4096

#ソケットの作成
client = socket(AF_INET,SOCK_STREAM)
#サーバー接続
host = input("接続先サーバ：")
try:
    client.connect((host,PORT))
except:
    print("接続できません")
    sys.exit()

#サーバーメッセージ受信
data = client.recv(BUF)
print(data.decode("UTF-8"))
#メッセージ送信
flag = 1
while flag:
    msg = input("メッセージ入力：(0入力で終了)")
    if msg == "0":
        flag = 0
    else:
        client.sendall(msg.encode("utf-8"))


client.close()
