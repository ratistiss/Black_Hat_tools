import sys
import socket
import threading

def server_loop(local_host, local_port, remote_host, remote_port,receive_first):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((local_host,local_port))
    except:
        print("Failed to listen")
        sys.exit(0)