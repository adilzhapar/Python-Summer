class Point:
    x = 0
    y = 0
p1 = Point()
print(p1.x, ';', p1.y)
print(p1)

p1.x = 5
p1.y = 7
print(p1.x, ';', p1.y)

p2 = Point()
p2.z = 10
print(p2.x, ';', p2.z)

#print(p1.z) #Ошибка

class Rectangle:
    x1 = 0
    y1 = 0
    l = 5
    h = 7

r1 = Rectangle()
print(r1)

r1.x1 = 3
r1.y1 = 4
r1.l = 8
r1.h = 10
print("x1 = ", r1.x1)
print("y1 = ", r1.y1)
print("l = ", r1.l)
print("h = ", r1.h)