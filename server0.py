import  socket
from encodings.utf_8_sig import encode

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("",50000))
server.listen()
client,addr = server.accept()
print(client,addr)
a = client.family
b=client.type
c=client.proto
d= client.getsockname()
e=client.fileno()
print(a,b,c,d,e)
client.sendall("投げやったでござる".encode("UTF-8"))
client.close()
server.close()
