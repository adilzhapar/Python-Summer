from tkinter import *
root = Tk()
root.resizable(False, False)
root.title("Homework 12")
root.geometry("600x400+400+200")

label1 = Label(root, text="Authorization", font='Helvetica 24', fg='blue')
label2 = Label(root, text='Login: ', font='Helvetica 18', fg='blue')
label3 = Label(root, text='Password: ', font='Helvetica 18', fg='blue')
entry1 = Entry(root, bd=4, width=30)
entry2 = Entry(root, bd=4, width=30, bg='white', show='*')
button = Button(root, text='Enter', width=15, height=2)

label1.grid(row=0, column=2)
label2.grid(row=1, column=0, sticky='e')
label3.grid(row=2, column=0, sticky='e')
entry1.grid(row=1, column=1, columnspan=2)
entry2.grid(row=2, column=1, columnspan=2)
button.grid(row=3, column=1, columnspan=2, pady=15)

root.mainloop()