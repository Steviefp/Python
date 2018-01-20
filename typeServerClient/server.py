import random
import socket
import threading

'''random string out of list'''
string_list=['josh','nill','steviefp']
random_string_selected=random.choice(string_list)
print('Chosen word: ',random_string_selected)
''' socket startup stuff '''
host=''
port=25565
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(2)

connection_list=[]
print("Server is started\n")



def client_thread(connection,address):
    while True:
        information=connection.recv(1024).decode('utf-8')
        print(address,information)

        if information == random_string_selected:
            print(address,'Winner')
            for connections in connection_list:
                connections.send(str(address).encode()+'Winner'.encode())
        else:
            connection.send(str(address).encode()+ 'Wrong'.encode())



while True:
    connection,address=s.accept()
    connection_list.append(connection)
    connection.send(random_string_selected.encode())
    thread_one=threading.Thread(target=client_thread,args=(connection,address))
    thread_one.start()


s.close()
