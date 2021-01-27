from datetime import *
from time import *
print(date.today())
print(datetime.today())

start = time()

d = date(2015, 7, 15)
print(d)

dt = datetime(2025, 7, 15, 22, 45, 30)
print(dt)

print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)

print("----------")
print(dt.strftime('%Y.%m.%d %H:%M:%S'))
print("----------")

print(time()) #текущее дата и время в секундах

dt = datetime.fromtimestamp(999123956)
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)

print(dt.timestamp())
i = 0
while i < 100000:
    i += 1
print("Время выполнения кода: ", time() - start)

print("Введите свой день рождения ")
y = int(input("Год: "))
m = int(input("Месяц: "))
d = int(input("День: "))
dt = datetime(y, m, d)
print("Вы живете: ", time() - dt.timestamp(), "секунд")


