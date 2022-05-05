import socket
import sys
import os
import pickle
#from xmlrpc.server import _DispatchArity2
from camera import capture
import subprocess
#from imviewer import preview
from dominantcolors import get_image_dominant_colors

HOST = '' # 0.0.0.0 accepts all connections 
PORT = 6666 # unused port

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
	request = conn.recv(1000)
	if request == b"PHOTO":
		print('Got connection from', addr) # prints the address of the client
		capture()
		openimg = subprocess.Popen(["open", "-W", "image.jpg"])
		#preview()
		data = pickle.dumps(get_image_dominant_colors(image_path='image.jpg',num_colors=1))
		conn.sendall(data) # sends byte message to client
		picStats = os.stat('image.jpg')
		#get the picSize and picLength
		picSize = picStats.st_size
		print(picSize)
		print("ok")
		picLength = len(str(picSize))
		print(picLength)

		conn.sendall(str(picLength).encode())
		#send the pic size
		conn.sendall(str(picSize).encode())

		with open('image.jpg', 'rb') as file:
			sendfile = file.read()
		conn.sendall(sendfile)
		#myfile = open('image.jpg', 'rb')

		#data2 = myfile.read()
		#data2 = pickle.dumps('image.jpg', 'rb')

		#all_data = [data, data2]
		#conn.sendall(data2) 
		openimg.terminate()
		openimg.kill()
		conn.close()
	else:
		conn.close()


server_socket.close()



