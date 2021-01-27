mytuple = tuple()
print(mytuple)

mytuple = (1,) #Создание из одного кортежа
print(mytuple)

mytuple = (1, '3', '5')
print(mytuple)
#mytuple[1] = '5' #Ошибка
print(mytuple[1])

mytuple = tuple('Python')
print(mytuple)

x = input("Введите строку: ")
mytuple = tuple(x)
print(mytuple)
for n in mytuple:
    print(n)