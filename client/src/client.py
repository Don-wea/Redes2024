print("esta funcionando el cliente con exito")


import socket
# import time
# from core  import clientLogic as cl


# DEFAULT_HOST = 'localhost'        # Symbolic name meaning all available interfaces
# DEFAULT_PORT = 44555              # Arbitrary non-privileged port\

# def start_client(host=DEFAULT_HOST, port=DEFAULT_PORT):
#     # - --- ~ event Creation ~ ---
#     cl.eventCreation()


#     # crear socket
#     clientSocket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    


#     try:
#         # ! conectar con el servidor
#         clientSocket.connect((host,port))


#         # - --- ~ event Connection Open ~ ---
#         response = cl.eventConnectionOpen()
#         # -->
#         clientSocket.sendall(response.encode())
#         # <--
#         data=clientSocket.recv(1024)

    
#         message='0'
#         while(True):

#             # - --- ~ event Step ~ ---
#             response = cl.eventStep(message)

#             #-->
#             if isinstance(response,str) and response.endswith('.json'): # sends json in case it is sending a json file.
#                 with open(response, 'rb') as f:  # Open the file in binary mode
#                     clientSocket.sendfile(f)  # Use sendfile to send the file over the socket
#                     print("JSON file sent to server")
#             elif response== "100":
#                 break
#             else:
#                 clientSocket.sendall(response.encode())

            
#             # <--
#             message=clientSocket.recv(20240).decode()
            


#     finally:
#         # ! Terminar conection con el servidor
#         clientSocket.close()

#         # - --- ~ event Connection Close ~ ---
#         cl.eventConnectionClose()
        


# if __name__ == "__main__":
#     start_client()
