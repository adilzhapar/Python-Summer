from tkinter import *
root = Tk()
root.resizable(False, False)
root.title("Homework 12")
root.geometry("600x400+400+200")

inp1 = input("Введите название картинки: ")
inp2 = input("Каким масштабом выводить изображение: ")

photo = PhotoImage(file=inp1 + ".png")

if float(inp2) < 1:
    myphoto = photo.subsample(int(1 / float(inp2)), int(1 / float(inp2)))
else:
    myphoto = photo.zoom(int(inp2), int(inp2))

image = Label(root, image=myphoto)

image.pack()

root.mainloop()
