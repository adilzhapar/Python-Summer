from tkinter import *
root = Tk()
root.resizable(False, False)
root.title("Homework 12")
root.geometry("600x400+400+200")

label1 = Label(root, text="Authorization", font='Helvetica 24', fg='blue')
label2 = Label(root, text='Login: ', font='Helvetica 18', fg='blue')
label3 = Label(root, text='Password: ', font='Helvetica 18', fg='blue')
entry1 = Entry(root, bd=4, bg='white')
entry2 = Entry(root, bd=4, bg='white', show='*')
button = Button(root, text='Enter', width=20, height=3)

label1.place(relx=0.5, y=40, anchor='center')
label2.place(relx=0.3, y=70, anchor='ne')
label3.place(relx=0.3, y=100, anchor='ne')
entry1.place(relx=0.35, y=70)
entry2.place(relx=0.35, y=100)
button.place(relx=0.5, y=140, anchor='n')

root.mainloop()