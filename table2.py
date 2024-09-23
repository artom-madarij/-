## Лабораторна робота з дисципліни "Алгоритмізація та програмування"
## Виконав: Мадярій Артьом Іванович(ІР-14)
## Лабораторна робота №2 (Варіант 12)
import math as m

a = 1
b = 2
h = 0.1
d = 0.001


def function(x):
    suma = 0
    k = 1
    while True:
        mm = ((-1) ** k * m.cos(2 ** k * x) ** 4) / 2 ** (2 * k)
        suma += mm
        if abs(mm) < d:
            break
        k += 1
        return suma


x = a
print("Табулювання функції на проміжку [1, 2] з кроком 0.1:")
print("x\t\t\tfunction(x)\n")
while x <= b:
    print(round(x, 3), '\t\t', round(function(x), 3))
    x += h
