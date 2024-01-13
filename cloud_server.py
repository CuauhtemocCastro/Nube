import socket

def cloud_server():
    # Crear un socket TCP/IP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Asigna el socket al puerto 8000
    sock.bind(("192.168.3.6", 8000))

    # Escucha conexiones entrantes
    sock.listen(1)

    while True:
         # Acepta una conexión
        connection, address = sock.accept()

        #Lee los datos del cliente
        data = connection.recv(1024)

        # Imprime los datos recibidos
        print(data)

cloud_server()