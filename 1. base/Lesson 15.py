isprint = False

def sum(x, y):
    s = float(x) + float(y)
    if isprint:
        print(s)
    else:
        return s

def sub(x, y):
    global result
    result = float(x) - float(y)


x = input("Введите число 1: ")
y = input("Введите число 2: ")
print("Сумма равна: ", sum(x, y))
sub(x, y)
print("Разность равна:", result)

Pi = 3.141592

def area(R):
    global S
    S = Pi * int(R)**2
R = input("Введите радиус окружности: ")
area(R)
print("Площадь круга", S)
