def number(n):
    if n >= 0:
        return len(str(n))
    else:
        return 'Число менше 0'


def create_m(Розміри):
    matrix = []
    for i in range(Розміри):
        line = [Розміри] * Розміри
        matrix.append(line)
    return matrix


def print_m(Матриця):
    for line in Матриця:
        for element in line:
            print(element, end='')
        print()

k = 0
while k == 0:
    try:
        n = int(input("Введіть ціле число: "))
        break
    except ValueError:
        print("Введіть число!!!")
num = number(n)
print("Кількість цифр у числі:", num)

matrix = create_m(num)
print("Матриця:")
print_m(matrix)