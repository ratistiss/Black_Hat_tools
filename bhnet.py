import threading
import paramiko
import subprocess

def ssh_command(ip, user, passwd, command):
    return