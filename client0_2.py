"""
基本的なソケットプログラム
IPv4
50000番ポートでサーバー接続
単方向(受信)
"""
from socket import *

HOST = "192.168.10.21"
PORT = 50000
BUF = 4096
ServerInfo=(HOST,PORT)      #タプルを変数に格納

#ソケット作成
client = socket(AF_INET,SOCK_STREAM)
#サーバーと接続
client.connect(ServerInfo)
#サーバからのメッセージ受信
data = client.recv(BUF)
print(data.decode("UTF-8"))
