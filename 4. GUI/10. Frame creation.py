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

frame1 = Frame(root, bg='red', bd=5)
frame2 = Frame(root, bg='blue', bd=5)

label1 = Label(frame1, text='Metka 1', font='Tahoma 20')
label2 = Label(frame2, text='Metka 2', font='Tahoma 20')
label3 = Label(frame2, text='Metka 3', font='Tahoma 20')

frame1.pack()
frame2.pack()
label1.pack()
label2.pack()
label3.pack()


myframe1 = Frame(root, bg='red', bd=4)
myframe2 = Frame(root, bg='black', bd=4)
myframe3 = Frame(root, bg='yellow', bd=0)

mylabel = Label(myframe1, text="Important form", font='Tahoma 20', fg='red')
myentry1 = Entry(myframe2, bd=3, bg="white")
myentry1.insert(END, "Write your name: ")
myentry2 = Entry(myframe2, bd=3, bg="white")
mybutton = Button(myframe3, text="Send the form")

myframe1.pack()
myframe2.pack()
myframe3.pack()
mylabel.pack()
myentry1.pack()
myentry2.pack()
mybutton.pack()
root.mainloop()