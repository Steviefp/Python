import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #tcp is SOCK_STREAM, udp is SOCK_DGRAM

server='pythonprogramming.net'

port=80

server_ip=socket.gethostbyname(server)#how u get server ip

request = "GET / HTTP/1.1\nHost: "+server+"\n\n"

s.connect((server,port))
s.send(request.encode())#python 3 and above you got to use encode
result=s.recv(4000)
print(result)
