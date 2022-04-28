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