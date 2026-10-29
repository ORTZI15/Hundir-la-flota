
import funciones as f  # Importamos las funciones del juego
import variables as v  # Importamos la configuración


# Creamos los tableros de ambos participantes
tablero_jugador = f.crear_tablero()
tablero_disparos_jugador = f.crear_tablero()

tablero_maquina = f.crear_tablero()
tablero_disparos_maquina = f.crear_tablero()


# Colocamos los barcos
f.colocar_barcos(tablero_jugador)
f.colocar_barcos(tablero_maquina)


# Iniciamos la partida
while f.quedan_barcos(tablero_jugador) and f.quedan_barcos(tablero_maquina):

    # Mostramos los tableros visibles para el jugador
    print("\nTUS BARCOS")
    print(tablero_jugador)

    print("\nTUS DISPAROS")
    print(tablero_disparos_jugador)

    # Turno del jugador
    f.turno_jugador(tablero_maquina, tablero_disparos_jugador)

    # Comprobamos si el jugador ha ganado
    if not f.quedan_barcos(tablero_maquina):
        break

    # Turno de la máquina
    f.turno_maquina(tablero_jugador, tablero_disparos_maquina)


# Mostramos el resultado final
if not f.quedan_barcos(tablero_maquina):
    print("¡Enhorabuena! Has hundido toda la flota.")
else:
    print("La máquina ha hundido toda tu flota.")
