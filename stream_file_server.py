import socket

def readfile(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = file.read()
    return data


HEADER_SIZE = 10

# Creating the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding the socket to lcoal host
s.bind((socket.gethostname(), 5050))

# Start listening for client requests
s.listen(5)

while True:
    client_socket, address = s.accept()
    print(f"Connection from {address} has been established")
    # reading the contents of file in string format
    data = readfile('file1.txt')
    # encoding the file contents
    data = data.encode('utf-8')

    # generating the response for the client with specifying the length of the content
    # in the header(just first 10 bytes or so)
    response = f"{len(data):<{HEADER_SIZE}}".encode('utf-8')+data

    # sending the response to the client
    client_socket.send(response)

    # closing the client connection
    client_socket.close()
    print("DONE")


