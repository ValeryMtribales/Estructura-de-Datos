class Empleado:
    def __init__(self, nombre, salario, departamento):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento

    def trabajar(self):
        print(f"{self.nombre} está trabajando.")

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento, equipo=None):
        super().__init__(nombre, salario, departamento)
        self.equipo = equipo if equipo else []
    
    def trabajar(self):
        print(f"{self.nombre} está supervisando a su equipo.")

class Desarrollador(Empleado):
    def __init__(self, nombre, salario, departamento, lenguajeDeProgramacion):
        super().__init__(nombre, salario, departamento)
        self.lenguajeDeProgramacion = lenguajeDeProgramacion
    
    def trabajar(self):
        print(f"{self.nombre} está escribiendo código en {self.lenguajeDeProgramacion}.")

gerente = Gerente("Ana", 5000, "Administración", ["Luis", "Maria"])
desarrollador = Desarrollador("Javier", 3000, "IT", "Python")

gerente.trabajar()
desarrollador.trabajar()

