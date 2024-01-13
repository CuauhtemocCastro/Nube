import zmq

def cloud_client(message, port):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect(f"tcp://127.0.0.1:{port}")
    socket.send_string(message)
    response = socket.recv_string()
    print(f"Respuesta recibida del servidor: {response}")

if __name__ == "__main__":
    cloud_client("Hola desde el cliente", 5555)