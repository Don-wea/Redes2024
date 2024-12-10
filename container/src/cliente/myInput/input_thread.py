# Maneja la recepción de mensajes
def handle_input(connection, input_queue):
    while True:
        try:
            message = connection.recv(1024).decode()
            if not message:
                print("Cliente desconectado.")
                break
            print(f"Mensaje recibido: {message}")
            input_queue.put(message)  # Enviar el mensaje a la cola de entrada para procesar
        except Exception as e:
            print(f"Error en recepción: {e}")
            break
    connection.close()