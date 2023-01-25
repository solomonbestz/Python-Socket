import socket 

HOST = "192.168.91.112" # Standard loopback interface address (localhost)
PORT = 65432 # Port to listen on (non-privileded ports are > 1023)


# socket.socket() creates a socket object
# The with allows us to use the socket object without calling soc.close()
"""
The arguments passed to socket() are constants used to specify the address family and socket type.
AF_INET is the Internet address family for IPv4. SOCK_STREAM is the socket type for TCP,
the protocol that will be used to transport messages in the network.
"""
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen(5)

    communication_socket, address = server.accept()

    with communication_socket:
        print(f"Connected to  {address}")
        while True:
            data_or_message = communication_socket.recv(1024).decode('utf-8')
            if not data_or_message:
                break
            print(f"Client: {data_or_message}")
            communication_socket.send(f"Message Sent!".encode("utf-8"))

    print(f"Connection with {address} ended")






