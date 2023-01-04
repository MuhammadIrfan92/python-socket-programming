import socket
from time import sleep
import pickle

''' Version 1: sending text msgs
HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 5000))
s.listen(5) # queue of 5 connections

while True:
    client_socket, address = s.accept()
    print(f"Connection from {address} has been established!")

    msg = "Welcome to the server!"
    msg = f'{len(msg):<{HEADERSIZE}}'+msg  # left aligned text.

    client_socket.send(msg.encode('utf-8'))
    #client_socket.close()

    while True:
        time.sleep(3)
        msg = f"the time is! {time.time()}"
        msg = f'{len(msg):<{HEADERSIZE}}' + msg  # left aligned text.
        client_socket.send(msg.encode('utf-8'))

'''

""" Version 2: Sending objects (as bytes)
HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 5000))
s.listen(5) # queue of 5 connections

while True:
    client_socket, address = s.accept()
    print(f"Connection from {address} has been established!")

    d = {
        1: "Hey",
        2: "There"
    }
    msg = pickle.dumps(d)

    msg = bytes(f'{len(msg):<{HEADERSIZE}}', 'utf-8') + msg # left aligned text.

    client_socket.send(msg)
    #client_socket.close()"""


def readfile(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = file.read()
    return data


HEADER_SIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 5004))
s.listen(5) # queue of 5 connections

while True:
    client_socket, address = s.accept()
    print(f"Connection from {address} has been established!")
    data = readfile('file1.txt')

    msg = b"Welcome to the server!"
    data = readfile('file1.txt')
    data = data.encode('utf-8')

    msg = f'{len(data):<{HEADER_SIZE}}'.encode('utf-8')+data  # left aligned text.
    #print(f'{len(msg):<{HEADER_SIZE}}'+msg)
    client_socket.send(msg)
    client_socket.close()

    print("DONE")
    # while True:
    #     #sleep(3)
    #     msg = i.strip()
    #     msg = f"{len(msg):<{HEADER_SIZE}}" + msg
    #     print(msg)
    #     client_socket.send(bytes(msg, "utf-8"))

    #client_socket.close()

    # while True:
    #     time.sleep(3)
    #     msg = f"the time is! {time.time()}"
    #     msg = f'{len(msg):<{HEADER_SIZE}}' + msg  # left aligned text.
    #     client_socket.send(msg.encode('utf-8'))
