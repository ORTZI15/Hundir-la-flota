# Hundir la Flota

## Descripción

Este proyecto consiste en desarrollar el juego Hundir la Flota utilizando Python. El jugador se enfrenta a la máquina, que coloca sus barcos de forma aleatoria y dispara también a posiciones aleatorias.

## Archivos del proyecto

- `main.py`: inicia y controla la partida.
- `variables.py`: contiene las variables y los símbolos utilizados en el juego.
- `funciones.py`: contiene las funciones necesarias para crear los tableros, colocar los barcos y gestionar los disparos y los turnos.

## Requisitos

- Python 3.
- NumPy.



## Reglas del juego

- Cada participante dispone de un tablero de 10 filas y 10 columnas.
- Cada flota está formada por seis barcos.
- Los barcos se colocan aleatoriamente al comenzar la partida.
- El jugador introduce las coordenadas para disparar.
- Si acierta, puede seguir disparando.
- Si falla, el turno pasa al otro participante.
- La máquina selecciona sus disparos aleatoriamente.
- La partida termina cuando uno de los participantes hunde todos los barcos del rival.