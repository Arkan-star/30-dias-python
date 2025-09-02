# Crear lista

numeros = [1,2,3,4,5]
print ("Lista original =", numeros)

# Indexacion (acceder a elementos por posicion)

print ("Primer elemento:", numeros [0]) 
print ("Ultimo elemento:", numeros [-1]) # -1 es el ultimo

# Slicing (es tomar una parte de la lista)

print ("Primeros 3:", numeros [:3]) # Va desde el índice inicial (incluido) hasta el índice final (excluido)
print ("Del 2 al 4:", numeros [2:5])

# Insertar

numeros.append (6) # Mete 6 al final de la lista
print ("Agregando un 6:", numeros)

numeros.insert (2, 99) # Mete 99 en la posicion que quiera
print ("Insertando 99 en posicion 2:", numeros)

# Eliminar

numeros.remove (99)
print ("Eliminando 99:", numeros)

eliminado = numeros.pop() # Quita el ultimo
print ("Hicimos pop():", eliminado, "Lista ahora:", numeros)

# Ejercicios

# 1) Dada una lista de números, devolver la lista en orden inverso
lista = [1,2,3,4]

print ("Lista Original:", lista, "Lista inversa:", lista [::-1])


# 2) Dada una lista, devolver el número mayor

print ("El numero mayor de la lista es:", max(lista))


# 3) Dada una lista, devolver solo los elementos pares

pares = []
for num in lista:
    if num % 2 == 0:
        pares.append (num)
print ("Los numeros pares de la lista son:", pares)

# 4) Dada una lista de strings, devolver la más larga

lista_super = ["jamon", "leche", "pollo", "agua", "azucar"]
mas_larga = lista_super [0] # Palabra vacia

for palabra in lista_super: # recorro cada palabra de la lista
    if len(palabra) > len (mas_larga): # comparo la longitud con la más larga hasta ahora
        mas_larga = palabra # si es más larga, la guardo

print ("La palabra mas larga es:", mas_larga)

# 5) Dada una lista de números, devolver la suma sin usar sum()

total = 0

for num in lista:
    total += num # Suma cada numero
print ("Total:", total)