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

label1 = Label(root, text='Metka 1', font='Tahoma 20', bg='red')
label2 = Label(root, text='Metka 2', font='Tahoma 20', bg='#A07')
label3 = Label(root, text='Metka 3', font='Tahoma 20', bg='#F98')
label4 = Label(root, text='Metka 4', font='Tahoma 20', bg='#5d1')
label5 = Label(root, text='Metka 5', font='Tahoma 20', bg='#aa8')

label1.grid(row=0, column=0, padx=10, pady=20)
label2.grid(row=0, column=1, ipadx=10, ipady=12)
label3.grid(row=1, column=0, columnspan=2, pady=20, ipadx=30)
label4.grid(row=2, column=0, rowspan=2, sticky='ne')
label5.grid(row=2, column=1, sticky='w')
Label(root, text='Metka 6', font='Tahoma 20', bg='#abf').grid(row=3, column=1, sticky='w')

root.mainloop()