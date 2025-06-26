# server.py
import socket  # This lets us use sockets

# Create a socket object (this makes the server)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set the host and port
host = '127.0.0.1'  # This is localhost (your own computer)
port = 12345        # You can pick any number over 1024

try:
    # Bind the server to the address
    server_socket.bind((host, port))

    # Listen for one connection at a time
    server_socket.listen(1)
    print(f"Server is listening on {host}:{port}...")

    # Accept the connection from the client
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    # Receive message from client
    data = conn.recv(1024).decode()
    print(f"Received from client: {data}")

    # Send a message back
    reply = "Hello from the server!"
    conn.send(reply.encode())

    # Close the connection
    conn.close()

except Exception as e:
    print("Server error:", e)

finally:
    server_socket.close()
