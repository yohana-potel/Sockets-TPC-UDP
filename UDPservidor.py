import socket

# Configuración del servidor
nombre_servidor = 'localhost'
puerto = 1500

# Crear el socket UDP
servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor_socket.bind((nombre_servidor, puerto))

print("Servidor UDP listo para recibir pings...")

while True:
    # Recibir mensaje del cliente
    mensaje, direccion_cliente = servidor_socket.recvfrom(1024)
    print(f"Mensaje recibido de {direccion_cliente}: {mensaje.decode()}")

    # Enviar respuesta al cliente
    respuesta = f"Respuesta: {mensaje.decode()}"
    servidor_socket.sendto(respuesta.encode(), direccion_cliente)
    print(f"Respuesta enviada a {direccion_cliente}")
