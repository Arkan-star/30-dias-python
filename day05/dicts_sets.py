# ----- SETS (conjuntos) -----

# Un set es como una lista, pero no permite duplicados y no tiene orden.

numeros = [1, 2, 2, 3, 4, 4, 5]
print ("Lista original:", numeros)

# Convertir a set elimina duplicados

numeros_unicos = set (numeros)
print ("Set sin duplicados:", numeros_unicos)

# ----- DICTS (diccinarios) -----
# Son pares clave: valor

persona = {
    "nombre": "Juan",
    "edad": 25,
    "profecion": "programador"
}

print ("Nombre:", persona["nombre"])
print ("Edad:", persona["edad"])

# Agregar una nueva clave

persona["pais"] = "Argentina"
print ("Diccionario actualizado:", persona)


# ------ MINI-PROBLEMA: frecuencia de palabras -----
texto = "hola hola mundo mundo mundo python python"
palabras = texto.lower().split() #separa en lista por espacios y lower convierte todo en minuscula
frecuencia = {} #diccionario vacio

for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1
 
print ("Frecuencia de palabras:", frecuencia)