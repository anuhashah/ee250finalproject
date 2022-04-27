### Interfacing With the Raspberry Pi
## MODULE 2 
# Peer-graded Assignment: Write a simple web server on your Raspberry Pi
	# Use the socket to write a simple web server running on your Raspberry Pi. 
	# When your server receives a request it should print “Got a request!” 
	# to the screen of the Raspberry Pi. Turn in your code and turn in a screen 
	# shot of your Raspberry Pi’s screen with “Got a request!” printed in order 
	# to demonstrate that it worked. 

	# In order to get the screen shot, you will need to set up your Raspberry Pi, 
	# run the server, and type the IP address of your Raspberry Pi into the address 
	# line of a web browser running on a desktop or a laptop. 

# YOU DON"T NEED CLIENT SCRIPT
# once you type in RPi IP into browser, computer will try to open connection 
# to other machine and send an HTTP request on Port 80

import socket
import sys

try:
	#create socket with arguments AF_INET (Address Family Internet) and SOCK_STREAM (TCP)
	ms = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
except socket.error: # generic socket exception/error
	print("Failed to create socket.")
	sys.exit()

ms.connect(('10.25.181.189', 6666)) # USC Guest Wireless Mac IP Address = 10.25.181.189, arbitrary port that won't be used
message = b"Here is my request!"

try:
	ms.sendall(message)
except socket.error:
	print("Failed to send.")
	sys.exit()

# data = ms.recv(1000)
# print(data)
ms.close()