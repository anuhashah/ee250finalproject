import socket
import sys
import pickle
from RGBtoHex import hexadecimal
from lcdscreen import color

try:
    #create socket with arguments AF_INET (Address Family Internet) and SOCK_STREAM (TCP)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    print("Socket created")
except socket.error: # generic socket exception/error
    print("Failed to create socket.")
    sys.exit()

client_socket.connect(('172.20.10.2', 6666)) # Macbook IP Address 

request = b"PHOTO"

try:
	client_socket.sendall(request)
except socket.error:
	print("Failed to send.")
	sys.exit()

data = pickle.loads(client_socket.recv(4096))
data = data[0]
hexa = hexadecimal(data)
print(data + " = " + hexa)

color()


client_socket.close()