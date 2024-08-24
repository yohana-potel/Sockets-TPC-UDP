from socket import *

nombreServidor = 'localhost'
puerto = 1500

try:
    SocketCliente = socket(AF_INET, SOCK_STREAM)
   
    print(f"Conectando a {nombreServidor} en el puerto {puerto}...")
    SocketCliente.connect((nombreServidor,puerto))

    mensaje = input('Escriba una frase en minúsculas:' )
    if not mensaje.islower():
        raise ValueError("El mensaje debe estar en minúsculas.")
    
    SocketCliente.send(mensaje.encode())

    mensajeModificado = SocketCliente.recv(2048)

    print(mensajeModificado.decode())


except OSError as conexionAlServidor:
    print(f"Error de conexión en el servidor: {conexionAlServidor}")

except ValueError as usuario:
    print(f"Error en lo que ingreso el usuario: {usuario}")

finally:

    SocketCliente.close()
    print("Conexión finalizada. ")