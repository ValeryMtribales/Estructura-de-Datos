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

for index, row in directorio.iterrows():
    directorio = Directorio(
        nombre=row['nombre'],
        nit=row['nit'],
        sede=row['sede'],
        municipio=row['municipio']
    )
    print(directorio) 