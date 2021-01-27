from tkinter import *
from random import randrange

root = Tk()
root.title("Window")
root.geometry("600x400+400+150")

def random(event):
    label = Label(root, text=randrange(1, 100), font='Tahoma 15')
    label.pack()


button = Button(root, text='Сгенерировать случайное число', font='Helvetica 20', bg='yellow')
button.bind("<Button-1>", random)

button.pack(pady=20)


root.mainloop()