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

photo = PhotoImage(file="загружено.png")

bgzoom = photo.zoom(2, 2)
bg = Label(root, image=bgzoom)

buttonimage = photo.subsample(4, 4)
button = Button(root, image=buttonimage)

bg.place(x=0, y=0, relwidth=1, relheight=1)
button.pack()

root.mainloop()