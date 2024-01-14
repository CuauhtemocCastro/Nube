# VERSION 3

import socket
import os
import threading

def receive_file(connection, filename):
    with open(filename, 'wb') as file:
        while True:
            data = connection.recv(1024)
            if not data:
                break
            file.write(data)

def send_file(connection, filename):
    with open(filename, 'rb') as file:
        for data in file:
            connection.sendall(data)

def list_files():
    return os.listdir()

def handle_client(connection, address):
    print(f"Conexión establecida desde {address}")

    # Recibe el comando o el nombre del archivo
    command_or_filename = connection.recv(1024).decode()

    if command_or_filename.lower() == "upload":
        # Cliente esta solicitando subir un archivo
        filename = connection.recv(1024).decode()
        print(f"Recibiendo archivo: {filename}")
        receive_file(connection, filename)
        print(f"Archivo {filename} recibido correctamente")

        # Envia un mensaje de confirmación
        connection.sendall("Archivo recibido correctamente".encode())
    elif command_or_filename.lower() == "download":
        # Cliente esta solicitando descargar un archivo
        filename = connection.recv(1024).decode()
        print(f"Enviando archivo: {filename}")
        send_file(connection, filename)
        print(f"Archivo {filename} enviado correctamente")
    elif command_or_filename.lower() == "list":
        # Cliente esta solicitando listar los archivos
        files_list = list_files()
        files_str = "\n".join(files_list)
        connection.sendall(files_str.encode())
    else:
        print("Comando desconocido")

    # Cierra la conexión
    connection.close()

def cloud_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("192.168.3.6", 8000))

    print("Servidor escuchando en 192.168.3.6:8000")

    while True:
        connection, address = sock.accept()

        # Incia un thread para manejar la conexión con multiples clientes
        client_thread = threading.Thread(target=handle_client, args=(connection, address))
        client_thread.start()

cloud_server()

# VERSION 2

# import socket
# import os
# import threading

# def receive_file(connection, filename):
#     with open(filename, 'wb') as file:
#         while True:
#             data = connection.recv(1024)
#             if not data:
#                 break
#             file.write(data)

# def handle_client(connection, address):
#     print(f"Conexión establecida desde {address}")

#     # Recibe el nombre del archivo
#     filename = connection.recv(1024).decode()
#     print(f"Recibiendo archivo: {filename}")

#     # Recibe el archivo
#     receive_file(connection, filename)
#     print(f"Archivo {filename} recibido correctamente")

#     # Cierra la conexión
#     connection.close()

# def cloud_server():
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sock.bind(("192.168.3.6", 8000))
#     sock.listen(5)

#     print("Servidor escuchando en 192.168.3.6:8000")

#     while True:
#         connection, address = sock.accept()
#         print(f"Conexión establecida desde {address}")

#         # Incia un thread para manejar la conexión con multiples clientes
#         client_thread = threading.Thread(target=handle_client, args=(connection, address))
#         client_thread.start()

#         # # Recibe el nombre del archivo
#         # filename = connection.recv(1024).decode()
#         # print(f"Recibiendo archivo: {filename}")

#         # # Recibe el archivo
#         # receive_file(connection, filename)
#         # print(f"Archivo {filename} recibido correctamente")

#         # # Cierra la conexión
#         # connection.close()

# cloud_server()

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