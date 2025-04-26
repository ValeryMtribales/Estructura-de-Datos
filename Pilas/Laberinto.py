def resolver_laberinto(laberinto, inicio, salida):
    filas, columnas = len(laberinto), len(laberinto[0])
    pila = [inicio]  # Guardamos el camino
    visitado = set()

    while pila:
        x, y = pila[-1]  # Última posición en la pila

        if (x, y) == salida:
            return pila  # Ruta encontrada

        visitado.add((x, y))

        # Movimientos posibles (derecha, abajo, izquierda, arriba)
        movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        movido = False

        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy

            if 0 <= nx < filas and 0 <= ny < columnas and laberinto[nx][ny] != 'X' and (nx, ny) not in visitado:
                pila.append((nx, ny))
                movido = True
                break  # Solo tomamos un movimiento válido

        if not movido:  # Retrocedemos si no hay opciones
            pila.pop()

    return None  # No hay solución

# Laberinto de prueba (S = inicio, E = salida, X = obstáculo, O = libre)
laberinto = [
    ['S', 'O', 'X', 'X', 'O'],
    ['X', 'O', 'O', 'X', 'O'],
    ['X', 'X', 'O', 'O', 'X'],
    ['O', 'O', 'X', 'O', 'E'],
    ['X', 'O', 'O', 'O', 'X']
]

inicio = (0, 0)
salida = (3, 4)

solucion = resolver_laberinto(laberinto, inicio, salida)
print("Ruta encontrada:" if solucion else "No hay solución", solucion)
