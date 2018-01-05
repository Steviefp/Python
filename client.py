import socket
import threading

host='97.87.232.136'
port=25565

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
userName=input("Enter username: ")
#message=input("What would you like to send, type quit to quit.\n")
clientState=True
def obtainInfo():
	global clientState
	data = s.recv(1024).decode('utf-8')
	print(str(data))
	if "exit" in data:
		clientState=False



def testingboy():
	message=input()
	s.send((userName.encode() + ': '.encode() + message.encode() + "\n".encode()))


while clientState:

	dope = threading.Thread(target=testingboy, args=())
	dope.start()

	obtainInfo()




	#message = input("enter message -> ")

s.close()
