a = int(input())
b = int(input())
cnt=0
while a<=b:
    a *= 3
    b *= 2
    cnt+=1
print(cnt)

print("----")

a = int(input())
b = int(input())
print(a, "+", b, "=", a+b)
print(a, "-", b, "=", a-b)
print(a, "*", b, "=", a*b)

print("----")

a = int(input())
d = int(input())
n = int(input())
ans = a + d*(n-1)
print(ans)

print("----")

a = int(input())
for i in range(1, 6):
    if i==5:
        print(a*i)
    else:
        print(a*i, end="---")

print("----")

a = 15 // (16 % 7)
b = 34 % a * 5 - 29 % 5 * 2
print(a + b)

a = 82 // 3 ** 2 % 7
print(a)

print(2/4)
print(2//4)