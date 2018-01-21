import random
import socket
import threading
import time
'''random string out of list'''
def make_word():
    char_list='a b c d e f g h i k l m n o p q r s t u v w x y z A B C D E F G H I J K M L M N O P Q R S T U V W X Y Z ! @ # $ % ^'.split()
    random_string_selected_temp=''
    for x in range(5):
        random_string_selected_temp += random.choice(char_list)
    return random_string_selected_temp

def assign_vars():
    random_string_selected_temp=make_word()
    print('Chosen word: ',random_string_selected_temp)
    send_counter=0
    return random_string_selected_temp,send_counter
''' socket startup stuff '''
test=True
random_string_selected,send_counter=assign_vars()
connection_dict = {}
host=''
port=25565
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(2)


print("Server is started\n")



def client_thread(connection,address):
    global random_string_selected,send_counter
    user_name_recv = connection.recv(1024).decode('utf-8')
    '''Gets username'''
    if "USER_NAME$$" in user_name_recv:
        connection_dict[connection] = user_name_recv[11:]

    while True:
        if len(connection_dict) == 2 and send_counter==0:
            for connections in connection_dict:
                connections.send(random_string_selected.encode())
            send_counter=1




        information = connection.recv(1024).decode('utf-8')
        print(address,connection_dict[connection],information)


        if information == random_string_selected:
            print(address, 'Winner')
            for connections in connection_dict:
                connections.send(
                    str(connection_dict[connection]).encode() + ' Winner\nNext round coming in 2 seconds'.encode())
            time.sleep(2)
            random_string_selected,send_counter = assign_vars()


        else:
            connection.send('Wrong'.encode())




while True:
    connection,address=s.accept()

    thread_one=threading.Thread(target=client_thread,args=(connection,address))
    thread_one.start()



s.close()
