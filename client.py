import socket
import sys

try:
    #create socket with arguments AF_INET (Address Family Internet) and SOCK_STREAM (TCP)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    print("Socket created")
except socket.error: # generic socket exception/error
    print("Failed to create socket.")
    sys.exit()

client_socket.connect(('172.20.10.2', 8485)) # Macbook IP Address 
connection = client_socket.makefile('wb')

client_socket.connect(('172.20.10.9', 6666)) # Raspberry Pi IP address, arbitrary port that won't be used
message = b"Here is my request!"

try:
	client_socket.sendall(message)
except socket.error:
	print("Failed to send.")
	sys.exit()

# data = client_socket.recv(1000)
# print(data)
client_socket.close()