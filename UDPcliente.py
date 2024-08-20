from socket import *
"""
"""

nombreServidor = 'localhost'
numeroPuerto = 1500
SocketCliente = socket(AF_INET, SOCK_DGRAM)
mensaje = input('Escriba una frase en minúsculas:')
SocketCliente.sendto(mensaje.encode(),(nombreServidor, numeroPuerto))
modificacionMensaje, direccionServidor = SocketCliente.recvfrom(2048)
print(modificacionMensaje.decode())
SocketCliente.close()