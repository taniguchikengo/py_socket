"""
UDP通信（サーバ）
デスクトップアプリ
"""
from socket import *
import datetime
from tkinter import *
import tkinter.ttk as ttk
import threading

PORT = 50000
BUF = 4096
n = 0

def main():
    root = Tk()
    root.title("メッセンジャー：サーバ")
    root.geometry("840x500")
    col = ("time", "ipa", "msg")
    tree1=ttk.Treeview(root,columns=col,height=20)

    # 列の設定
    tree1.column("#0", width=0, stretch=False)  # この記述がないと列が表示される
    tree1.column("time", width=100)             #時間
    tree1.column("ipa", width=200)              #IPアドレス
    tree1.column("msg", width=500)              #メッセージ
    # 見出しの設定
    tree1.heading("#0", text="")
    tree1.heading("time", text="時間")
    tree1.heading("ipa", text="IPアドレス")
    tree1.heading("msg", text="メッセージ")
    #サーバー起動ボタン
    bt1 = Button(root,text="起動",command=lambda :socket_start(tree1),width=15)

    tree1.place(x=20,y=10)
    bt1.place(x=700,y=460)

def socket_start(tree1):  # 起動ボタン
    global n
    server = socket(AF_INET, SOCK_DGRAM)
    server.bind(("192.168.10.21", PORT))
    ti = datetime.datetime.now().strftime("%H:%M:%S")
    tree1.insert(parent="", index="end", iid=n, values=(ti, "", "サーバ起動"))
    n += 1
    print("待ち受け開始")

    p = threading.Thread(target=client_h, args=(server, tree1))
    p.start()


def client_h(server,tree1):
    global n
    c_lis = []
    msg=""
    while True:
        n += 1
        data, client = server.recvfrom(BUF)
        if not (client in c_lis):
            c_lis.append(client)
        if data.decode("UTF-8") == "0":
            c_lis.remove(client)
        else:
            ti = datetime.datetime.now().strftime("%H:%M:%S")
            msg = f"{ti} [{client[0]}] > {data.decode('UTF-8')}"
            tree1.insert(parent="", index="end", iid=n, values=(ti, client[0], data.decode('UTF-8')))
            print(msg)
        for c in c_lis:
            server.sendto(msg.encode("utf-8"), c)
main()
mainloop()