from tkinter import *
root = Tk()
root.resizable(True, True)
root.title('Programm window')
w = 600
h = 500
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = int(ws / 2 - w / 2)
y = int(hs / 2 - h / 2)
root.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))


def handlerclick1(x):
    print(x)


def handlerclick2(event):
    print("Нажата кнопка:")
    print(event.widget.cget("text"))


def handlerclick3(event):
    print(event.widget)
    print("Нажата правая кнопка мыши")


def handlerroot(event):
    print(event)
    print("Сработало событие 'a'")


button1 = Button(root, text='Button 1', font='Tahoma 20', command=lambda: handlerclick1("Button 1"))
button2 = Button(root, text='Button 2', font='Tahoma 20', command=lambda: handlerclick2)
button3 = Button(root, text='Button 3', font='Tahoma 20')

button2.bind("<Button-3>", handlerclick2)
button3.bind("<Button-3>", handlerclick3)
root.bind("a", handlerroot)

button1.pack()
button2.pack()
button3.pack()

root.mainloop()