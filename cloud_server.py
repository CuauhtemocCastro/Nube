#servidor

import socket
import os
import threading

# Establece la ruta de destino para los archivos descargados
DOWNLOAD_PATH = r"C:\Users\jorge\OneDrive\Documents\Redes\\"

def receive_file(connection, filename):
    destination_path = os.path.join(DOWNLOAD_PATH, filename)
    with open(destination_path, 'wb') as file:
        while True:
            data = connection.recv(1024)
            if not data:
                break
            file.write(data)
            print(f"Recibidos {len(data)} bytes")

def send_file(connection, filename):
    with open(filename, 'rb') as file:
        for data in file:
            connection.sendall(data)
            print(f"Enviados {len(data)} bytes")

def handle_client(connection, address):
    print(f"Conexión establecida desde {address}")

    # Recibe la solicitud del cliente (upload o download)
    request = connection.recv(1024).decode()

    if request == 'upload':
        # El cliente quiere subir un archivo al servidor
        filename = connection.recv(1024).decode()
        print(f"Recibiendo archivo: {filename}")
        receive_file(connection, filename)
        print(f"Archivo {filename} recibido correctamente")
    elif request == 'download':
        # El cliente quiere descargar un archivo del servidor
        filename = connection.recv(1024).decode()
        print(f"Enviando archivo: {filename}")
        send_file(connection, filename)
        print(f"Archivo {filename} enviado correctamente")

    # Cierra la conexión
    connection.close()

def cloud_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("192.168.3.6", 8000))
    sock.listen(5)

    print("Servidor escuchando en 192.168.1.6:8000")

    while True:
        connection, address = sock.accept()
        print(f"Conexión establecida desde {address}")

        # Inicia un hilo para manejar la conexión con múltiples clientes
        client_thread = threading.Thread(target=handle_client, args=(connection, address))
        client_thread.start()

cloud_server()