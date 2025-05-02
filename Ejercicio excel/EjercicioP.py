import pandas as pd

class Directorio:
    def __init__(self, nombre:str, nit:int, sede:str, municipio:str):
        self.nombre = nombre 
        self.nit = nit 
        self.sede = sede 
        self.municipio = municipio 

    def __str__(self):
      return f"NOMBRE: {self.nombre}, NIT: {self.nit}, SEDE: {self.sede}, MUNICIPIO: {self.municipio}" 

class Nodo:
    def __init__(self, directorio:Directorio):
        self.directorio = directorio 
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, directorio: Directorio):
        if self.raiz is None:
            self.raiz = Nodo(directorio)
        else:
            self._insertar(self.raiz, directorio)

    def _insertar(self, nodo_actual: Nodo, directorio: Directorio):
        if directorio.nit < nodo_actual.directorio.nit:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(directorio)
            else:
                self._insertar(nodo_actual.izquierda, directorio)
        else:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(directorio)
            else:
                self._insertar(nodo_actual.derecha, directorio)


    def inorden(self):
        self._inorden(self.raiz)

    def _inorden(self, nodo: Nodo):
        if nodo is not None:
            self._inorden(nodo.izquierda)
            print(nodo.directorio)
            self._inorden(nodo.derecha)

def buscar_hospital(arbol: ArbolBinario, nit_buscado: int):
    def _buscar(nodo: Nodo, nit: int):
        if nodo is None:
            return None
        if nit == nodo.directorio.nit:
            return nodo.directorio
        elif nit < nodo.directorio.nit:
            return _buscar(nodo.izquierda, nit)
        else:
            return _buscar(nodo.derecha, nit)

    resultado = _buscar(arbol.raiz, nit_buscado)
    if resultado:
        print(f"\nHospital encontrado:\n"
              f"Nombre de la organización: {resultado.nombre}\n"
              f"Nombre de la sede: {resultado.sede}\n"
              f"Municipio: {resultado.municipio}")
    else:
        print("\nHospital no encontrado.")

directorio = pd.read_csv('Ejercicio excel/Directorio.csv')
#print(directorio.head()) 
directorio.rename(columns={
    'Razón Social Organización': 'nombre',
    'Número NIT': 'nit',
    'Nombre Sede': 'sede',
    'Nombre Municipio': 'municipio',
}, inplace=True)

directorio['nit'] = directorio ['nit'].str.replace(',','')
print(directorio.head()) 
print(directorio.dtypes)
directorio['nit'] = directorio ['nit'].astype(int)
print(directorio.head()) 
print(directorio.dtypes)

print(directorio.columns)
print(directorio['nit'])

arbol = ArbolBinario()

for index, row in directorio.iterrows():
    directorio = Directorio(
        nombre=row['nombre'],
        nit=row['nit'],
        sede=row['sede'],
        municipio=row['municipio']
    )
    arbol.insertar(directorio)

print("\nHospitales ordenados por NIT:\n")
arbol.inorden()

nit_buscado = int(input("\nIngrese el NIT del hospital que desea buscar: "))
buscar_hospital(arbol, nit_buscado)
