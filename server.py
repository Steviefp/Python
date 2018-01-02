import socket

host=''
port=25565

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))

s.listen(1)
c,addr=s.accept()


print("Connection from: ",str(addr))
while True:
	data=c.recv(1024).decode('utf-8')
	if not data:
		break
	print("from connected user:", str(data))
	data=input("say something back to this pussy\n")
	print("sending:",str(data))
	c.send(data.encode())
c.close()
