matrix = [[1, 2, 3,4], [4, 5, 6,4], [7, 8, 9,4]]

# Number of rows
num_rows = len(matrix)

# Number of columns (assuming all rows have the same length)
num_cols = len(matrix[0])

print("Number of rows:", num_rows)

print("Number of columns:", num_cols)

def suma_diagonal_secundaria(matriz):
    """Calcula la suma de la diagonal secundaria de una matriz.

    Args:
        matriz: Una lista de listas representando una matriz cuadrada.

    Returns:
        La suma de los elementos de la diagonal secundaria.
    """

    n = len(matriz)
    suma = 0
    for i in range(n):
        suma += matriz[i][n - i - 1]
    return suma

# Ejemplo de uso:
matriz =    [[1, 2, 3],
            [4, 5, 6],
            [6, 8, 9]]

resultado = suma_diagonal_secundaria(matriz)
print("Suma de la diagonal secundaria:", resultado)

def solveMeFirst(a,b):
	# Hint: Type return a+b below
    return a+b

num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1,num2)
print(res)

