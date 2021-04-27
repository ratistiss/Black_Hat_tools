import socket

target_host = "www.google.com"
target_port = 80

#socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect to the client
client.connect((target_host,target_port))
