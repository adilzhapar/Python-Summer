n = int(input())
a0 = int(input())
for i in range(1, n):
    a = int(input())
    if a0 != a:
        print("No")
        exit(0)
print("Yes")