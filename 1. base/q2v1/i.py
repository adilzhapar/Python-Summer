a = int(input())
a = str(bin(a))

l = ""
for i in range(len(a)):
    l = a[i] + l

for i in range(len(l)):
    if l[i] == "1":
        print(i)
        exit(0)
