import random

myset = set()
print(myset)
myset = {}
print(myset)

myset = set("Python")
print(myset)

myset = {'1', 2, 3, 1,  '-1'}
print(myset)

print(int(random.random() * 10))

arr = [int(random.random() * 10) for i in range(0, 10)]
print(arr)
arr = list(set(arr)) #Сортирует и убирает повторяющиеся цифры
print(arr)

#HOMEWORK

x = int(input("Веведите коллличество элементов: "))
arr = [int(random.random() * 100) for i in range(0, x)]
print(arr)
arr = set(arr)
print(arr)

for n in arr:
    print(n)
print("-------")
i = 0
while i < x:
    s = int(random.random() * 100)
    print(s)
    i += 1





