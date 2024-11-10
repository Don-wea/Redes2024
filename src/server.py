print("esta funcionando el servidor con exito")

# import socket
# #import time
# from core import serverLogic as sl

# DEFAULT_HOST = 'localhost'         # Symbolic name meaning all available interfaces
# DEFAULT_PORT = 44555               # Arbitrary non-privileged port\

# def start_server(host=DEFAULT_HOST, port=DEFAULT_PORT):
#     # - --- ~ event Creation ~ ---
#     sl.eventCreation()

#     # ! Crear Socket
#     mySocket = (socket.socket(socket.AF_INET,socket.SOCK_STREAM))
#     mySocket.bind((host,port))
#     mySocket.listen()
    
#     try:
#         # ! Conectar con el cliente.
#         connection,client_adresss = mySocket.accept()
#         print(f'Conexión establecida con {client_adresss}')


#         # <--
#         message = connection.recv(1024).decode()
#         # - --- ~ event Connection Open ~ ---
#         response = sl.eventConnectionOpen(message)
#         # -->
#         connection.sendall(response.encode())
        
#         while(True):
            
#             # <--
#             message = connection.recv(20240).decode()
#             # - --- ~ event Step ~ ---
#             response = sl.eventStep(message)
#             # -->
#             if isinstance(response,str) and response.endswith('.json'): # sends json in case it is sending a json file.
#                 with open(response, 'rb') as f:  # Open the file in binary mode
#                     connection.sendfile(f)  # Use sendfile to send the file over the socket
#                     print("JSON file sent to client")
#             elif response == "100":
#                 break   # se ha finalizado el proceso de intercambio de informacion.
#             else:
#                 connection.sendall(response.encode())

#     finally:
#         # ! Terminar conection con el cliente.
#         connection.close()
#         # - --- ~ event Connection Close ~ ---
#         sl.eventConnectionClose()

# if __name__ == "__main__":
#     print("programa comenzado...")
#     start_server('localhost',44555)
