from tkinter import *
root = Tk()
root.title("окно программы")
root.resizable(True, True)
root.geometry("800x500+270+100")

def handlerclick(event):
    event.widget.config(bg='red')

def handlerleave(event):
    event.widget.config(bg='yellow')

button1 = Button(root, text='Button 1', font='Tahoma 20', bg='yellow')
button2 = Button(root, text='Button 2', font='Tahoma 20', bg='yellow')

button1.bind("<Enter>", handlerclick)
button1.bind("<Leave>", handlerleave)
button2.bind("<Enter>", handlerclick)
button2.bind("<Leave>", handlerleave)

button1.pack()
button2.pack()

root.mainloop()
