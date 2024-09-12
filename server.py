import sys
import socket
import ssl


def main():
    # Create TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    # Allow reuse of addr
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        sock.bind(('localhost', 8443))  # Port of server
        sock.listen(5)
    except OSError as e:
        print(f"Error binding port: {e}")
        sys.exit(1)

    # Create context for SSL
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile='server.crt', keyfile='server.key')

    # Convert socket to an SSL socket
    with context.wrap_socket(sock, server_side=True) as tls_sock:
        while True:
            client_sock, addr = tls_sock.accept()
            print(f"Connected to client: {addr}")
            client_sock.sendall(b"Hello Client!\n")
            print("Sending 'Hello Client!' to the client.")
            client_sock.close()


if __name__ == "__main__":
    main()
