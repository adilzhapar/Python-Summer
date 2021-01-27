list = {0, 4, 6, 8, 9}
n = int(input())
arr = []
# arr = [int(input()) for i in range (0, n)]
for i in range(0, n):
    num = map(int, input().split())
    arr.append(num)

sum = 0
for i in arr:
    for j in list:
        if i==j:
            sum += i

print(arr)
print(sum)