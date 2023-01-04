import socket


def send_file(s):
    # Receive the file name from the client
    file_name = s.recv(1024).decode()

    # Open the file in binary mode
    with open(file_name, 'rb') as file:
        # Read the contents of the file
        file_data = file.read()

        # Send the contents of the file to the client
        s.sendall(file_data)

    # Close the socket
    s.close()


# Create a socket
#s = socket.socket()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a port
# s.bind(('', 8080))

s.bind((socket.gethostname(), 5003))

# Listen for incoming connections
s.listen()
while True:
    # Accept a connection
    connection, address = s.accept()

    # Call the send_file function with the accepted connection
    send_file(connection)

    # Close the original socket
    s.close()
