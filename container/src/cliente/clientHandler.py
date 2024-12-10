
# global imports
import threading
import logging
from queue import Queue

# my packages
from cliente.myInput import input_thread as ii
from cliente.myOutput import output_thread as oo



    # --- ~~ ~~ PUBLIC EVENTS ~~ ~~ --- 
    # Maneja la lógica de un cliente
def clientHandler(connection, address,serverClient_queue):
    print(f"Cliente conectado desde: {address}")

    # Crear colas para entrada y salida
    logging.info("Creando Queue's de comunicacion entre logica de cliente y threads de entrada y salida")
    input_queue = Queue()
    output_queue = Queue()


    # --  ~ ~ CLIENT INPUT THREAD ~ ~  -- 
    logging.info("Creando thread de entrada")
    input_thread = threading.Thread(target=ii.handle_input, args=(connection, input_queue))
    input_thread.start()

    
    # --  ~ ~ CLIENT OUTPUT THREAD ~ ~  -- 
    logging.info("Creando thread de salida")
    output_thread = threading.Thread(target=oo.handle_output, args=(connection, output_queue))
    output_thread.start()


    try:
        while True:
            # Transmitiendo los mensajes al servidor.
            if not input_queue.empty():
                message = input_queue.get()
                logging.info("Mensaje recibido desde {address}, enviando mensaje a la logica del servidor")
                serverClient_queue.put((address, message))


            # Transmitiendo mensajes del servidor al cliente.
            if not serverClient_queue.empty():
                message = serverClient_queue.get()
                logging.info("Mensaje recibido desde la logica del servidor, enviando mensaje al cliente {address}")
                output_queue.put(message)
    finally:
        # Finalizar hilos y cerrar conexión
        output_queue.put("STOP")
        input_thread.join()
        output_thread.join()
        print(f"Conexión cerrada con {address}")
