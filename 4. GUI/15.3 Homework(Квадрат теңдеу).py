from tkinter import *
from math import *
root = Tk()
root.title("Корни уравнения")
root.geometry("700x600+300+90")
root.config(bg='#87CEEB')

def handlerclick(event=False):
    global en1
    global en2
    global en3
    global result1
    global result2
    try:
        D = float(float(en2.get()) ** 2 - 4 * float(en1.get()) * float(en3.get()))
        if D < 0:
            result1.config(text='Нет корней')
        else:
            x1 = str((float(en2.get()) * (-1)) + sqrt(D) / 2 * float(en1.get()))
            x2 = str((float(en2.get()) * (-1)) - sqrt(D) / 2 * float(en1.get()))
            result1.config(text='x1 = ' + x1)
            result2.config(text='x2 = ' + x2)
    except ValueError:
        if not en1.get() or not en2.get() or en3.get():
            result1.config(text='Вы ничего не ввели')
        else:
            result1.config(text='Вы ввели не числа')



header = Label(root, text='ax^2 + bx + c = 0', font='Monospace 20', bg='#87CEEB')
en1 = Entry(root, font='Tahoma 20', bg='#F0FFFF')
en2 = Entry(root, font='Tahoma 20', bg='#F0FFFF')
en3 = Entry(root, font='Tahoma 20', bg='#F0FFFF')
l1 = Label(root, font='Tahoma 20', text='a: ', bg='#87CEEB')
l2 = Label(root, font='Tahoma 20', text='b: ', bg='#87CEEB')
l3 = Label(root, font='Tahoma 20', text='c: ', bg='#87CEEB')
button = Button(root, font="Monospace 20", text='Вычислить корни уравнения', command=handlerclick, bg='#F0FFFF')
result1 = Label(root, font='Tahoma 20', bg='#87CEEB')
result2 = Label(root, font='Tahoma 20', bg='#87CEEB')

en1.bind("<Return>", handlerclick)
en2.bind("<Return>", handlerclick)
en3.bind("<Return>", handlerclick)


header.place(relx=0.5, rely=0.01, anchor='n')
en1.place(relx=0.5, rely=0.1, anchor='n')
en2.place(relx=0.5, rely=0.2, anchor='n')
en3.place(relx=0.5, rely=0.3, anchor='n')
l1.place(relx=0.2, rely=0.1, anchor='n')
l2.place(relx=0.2, rely=0.2, anchor='n')
l3.place(relx=0.2, rely=0.3, anchor='n')
button.place(relx=0.5, rely=0.4, anchor='n')
result1.place(relx=0.5, rely=0.5, anchor='n')
result2.place(relx=0.5, rely=0.6, anchor='n')

root.mainloop()
