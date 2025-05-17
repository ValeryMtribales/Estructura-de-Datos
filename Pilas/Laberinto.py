# 0 = libre
# 1 = muro
# 2 = salida
# 3 = ruta recorrida
# 4 = ruta obsoleta

laberinto = [
    [1, 2, 1, 1, 1],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 1, 0, 0]
]

def mostrar(laberinto):
    for fila in laberinto:
        for celda in fila:
            if celda == 3:
                print("X", end=" ")  
            elif celda == 4:
                print(".", end=" ")  
            elif celda == 1:
                print("#", end=" ")  
            elif celda == 2:
                print("E", end=" ")  
            else:
                print("0", end=" ") 
        print()  # Salto de línea después de cada fila
    print()  

def es_valido(i:int, j:int):
    # Verifica si una posición (i, j) está dentro de los límites del tablero
    return 0 <= i < len(laberinto) and 0 <= j < len(laberinto[0]) 

def buscar_con_pila(laberinto, inicio_i, inicio_j):
    # Realiza una búsqueda de la salida utilizando una pila (búsqueda en profundidad)
    
    pila = [(inicio_i, inicio_j)]  
    movimientos = [(-1, 0), (0, -1), (1, 0), (0, 1)]  

    while pila:
        i, j = pila.pop()  # Obtiene la última posición agregada a la pila

        # Si la posición es inválida o ya ha sido visitada (muro, ruta o ruta obsoleta), se omite
        if not es_valido(i, j) or laberinto[i][j] in (1, 3, 4):  
            continue  

        if laberinto[i][j] == 2:  
            print("¡Encontró la salida!")
            mostrar(laberinto)
            return True

        # Marca la celda actual como parte de la ruta recorrida
        laberinto[i][j] = 3  

        # Agrega las posiciones adyacentes a la pila en las cuatro direcciones posibles
        for di, dj in movimientos:
            pila.append((i + di, j + dj))

    # Si no se encontró la salida, convierte todas las rutas recorridas en rutas antiguas
    for i in range(len(laberinto)):
        for j in range(len(laberinto[i])):
            if laberinto[i][j] == 3:
                laberinto[i][j] = 4  

    print("No se encontró la salida.")
    return False

buscar_con_pila(laberinto, 4, 0)
print(laberinto)
