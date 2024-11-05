import socket

nombre_servidor = 'localhost'
puerto = 1500
servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor_socket.bind((nombre_servidor, puerto))

print("Servidor UDP listo para recibir pings...")

try:
    while True:
      
        mensaje, direccion_cliente = servidor_socket.recvfrom(1024)
        print(f"Mensaje recibido de {direccion_cliente}: {mensaje.decode()}")

        if mensaje.decode().startswith("PING"):
            respuesta = f"PONG {mensaje.decode()[5:]}"  
        else:
            respuesta = "Mensaje no reconocido"

        servidor_socket.sendto(respuesta.encode(), direccion_cliente)
        print(f"Respuesta enviada a {direccion_cliente}")

except KeyboardInterrupt:
    print("\nServidor cerrado por el usuario.")

finally:
    servidor_socket.close()
    print("Socket cerrado.")
