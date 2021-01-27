a = []
for i in range(0, 8):
    a.append([0 for j in range(0, 8)])


n = int(input())
for i in range(0, n):
    cor = input()
    a[ord(cor[0])-65][int(cor[1])] = '*'

for i in range(0, 8):
    for j in range(0, 8):
        print(a[i][j], end='')
    print()