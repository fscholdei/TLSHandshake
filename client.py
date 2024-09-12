import os
import ssl
import socket


def main():
    # To be able to decrypt encrypted communication afterward
    os.environ['SSLKEYLOGFILE'] = 'premastersecret.log'

    # Create context for SSL
    context = ssl.create_default_context()
    context.maximum_version = ssl.TLSVersion.TLSv1_2  # Deactivate TLS 1.3

    # Accept self-signed server certificate
    # context.load_verify_locations('server.crt')
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    # Establishing a connection to the server
    with socket.create_connection(('localhost', 8443)) as sock:
        with context.wrap_socket(sock, server_hostname='localhost') as tls_sock:
            print(f"Conntected to server {tls_sock.getpeername()}")
            received_data = tls_sock.recv(1024)
            print(received_data.decode('utf-8'))


if __name__ == "__main__":
    main()
