import socket
import pickle



''' Version 1
HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 5000))


while True:
    full_msg = ''
    new_msg = True
    while True:
        msg = s.recv(16) # little more than msg
        if new_msg:
            print(f"new message length: {msg[:HEADERSIZE]}")
            msglen = int(msg[:HEADERSIZE])
            new_msg = False
        full_msg += msg.decode('utf-8')

        if len(full_msg)-HEADERSIZE == msglen:
            print("full msg received")
            print(full_msg[HEADERSIZE:])
            new_msg = True
            full_msg = ''

    print(full_msg)

'''

""" Version 2: Receiving Bytes
HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 5000))


while True:
    full_msg = b''
    new_msg = True
    while True:
        msg = s.recv(16) # little more than msg
        if new_msg:
            print(f"new message length: {msg[:HEADERSIZE]}")
            msglen = int(msg[:HEADERSIZE])
            new_msg = False
        full_msg += msg

        if len(full_msg)-HEADERSIZE == msglen:
            print("full msg received")
            print(full_msg[HEADERSIZE:])
            d = pickle.loads(full_msg[HEADERSIZE:])
            print(d)
            new_msg = True
            full_msg = b''

    print(full_msg)"""

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 5004))




full_msg = b''
new_msg = True
while True:
    msg = s.recv(16) # little more than msg
    if new_msg:
        msglen = int(msg[:HEADERSIZE])
        #print(f"new message length: {msg[:HEADERSIZE]}")
        new_msg = False
    # try:
    #print(msg)
    full_msg += msg
    # except:
    #     pass
    #print(f"Initial message is: {full_msg}")

    #print(len(full_msg)-HEADERSIZE,"***************",len(full_msg),'***********', msglen)
    if len(full_msg)-HEADERSIZE == msglen:
        print("full msg received")
        print(full_msg[HEADERSIZE:].decode('utf-8'))
        new_msg = True
        full_msg = ''
        break

        #print(full_msg)
