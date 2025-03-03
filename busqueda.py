def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return i, j  # Retorna la posición (fila, columna)
    return None  # Retorna None si el valor no se encuentra

# Definir la matriz
matriz = [
    [5, 8, 3],
    [2, 6, 7],
    [1, 4, 9]
]

# Valor a buscar
valor = int(input("Ingrese el número a buscar: "))

# Llamar la función
resultado = buscar_valor(matriz, valor)

# Mostrar el resultado
if resultado:
    print(f"El número {valor} se encuentra en la posición: {resultado}")
else:
    print(f"El número {valor} no está en la matriz.")