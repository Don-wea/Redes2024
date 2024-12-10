# Maneja el envío de mensajes
def handle_output(connection, output_queue):
    while True:
        try:
            message = output_queue.get()  # Bloquea hasta que haya un mensaje para enviar
            if message == "STOP":
                print("Cerrando conexión con cliente.")
                break
            connection.sendall(message.encode())
        except Exception as e:
            print(f"Error en envío: {e}")
            break
    connection.close()