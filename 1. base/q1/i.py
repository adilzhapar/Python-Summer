n = int(input())
list = [int(input()) for i in range(0, n)]
j=0
for i in list:
    if j%2==0:
        print(i)
    j+=1