def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]  # Intercambiar elementos
    return fila

# Definir la matriz
matriz = [
    [9, 2, 5],
    [3, 7, 1],
    [8, 6, 4]
]

# Mostrar matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Fila a ordenar (por ejemplo, la segunda fila - índice 1)
fila_a_ordenar = 1

# Ordenar la fila específica
matriz[fila_a_ordenar] = bubble_sort(matriz[fila_a_ordenar])

# Mostrar matriz con la fila ordenada
print("\nMatriz después de ordenar la fila seleccionada:")
for fila in matriz:
    print(fila)