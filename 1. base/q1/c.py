n = int(input())
list = [int(input()) for i in range(0, n)]

sum = 0
j=0
for i in list:
    if (j+1) % 7 == 0:
        sum += i
    j += 1

print(sum)