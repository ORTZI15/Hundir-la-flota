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


def disparar(tablero, fila, columna):  # Recibe el tablero y las coordenadas del disparo

    if tablero[fila, columna] == v.tocado or tablero[fila, columna] == v.fallo:  # Comprobamos si ya se disparó aquí
        return "Ya has disparado en esta casilla."  # Avisamos de que el disparo está repetido

    if tablero[fila, columna] == v.barco:  # Comprobamos si hay un barco en la casilla
        tablero[fila, columna] = v.tocado  # Marcamos la casilla como tocada
        return "¡Tocado!"  # Devolvemos el resultado del disparo

    else:  # Si no hay barco, la casilla contiene agua
        tablero[fila, columna] = v.fallo  # Marcamos la casilla como fallo
        return "Agua."  # Devolvemos el resultado del disparo
