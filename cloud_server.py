# VERSION 2

import socket
import os

def receive_file(connection, filename):
    with open(filename, 'wb') as file:
        while True:
            data = connection.recv(1024)
            if not data:
                break
            file.write(data)

def cloud_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("192.168.3.6", 8000))
    sock.listen(5)

    print("Servidor escuchando en 192.168.3.6:8000")

    while True:
        connection, address = sock.accept()
        print(f"Conexión establecida desde {address}")

        # Recibe el nombre del archivo
        filename = connection.recv(1024).decode()
        print(f"Recibiendo archivo: {filename}")

        # Recibe el archivo
        receive_file(connection, filename)
        print(f"Archivo {filename} recibido correctamente")

        # Cierra la conexión
        connection.close()

cloud_server()

# VERSION 1

# import socket

# def cloud_server():
#     # Crear un socket TCP/IP
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#     # Asigna el socket al puerto 8000
#     sock.bind(("192.168.3.6", 8000))

#     # Escucha conexiones entrantes
#     sock.listen(1)

#     while True:
#          # Acepta una conexión
#         connection, address = sock.accept()

#         #Lee los datos del cliente
#         data = connection.recv(1024)

#         # Imprime los datos recibidos
#         print(data)

# cloud_server()