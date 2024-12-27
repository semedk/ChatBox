# Only help I got involved TAs and previous assignments when constructing code

import socket
import math

"IP Address"
serverIP = '127.0.0.1' 
"Port Number"
serverPort = 1612

"Establishes we're using network IPv4 and that we're using a TCP socket'"
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
"Binds IP address and port number for our server"
serverSocket.bind((serverIP, serverPort))
"Waiting for a connection to happen"
serverSocket.listen(1)
"Socket for client"
connection, address = serverSocket.accept()
connection.setblocking(True)

while True:
    "Collects information from socket"
    size = int(connection.recv(1024).decode()) # Collects information of the size of the incoming message
    if size == 0:
        break
    List = []
    for _ in range(math.ceil(size / 1024)): # In order to not recv when we don't need to and do so for more than 1024 chars
        message = connection.recv(1024) # Collect the first 1024
        message = message.decode() # Decode it
        List.append(message) # Append information to list
        if not message:
            break
    
    truemessage = ''.join(List) # Overall String from the list we were appending too

    "Prints out information"
    print('Received: ' + str(truemessage))

    "Prompt for a reply"
    reply = input("Response: ")

    "Potential choice to quit server"
    if reply == "/q":
        connection.sendall(str(0).encode()) # Sending 0 to notify /q was used
        break

    "Server sends reply"
    connection.sendall(str(len(reply)).encode())
    connection.sendall(reply.encode())

"Closes Connection"
connection.close()