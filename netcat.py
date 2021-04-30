import sys
import socket
import getopt
import threading
import subprocess

#global variables
listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0

def usage():
    print "BHP Net Tool"
    print 
    print "Usage: bhpnet.py -t target_host -p port"
    print "l --listen     - listen on [host]:[port] for incoming connections"
    print "-e --executive= file_to_run    -execute the given file upon - receiving a connection"
    print "-c --command     - initialize a command shell"

