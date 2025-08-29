x = 1

if x > 0:
    print ("Positivo") #Con el if lo que pasa es que si x es mayor a 0, es positivo
elif x == 0:
    print ("Cero") #Sino si es igual a 0, entonces es cero, sino es Negativo
else:
    print ("Negativo")
    
    
for i in range (7):
    print(i) #Imprime siete numeros
    
    
n = 0
while n < 5:
    print(n)
    n +=1
    
squares = [i**2 for i in range(5)]
print(squares)
