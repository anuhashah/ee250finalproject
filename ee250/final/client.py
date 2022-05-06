import socket
import sys
import pickle
from RGBtoHex import hexadecimal
from lcdscreen import LCDcontrol
from mosaic_tiles import createPhotomosaic

try:
    #create socket with arguments AF_INET (Address Family Internet) and SOCK_STREAM (TCP)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    print("Socket created")
except socket.error: # generic socket exception/error
    print("Failed to create socket.")
    sys.exit()

client_socket.connect(('192.168.36.128', 6666)) # <-- VM Address, Macbook IP Address: 172.20.10.2

request = b"PHOTO"

try:
	client_socket.sendall(request)
except socket.error:
	print("Failed to send.")
	sys.exit()

data = pickle.loads(client_socket.recv(4096))
sizeLength_data = client_socket.recv(1).decode()
sizeLength = int(sizeLength_data)
size_data = client_socket.recv(sizeLength).decode()
size = int(size_data)

#receiving the photo
with client_socket, open('image.jpg', 'wb') as file:
        while True:
            recvfile = client_socket.recv(4096)
            if not recvfile: break
            file.write(recvfile)

#image= client_socket.recv(size)
data = data[0]
file.close()
hexa = hexadecimal(data)
print("RGB: ("  + str(data[0]) + ", " + str(data[1]) + ", " + str(data[2]) + ") = Hexadecimal: #" + hexa)
print("turning photo into a photomosaic...")

LCDcontrol(data, hexa)
createPhotomosaic('image.jpg')


client_socket.close()