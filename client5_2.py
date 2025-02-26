"""
UDP通信（クライアント）
デスクトップアプリ
"""

from socket import *
import datetime
import threading
import sys
from tkinter import *
import tkinter.ttk as ttk
PORT = 50000
BUF = 4096
client = socket(AF_INET, SOCK_DGRAM)

def main():
    root = Tk()
    root.title("メッセンジャー：クライアント")
    root.geometry("840x500")
    col = ("time", "ipa", "msg")
    tree1 = ttk.Treeview(root, columns=col, height=17)

    # 列の設定
    tree1.column("#0", width=0, stretch=False)  # この記述がないと列が表示される
    tree1.column("time", width=100)
    tree1.column("ipa", width=200)
    tree1.column("msg", width=500)
    # 見出しの設定
    tree1.heading("#0", text="")
    tree1.heading("time", text="時間")
    tree1.heading("ipa", text="IPアドレス")
    tree1.heading("msg", text="メッセージ")

    # メッセージ送信用ボックス
    lab1 = Label(root,text="接続先サーバ：IPアドレス")
    en1 = Entry(root, width=30)
    en1.insert(0, "192.168.10.21")
    en2 = Entry(root, width=100)
    lab2 = Label(root,text="送信メッセージ記入欄")
    # メッセージ送信ボタン
    bt1 = Button(root, text="接続", width=10, command=lambda: server_connect(en1.get(),tree1))
    bt2 = Button(root,text="送信",width=10,command=lambda :send_msg(en1.get(),en2))

    tree1.place(x=20, y=10)
    lab1.place(x=20,y=378)
    en1.place(x=20, y=400)
    bt1.place(x=250,y=395)
    lab2.place(x=20, y=425)
    en2.place(x=20, y=450)
    bt2.place(x=650, y=445)

#サーバー接続とスレッド作成
def server_connect(host,tree1):
    p = threading.Thread(target=server_h, args=(client,tree1))
    p.setDaemon(True)

def send_msg(host,en):
    msg =en.get()
    client.sendto(msg.encode("UTF-8"), (host, PORT))
    en.delete("0",END)

def server_h(client,tree1):
    n = 0
    while True:
        n += 1
        try:
            data = client.recv(BUF)
            ti = datetime.datetime.now().strftime("%H:%M:%S")
            tree1.insert(parent="", index="end", iid=n, values=(ti, client[0], data.decode('UTF-8')))
            print(data.decode("UTF-8"))
        except:
            sys.exit()
    #client.close()

main()
mainloop()