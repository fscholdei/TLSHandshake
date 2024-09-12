import socket
import threading
import sys


def handle_client(client_socket, server_addr, server_port):
    # Establish connection with real server
    server_socket = socket.create_connection((server_addr, server_port))

    def forward(src, dst, name):
        while True:
            try:
                data = src.recv(4096)
                if not data:
                    break

                if src is client_socket:
                    print("Received data from client.")

                if src is server_socket:
                    print("Received data from server.")

                dst.sendall(data)
                # print(f"{name} received: {data}")
            except Exception as e:
                print(f"Exception in {name}: {e}")
                break

    # Set up threads for data forwarding
    client_to_server = threading.Thread(target=forward, args=(client_socket, server_socket, 'Client-to-Server'))
    server_to_client = threading.Thread(target=forward, args=(server_socket, client_socket, 'Server-to-Client'))

    # Start threads
    client_to_server.start()
    server_to_client.start()

    # Wait until threads are finished
    client_to_server.join()
    server_to_client.join()

    # Close sockets
    client_socket.close()
    server_socket.close()


def main(port, server_addr, server_port):
    mitm_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mitm_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        mitm_server.bind(('localhost', port))
        mitm_server.listen(5)
    except OSError as e:
        print(f"Error binding port: {e}")
        sys.exit(1)

    print("MITM proxy is running...")

    while True:
        client_socket, addr = mitm_server.accept()
        print(f"Accepted connection from {addr}")
        threading.Thread(target=handle_client, args=(client_socket, server_addr, server_port)).start()


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='mitm tool')
    parser.add_argument('--port', metavar='port', type=int, default=8443, help='set mitm port')
    parser.add_argument('--server_addr', metavar='addr', default='localhost', help='set server address')
    parser.add_argument('--server_port', metavar='port', type=int, default=8444, help='set server port')
    args = parser.parse_args()
    main(port=args.port, server_addr=args.server_addr, server_port=args.server_port)
