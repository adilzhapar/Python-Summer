h1 = int(input())
m1 = int(input())
h2 = int(input())
m2 = int(input())

if h2 < h1:
    print("No")
    # exit(0)
elif h2 > h1:
    print("Yes")
    # exit(0)
else:
    if m2 <= m1:
        print("No")
    else:
        print("Yes")