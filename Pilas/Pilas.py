class NodoPila:
    def __init__(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

class PilaNodos:
    def __init__(self):
        self.cima = None

    def push(self, valor):
        nuevo = NodoPila(valor)
        nuevo.siguiente = self.cima
        self.cima = nuevo

    def pop(self):
        if self.cima is None:
            print("La pila está vacía.")
            return None
        valor = self.cima.valor
        self.cima = self.cima.siguiente
        print(f"Elemento eliminado: {valor}")
        return valor

    def top(self):
        if self.cima is None:
            print("La pila está vacía.")
            return None
        print(f"Elemento superior: {self.cima.valor}")
        return self.cima.valor

    def vacia(self):
        if self.cima is None:
            print("La pila está vacía.")
            return True
        else:
            print("La pila NO está vacía.")
            return False


# Creación de una instancia de la clase Pila
pila = PilaNodos()

# Menú interactivo para manejar la pila
while True:
    print("\n------ Menú de Pila ------")
    print("1. Insertar elemento (push)")
    print("2. Eliminar elemento (pop)")
    print("3. Ver elemento superior (top)")
    print("4. Verificar si la pila está vacía (isEmpty)")
    print("5. Salir")
    

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        elemento = input("Ingrese el elemento a agregar: ")
        pila.push(elemento)
    elif opcion == "2":
        pila.pop()
    elif opcion == "3":
        pila.top()
    elif opcion == "4":
        pila.vacia()
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida, intente de nuevo.")