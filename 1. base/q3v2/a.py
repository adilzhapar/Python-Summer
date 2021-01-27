n = int(input())
bank = list(map(int, input().split()))
q = int(input())
ans = []
for i in range(0, q):
    x = int(input())
    cnt = 0
    for j in bank:
        if j == x:
            cnt += 1
    ans.append(cnt)

for i in ans:
    print(i)
