# Esquiva al Dragón

Proyecto integrador de primer nivel · Lógica de Programación · UIDE · Paralelo C

Juego en tiempo real para dos jugadores simultáneos con modo local y modo multijugador cliente-servidor en red LAN mediante sockets TCP, donde ambos esquivan los ataques progresivos de un dragón en una arena compartida.

## Integrantes

- Matías Tirira
- Elkin Guaman
- José Freire

## Cómo ejecutarlo

Requiere Python 3.12 Desde la carpeta del repositorio:
Requiere Pygame 2.6.1 Desde la carpeta del repositorio
```bash
python game.py          # Menú principal (Jugar en modo local, Jugar en modo LAN, Salir)

```

## Estructura del repositorio

| Archivo | Qué hace | Estado |
|---|---|---|
| `game.py` | [Menú que se repite hasta «Salir» (parte de DF1). Validación de la jugada (DF2) y fin de la partida (DF3). Personalización del personaje. Configucación de sonido] | [Terminado] 
| `escenas.py` | [Variables para escenas que pueden ser editadas a futuro] | [Terminado]
| `sprites/` | [Carpeta con texturas usadas ] | [Terminado]
| `music/` | [Carpeta con musica usada ] | [Terminado]
| `sounds/` | [Carpeta con sonidos usados ] | [Pendiente]
| `server.py` | [Comentario con lo que hará el servidor (Jugador 1)] | [Pendiente]
| `client.py` | [Comentario con lo que hará el cliente (Jugador 2)] | [Pendiente] |
| `diseno/` | Diagramas `.rap` de la Fase 2 | [Subido] |

## Del diseño al código

| Diagrama de la Fase 2 | Archivo y líneas | Qué cambió al traducirlo |
| DF1 Partida completa (solo el menú) | `game.py`, líneas 211-239 | |
| DF2 Validación de la jugada | `game.py`, líneas 240–314 | |
| DF3 Fin de la partida | `game.py`, líneas 245–251 ||

## Video explicativo

[Enlace al video] (máximo 5 minutos: el menú, la validación con una jugada inválida, el fin de la partida y cómo traducimos un diagrama a código).

## Licencia

Este proyecto se distribuye bajo la licencia MIT. El texto completo está en el archivo `LICENSE`.

## Declaración de autoría

Declaramos que el código de este repositorio fue escrito por los integrantes del equipo, salvo los recursos citados en la sección «Créditos».

## Créditos

| Recurso (código, librería, imagen…) | Autor o fuente | Dónde se usa | Licencia |
| Librería estándar de Python (`socket`, `time`, `sys`) | Python Software Foundation | `juego.py`, `game_logic.py`, `server.py`, `client.py` | PSF License |
| Topología de red LAN y direccionamiento VLSM | Diseño propio (Proyecto Integrador Redes - Fase 2) | Documentación de arquitectura `server.py` y `client.py` | MIT |

### Uso de IA

| Herramienta | Para qué la usamos | Qué revisamos o cambiaron nosotros |
| ChatGPT (OpenAI) | Orientación para la organización del repositorio, documentación y comprensión de conceptos de programación. | Revisamos las sugerencias y adaptamos la documentación a los requisitos de la Fase 3 y al funcionamiento del proyecto. |


## Cómo ejecutar
Requiere Python 3.12.
1. py -3.12 -m venv venv
2. .\venv\Scripts\Activate.ps1
3. pip install -r requirements.txt
4. python game.py