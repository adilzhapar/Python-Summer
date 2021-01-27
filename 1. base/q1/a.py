def Palindrome(n):
    return n == n[::-1]


n = input()
ans = Palindrome(n)

if ans:
    print("YES")
else:
    print("NO")
