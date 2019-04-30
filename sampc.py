import socket
import sys

s = socket.socket()
host = input(str("Please enter the hostname of the server : "))
port = 8080
s.connect((host,port))
name = input(str("name: "))
print(" Connected to chat server")

s.send(name.encode())
s_name = s.recv(1024)
s_name = s_name.decode()
print("")
print("*****",s_name, " is online *****")

while 1:
    message = s.recv(1024)
    message = message.decode()
    print(s_name,":" ,message)
    print("")
    message = input(str("You: "))
    message = message.encode()
    s.send(message)
    print("√√")
    print("")
