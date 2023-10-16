import socket
import time
import threading
from tkinter import *

root = Tk()
root.geometry("300x600")  #bg size
root.config(bg = "white")  #bg color

#starting chatting function
def func():
    t = threading.Thread(target=recv)
    t.start()

#RECEIVE FUNCTION
def recv():
    listensocket = socket.socket()
    port = 3050   #this is receiving port number, shoud be same as sending port number of the other code
    maxconnection = 99
    ip = socket.gethostname()
    print(ip)

    listensocket.bind(('', port))
    listensocket.listen(maxconnection)
    (clientsocket, address) = listensocket.accept()

    while True:
        sendermessage=clientsocket.recv(1024).decode()
        if not sendermessage=="":
            time.sleep(5)
            lstbx.insert(0,"client: "+sendermessage)

#SEND PART
xr=0

def sendmsg():
    global xr   #called global variable s
    if xr==0:
        s=socket.socket()
        hostname="computer name" #PUT COMPUTER NAME
        port = 4050
        s.connect((hostname, port))
        msg = messagebox.get()
        lstbx.insert(0, "You: "+msg)
        s.send(msg.encode())
        xr =xr+1

    else:
        msg = messagebox.get()
        lstbx.insert(0, "You: "+msg)
        xr.send(msg.encode())

def threadsendmsg():
    th=threading.Thread(target=sendmsg)
    th.start()


startchatimage = PhotoImage(file='start.png')

buttons = Button(root, text = "Start Chat", command=func, borderwidth=0, height=3, width = 10 )
buttons.place(x=90, y=10)

message = StringVar()
messagebox = Entry(root, textvariable=message, font=('calibre', 10, 'normal'), border=2, width=32)
messagebox.place(x=10, y=444)

sendmessageimg=PhotoImage(file='send.png')

sendmessagebutton=Button(root, text = "Send", command=threadsendmsg, borderwidth=0, height = 5, width = 10)
sendmessagebutton.place(x=260, y=440)

lstbx=Listbox(root, height=20, width=43)
lstbx.place(x=15, y=80)

root.mainloop()
