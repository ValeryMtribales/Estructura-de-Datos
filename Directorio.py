class Persona:
    def __init__(self, nombre: str, telefono: int):
        self.nombre: str = nombre
        self.telefono: int = telefono

def calcular_hash(nombre: str, tamaño: int) -> int:
    return hash(nombre) % tamaño


tamaño_tabla: int = 10 

tabla_hash = [None] * tamaño_tabla

def agregar_persona(persona: Persona) -> None:
    indice: int = calcular_hash(persona.nombre, tamaño_tabla)
    tabla_hash[indice] = persona
    print(f"Persona '{persona.nombre}' agregada.")

def buscar_persona(nombre: str):
    indice: int = calcular_hash(nombre, tamaño_tabla)
    persona = tabla_hash[indice]
    if persona and persona.nombre == nombre:
        return persona
    return None

def eliminar_persona(nombre: str) -> None:
    indice: int = calcular_hash(nombre, tamaño_tabla)
    if tabla_hash[indice] and tabla_hash[indice].nombre == nombre:
        tabla_hash[indice] = None
        print(f"Persona '{nombre}' eliminada.")

def listar_personas() -> None:
    print("\nPersonas registradas:")
    for persona in tabla_hash:
        if persona:
            print(f"{persona.nombre} - {persona.telefono}")
    print("-" * 30)


agregar_persona(Persona("Valery", 3502077181))
agregar_persona(Persona("Ana", 987654321))
agregar_persona(Persona("Carlos", 123456789))
listar_personas()


persona = buscar_persona("Valery")
if persona:
    print(f"\nEncontrado: {persona.nombre} - {persona.telefono}")
else:
    print("\nPersona no encontrada.")
    

eliminar_persona("Carlos")
listar_personas()