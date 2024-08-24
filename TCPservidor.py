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
    mensajeModificado = mensaje.upper()
    coneccionSocket.send(mensajeModificado.encode())
    
    #se cierra conección con el cliente  
    coneccionSocket.close()
