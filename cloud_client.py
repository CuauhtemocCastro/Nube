import zmq

def cloud_client(message, host, port):
    """
    Función que representa un cliente en la nube local.

    Parameters:
    - message (str): El mensaje que se enviará al servidor.
    - host (str): La dirección IP o nombre de host del servidor.
    - port (int): El puerto al que el cliente se conectará.

    Returns:
    None
    """
    # Crear un contexto de ZeroMQ
    context = zmq.Context()

    # Crear un socket de tipo REQ (requisición)
    socket = context.socket(zmq.REQ)

    # Conectar el socket al servidor
    socket.connect(f"tcp://{host}:{port}")

    # Enviar el mensaje al servidor
    socket.send_string(message)

    # Recibir la respuesta del servidor
    response = socket.recv_string()

    # Imprimir la respuesta recibida del servidor
    print(f"Respuesta recibida del servidor: {response}")

    # Cerrar el socket y el contexto
    socket.close()
    context.term()

# Ejemplo de uso del cliente
cloud_client("Hola desde el cliente", "192.168.3.10", 5555)