class Animal:
    def __init__(self, nombre, edad, tipo):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo
        self.siguiente = None

    def __str__(self):
        return f"{self.nombre} ({self.tipo}), Edad: {self.edad}"


class ListaEnlazadaAnimales:
    def __init__(self):
        self.cabeza = None

    def agregar_animal(self, nombre, edad, tipo):
        if self.existe_animal(nombre, tipo):
            print(f"El animal {nombre} ({tipo}) ya está registrado.")
            return
        
        nuevo_animal = Animal(nombre, edad, tipo)
        if not self.cabeza:
            self.cabeza = nuevo_animal
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_animal

    def existe_animal(self, nombre, tipo):
        actual = self.cabeza
        while actual:
            if actual.nombre == nombre and actual.tipo == tipo:
                return True
            actual = actual.siguiente
        return False

    def mostrar_animales_repetido(self):
        actual = self.cabeza
        while actual:
            print(actual)
            actual = actual.siguiente

    def mostrar_animales_recursivo(self, nodo=None):
        if nodo is None:
            nodo = self.cabeza
        
        if nodo:
            print(nodo)
            self.mostrar_animales_recursivo(nodo.siguiente)

zoologico = ListaEnlazadaAnimales()
zoologico.agregar_animal("Águila", 5, "Ave")
zoologico.agregar_animal("Pantera", 7, "Felino")
zoologico.agregar_animal("Vaca", 4, "Mamífero")
zoologico.agregar_animal("Águila", 5, "Ave")  # Intento de duplicado

print("\nAnimales (Iterativo):")
zoologico.mostrar_animales_repetido()

print("\nAnimales (Recursivo):")
zoologico.mostrar_animales_recursivo()
