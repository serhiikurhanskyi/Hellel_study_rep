# Задача_1
from random import random
a = int(random() * 100)
b = int(random() * 100)
if a % 2 and b % 2 or a % 2 == 0 and b % 2 == 0:
    a += 1
print(a, b)
if a % 2:
    print(a)
else:
    print(b)

# Задача_2
print('Введите три числа: ')
a = int(input())
b = int(input())
c = int(input())
if b < a < c or c < a < b:
    print('Среднее:', a)
elif a < b < c or c < b < a:
    print('Среднее:', b)
else:
    print('Среднее:', c)


# Задача_3
from math import sqrt
x = float(input("x="))
y = float(input("y="))
r = float(input("r="))
h = sqrt(x ** 2 + y ** 2)
print("Расстояние до точки от начала координат равно %.2f" % h)
if h > r:
    print("точка находится за пределами круга")
else:
    print("точка принадлежит кругу")

# Задача_4
from random import random
x = int(random() * 100)
if x > 0:
    y = 2 * x - 10
elif x == 0:
    y = 0
else:
    y = 2 * abs(x) - 1
print(y)

# Задача_5
print('Введите три числа: ')
a = int(input())
b = int(input())
c = int(input())
if a > b > c:
    print('большее:', a)
elif b > a > c:
    print('большее:', b)
else:
    print('большее:', c)

# Задача_6
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if a + b <= c or a + c <= b or b + c <= a:
    print("Треугольник не существует")
elif a != b and a != c and b != c:
    print("Разносторонний")
elif a == b == c:
    print("Равносторонний")
else:
    print("Равнобедренный")

# Задача_7
x = int(input("x="))
y = int(input("y="))
if x > 0 and y > 0:
    print('Первая четверть')
elif x < 0 < y:
    print('Вторая четверть')
elif x < 0 and y < 0:
    print('Третья четверть')
elif x > 0 > y:
    print('Четвертая четрверть')

# Задача_8
a = int(input())
b = int(input())
if a % b == 0:
    print("%d делится на %d" % (a, b))
else:
    print("%d не делится на %d" % (a, b))
    print("Остаток: %d" % (a % b))
print("Частное: %d" % (a//b))

# Задача_9
import math
print("Введите коэффициенты для уравнения")
print("ax^2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
discr = b ** 2 - 4 * a * c
print("Дискриминант D = %.2f" % discr)
if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("Корней нет")
