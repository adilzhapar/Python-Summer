b1 = True
b2 = False
print("b1 =", b1)
print("b2 =", b2)
b3 = b1 or b2
print("b1 or b2 =", b3)
print("b1 and b2 =", b1 and b2)
print("not b1 =", not b1)
print("b1 != b2 =", b1 != b2)
print("b1 == b2 =", b1 == b2)

print()

x = 5
y = 7
print("x =", x)
print("y =", y)
print("x > y =", x > y)
print("x < y =", x < y)
print("x >= y =", x >= y)
print("x <= y =", x <= y)

print("x and b1 or (x > 10) =", x and b1 or (x > 10))
print("x > 10 or y < 7 =", x > 10 or y < 7)
print("x > 10 or y <= 7 =", x > 10 or y <= 7)

#HOMEWORK

print("answer =", b1 and (b1 or (b2 and b1 or b2) and b1 or b1 != b2))
print("second answer =", 15 > 20 or (5 < 7 and  8 > 12 or 12 >= 12 and 15 < 18))

print("False or True =", False or True)   #Have to remember
print("False and True =", False and True)





