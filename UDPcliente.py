import socket
import time

nombre_servidor = 'localhost'
puerto = 1500
timeout = 1.0  

cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cliente_socket.settimeout(timeout)

# Variables para estadísticas
paquetes_enviados = 0
paquetes_recibidos = 0
rtt_tiempos = []  

for i in range(1, 11):
    mensaje = f"PING {i}"
    try:

        tiempo_envio = time.time()
        cliente_socket.sendto(mensaje.encode(), (nombre_servidor, puerto))
        print(f"Enviado: {mensaje}")
        paquetes_enviados += 1

        respuesta, _ = cliente_socket.recvfrom(1024)
        tiempo_recepcion = time.time()

        # Calcular el RTT
        rtt = (tiempo_recepcion - tiempo_envio) * 1000 
        rtt_tiempos.append(rtt)
        paquetes_recibidos += 1
        print(f"Respuesta recibida: {respuesta.decode()} - RTT: {rtt:.2f} ms")

    except socket.timeout:
        print(f"Tiempo de espera agotado para {mensaje} (paquete perdido)")

cliente_socket.close()

# Calcular estadísticas
if rtt_tiempos:
    rtt_minimo = min(rtt_tiempos)
    rtt_maximo = max(rtt_tiempos)
    rtt_promedio = sum(rtt_tiempos) / len(rtt_tiempos)
else:
    rtt_minimo = rtt_maximo = rtt_promedio = 0

# Mostrar estadísticas
print("\nEstadísticas de ping:")
print(f"Paquetes: enviados = {paquetes_enviados}, recibidos = {paquetes_recibidos}, perdidos = {paquetes_enviados - paquetes_recibidos} ({(paquetes_enviados - paquetes_recibidos) / paquetes_enviados * 100:.2f}% perdidos)")
print("Tiempos aproximados de ida y vuelta en milisegundos:")
print(f"    Mínimo = {rtt_minimo:.2f} ms, Máximo = {rtt_maximo:.2f} ms, Media = {rtt_promedio:.2f} ms")
