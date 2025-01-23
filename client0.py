import socket
"""
基本的なソケットプログラム
IPv4
50000番ポートでサーバー接続
単方向(受信)
"""

HOST = "localhost"
#HOST = "127.0.0.1"     #IPv4ループバック
PORT = 50000
BUF = 4096

#ソケット作成
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)       #第1引数　AF_INET:IPv4,AF_INET6:IPv6,AF_UNIX:ローカル通信
                                                                #第2引数　SOCK_STREAM:TCP,SOCK_DGRAM:UDP
                                                                #第3引数　プロトコル番号(省略可)
                                                                #第4引数　ファイル記述指定(省略可)
#サーバーと接続
client.connect((HOST,PORT))
#サーバからのメッセージ受信
data = client.recv(BUF)
print(data.decode("UTF-8"))
#コネクションクローズ
#client.close()
