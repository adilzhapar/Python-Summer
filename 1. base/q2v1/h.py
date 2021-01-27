string = input()
cnt = 0
for i in range(len(string)):
    if string[i: i+3] == "rgb":
        cnt += 1

print(cnt)