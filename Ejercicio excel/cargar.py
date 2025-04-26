import pandas as pd

hospitales = pd.read_csv('Ejercicio excel/Directorio.csv')
print(hospitales.head()) 
print(hospitales.dtypes) 
hospitales['Número NIT'] = hospitales ['Número NIT'].str.replace(',','')
print(hospitales.head()) 
print(hospitales.dtypes)
hospitales['Número NIT'] = hospitales ['Número NIT'].astype(int)
print(hospitales.head()) 
print(hospitales.dtypes)
print(hospitales.columns)