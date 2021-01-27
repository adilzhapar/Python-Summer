list = []
print(list)
list = ['h', 'e', 'l', 'l', 'o']
print(list)

print(list[1])
print("The last symbol:", list[-1])
print(list[-4])
print("Длинна массива(колличество элемментов):", len(list))
print("Последний элемент:", list[len(list)-1])

print('-------')

i = 0
while i < len(list):
    print(list[i])
    i += 1

print('-------')
list = ['a', 3, 5.7, True]
i = 0
while i < len(list):
    print(list[i])
    i += 1
list[1] = 'b'
print(list[1])

list = [[2,3], 4]
print(list[0][0])
print(list[0][1])
print(list[1])

print('--------')

list = [[2,3], [4,5,6]]
i = 0
while i < len(list):
    j = 0
    while j < len(list[i]):
        print(list[i][j])
        j += 1
    i += 1

print('--------')

prices = [20, 30, 15, 20, 45, 15]
min = prices[0]
max = prices[0]
i = 1
while i < len(prices):
    if prices[i] < min:
        min = prices[i]
    if prices[i] > max:
        max = prices[i]
    i += 1
print("Массив: ", prices)
print("Минимальное значение: ", min)
print("Максимальное значение: ", max)

print('-------')

table = ['0', 'Adil', 'Kana', 'Aibar', 'Jans', 'Adiya']
i = 0
while i < len(table):
    print(i, "-", table[i], ';')
    i += 1

while True:
    x = input("Введите индекс от 1 до 5: ")
    if x == "end":
        print("that is \nEnd")
        exit(0)
    if int(x) > 5:
        print("Элемента с таким индексом не существует.")
        continue
    print(x, "=", table[int(x)])


