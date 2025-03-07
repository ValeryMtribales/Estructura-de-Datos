temperatura=[]
for n in range (0,5):
 t=int(input("Registre la temperatura")) 
 temperatura.append(t)

promedio= sum(temperatura)/len(temperatura) 

print ("La temperatura promedio es : ", promedio)
if promedio < 20: 
  print ("Necesita una revisión")
elif 20>= promedio <= 30:
    print("La temperaura esta bien") 
else: 
  print ("Se necesita una revisión de los conducto del aire")  