# client.py - JUGADOR 2 (hace de CLIENTE)

# Idea general de la conexion LAN:
#   - El jugador 2 se une a una partida creada por el jugador 1.
#   - Necesita el CODIGO que muestra el servidor en su pantalla.
#   - Las dos computadoras deben estar en la misma red (mismo Wi-Fi o router).
#   - Se comunican por sockets TCP usando el mismo puerto que el servidor (5000).

# 1. Datos de la conexion
# - Definir el mismo puerto que usa el servidor (5000).

# 2. Pedir el codigo al jugador 2
# - En el menu del juego, el jugador 2 escribe el codigo que le dio
#   el jugador 1.
# - Verificar que el codigo tenga el formato correcto. Si no, mostrar
#   un mensaje de "codigo invalido".

# 3. Convertir el codigo en la direccion del servidor
# - Hacer el proceso inverso al del servidor: transformar el codigo
#   de vuelta a la direccion IP del jugador 1.

# 4. Conectarse al servidor
# - Crear el socket del cliente.
# - Intentar conectarse a la IP y al puerto del servidor, con un
#   tiempo maximo de espera.
# - Si se conecta, avisar que la partida puede comenzar.
# - Si falla (servidor apagado, otra red, firewall), mostrar un
#   mensaje de error y volver al menu.

# 5. Enviar mensajes al servidor
# - Enviar las acciones del jugador 2 (movimientos, ataque elegido,
#   etc.) en el mismo formato simple que usa el servidor (JSON).
# - Enviar solo cuando el jugador haga algo.

# 6. Recibir mensajes del servidor
# - Revisar en cada vuelta del juego si el servidor envio el estado
#   actualizado (posiciones, turno, vida, fin de partida).
# - Hacerlo sin bloquear la pantalla.
# - Actualizar lo que se dibuja en pantalla con esa informacion.

# 7. Manejo de errores y desconexion
# - Si el servidor se cierra o se pierde la red, detectarlo,
#   mostrar un mensaje y volver al menu.

# 8. Cerrar la conexion
# - Al terminar la partida o salir del juego, cerrar el socket.
