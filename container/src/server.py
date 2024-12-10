import socket
import threading
import argparse
from queue import Queue

from servidor import serverLogic as sl
from cliente import clientHandler as ch

#import time


DEFAULT_HOST = 'redes2024_container_server'         # Symbolic name meaning all available interfaces
DEFAULT_PORT = 44555                                # Arbitrary non-privileged port


# Inicia el servidor
def start_server(host=DEFAULT_HOST, port=DEFAULT_PORT):
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mySocket.bind((host, port))
    mySocket.listen(5)
    print(f"Servidor iniciado en {host}:{port}")

    # Crear una cola para transmitir información
    serverClient_queue = Queue()

    # --  ~ ~ SERVER LOGIC THREAD ~ ~  -- 
    serverLogic_thread = threading.Thread(target=sl.mainLogic, args=(host, port,serverClient_queue))
    serverLogic_thread.start()
    

    try:
        while True:
            connection, address = mySocket.accept()
            # --  ~ ~ CLIENT THREAD ~ ~  -- 
            client_thread = threading.Thread(target=ch.clientHandler, args=(connection, address,serverClient_queue))
            client_thread.start()


    finally:
        mySocket.close()
        print("Servidor cerrado.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start a server with a specified host and port.")
    parser.add_argument("--host", default=DEFAULT_HOST, help="Host to bind the server to")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT, help="Port to bind the server to")

    args = parser.parse_args()

    print("Program started...")
    start_server(host=args.host, port=args.port)

