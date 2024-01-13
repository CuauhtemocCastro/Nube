import threading
import zmq

def cloud_server(node_id, port):
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind(f"tcp://127.0.0.1:{port}")

    while True:
        message = socket.recv_string()
        print(f"Nodo {node_id} reibido: {message}")
        response = f"Respuesta del nodo {node_id}"
        socket.send_string(response)

if __name__ == "__main__":
    node_thread = threading.Thread(target=cloud_server, args=(1, 5555))
    node_thread.start()
    node_thread.join()