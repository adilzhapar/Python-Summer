
def IsPrime(n):
    if n <= 1:
        return False
    elif n == 2 or n == 3:
        return True
    else:
        test = False
        i = 2
        while i*i <= n:
            if n % i == 0:
                test = False
                break
            else:
                test = True
            i += 1
    return test


cnt = 0
size = int(input())
list = [int(input()) for i in range(0, size)]
for i in list:
    if IsPrime(i):
        cnt += 1
    else:
        continue

print(cnt)