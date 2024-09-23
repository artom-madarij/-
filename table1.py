## Лабораторна робота з дисципліни "Алгоритмізація та програмування"
## Виконав: Мадярій Артьом Іванович(ІР-14)
## Лабораторна робота №2 (Варіант 12)
import math as m

a = 0.5
b = 2.0
h = 0.2


def arctan(x):
    return 1 / m.tan(x)


def function(x):
    if x < 1:
        return m.cos(m.sqrt(x ** 3))
    elif 1 <= x <= 1.5:
        return arctan(m.exp(x))
    else:
        return m.sin(m.log(x)) ** 5


x = a
print("Табулювання функції на проміжку [0.5, 2.0] з кроком 0.2:")
print("x\t\t\tfunction(x)\n")
while x <= b:
    print(round(x, 3), '\t\t', round(function(x), 3))
    x += h
