class Point:
    __x = 0
    __y = 0
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def setX(self, x):
        self.__x = x
    def setY(self, y):
        self.__y = y
    def __test(self): #private
        print("Private метод")
    def runPrivate(self): #public
        self.__test()


p = Point(10, 15)
#print(p.__x) Ошибка
print(p.getX())
print(p.getY())
p.setX(23)
p.setY(29)
print(p.getX())
print(p.getY())

#p.__test() Ошибка

p.runPrivate()

class Rectangle:
    __x = 0
    __y = 0
    __l = 0
    __h = 0
    def __init__(self, x = 0, y = 0, l = 0, h = 0):
        self.__x = x
        self.__y = y
        self.__l = l
        self.__h = h
    def getX(self):
        print(rec.__printlogget(), "x: ", self.__x)
    def getY(self):
        print(rec.__printlogget(), "y: ")
        return self.__y
    def getL(self):
        print(rec.__printlogget(), "l: ")
        return self.__l
    def getH(self):
        print(rec.__printlogget(), "h: ")
        return self.__h
    def setX(self, x):
        self.__x = x
        print(rec.__printlogset(), "x на: ", x)
    def setY(self, y):
        self.__y = y
        print(rec.__printlogset(), "y на: ", y)
    def setL(self, l):
        self.__l = l
        print(rec.__printlogset(), "l на: ", l)
    def setH(self, h):
        self.__h = h
        print(rec.__printlogset(), "h на: ", )
    def __str__(self):
        return "Прямоугольник с координатами (" + str(self.__x) + ';' + str(self.__y) + ') шириной: ' + str(self.__l) + ' и высотой: ' + str(self.__h)
    def square(self):
            return self.__h * self.__l
    def perimetr(self):
            return (self.__h + self.__l) * 2
    def __printlogget(self):
        return "Запрошено свойство"
    def __printlogset(self):
        return "Изменено свойство"


rec = Rectangle(2, 2, 4, 5)
rec.getX()
rec.setX(4)
print(rec.getH())
rec.setL(29)


