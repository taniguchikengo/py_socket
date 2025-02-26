from socket import *
import sys

"""
基本的なソケットプログラム
IPv4
50000番ポートでサーバー接続
双方向(送受信)
一回だけ
"""

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
print("サーバーからのメッセージ：")
print(data.decode("UTF-8"))
#メッセージ送信
msg = input("メッセージ入力：")
client.sendall(msg.encode("utf-8"))


client.close()