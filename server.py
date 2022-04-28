import socket
import sys
#import camera 

HOST = '' # 0.0.0.0 accepts all connections 
PORT = 6666 # have to use 'sudo python3 xxx.py' to use port 80

#create socket with arguments AF_INET (Address Family Internet) and SOCK_STREAM (TCP)
try:
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print('Socket created') 
except socket.error: # generic socket exception/error
	print("Failed to create socket.")
	sys.exit()

try:
	server_socket.bind((HOST, PORT)) # binding socket to port  
	print('Socket bind complete')
except socket.error:
	print("Bind failed.")
	sys.exit()

# server listens for request + handles one request at a time and 
# argument 5 says how many requests can wait while server is handling one request
server_socket.listen(5) 
print('Socket now listening')

while True:
	conn, addr = server_socket.accept() # accepts connection request from client
	print('Got connection from', addr) # prints the address of the client
	data = camera()
	conn.sendall(data) # sends byte message to client to view in web browser
	conn.close()
	break

server_socket.close()




# once you type in RPi IP into browser, computer will try to open connection 
# to other machine and send an HTTP request on Port 80
# once connection is made 
