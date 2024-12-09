import socket
import argparse
from core import serverLogic as sl

DEFAULT_HOST = 'redes2024_container_server'         # Symbolic name meaning all available interfaces
DEFAULT_PORT = 44555                                # Arbitrary non-privileged port

def start_server(host=DEFAULT_HOST, port=DEFAULT_PORT):
    # - --- ~ event Creation ~ ---
    sl.eventCreation()

    # ! Create Socket
    mySocket = (socket.socket(socket.AF_INET, socket.SOCK_STREAM))
    mySocket.bind((host, port))
    mySocket.listen()
    
    try:
        # ! Connect with the client.
        connection, client_address = mySocket.accept()
        print(f'Connection established with {client_address}')

        # <--
        message = connection.recv(1024).decode()
        # - --- ~ event Connection Open ~ ---
        response = sl.eventConnectionOpen(message)
        # -->
        connection.sendall(response.encode())
        
        while True:
            # <--
            message = connection.recv(20240).decode()
            # - --- ~ event Step ~ ---
            response = sl.eventStep(message)
            # -->
            if isinstance(response, str) and response.endswith('.json'):  # Send JSON if it is a JSON file.
                with open(response, 'rb') as f:  # Open the file in binary mode
                    connection.sendfile(f)  # Use sendfile to send the file over the socket
                    print("JSON file sent to client")
            elif response == "100":
                break  # Process of information exchange has ended.
            else:
                connection.sendall(response.encode())

    finally:
        # ! End connection with the client.
        connection.close()
        # - --- ~ event Connection Close ~ ---
        sl.eventConnectionClose()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start a server with a specified host and port.")
    parser.add_argument("--host", default=DEFAULT_HOST, help="Host to bind the server to")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT, help="Port to bind the server to")

    args = parser.parse_args()

    print("Program started...")
    start_server(host=args.host, port=args.port)
