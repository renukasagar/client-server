import socket
import sys

s = socket.socket()
host = socket.gethostname()
print(" server will start on host : ", host)
port = 8080
s.bind((host,port))
name = input(str("Name:"))
print("")
print( name,"is waiting for chatting")
print("")
s.listen(1)
conn, addr = s.accept()
print("connected")
print("")
s_name = conn.recv(1024)
s_name = s_name.decode()
print("*****",s_name, "is online *****")
conn.send(name.encode())

while 1:
    message = input(str("You: "))
    conn.send(message.encode())
    print("√√")
    print("")
    message = conn.recv(1024)
    message = message.decode()
    print(s_name, ":" ,message)
    print("")
