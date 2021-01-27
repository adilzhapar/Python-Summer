def absolute(a, b):
    c = a - b
    if c < 0:
        c = c * (-1)
        return c
    elif c >= 0:
        return c


a = int(input())
b = int(input())
print(absolute(a, b))