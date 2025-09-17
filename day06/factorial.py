def factorial_iterativo(n: int) -> int:
    resultado = 1
    for i in range(1, n+1):  # desde 1 hasta n
        resultado *= i
    return resultado

# Ejemplo:
print(factorial_iterativo(5))  # → 120
