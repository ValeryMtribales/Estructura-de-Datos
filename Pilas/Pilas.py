class Pila:
    def __init__(self):
        self.pila = []  

    def push(self, elemento:str): 
        self.pila.append(elemento)
        print("Elemento agregado a la pila.")

    def pop(self): 
        if self.pila:
            print("Elemento eliminado:", self.pila.pop())
        else:
            print("Error: La pila está vacía.")

    def peek(self): 
        if self.pila:
            print("Elemento en la cima:", self.pila[-1])
        else:
            print("Error: La pila está vacía.")

    def is_empty(self): 
        if not self.pila:
            print("La pila está vacía.")
        else:
            print("La pila NO está vacía.")


# Creación de una instancia de la clase Pila
pila = Pila()

# Menú interactivo para manejar la pila
while True:
    print("\n------ Menú de Pila ------")
    print("1. Insertar elemento (push)")
    print("2. Eliminar elemento (pop)")
    print("3. Ver elemento superior (peek)")
    print("4. Verificar si la pila está vacía (isEmpty)")
    print("5. Salir")
    

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        elemento = input("Ingrese el elemento a agregar: ")
        pila.push(elemento)
    elif opcion == "2":
        pila.pop()
    elif opcion == "3":
        pila.peek()
    elif opcion == "4":
        pila.is_empty()
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida, intente de nuevo.")