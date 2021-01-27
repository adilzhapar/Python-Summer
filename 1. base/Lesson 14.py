def printpython():
    print("Python")

def sum(x, y):
    return x + y
def sub(x, y):
    return x - y

def summaprint(x , y, r = False):
    s = sum(x, y)
    if r:
        return s
    else:
        print(s)

def bigsum(*numbers):
    s = 0
    for n in numbers:
        s += n
    print(s)

def printdict(**dict):
    for key in dict:
        print(key, "=", dict[key])

def getmax(arr):
    max = arr[0]
    for n in arr:
        if n > max:
            max = n
    return max


printpython()
s = sum(5, 7)
print(s)
print(sub(10, 15))

summaprint(49,1)
print(summaprint(49,1, True))

print(sub(y=10, x = 5))
bigsum(1, 6, 7, 3, 9)
printdict(Name = "Adil", Age = "17", Nation = "Kazakh")

print("Анонимные функции")

lambdafunc = lambda x, y: print(x + y)
lambdafunc(6, 9)

result = (lambda x, y: x + y) (3,7)
print(result)

print("--------")
print(getmax([9, -3, 0, 54, 121]))

print("Homework:")

def getcouple(x, r = True):
    if r:
        return x % 2 == 0
    else:
        print(False)
print(getcouple(7))

def getmax(arr):
    max = arr[3]
    for n in arr:
        if n > max:
            max = n
    return(max)
print(getmax([2, 5, 9, 0, 25]))

def midle(list):
    s = 0
    for n in list:
        s += n
        a = s / len(list)
    return a
print("Среднее арифметическое =", int(midle([2, 4, 6, 8])))





