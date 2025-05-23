class NodoPila:
    def _init_(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

class PilaNodos:
    def _init_(self):
        self.cima = None

    def push(self, valor):
        nuevo = NodoPila(valor)
        nuevo.siguiente = self.cima
        self.cima = nuevo

    def pop(self):
        if self.cima == None:
            return None
        valor = self.cima.valor
        self.cima = self.cima.siguiente
        return valor

    def top(self):
        if self.cima == None:
            return None
        return self.cima.valor

    def vacia(self):
        if self.cima == None:
            return True
        else:
            return False


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