#import random
#import marh as m
from random import *
from math import sin, cos
import math, cmath as cm
import calc

#print(random.randint(0, 10)
#print(m.sin(2))
print(randint(7,13))
print(sin(3.14))
print(cos(0.5))
print(math.ceil(9.8))
print(cm.log10(1000))

while True:
    print("Сложение - 1; Вычитание - 2; Умножение - 3; Деление - 4; Выход - 0 ")
    code = input("Введите команду: ")
    if code == "0":
        break
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    if code == "1":
        r = calc.sum(a, b)
    elif code == "2":
        r = calc.sub(a, b)
    elif code == "3":
        r = calc.mult(a, b)
    elif code == "4":
        r = calc.div(a, b)
    print("Результат: ", r)

while True:
    print("Маскимальное значение - 1; Минимальное значение - 2; Сумма - 3; Выход - 0")
    code = input("Введите команду: ")
    if code == "0":
        exit(0)
    arr = [2, 3, 4, 5, 6, 7]
    if code == "1":
        r = calc.getmax(arr)
    elif code == "2":
        r = calc.getmin(arr)
    elif code == "3":
        r = calc.allsum(arr)
    print("Результат: ", r)
