from tkinter import *
from random import randrange

root = Tk()
root.resizable(True, True)
root.title("Random number")
root.geometry("300x300+500+150")

def random(event):
    label = Label(root, text=randrange(1, 40), font='Helvetica 20')
    label.pack()

button = Button(root, text='Generate', bg='white',font='Helvetica 20')
button.bind("<Button-1>", random)
button.pack(pady=20)

root.mainloop()