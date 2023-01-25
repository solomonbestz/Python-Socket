import socket

HOST = "192.168.91.112" # The server's hostname or IP address
PORT = 65432 # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    client_message = input("Enter Name: ")
    client.send(client_message.encode("utf-8"))
    data = client.recv(1024).decode('utf-8')

print(f'Server: {data}')