
# global imports
import threading
from queue import Queue

# my packages
from cliente.myInput import input_thread as ii
from cliente.myOutput import output_thread as oo





    # --- ~~ ~~ PUBLIC EVENTS ~~ ~~ --- 

    # Maneja la lógica de un cliente
def clientHandler(connection, address,serverClient_queue):
    print(f"Cliente conectado desde: {address}")

    # Crear colas para entrada y salida
    input_queue = Queue()
    output_queue = Queue()


    # --  ~ ~ CLIENT INPUT THREAD ~ ~  -- 
    input_thread = threading.Thread(target=ii.handle_input, args=(connection, input_queue))
    input_thread.start()

    # --  ~ ~ CLIENT OUTPUT THREAD ~ ~  -- 
    output_thread = threading.Thread(target=oo.handle_output, args=(connection, output_queue))
    output_thread.start()


    try:
        while True:
            # Transmitiendo los mensajes al servidor
            if not input_queue.empty():
                message = input_queue.get()
                serverClient_queue.put((address, message))


            if not serverClient_queue.empty():
                message = serverClient_queue.get()
                output_queue.put(message)
    finally:
        # Finalizar hilos y cerrar conexión
        output_queue.put("STOP")
        input_thread.join()
        output_thread.join()
        print(f"Conexión cerrada con {address}")
