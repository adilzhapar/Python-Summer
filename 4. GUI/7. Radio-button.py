from tkinter import *

def setwindow(root):
    root.title("Окно программы")
    root.resizable(True, True)

    w = 700
    h = 500
    ws = root.winfo_screenwidth()
    wh = root.winfo_screenheight()

    x = int(ws / 2 - w / 2)
    y = int(wh / 2 - h / 2)

    root.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))

root = Tk()
setwindow(root)

label = Label(root, text='Ваш любимый цвет', font='Tahoma 20')

choice = StringVar()

r1 = Radiobutton(root, text='Красный', font='Tahoma 18', variable=choice, value='red')
r2 = Radiobutton(root, text='Зеленый', font='Tahoma 18', variable=choice, value='green')
r3 = Radiobutton(root, text='Синий', font='Tahoma 18', variable=choice, value='blue')

choice.set('green')
print(choice.get())
label2 = Label(root, text='Choose your city: ', font='Tahoma 20', fg='blue')

label.pack()
r1.pack()
r2.pack()
r3.pack()
label2.pack()

list = ('Denver', 'Moskva', 'Berlin', 'Nairobi', 'Helsinki')
number = IntVar()
x = 0
for n in list:
    r = Radiobutton(root, text=list[x], font='Tahoma 20', variable=number, value=x)
    r.pack()
    x += 1
number.set(3)

root.mainloop()