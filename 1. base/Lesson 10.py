array = [1, 5, -4, 4.5]
for x in array:
    print(x)

print("------")

str = "Python"
print(str[0])

for s in str:
    print(s)
print("------")

for s in str:
    if s == "Y":
        break
else:
    print("Символа Y в строке", str, "нет")
print("------")

array = list(range(2, 15))
print(array)
print(array[3])
for n in array:
    print(n)

print("--------------") #Разные способы выводить списки

array = list(range(1, 10))
print(array)

array = [i for i in range(1, 10)]
print(array)
#Генератор списка:
array = [i for i in range(1, 15) if i % 2 == 0]
print(array)
array = [i for i in range(1, 15) if (i +1 ) % 2 == 0]
print(array)

print('\\\\\\\\')

array = range(3, 8)
s = 0
for n in array:
    s += n
print("Сумма чисел:", s)

s = 0
for n in array:
    s += n
    a = s / len(array)
print("Среднее арифметическое массива:", a)
print("----------")
i = 0
s = 0
while i < len(array):
    s += array[i]
    i += 1
print("Сумма чисел:", s)

i = 0
s = 0
while i < len(array):
    s += array[i]
    i += 1
    a = s / len(array)
print("Среднее арифметическое массива:",a)

