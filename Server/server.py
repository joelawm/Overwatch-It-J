"""
Server.py
By: Joe Meyer

Function: This establishes and manages connectiosn amongst the clients.
It then will send out instructions based on a GUI client.
"""
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    clientsocket.send(bytes("Welcome to the server!","utf-8"))