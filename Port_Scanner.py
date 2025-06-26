import socket

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout after 1 second
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except socket.error:
        return False

def get_valid_host():
    while True:
        host = input("Enter target host (e.g., 127.0.0.1 or scanme.nmap.org): ").strip()
        if host:
            return host
        print("Host cannot be empty. Please enter a valid host.")
def get_valid_port(prompt):
    while True:
        port_str = input(prompt).strip()
        if port_str.isdigit():
            port = int(port_str)
            if 0 <= port <= 65535:
                return port
            else:
                print("Port must be between 0 and 65535.")
        else:
            print("Please enter a valid numeric port.")

def main():
    host = get_valid_host()
    start_port = get_valid_port("Enter start port number: ")
    end_port = get_valid_port("Enter end port number: ")

    if end_port < start_port:
        print("End port is less than start port. Swapping values.")
        start_port, end_port = end_port, start_port

    print(f"Scanning {host} from port {start_port} to {end_port}...\n")

    for port in range(start_port, end_port + 1):
        if scan_port(host, port):
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")

if __name__ == "__main__":
    main()
