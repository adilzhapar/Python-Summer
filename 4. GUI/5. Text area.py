from tkinter import *

def setwindow(root):
    root.title("Окно программы")
    root.resizable(False, False)

    w = 700
    h = 500
    ws = root.winfo_screenwidth()
    wh = root.winfo_screenheight()

    x = int(ws / 2 - w / 2)
    y = int(wh / 2 - h / 2)

    root.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))

root = Tk()
setwindow(root)

text = Text(root, bd=2, font='Helvetica 20', bg='red', fg='white', width=10, height=5, padx=7, pady=7)

text.insert(END, 'String\nNice')
print(text.get('1.0', END))
text.pack()

handler = open('a.txt', 'w')
handler.write("It is hard to reminisce something without practise")
handler.close()
handler = open('a.txt', 'r')

mytext = Text(root, bd=3, font='Tahoma 17', width=20, height=10)
mytext.insert(END, handler.read())

scrollbar = Scrollbar(root, command=mytext.yview, orient=VERTICAL)
mytext['yscrollcommand'] = scrollbar.set


mytext.pack(side='left')
scrollbar.pack(side='left', fill=Y)
root.mainloop()