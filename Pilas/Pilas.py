class Pila:
    def __init__(self, max_tam=8):
        self.max = max_tam
        self.tope = 0
        self.pila = [None] * self.max  

    def pila_vacia(self):
        return self.tope == 0

    def pila_llena(self):
        return self.tope == self.max

    def push(self, dato):
        if self.pila_llena():
            print("Error: La pila está llena, no se puede agregar más elementos.")
        else:
            self.pila[self.tope] = dato
            self.tope += 1
            print(f"Elemento {dato} agregado a la pila.")

    def pop(self):
        if self.pila_vacia():
            print("Error: La pila está vacía, no hay elementos para quitar.")
        else:
            eliminado = self.pila[self.tope - 1]
            self.pila[self.tope - 1] = None  
            print(f"Elemento {eliminado} eliminado de la pila.")

    def mostrar_elementos(self):
        if self.pila_vacia():
            print("La pila está vacía.")
        else:
            print("\nElementos actuales en la pila (de arriba hacia abajo):")
            for i in range(self.tope - 1, -1, -1):  
                print(f"Posición {i + 1}: {self.pila[i]}")
            print()  
def menu():
    pila = Pila()
    
    while True:
        print(f"\nPila (Tope = {pila.tope})")
        print("1 - Conocer si la pila está vacía")
        print("2 - Conocer si la pila está llena")
        print("3 - Colocar un elemento a la pila")
        print("4 - Quitar un elemento de la pila")
        print("5 - Mostrar los elementos actuales de la pila")
        print("Cualquier otro número - Salir")

        try:
            seleccion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Entrada no válida, ingrese un número.")
            continue

        if seleccion == 1:
            print("La pila está vacía" if pila.pila_vacia() else "La pila NO está vacía")
        elif seleccion == 2:
            print("La pila está llena" if pila.pila_llena() else "La pila NO está llena")
        elif seleccion == 3:
            try:
                dato = int(input("Ingrese un dato numérico: "))
                pila.push(dato)
            except ValueError:
                print("Entrada no válida, ingrese un número.")
        elif seleccion == 4:
            pila.pop()
        elif seleccion == 5:
            pila.mostrar_elementos()
        else:
            print("Saliste del programa")
            break

# Ejecutar el programa
menu()
