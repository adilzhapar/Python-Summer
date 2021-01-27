def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b

def getmax(arr):
    max = arr[0]
    for n in arr:
        if n > max:
            max = n
    return max

def getmin(arr):
    min = arr[0]
    for n in arr:
        if n < min:
            min = n
    return min

def allsum(arr):
    s = 0
    for n in arr:
        s += n
    return s