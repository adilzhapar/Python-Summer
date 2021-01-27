from tkinter import *

def setwindow(root):
    root.title("Окно программы")
    root.resizable(False, False)

    w = 700
    h = 500
    ws = root.winfo_screenwidth()
    wh = root.winfo_screenheight()

    x = int(ws / 2 - w / 2)
    y = int(wh / 2 - h / 2)

    root.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))

root = Tk()
setwindow(root)


choice = IntVar()
check = Checkbutton(root, bd=20, text='Согласие на обработку данных', variable=choice, onvalue=1, offvalue=0)
print('Если выключен: ', choice.get())
check.select()
#check.deselect()
print('Если включен: ', choice.get())
check.pack()

import random
choice = IntVar()
mycheck = Checkbutton(root, bd=40, text='Second confirm button', variable=choice, onvalue=1, offvalue=0)
x = random.randrange(0, 2)
choice.set(x)

mycheck.pack()



root.mainloop()