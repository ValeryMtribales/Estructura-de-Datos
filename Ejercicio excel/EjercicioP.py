import pandas as pd

directorio = pd.read_csv('Ejercicio excel/Directorio.csv')
print(directorio.head()) 
print(directorio.dtypes) 
directorio['Número NIT'] = directorio ['Número NIT'].str.replace(',','')
print(directorio.head()) 
print(directorio.dtypes)
directorio['Número NIT'] = directorio ['Número NIT'].astype(int)
print(directorio.head()) 
print(directorio.dtypes)

print(directorio.columns)
print(directorio['Número NIT'])
