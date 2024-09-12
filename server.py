import socket
import ssl


def main():
    # Socket erstellen
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    sock.bind(('localhost', 8443))
    sock.listen(5)

    # Kontext für SSL erstellen
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile='server.crt', keyfile='server.key')

    # Socket in einen SSL-Socket umwandeln
    with context.wrap_socket(sock, server_side=True) as tls_sock:
        while True:
            client_sock, addr = tls_sock.accept()
            print(f"Connected to client {addr}.")
            client_sock.sendall(b"Hello Client!\n")
            client_sock.close()


if __name__ == "__main__":
    main()
