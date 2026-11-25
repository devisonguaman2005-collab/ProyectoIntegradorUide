# server.py - JUGADOR 1 (hace de SERVIDOR)

# Idea general de la conexion LAN:
#   - Las dos computadoras deben estar en la misma red (mismo Wi-Fi o router).
#   - El jugador 1 crea la partida y su computadora actua como servidor.
#   - El jugador 2 se une y su computadora actua como cliente.
#   - Se comunican por sockets TCP usando un puerto acordado (5000).

# 1. Datos de la conexion
# - Definir el puerto en el que va a escuchar el servidor (5000).
# - Averiguar la direccion IP local de esta computadora en la red.

# 2. Generar el codigo de la partida
# - Convertir la IP local en un codigo corto (por ejemplo, 8 caracteres).
# - Este codigo se muestra en pantalla al jugador 1.
# - El jugador 1 se lo dice o se lo escribe al jugador 2 para que se una.

# 3. Crear el servidor y esperar al jugador 2
# - Crear el socket del servidor.
# - Asociarlo al puerto y ponerlo a escuchar conexiones.
# - Esperar (sin congelar el juego) hasta que el jugador 2 se conecte.
# - Cuando se conecte, guardar esa conexion y avisar que la partida
#   puede comenzar.

# 4. Enviar mensajes al jugador 2
# - Preparar la informacion del juego (posiciones, turno, ataques,
#   vida, etc.) en un formato simple, como un diccionario/JSON.
# - Enviarla al jugador 2 cada vez que cambie el estado del juego.

# 5. Recibir mensajes del jugador 2
# - Revisar en cada vuelta del juego si el jugador 2 envio algo
#   (movimientos, ataque elegido, etc.) sin bloquear la pantalla.
# - Si llego algo, convertirlo de nuevo a datos y aplicarlo al juego.
# - Como el servidor es quien manda, tambien valida que lo recibido
#   sea correcto antes de aplicarlo.

# 6. Manejo de errores y desconexion
# - Si el jugador 2 se desconecta o se pierde la red, detectarlo y
#   mostrar un mensaje en pantalla.
# - Volver al menu o permitir esperar a otro jugador.

# 7. Cerrar la conexion
# - Al terminar la partida o salir del juego, cerrar la conexion
#   del jugador 2 y el socket del servidor para liberar el puerto.
