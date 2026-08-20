import socket
def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind(("localhost", 5000))
    s.listen(1)

    print("Waiting for client...")

    conn, addr = s.accept()
    print("Connected from:", addr)

    receive_msg(conn)
    send_msg(conn)

    conn.close()
    s.close()


def receive_msg(conn):
    msg = conn.recv(1024).decode()
    print("Client:", msg)


def send_msg(conn):
    reply = input("Enter message for client: ")
    conn.send(reply.encode())


start_server()

import socket

def start_client():
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    c.connect(("localhost", 5000))

    send_msg(c)
    receive_msg(c)

    c.close()
    

def send_msg(c):
    msg = input("Enter message for server: ")
    c.send(msg.encode())


def receive_msg(c):
    reply = c.recv(1024).decode()
    print("Server:", reply)


start_client()