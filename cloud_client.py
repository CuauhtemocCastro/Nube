#cliente
import socket

def send_file(sock, filename):
    with open(filename, 'rb') as file:
        for data in file:
            sock.sendall(data)
            print(f"Enviados {len(data)} bytes")

def download_file(sock, filename):
    destination_path = r'C:\Users\jorge\OneDrive\Documents\Redes' + filename
    with open(destination_path, 'wb') as file:
        while True:
            data = sock.recv(1024)
            if not data:
                break
            file.write(data)
            print(f"Recibidos {len(data)} bytes")

def cloud_client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("192.168.1.6", 8000))

    # Solicita al usuario la acción (upload o download)
    action = input("Ingrese 'upload' para subir un archivo o 'download' para descargar: ")
    sock.sendall(action.encode())

    if action == 'upload':
        # El cliente quiere subir un archivo al servidor
        filename = input("Ingrese el nombre del archivo a subir: ")
        sock.sendall(filename.encode())
        send_file(sock, filename)
        print(f"Archivo {filename} enviado correctamente")
    elif action == 'download':
        # El cliente quiere descargar un archivo del servidor
        filename = input("Ingrese el nombre del archivo a descargar: ")
        sock.sendall(filename.encode())
        download_file(sock, filename)
        print(f"Archivo {filename} descargado correctamente")

    # Cierra la conexión
    sock.close()

cloud_client()