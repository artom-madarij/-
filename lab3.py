def cust_len(l):
    count = 0
    for i in l:
        count += 1
    return count


def number(x):
    if x >= 0:
        return cust_len(str(n))
    else:
        return 'Ваше число менше 0'


def create_matrix(Розміри):
    matrix = []
    for i in range(Розміри):
        line = [Розміри] * Розміри
        matrix.append(line)
    return matrix


def print_matrix(Матриця):
    for line in Матриця:
        for element in line:
            print(element, end='')
        print()


while True:
    try:
        n = int(input("Введіть ціле число: "))
        break
    except ValueError:
        print("Введіть число!!!")
num = number(n)
print("Кількість цифр у числі:", num)

matrix = create_matrix(num)
print("Матриця:")
print_matrix(matrix)
