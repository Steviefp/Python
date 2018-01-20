import socket
import threading

'''socket information'''
host='97.87.232.136'
port=25565

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
'''socket information'''

def obtain_string():

    information=s.recv(1024).decode('utf-8')
    print(str(information))



def get_input():
    message=input()
    s.send(message.encode())


while True:
    thread_one=threading.Thread(target=get_input,args=())
    thread_one.start()
    obtain_string()


s.close()

