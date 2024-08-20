from socket import *

serverName = 'localhost'
serverPort = 1500
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
message = input('Escriba una frase en minúsculas:')
clientSocket.send(message.encode())

modifiedMessage = clientSocket.recv(2048)
print(modifiedMessage.decode())

clientSocket.close()