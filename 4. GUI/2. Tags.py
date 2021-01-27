from tkinter import *
import random

def setwindow(root):
    root.title("Окно программы")
    root.resizable(False, False)

    w = 1000
    h = 500
    ws = root.winfo_screenwidth()
    wh = root.winfo_screenheight()

    x = int(ws / 2 - w / 2)
    y = int(wh / 2 - h / 2)

    root.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))

root = Tk()
setwindow(root)



label = Label(root, text='Моя метка', font='Helvetica 20', bg='#dfc', fg='blue')
label.pack()

string = Label(root, text='---------')
string.pack()

number = Label(root, text=str(random.randrange(1, 1000)), font='Helvetica 15', bg='black', fg='white')
number.pack()


root.mainloop()