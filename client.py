import socket

host='127.0.0.1'
port=80

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

message=input("What would you like to send, type quit to quit.\n")

while message != "quit":
	s.send(message.encode())
	data=s.recv(1024).decode('utf-8')
	print("Recieved from server:",str(data))
	message=input("What would you like to send, type quit to quit.\n")

s.close()
