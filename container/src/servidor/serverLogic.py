# import json
# import os
import time

# --- ~~ ~~ __Private methods ~~ ~~ --- 


        

# --- ~~ ~~ PUBLIC EVENTS ~~ ~~ --- 


def mainLogic(host, port,serverClient_queue):

    lapseCount = 0
    while True:

        # LOGICA DEL SERVIDOR
        time.sleep(5)


        # 1. checkear si hay respuesta del cliente (transmitir mensajes entre hilos)
        if not serverClient_queue.empty():
            address,message = serverClient_queue.get()
            print(f"Mensaje recibido desde {address}: {message}")

        # 2. en caso de haber respuesta del cliente, procesarla (conexion con DAO de ser necsario) (y enviar respuesta si es que es necesario)
        # comunicacion con base de datos DAO

    

        # 3. resto de la logica del servidor


        print("iteracion "+ str(lapseCount) +" de la logica del servidor")
        lapseCount +=1


    return