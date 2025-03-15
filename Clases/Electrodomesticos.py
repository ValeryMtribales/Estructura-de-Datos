class Electrodomestico:
    def __init__(self, marca, modelo, consumo_energetico):
        self.marca = marca
        self.modelo = modelo
        self.consumo_energetico = consumo_energetico
    
    def encender(self):
        pass

class Lavadora(Electrodomestico):
    def __init__(self, marca, modelo, consumo_energetico, capacidad):
        super().__init__(marca, modelo, consumo_energetico)
        self.capacidad = capacidad
    
    def encender(self):
        return f"La lavadora {self.marca} modelo {self.modelo} ha iniciado el ciclo de lavado."

class Refrigerador(Electrodomestico):
    def __init__(self, marca, modelo, consumo_energetico, tiene_congelador):
        super().__init__(marca, modelo, consumo_energetico)
        self.tiene_congelador = tiene_congelador
    
    def encender(self):
        return f"El refrigerador {self.marca} modelo {self.modelo} está regulando la temperatura."


lavadora = Lavadora("LG", "T31", "500W", 15)
refrigerador = Refrigerador("Samsung", "R45", "700W", True)
print(lavadora.encender())
print(refrigerador.encender())
