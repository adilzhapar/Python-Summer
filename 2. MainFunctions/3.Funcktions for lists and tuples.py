list = [1, 2, 0, 5]
print(list)
print(len(list))
list.append(9)
print(list)
list.extend([0, 1])
print(list)
list.insert(1, 5)
print(list)

print("------")

print(list.index(9))
print(list.index(1, 3))
print(list.count(1))

list.reverse()
print(list)

print("------")

list.remove(0)
print(list)
list.pop(3)
print(list)

print("------")

list = [1, 7, 3, 6, 0]
list.sort()
print(list)
list.sort(reverse=True)
print(list)

print("------")

t = tuple("Hello")
print(t.index('o'))
print(t.count('l'))



x = int(input("Введите колличество элементов: "))
list = [input("Введите число: ") for i in range(0, x)]
print(list)

list = []
n = 0
x = int(input("Введите колличество элементов: "))
while n < x:
    list.append(input("Введите число " + str(n) + ": "))
    n += 1
print(list)
