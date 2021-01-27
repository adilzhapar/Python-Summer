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

button1 = Button(root, text='My button 1', bg='white', fg='blue', font='Tahome 24')
button2 = Button(root, text='My button 2', bg='white', fg='blue', font='Tahoma 29')

button1.pack()
button2.pack()




root.mainloop()