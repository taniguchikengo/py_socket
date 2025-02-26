"""
基本的なソケットプログラム
IPv6
50000番ポートでサーバー接続
単方向(受信)
"""

from socket import *

HOST = "localhost"
#HOST = "::1"     #IPv6ループバック
PORT = 50000
BUF = 4096
Server_info=(HOST,PORT)

#ソケット作成
client = socket(AF_INET6,SOCK_STREAM)       #AF_INET6:IPv6,SOCK_STREAM:TCP
#サーバー接続
client.connect(Server_info)
#サーバからのメッセージ受信
data = client.recv(BUF)
print(data.decode("UTF-8"))
#コネクションクローズ
client.close()