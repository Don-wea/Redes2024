print("esta funcionando el cliente con exito")
import socket
import argparse
from core  import clientLogic as cl


DEFAULT_HOST = 'redes2024_container_server'        # Symbolic name meaning all available interfaces
DEFAULT_PORT = 44555              # Arbitrary non-privileged port\


def start_client(host=DEFAULT_HOST, port=DEFAULT_PORT):
    # - --- ~ event Creation ~ ---
    cl.eventCreation()


    # crear socket
    clientSocket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    


    try:
        # ! conectar con el servidor
        clientSocket.connect((host,port))


        # - --- ~ event Connection Open ~ ---
        response = cl.eventConnectionOpen()
        # -->
        clientSocket.sendall(response.encode())
        # <--
        data=clientSocket.recv(1024)

    
        message='0'
        while(True):

            # - --- ~ event Step ~ ---
            response = cl.eventStep(message)

            #-->
            if isinstance(response,str) and response.endswith('.json'): # sends json in case it is sending a json file.
                with open(response, 'rb') as f:  # Open the file in binary mode
                    clientSocket.sendfile(f)  # Use sendfile to send the file over the socket
                    print("JSON file sent to server")
            elif response== "100":
                break
            else:
                clientSocket.sendall(response.encode())

            
            # <--
            message=clientSocket.recv(20240).decode()
            


    finally:
        # ! Terminar conection con el servidor
        clientSocket.close()

        # - --- ~ event Connection Close ~ ---
        cl.eventConnectionClose()
        


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start a server with a specified host and port.")
    parser.add_argument("--host", default=DEFAULT_HOST, help="Host to bind the server to")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT, help="Port to bind the server to")

    args = parser.parse_args()
    start_client(host=args.host, port=args.port)
