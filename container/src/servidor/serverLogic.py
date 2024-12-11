# import json
# import os
import time
import logging

from servidor.dao import guardarMensajes as gm

# --- ~~ ~~ __Private methods ~~ ~~ --- 


        

# --- ~~ ~~ PUBLIC EVENTS ~~ ~~ --- 

def mainLogic(host, port,serverClient_queue):

    lapseCount = 0
    while True:

        # LOGICA DEL SERVIDOR
        time.sleep(5)

        message=''

        # 1. checkear si hay respuesta del cliente (transmitir mensajes entre hilos)
        if not serverClient_queue.empty():
            address,message = serverClient_queue.get()
            print(f"Mensaje recibido desde {address}: {message}")
            logging.info("Mensaje recibido en el servidor, procesando mensaje...")

        # 2. en caso de haber respuesta del cliente, procesarla (conexion con DAO de ser necsario) (y enviar respuesta si es que es necesario)
        # comunicacion con base de datos DAO
        if message!='':
            # si llega algun mensaje valido, este se debe guardar en la base de datos -> address y message.
            if message is not None: # la idea es que si el mensaje es valido se guarde en la base de datos
                a=0
            else :                  # si el mensaje no es valida, en la base  de datos se guarda la direccion del cliente en la lista negra pa banearlo.
                b=0
        # 3. resto de la logica del servidor


        print("iteracion "+ str(lapseCount) +" de la logica del servidor")
        lapseCount +=1


    return