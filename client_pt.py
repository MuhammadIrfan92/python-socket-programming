import socket


def request_file(file_name):
    # Create a socket
    # s = socket.socket()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    # s.connect(('server_hostname', 8080))
    s.connect((socket.gethostname(), 5003))

    # Send the file name to the server
    s.send(file_name.encode())

    # Receive the contents of the file from the server
    file_data = s.recv(1024)

    # Write the contents of the file to a local file
    with open("Pro_"+file_name, 'wb') as file:
        file.write(file_data)

    # Close the socket
    s.close()


# Test the function
request_file('file1.txt')
