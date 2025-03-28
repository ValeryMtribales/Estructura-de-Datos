
class Vehiculo:
    def __init__(self, marca: str, combustible: float, tipo: str, color: str = "Desconocido", modelo: int = 0, cilindraje: int = 0, numero_ruedas: int = 4) -> None:
        self.marca = marca
        self.combustible = combustible 
        self.tipo = tipo
        self.encendido = False

    def __str__(self) -> str:
        return f"Tipo: {self.tipo} | Marca: {self.marca} | Combustible: {self.combustible:.2f} gal"

    def encender(self):
        if self.combustible < 1:  # 10% de un tanque de 10 galones
            print(f"Advertencia: La {self.tipo} {self.marca} tiene poco combustible. ¡Ve a la gasolinera!")
        else:
            self.encendido = True
            print(f"El {self.tipo} {self.marca} ha sido encendido.")

    def marchar(self, consumo: float):
        if not self.encendido:
            print(f" {self.tipo} {self.marca} está apagado. ¡Enciéndelo primero!")
            return

        if self.combustible <= 0:
            print(f"El {self.tipo} {self.marca} se ha detenido. ¡No hay combustible!")
            self.encendido = False
            return

        self.combustible -= consumo
        if self.combustible < 0:
            self.combustible = 0

        print(f"El {self.tipo} {self.marca} está en marcha. Combustible restante: {self.combustible:.2f} gal")

        if self.combustible < 1:
            print(f"Advertencia: El {self.tipo} {self.marca} necesita ir a la gasolinera.")
        
        if self.combustible == 0:
            print(f"El {self.tipo} {self.marca} se ha detenido. ¡Sin combustible!")
            self.encendido = False

class Moto(Vehiculo):
    def __init__(self, marca: str, combustible: float):
        super().__init__(marca, combustible, tipo="Moto", numero_ruedas=2)

class Carro(Vehiculo):
    def __init__(self, marca: str, combustible: float):
        super().__init__(marca, combustible, tipo="Carro", numero_ruedas=4)


vehiculo1 = Carro("Chevrolet", 8)
print(vehiculo1)

moto1 = Moto("Honda", 0.5)
print(moto1)

carro1 = Carro("Kia", 2)
print(carro1)

moto1.encender()
moto1.marchar(0.3)
moto1.marchar(0.3)

carro1.encender()
carro1.marchar(1)
carro1.marchar(1)
carro1.marchar(1)
