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

data = ["Birmingham", "Winterfell", "Palermo", "Denver"]
list = Listbox(root, font='Tahoma 20', width=20, height=4, selectmode=MULTIPLE)


for d in data:
    list.insert(END, d)

list.selection_set(0, 2)
print(list.selection_get())

list1 = []
while True:
    x = input("Введите название страны: ")
    if x == '0':
        break
    list1.append(x)

list_for_window = Listbox(root, font='Tahoma 18', width=10, height=3, selectmod=SINGLE, fg='white', bg='blue')

for i in list1:
    list_for_window.insert(END, i)

scrollbar = Scrollbar(root, command=list_for_window.yview, orient=VERTICAL)
list_for_window['yscrollcommand'] = scrollbar.set

list.pack()
list_for_window.pack(side='left')
scrollbar.pack(side='left', fill=Y)
root.mainloop()