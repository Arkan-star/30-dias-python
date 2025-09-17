
#def saludar (nombre): #defino la funcion
    #print ("Hola, ", nombre)

#saludar("Arkan")


# Parametros

def suma (a, b):
    return a + b

# Valores 

def saludar (nombre="desconocido"):
    return "Hola,", nombre

# Args (lista de valores variables)
def sumar_todos(*args):
    return sum(args)

print (sumar_todos(1,2,3,4))

# Kwargs

def mostrar_info (**kwargs):
    return kwargs

print (mostrar_info(nombre="Arkan", edad=19))