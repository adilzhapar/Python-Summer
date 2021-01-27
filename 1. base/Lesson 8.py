i = 0
while i < 10:
    i += 1 # i = i + 1
    print("Hello, world")
print("End of cycle")

print("------")

i = 0
while i < 10:
    i += 1
    print(i)

print("------")

i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    if i == 8:
        break
    print(i)
print("End of cycle")

print("------")

s = 0
to = 10
x = 1
while x <= to:
    s += x
    x += 1
print("Сумма чисел от 1 до", to, "равна", s)

while True:
    code = input("Введите 0 для выхода: ")
    if code == "0":
        break


print("------")


#HOMEWORK
sum = 0
while True:
    x = input("Enter a number to add, 'sum' to display the sum or 'exit/quit' to exit:")
    if x == "quit" or x == "exit":
        print("Exiting...\n")
        exit(0)
    elif x == "sum":
        print("Your sum =", sum, "\n")
        sum = 0
        continue
    else:
        sum = sum + int(x)



