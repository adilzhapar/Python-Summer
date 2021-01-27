from math import sqrt

class Point:
    x = 0
    y = 0
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def range(self, p):
        return sqrt((p.x - self.x) ** 2 + (p.y - self.y) ** 2)
    def __str__(self):
        return 'Координаты: (' + str(self.x) + '; ' + str(self.y) + ')'

class Auto:
    p = Point(0, 0)
    speed = 0
    def __init__(self, p = Point(0, 0), speed = 0):
        self.p = p
        self.speed = speed
    def setspeed(self, speed):
        self.speed = speed
    def gettime(self, endp):
        if self.speed != 0:
            return self.p.range(endp) / self.speed
        else:
            return -1


p = Point(5, 5)
print(p)
print(p.range(Point()))
print(p.range(Point(3, 10)))

auto = Auto()
print(auto.speed)
auto.setspeed(50)
print(auto.speed)

print(auto.gettime(Point(100, 200)))

class Rectangle:
    x = 0
    y = 0
    l = 0
    h = 0
    def __init__(self, x = 0, y = 0, l = 0, h = 0):
        self.x = x
        self.y = y
        self.l = l
        self.h = h
    def __str__(self):
        return "Прямоугольник с координатами (" + str(self.x) + ';' + str(self.y) + ') шириной: ' + str(self.l) + ' и высотой: ' + str(self.h)
    def square(self):
            return self.h * self.l
    def perimetr(self):
            return (self.h + self.l) * 2

c = Rectangle(1, 1, 8, 9)
print(c)
print('Площадь равна: ', c.square())
print("Периметр равен: ", c.perimetr())





