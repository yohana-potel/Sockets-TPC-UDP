from socket import *
"""
"""

serverName = 'localhost'
serverPort = 1500
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Escriba una frase en minúsculas:')
clientSocket.sendto(message.encode(),(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()