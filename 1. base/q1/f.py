list = [int(input()) for i in range (0, 3)]
max = 99

for i in list:
    if i<99 or i>699:
        print("Error")
        exit(0)
    elif i>=max:
        max = i

print(max)