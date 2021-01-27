def calc(symb, a, b):
    if symb == '+':
        return a + b
    elif symb == "-":
        return a - b
    elif symb == '*':
        return a * b
    else:
        return a / b


n = int(input())
ans_list = []
for i in range(0, n):
    arithmetic = input()
    mylist = list(map(str, input().split(maxsplit=4)))
    x = calc(arithmetic, int(mylist[1]), int(mylist[3]))
    s = "{} {} {} = {}".format(mylist[0], arithmetic, mylist[2], str(x))
    ans_list.append(s)

for i in ans_list:
    print(i)
