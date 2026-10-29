import numpy as np
import variables as v

def crear_tablero():
    tablero = np.full((v.tamano_tablero,v.tamano_tablero), v.agua)
    return tablero


def colocar_barcos(tablero):  # Recibe el tablero donde colocaremos los barcos

    for longitud in v.barcos:  # Recorremos los barcos de mayor a menor longitud

        colocado = False  # Indica si el barco actual ya se ha colocado

        while not colocado:  # Repetimos el intento hasta encontrar una posición válida

            fila = np.random.randint(0, v.tamano_tablero)  # Elegimos una fila aleatoria
            columna = np.random.randint(0, v.tamano_tablero)  # Elegimos una columna aleatoria
            orientacion = np.random.choice(["horizontal", "vertical"])  # Elegimos orientación

            posiciones = []  # Guardamos las casillas que ocupará el barco

            if orientacion == "horizontal":  # Si el barco va en horizontal

                if columna + longitud > v.tamano_tablero:  # Comprobamos si se sale del tablero
                    continue  # Si se sale, volvemos a intentarlo

                for desplazamiento in range(longitud):  # Recorremos cada casilla del barco
                    posiciones.append((fila, columna + desplazamiento))  # Guardamos su posición

            else:  # Si el barco va en vertical

                if fila + longitud > v.tamano_tablero:  # Comprobamos si se sale del tablero
                    continue  # Si se sale, volvemos a intentarlo

                for desplazamiento in range(longitud):  # Recorremos cada casilla del barco
                    posiciones.append((fila + desplazamiento, columna))  # Guardamos su posición

            libre = True  # Suponemos inicialmente que todas las casillas están libres

            for fila_pos, columna_pos in posiciones:  # Revisamos cada casilla candidata
                if tablero[fila_pos, columna_pos] != v.agua:  # Si ya está ocupada
                    libre = False  # La posición no sirve
                    break  # Dejamos de revisar las demás casillas

            if libre:  # Si todas las casillas están libres
                for fila_pos, columna_pos in posiciones:  # Recorremos las posiciones válidas
                    tablero[fila_pos, columna_pos] = v.barco  # Colocamos el barco en el tablero

                colocado = True  # Terminamos los intentos para este barco

    return tablero  # Devolvemos el tablero con todos los barcos colocados


def disparar(tablero, fila, columna):  # Recibe el tablero y las coordenadas

    # Comprobamos que las coordenadas estén dentro del tablero
    if not (0 <= fila < v.tamano_tablero and 0 <= columna < v.tamano_tablero):
        return "Coordenadas fuera del tablero."

    # Comprobamos si ya se ha disparado en esa casilla
    if tablero[fila, columna] == v.tocado or tablero[fila, columna] == v.fallo:
        return "Ya has disparado en esta casilla."

    # Si hay un barco, lo marcamos como tocado
    if tablero[fila, columna] == v.barco:
        tablero[fila, columna] = v.tocado
        return "¡Tocado!"

    # Si no hay barco, marcamos agua
    else:
        tablero[fila, columna] = v.fallo
        return "Agua."


def quedan_barcos(tablero):  # Recibe el tablero que queremos comprobar

    # Comprobamos si todavía queda alguna casilla con un barco
    return np.any(tablero == v.barco)



def turno_jugador(tablero_maquina, tablero_disparos):  # Recibe los dos tableros necesarios

    # Repetimos el turno mientras el jugador acierte
    while True:

        # Intentamos convertir las coordenadas a números enteros y try para evitar que rompa
        try:
            fila = int(input("Introduce la fila (0-9): "))
            columna = int(input("Introduce la columna (0-9): "))

        except ValueError:  # Si se introduce algo que no es un número válido
            print("Error: debes introducir números enteros.")
            continue  # Volvemos a pedir las coordenadas
        # Ejecutamos el disparo contra el tablero de la máquina
        resultado = disparar(tablero_maquina, fila, columna)
        print(resultado)

        # Si el disparo no es válido, volvemos a pedir coordenadas
        if resultado == "Coordenadas fuera del tablero." or resultado == "Ya has disparado en esta casilla.":
            continue

        # Registramos el resultado en el tablero de disparos del jugador
        if resultado == "¡Tocado!":
            tablero_disparos[fila, columna] = v.tocado
        else:
            tablero_disparos[fila, columna] = v.fallo

        # Si falla, termina el turno del jugador
        if resultado == "Agua.":
            break


def turno_maquina(tablero_jugador, tablero_disparos):  # Recibe los tableros de la partida

    # La máquina sigue jugando mientras acierte
    while True:

        # Elegimos coordenadas aleatorias dentro del tablero
        fila = np.random.randint(0, v.tamano_tablero)
        columna = np.random.randint(0, v.tamano_tablero)

        # Si ya se disparó en esa casilla, elegimos otras coordenadas
        if tablero_disparos[fila, columna] == v.tocado or tablero_disparos[fila, columna] == v.fallo:
            continue

        # Ejecutamos el disparo contra el tablero del jugador
        resultado = disparar(tablero_jugador, fila, columna)
        print("La máquina dispara en:", fila, columna)
        print(resultado)

        # Registramos el resultado en el tablero de disparos de la máquina
        if resultado == "¡Tocado!":
            tablero_disparos[fila, columna] = v.tocado
        else:
            tablero_disparos[fila, columna] = v.fallo

        # Si falla, termina su turno
        if resultado == "Agua.":
            break
