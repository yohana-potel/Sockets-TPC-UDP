
from socket import *


puertoServidor = 1500
SocketServidor = socket(AF_INET, SOCK_DGRAM)
SocketServidor.bind(('localhost', puertoServidor))
print("El servidor está listo para recibir")
while True:
    mensaje, direccionCliente = SocketServidor.recvfrom(2048)
    Mensaje = mensaje.decode().upper()
    print(Mensaje)
    SocketServidor.sendto(Mensaje.encode(), direccionCliente)