import socket
from core  import clientLogic as cl


DEFAULT_HOST = 'localhost'        # Symbolic name meaning all available interfaces
DEFAULT_PORT = 44555              # Arbitrary non-privileged port\

def start_client(host=DEFAULT_HOST, port=DEFAULT_PORT):
    # - --- ~ ||| EVENT CREATION ||| ~ ---
    # cl.eventCreation()


    # crear socket
    clientSocket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    


    try:
        # ! conectar con el servidor
        clientSocket.connect((host,port))


        # # - --- ~ ||| EVENT CONNECTION OPEN ||| ~ ---
        # response = cl.eventConnectionOpen()
        
        # # -->
        # clientSocket.sendall(response.encode())

        # # <--
        # data=clientSocket.recv(1024)

    
        message='0'
        while(True):
            print("while")
            # # - --- ~ ||| EVENT STEP ||| ~ ---
            # response = cl.eventStep(message)

            # #-->
            # if isinstance(response,str) and response.endswith('.json'): # sends json in case it is sending a json file.
            #     with open(response, 'rb') as f:  # Open the file in binary mode
            #         clientSocket.sendfile(f)  # Use sendfile to send the file over the socket
            #         print("JSON file sent to server")
            # elif response== "100":
            #     break
            # else:
            #     clientSocket.sendall(response.encode())

            
            # # <--
            # message=clientSocket.recv(20240).decode()
            


    finally:
        print("finally")
        # ! Terminar conection con el servidor
        # clientSocket.close()

        # - --- ~ |||  EVENT CONNECTION CLOSE ||| ~ ---
        # cl.eventConnectionClose()
        


if __name__ == "__main__":
    start_client()
