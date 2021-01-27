from abc import ABC, abstractmethod

class Shape:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def printXY(self):
        print('(' + str(self.x) + ';' + str(self.y) + ')')
    def draw(self):
        print("Рисуем фигуру")

class Circle(Shape):
    r = 0
    def __init__(self, x, y, r):
        Shape.__init__(self, x, y)
        self.r = r
    def draw(self):
        print("Рисуем окружность (", self.x, ';', self.y, ';', self.r, ')', sep='')

class Rectangle(Shape):
    w = 0
    b = 0
    def __init__(self, x, y, w, h):
        Shape.__init__(self, x, y)
        self.w = w
        self.h = h
    def draw(self):
        print("Рисуем прямоугольник (", self.x, ';', self.y, ';', self.w, ';', self.h, ')', sep='')

s = Shape(5, 7)
s.draw()

c = Circle(10, 20, 5)
c.draw()

r = Rectangle(0,0, 30, 50)
r.w = 35
r.draw()

s.printXY()
c.printXY()
r.printXY()

class Auto(ABC):
    x = 0
    y = 0
    speed = 0
    wheight = 0
    def __init__(self, x, y, speed, wheight):
        self.x = x
        self.y = y
        self.speed = speed
        self.wheight = wheight

    @abstractmethod
    def move(self, m, n):
        pass

class BMW(Auto):
    engine = 530
    def __init__(self, x, y, speed, wheight, engine):
        Auto.__init__(self, x, y, speed, wheight)
        self.engine = engine
    def move(self, m, n):
        self.m = m
        self.n = n
        print("Движение BMW в точку x, y: (", str(m) + ';' + str(n) + ')', sep='')


#car = Auto(1, 1, 150, 300)
#car.move(9, 9)
mycar = BMW(1, 1, 250, 300, 530)
mycar.move(13, 13)