from math import prod, pow

def exchange_sort(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for col in range(cols):
        for i in range(rows - 1):
            for j in range(rows - i - 1):
                if matrix[j][col] < matrix[j + 1][col]:
                    matrix[j][col], matrix[j + 1][col] = matrix[j + 1][col], matrix[j][col]
    return matrix

def custom_suma(x):
    n = 0
    for i in x:
        n += i
    return n

def calculate_fi(matrix):
    fi_values = []
    for i in range(len(matrix)):
        row = matrix[i]
        geometric_values = [
            row[j] for j in range(i + 1, len(row)) if row[j] > 0
        ]
        if geometric_values:
            product = prod(geometric_values)
            n = len(geometric_values)
            fi_values.append(pow(product, 1 / n))
        else:
            fi_values.append(0)
    return fi_values

def calculate_F(fi_values):
    return custom_suma(fi_values)

matrix = [
    [0, 2, -2, 89, 21],
    [-1, -4, 36, 41, 71],
    [56, 93, 51, -2, -51],
    [1, 3, -8, 0, 9],
    [23, 41, 5, 8, -2]
]

print("Початкова матриця:")
for row in matrix:
    print(row)

sorted_matrix = exchange_sort(matrix)

print("\nВідсортована матриця:")
for row in sorted_matrix:
    print(row)

fi_values = calculate_fi(sorted_matrix)
print("\nЗначення fi(aij) для кожного рядка:")
print(fi_values)

F_value = calculate_F(fi_values)
print("\nЗначення F(fi(aij)):")
print(F_value)
