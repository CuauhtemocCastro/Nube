import threading
import zmq

def cloud_server(node_id, host, port):
    """
    Función para manejar el servidor de la nube.

    Args:
        node_id (int): Identificador del nodo.
        host (str): Dirección IP del host.
        port (int): Puerto de comunicación.

    """
    # Inicializar el contexto y el socket REP (Reply) de ZeroMQ
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind(f"tcp://{host}:{port}")

    # Bucle principal del servidor
    while True:
        # Recibir mensaje del cliente
        message = socket.recv_string()
        print(f"Nodo {node_id} recibido: {message}")

        # Enviar respuesta al cliente
        response = f"Respuesta del nodo {node_id}"
        socket.send_string(response)

# Iniciar hilo del servidor
node_thread = threading.Thread(target=cloud_server, args=(1, "192.168.3.6", 5555))
node_thread.start()

# Esperar a que el hilo del servidor termine (en este caso, nunca sucede debido al bucle infinito)
node_thread.join()