"""
基本的なソケットプログラム
IPv4,TCP
50000番ポートで待ち受け
単方向(送信)
"""

import  socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("",50000))
server.listen()
client,addr = server.accept()
# print(addr)
# print(client)
# a = client.family
# b=client.type
# c=client.proto
# d= client.getsockname()
# e=client.fileno()
# f=client.getpeername()
# print(f"アドレスファミリ={a}")
# print(f"ポート={b}")
# print(f"ソケットタイプ={c}")
# print(f"サーバアドレス={d}")
# print(f"クライアントアドレス={f}")
# print(f"ファイルナンバー={e}")
client.sendall("投げやったでござる".encode("UTF-8"))
client.close()
server.close()
