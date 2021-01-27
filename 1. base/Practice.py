import math
import random

a = 7
P = 4 * a
print("Perimetr: ", P)
S = a * a
print("Ploshad\'", S)
b = 5
S = a * b
print("Ploshad\'", S)
P = (a + b) * 2
print("Perimetr: ", P)
d = 9
Pi = 3.14
S = Pi * d * d / 4
print("Ploshad\' shara", S)
V = a * a *a
print("Ob\'em ", V)
S = 6 * a * a
print("Площадь поверхности куба: ", S)


x1 = 4
x2 = 9
y1 = 16
y2 = 25
L = math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))
print("L =", L)

print("1.")
def arithmetic(x, y, s):
    if s == '+':
        print(x + y)
    elif s == '-':
        print(x - y)
    elif s == '*':
        print(x * y)
    elif s == '/':
        print(x / y)
    else:
        print("Неизвестная ошибка")

arithmetic(9, 3, '*')

print("2.")
def is_year_leap(x):
    if x % 4 != 0:
        print('Обычный')
    elif x % 100 == 0:
        if x % 400 == 0:
            print("Високосный")
        else:
            print('Обычный')
    else:
        print('Обычный')

is_year_leap(1965)

print('3.')
def square(a):
    S = a * a
    P = 4 * a
    D = math.sqrt(2) * a
    tuple = [S, P, D]
    print(tuple)

square(9)

print('4.')
def season(x):
    if x == 12 or x == 1 or x == 2:
        return 'Winter'
    elif x == 3 or x == 4 or x == 5:
        return 'Spring'
    elif x == 6 or x == 7 or x == 8:
        return 'Summer'
    elif x == 9 or x == 10 or x == 11:
        return 'Autumn'
    else:
        return 'Months are only 12'
print(season(8))

print('5.')
def bank(a, year):
    print(a + (a * 10 / 100 * year))

bank(5000, 5)

print('6.')
def is_prime(x):
    if x > 1 and x < 1000:
        if type(x) == int:
            return True
        else:
            return False
    else:
        return "число больше 1000"

print(is_prime(500.5))

print('7.')
def date(day, month, year):
    if day <= 31 and month <= 12 and year > 1:
        return True
    else:
        return 'Impossible'

print(date(13, 8, 2002))

print('8.')
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
i = 0
while a[i] < 6:
    print(a[i])
    i += 1

print('9.')
a = {1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89}
b = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
print(a.intersection(b))

print('Begin 20.')
x1 = random.randrange(-10, 10)
x2 = random.randrange(-10, 10)
y1 = random.randrange(-10, 10)
y2 = random.randrange(-10, 10)
S = math.sqrt((y2 - y1)**2 + (x2-x1)**2)
print("Расстояние: ", S)

print("Begin 21.")
x1, y1 = random.sample(range(-10, 10), 2)
x2, y2 = random.sample(range(-10, 10), 2)
x3, y3 = random.sample(range(-10, 10), 2)
list = (x1, x2, x3, y1, y2, y3)
print(list)
a = math.sqrt((y2 - y1)**2 + (x2-x1)**2)
b = math.sqrt((y3 - y2)**2 + (x3-x2)**2)
c = math.sqrt((y3 - y1)**2 + (x3-x1)**2)
P = a + b + c / 2
S = math.sqrt(P * (P - a) * (P - b) * (P - c))
print(S)

print("Перевод в двоичную систему.")



