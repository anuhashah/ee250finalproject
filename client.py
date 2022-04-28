import socket
import sys

try:
    #create socket with arguments AF_INET (Address Family Internet) and SOCK_STREAM (TCP)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    print("Socket created")
except socket.error: # generic socket exception/error
    print("Failed to create socket.")
    sys.exit()

client_socket.connect(('172.20.10.2', 6666)) # Macbook IP Address 

request = b"Take Photo"

try:
	client_socket.sendall(request)
except socket.error:
	print("Failed to send.")
	sys.exit()

data = client_socket.recv(4096)
print(data)
client_socket.close()