import socket
#import time
from core import serverLogic as sl

DEFAULT_HOST = 'localhost'         # Symbolic name meaning all available interfaces
DEFAULT_PORT = 44555               # Arbitrary non-privileged port\

def start_server(host=DEFAULT_HOST, port=DEFAULT_PORT):
    # - --- ~ ||| EVENT CREATION ||| ~ ---
    # sl.eventCreation()

    # ! Crear Socket
    mySocket = (socket.socket(socket.AF_INET,socket.SOCK_STREAM))
    mySocket.bind((host,port))
    mySocket.listen()
    
    try:
        # ! Conectar con el cliente.
        connection,client_adresss = mySocket.accept()
        print(f'Conexión establecida con {client_adresss}')


        # <--
        # message = connection.recv(1024).decode()

        # - --- ~ ||| EVENT CONNECTION OPEN ||| ~ ---
        # response = sl.eventConnectionOpen(message)

        # -->
        # connection.sendall(response.encode())
        
        while(True):
            print("while")
            # <--
            # message = connection.recv(20240).decode()

            # - --- ~ ||| EVENT STEP ||| ~ ---
            # response = sl.eventStep(message)

            # -->
            # if isinstance(response,str) and response.endswith('.json'): # sends json in case it is sending a json file.
            #     with open(response, 'rb') as f:  # Open the file in binary mode
            #         connection.sendfile(f)  # Use sendfile to send the file over the socket
            #         print("JSON file sent to client")
            # elif response == "100":
            #     break   # se ha finalizado el proceso de intercambio de informacion.
            # else:
            #     connection.sendall(response.encode())

    finally:
        print("finally")
        # ! Terminar conection con el cliente.
        # connection.close()
        
        # - --- ~ |||  EVENT CONNECTION CLOSE ||| ~ ---
        # sl.eventConnectionClose()

if __name__ == "__main__":
    start_server('localhost',44555)
