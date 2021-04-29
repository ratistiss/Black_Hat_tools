import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_NET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

server.listen(5)

print "[*] Listening on %s:%d" % (bind_ip,bind_port)

#client handling thread
def handle_client(client_socket):
    #printing what client sends
    request = client_socket.recv(1024)

    print "[*] Listening on %s" % request

    #returning a packet
    client_socket.send("your response")

    client_socket.close()


while True:
    client,addr = server.accept()

    print "[*] Accepted connection from:  %s:%d" % (addr[0],addr[1])

    #start thread to handle incoming data
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()

