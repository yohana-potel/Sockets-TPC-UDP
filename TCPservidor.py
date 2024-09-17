"""import os
from socket import *


puertoServidor = 1500

SocketServidor = socket(AF_INET, SOCK_STREAM)

#dirección y puerto del socket
SocketServidor.bind(('localhost', puertoServidor))


SocketServidor.listen(1)
print("El servidor está listo para recibir: ")

while True:
    coneccionSocket, addr = SocketServidor.accept()
    mensaje = coneccionSocket.recv(2048).decode()
    print(mensaje)
    mensajeModificado = mensaje.upper()
    coneccionSocket.send(mensajeModificado.encode())
    
    #se cierra conección con el cliente  
    coneccionSocket.close()
"""
import os
from socket import *

# Variables de entorno
nombreServidor = os.getenv('SERVER_HOST', 'localhost')
puerto = int(os.getenv('SERVER_PORT', 1500))
timeout = float(os.getenv('SOCKET_TIMEOUT', 10.0))

# Configuración del socket servidor
try:
    SocketServidor = socket(AF_INET, SOCK_STREAM)
    SocketServidor.bind((nombreServidor, puerto))
    SocketServidor.listen(1)
    SocketServidor.settimeout(timeout)  
    print(f"El servidor está listo para recibir en {nombreServidor}:{puerto} con timeout de {timeout} segundos")

    while True:
        try:
            conexionSocket, addr = SocketServidor.accept()
            print(f"Conexión aceptada de {addr}")
                    
            mensaje = conexionSocket.recv(2048).decode()
            print(f"Mensaje recibido: {mensaje}")

            conexionSocket.send(mensaje.upper().encode())
            conexionSocket.close()
        
        except socket.timeout:
            print("Timeout: No se recibió ninguna conexión en el tiempo especificado.")
        
except OSError as e:
    print(f"Error del servidor: {e}")

finally:
    SocketServidor.close()
    print("Servidor cerrado.")
