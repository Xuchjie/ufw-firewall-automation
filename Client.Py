import socket

def main():
    try:
        # Connect to server
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('127.0.0.1', 12345))
        print("Connected to server at 127.0.0.1:12345")

        # Send a message
        message = "Hello from the client!"
        client.sendall(message.encode())
        print("Sent to server:", message)

        # Receive a message
        response = client.recv(1024).decode()
        print("Received from server:", response)

    except ConnectionRefusedError:
        print("Client error: [WinError 10061] No connection could be made because the target machine actively refused it")
    except Exception as e:
        print("Client error:", e)
    finally:
        # Gracefully close connection
        client.close()
        print("Connection closed.")

if __name__ == '__main__':
    main()
