from socket import *

nombreServidor = 'localhost'
puerto = 1500
SocketCliente = socket(AF_INET, SOCK_STREAM)
SocketCliente.connect((nombreServidor,puerto))
mensaje = input('Escriba una frase en minúsculas:')
SocketCliente.send(mensaje.encode())

mensajeModificado = SocketCliente.recv(2048)
print(mensajeModificado.decode())

SocketCliente.close()