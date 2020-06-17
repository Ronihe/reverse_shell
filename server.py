import socket
import sys


# create a socket to connect two computers
def create_socket():
    try:
        global host
        global port
        global s

        host = ""
        port = 8888
        s = socket.socket()
    except socket.error as error_msg:
        print("socket creation error:" + str(error_msg))
    
