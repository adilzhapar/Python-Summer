from tkinter import *

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

entry1 = Entry(root, font='Tahoma 20', bg='green', fg='yellow', bd=4)
entry2 = Entry(root, font='Tahoma 20', bg='green', fg='yellow', bd=4, show='*')
entry1.insert(END, 'Hello')
entry1.insert(END, 'ABC')

print(entry1.cget('fg'))
print(entry1['fg'])

entry1['fg'] = 'blue'

myentry = Entry(root, font='Helvetica 14', bg='black', fg='white', bd=3)
myentry.insert(END, input('Введите слово: '))


entry1.pack()
entry2.pack()
myentry.pack()

root.mainloop()