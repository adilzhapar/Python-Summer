from tkinter import *
root = Tk()
root.title("окно программы")
root.resizable(True, True)
root.geometry("400x200+270+100")

import random

orig_color = root.cget("bg")
print(orig_color)

colors = ['red', 'blue', 'purple']
x = random.randrange(0, 3)

def handlerenter(event):
    event.widget.config(bg=colors[x])

def handlerleave(event):
    event.widget.config(bg='SystemButtonFace')

root.bind("<Enter>", handlerenter)
root.bind("<Leave>", handlerleave)

root.mainloop()