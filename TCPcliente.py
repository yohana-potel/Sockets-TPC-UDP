import os
import re
from socket import *

#variables de entorno

nombreServidor = os.getenv('SERVER_HOST', 'localhost')
puerto = int(os.getenv('SERVER_PORT', 1500))
timeout = float(os.getenv('SOCKET_TIMEOUT', 10.0))

#Socket Cliente

try:
    SocketCliente = socket(AF_INET, SOCK_STREAM)
    SocketCliente.settimeout(timeout)  

    print(f"Conectando a {nombreServidor} en el puerto {puerto} con timeout de {timeout} segundos...")
    SocketCliente.connect((nombreServidor, puerto))

    while True:
        mensaje = input('Escriba una frase solo con letras minúsculas (o "salir" para terminar): ')

        # Permitir la salida con la palabra "salir"
        if mensaje == "salir":
            print("Finalizando conexión a solicitud del usuario...")
            break

        # Validar que solo contenga letras minúsculas
        if not re.fullmatch(r'[a-z]+', mensaje):
            print("Error: El mensaje solo debe contener letras minúsculas sin espacios, números o caracteres especiales.")
            continue  

        SocketCliente.send(mensaje.encode())
        mensajeModificado = SocketCliente.recv(2048)
        print(f"Mensaje modificado recibido: {mensajeModificado.decode()}")

   
except OSError as conexionAlServidor:
    print(f"Error de conexión al servidor: {conexionAlServidor}")

except ValueError as usuario:
    print(f"Error en la entrada del usuario: {usuario}")

except timeout:
    print("Timeout: No se recibió respuesta del servidor.")

finally:
    SocketCliente.close()
    print("Conexión finalizada.")
