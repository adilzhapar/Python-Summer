c = input()
s = input()
s = list(s)
l = ""
for i in s:
    if i==c:
        continue
    else:
        l += i

print(l)