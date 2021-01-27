a = int(input())

list = [int(input()) for i in range(0, a)]

cnt = 0
for i in list:
    if i % 2 == 0:
        cnt += 1
print(cnt)
