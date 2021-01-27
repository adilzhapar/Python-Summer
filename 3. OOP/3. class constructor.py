class Circle:
    x = 0
    y = 0
    r = 0
    def __init__(self, x, y, r = 0):
        self.x = x
        self.y = y
        self.r = r
        if r == 0:
            print("Радиус не задан!")

c = Circle(5, 7, 10)
print(c.x, ';', c.y, ';', c.r)
c.x = 10
print(c.x)

c = Circle(5, 20)
print(c.x, ';', c.y, ';', c.r)

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



