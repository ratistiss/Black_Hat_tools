import socket

target_host = "127.0.01"
target_port = 80

#socket object
client = socket.socket(socket.AF_INET, socket_SOCK_DGRAM)

#send data
client.sendto("data",(target_host, target_port))

#receive data
data, addr = client.recvfrom(4096)

#print data
print data