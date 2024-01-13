# VERSION 2

import socket

def send_file(sock, filename):
    with open(filename, 'rb') as file:
        for data in file:
            sock.sendall(data)

def cloud_client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("192.168.3.6", 8000))

    # Envia el nombre del archivo
    filename = input("Ingrese el nombre del archivo: ")
    sock.sendall(filename.encode())

    # Envia el archivo
    send_file(sock, filename)

    # Cierra la conexión
    sock.close()

cloud_client()

# VERSION 1

# import socket

# def cloud_client():
#     # Crea un socket TCP/IP
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#     # Conecta el socket en el puerto cuando el servidor esté escuchando (8000)
#     sock.connect(("192.168.3.6", 8000))

#     message = input("Mensaje a enviar: ")

#     # Escribe los datos al servidor
#     sock.sendall(message.encode())

#     # Cierra la conexión
#     sock.close()

# cloud_client()