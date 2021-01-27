print("Введите 0, 1 или 2:")
a = input()
if a == "0":
    print('Вы ввели ноль')
    print("Это число меньше 10")
elif a == "1":
    print("Вы ввели один")
elif a == "2":
    print("Вы ввели два")
else:
    print("Некорректный ввод")

cond = a == "0" or a == "1" or a == "2"

if cond:
    x = 0
else:
    x = 3

print("x =", x)

x = 0 if cond else 3
print("x =", x)

#PRACTICE

print("Enter the number: ")
a = input()
b = input()

if b == "0":
    print("a / b = infinity")
elif int(a) / int(b) != "0":
    print("a / b =", int(a) / int(b))
