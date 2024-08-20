from socket import *


serverPort = 1500
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('localhost', serverPort))
serverSocket.listen(1)
print("El servidor está listo para recibir")

while True:
    connectionSocket, addr = serverSocket.accept()
    message = connectionSocket.recv(2048).decode()
    modifiedMessage = message.upper()
    connectionSocket.send(modifiedMessage.encode())
    connectionSocket.close()
