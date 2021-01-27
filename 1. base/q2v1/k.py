n = int(input())

arr = list(map(int, input().split()))

i = 0
while i < n:
    if arr[i] < 0:
        arr[i] *= (-1)
    i += 1


print(arr)
