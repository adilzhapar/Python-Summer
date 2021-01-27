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

label1.place(x=0, y=0, anchor='nw')
label2.place(relx=0.5, rely=0.5, anchor='center')
label3.place(relx=0.5, rely=0, anchor='n')
label4.place(relx=0.5, rely=0.7, width=100, height=70, anchor='center')
label4.place(relx=0.5, rely=0.7, anchor='center')
label5.place(relx=1, y=0, anchor='ne')
root.mainloop()