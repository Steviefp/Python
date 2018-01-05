import socket
import threading

host=''
port=25565

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))

s.listen(2)


print("Server started!\n")
connectionlist=[]
serverState=True
def clientThread(c,addr):
    global serverState
    while serverState:
        data = c.recv(1024).decode('utf-8')
        print(addr,data)
        if "exit" in data:
            serverState = False

        for i in connectionlist:
            if i != connectionlist:
                i.send(data.encode())
       # c.send(data.encode())
    c.close()




while serverState:
    c, addr = s.accept()
    connectionlist.append(c)
    t1=threading.Thread(target=clientThread, args=(c,addr))
    t1.start()
    print(t1)




c.close()
