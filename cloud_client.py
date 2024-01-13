import socket

def cloud_client():
    # Crea un socket TCP/IP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conecta el socket en el puerto cuando el servidor esté escuchando (8000)
    sock.connect(("192.168.3.6", 8000))

    message = input("Mensaje a enviar: ")

    # Escribe los datos al servidor
    sock.sendall(message.encode())

    # Cierra la conexión
    sock.close()

cloud_client()