
import socket


HEADER_SIZE = 10

# creating socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connecting to the server
s.connect((socket.gethostname(), 5050))

# dummy byte string for buffering the response
full_msg = b''
# Boolean for marking if there's any new message left to receive
new_msg = True

while True:
    # receiving header plus 6 bytes
    msg = s.recv(16)

    # checking if there's new message to receive
    if new_msg:
        # checking the length of the message
        msglen = int(msg[:HEADER_SIZE])
        new_msg = False

    # buffering msg
    full_msg += msg

    # checking the length of the message received with the length that was specified in the header
    if len(full_msg)-HEADER_SIZE == msglen:
        print('Full message received: ')
        # printing out the whole message except the header bytes
        print(full_msg[HEADER_SIZE:].decode("utf-8"))
        break

