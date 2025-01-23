from socket import *

HOST = "192.168.10.21"
PORT = 50000
BUF = 4096
Server_info=(HOST,PORT)

#ソケット作成
client = socket(AF_INET,SOCK_STREAM)
#サーバーと接続
client.connect(Server_info)
#サーバからのメッセージ受信
data = client.recv(BUF)
print(data.decode("UTF-8"))
#コネクションクローズ
client.close()