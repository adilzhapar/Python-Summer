handler = open('a.txt', 'w')
handler.write("abc 123\n890")
handler.close()

handler = open('a.txt', 'r')
print(handler.read(2))
print(handler.read())

handler.seek(0)
print(handler.read())
print("----------")
handler.seek(0)
for line in handler:
    print(line)

handler.close()
print("------------------")
file = 'b.txt'
while True:
    print("1 - Записать файл; 2 - Прочитать файл; 0 - Выход")
    inp = input("Введите команду: ")
    if inp == "0":
        break
    elif inp == "1":
        text = input("Введите строку: ")
        handler = open(file, 'w')
        handler.write(text)
        handler.close()
    elif inp == "2":
        try:
            handler = open(file, 'r')
            print(handler.read())
            handler.close()
        except FileNotFoundError:
            print("Файла еще не существует")
    else:
        print("Неизвестная команда")

while True:
    print("Введите 'read' или 'copy', 0 - quit: ")
    inp = input("Ввод: ")
    if inp == "0":
        break
    elif inp == "read":
        x = input("Напишите путь к файлу: ")
        handler = open(x + ".txt", 'r')
        s = handler.read()
        print(s)
        handler.close()
    elif inp == "copy":
        x = input("Напишите имя скопируемого файла: ")
        handler = open(x + ".txt" + "(1)", 'w')
        handler.write(s)
        handler.close()


