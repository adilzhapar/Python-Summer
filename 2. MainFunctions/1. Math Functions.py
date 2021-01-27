from math import *

print(e)
print(pi)

print("----------")

print(sin(1))
print(cos(1))
print(tan(1))
print(1 / tan(1))

print(sin(radians(30)))

print("----------")

print(fabs(-5))
print(floor(5.9))
print(ceil(5.9))
print(sqrt(9))

print("----------")

print(round(5.434, 2))
print(round(1 / 3, 2))

print("----------")

print(round(4.5689, 2))

array = range(0, 181)
for n in array:
    print("sin", n, "=", sin(radians(n)))
