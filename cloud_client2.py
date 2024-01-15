#cliente
import socket
import os
def send_file(sock, filename):
    with open(filename, 'rb') as file:
        for data in file:
            sock.sendall(data)
            print(f"Enviados {len(data)} bytes")

def download_file(sock, filename, destination_path):
    with open(os.path.join(destination_path, filename), 'wb') as file:
        while True:
            data = sock.recv(1024)
            if not data:
                break
            file.write(data)
            print(f"Recibidos {len(data)} bytes")

def cloud_client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("127.0.0.1", 8000)) #se conecta al servidor con la IP dada en el puerto dado

    # Solicita al usuario la acción (upload o download)
    action = input("Ingrese 'upload' para subir un archivo o 'download' para descargar: ")
    sock.sendall(action.encode())

    if action == 'upload':
        # El cliente quiere subir un archivo al servidor
        filepath = input("Ingrese la ruta completa del archivo a subir: ") #se pone la ruta absoluta del archivo
        filename = os.path.basename(filepath)  # Extrae el nombre del archivo de la ruta
        sock.sendall(filename.encode())
        send_file(sock, filepath)  # Usa la ruta completa para leer y enviar el archivo
        print(f"Archivo {filename} enviado correctamente")
    if action == 'download':
        filename = input("Ingrese el nombre del archivo a descargar: ")
        destination = input("Ingrese la ruta absoluta donde desea guardar el archivo: ")
        sock.sendall(filename.encode())
        download_file(sock, filename, destination)  # Añade el destino como un parámetro
        print(f"Archivo {filename} descargado correctamente")

    # Cierra la conexión
    sock.close()

cloud_client()
