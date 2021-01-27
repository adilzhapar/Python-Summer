from tkinter import *

root = Tk()
root.title("Коммунальные услуги")
root.resizable(True, True)
root.geometry("800x600+270+30")
root.config(bg='#FFF5EE')



global sum
global r1
global r2
sum = 0

def handlerbutton1(event=False):
    global sum
    global over
    try:
        r1 = (float(last.get()) - float(pre.get())) * 17.79 + float(debt.get()) - float(over.get())
        r1 = str(float("{:.2f}".format(r1)))
        rD = float(last.get())-float(pre.get())
        rD = str(float("{:.2f}".format(rD)))
        sum += float(r1)
        result1.config(text=r1)
        resultD.config(text='Difference: ' + rD)
    except ValueError:
        if not last.get() or not pre.get() or not debt.get() or not over.get():
            result1.config(text='Empty!')
        else:
            result1.config(text='Not digits!')


def handlerbutton2(event=False):
    global sum
    global gover
    try:
        r2 = (float(glast.get()) - float(gpre.get())) * 29.44 + float(gdebt.get()) - float(gover.get())
        r2 = str(float("{:.2f}".format(r2)))
        rd2 = float(glast.get())-float(gpre.get())
        rd2 = str(float("{:.2f}".format(rd2)))
        sum += float(r2)
        result2.config(text=r2)
        resultD2.config(text='Difference: ' + rd2)
    except ValueError:
        if not glast.get() or not gpre.get() or not gdebt.get() or not gover.get():
            result2.config(text='Empty!')
        else:
            result2.config(text='Not digits!')


def handlerbutton4(event=False):
    global over, sum
    sum -= float(over.get())

def handlerbutton5(event=False):
    global gover, sum
    sum -= float(gover.get())


def handlerbutton3(event=False):
    global sum
    try:
        wat = float(water.get()) + float(dwater.get())
        wat = float("{:.2f}".format(wat))
        sum += wat + 3318.24 + 225 + 5899
        sum = str(float("{:.2f}".format(sum)))
        result3.config(text=sum)
    except ValueError:
        if not water.get() or not dwater.get():
            result3.config(text="Empty!")
        else:
            result3.config(text='Not digits!')


header1 = Label(root, text='Last for electricity: ', font='Tahoma 14', bg='#FFF5EE')
header2 = Label(root, text='Previous for electricity: ', font='Tahoma 14', bg='#FFF5EE')
header3 = Label(root, text='Debt for electricity: ', font='Tahoma 14', bg='#FFF5EE')
header4 = Label(root, text='Overpay for electricity: ', font='Tahoma 14', bg='#FFF5EE')
last = Entry(root, font='Tahoma 14', bg='#F5F5F5')
pre = Entry(root, font='Tahoma 14', bg='#F5F5F5')
debt = Entry(root, font='Tahoma 14', bg='#F5F5F5')
over = Entry(root, font='Tahoma 14', bg='#F5F5F5')
button = Button(root, text='electricity cost', font='Tahoma 14', command=handlerbutton1, bg='#F5F5F5')
result1 = Label(root, font='Tahoma 14', bg='#FFF5EE')
resultD = Label(root, font='Tahoma 14', bg='#FFF5EE')


header2_1 = Label(root, text='Last for gas: ', font='Tahoma 14', bg='#FFF5EE')
header2_2 = Label(root, text='Previous for gas: ', font='Tahoma 14', bg='#FFF5EE')
header2_3 = Label(root, text='Debt for gas: ', font='Tahoma 14', bg='#FFF5EE')
header2_4 = Label(root, text='Overpay for gas: ', font='Tahoma 14', bg='#FFF5EE')
glast = Entry(root, font='Tahoma 14', bg='#F5F5F5')
gpre = Entry(root, font='Tahoma 14', bg='#F5F5F5')
gdebt = Entry(root, font='Tahoma 14', bg='#F5F5F5')
gover = Entry(root, font='Tahoma 14', bg='#F5F5F5')
gbutton = Button(root, text='gas cost', font='Tahoma 14', command=handlerbutton2, bg='#F5F5F5')
result2 = Label(root, font='Tahoma 14', bg='#FFF5EE')
resultD2 = Label(root, font='Tahoma 14', bg='#FFF5EE')

header3_1 = Label(root, text='Water: ', font='Tahoma 14', bg='#FFF5EE')
header3_2 = Label(root, text='Debt for water', font='Tahoma 14', bg='#FFF5EE')
water = Entry(root, font='Tahoma 14', bg='#F5F5F5')
dwater = Entry(root, font='Tahoma 14', bg='#F5F5F5')
overbutton = Button(root, text='Cost', font='Tahoma 14', command=handlerbutton3, bg='#F5F5F5')
result3 = Label(root, font="Tahoma 14", bg='#FFF5EE')

button_elec_over = Button(root, text='do not include', font='Tahoma 14', command=handlerbutton4, bg='#F5F5F5')
button_gas_over = Button(root, text='do not include', font='Tahoma 14', command=handlerbutton5, bg='#F5F5F5')


header1.place(relx=0.2, rely=0.05, anchor='n')
last.place(relx=0.5, rely=0.05, anchor='n')
header2.place(relx=0.2, rely=0.1, anchor='n')
pre.place(relx=0.5, rely=0.1, anchor='n')
header3.place(relx=0.2, rely=0.15, anchor='n')
debt.place(relx=0.5, rely=0.15, anchor='n')
header4.place(relx=0.2, rely=0.2, anchor='n')
over.place(relx=0.5, rely=0.2, anchor='n')
button_elec_over.place(relx=0.7, rely=0.19)
button.place(relx=0.5, rely=0.3, anchor='n')
result1.place(relx=0.7, rely=0.31)
resultD.place(relx=0.7, rely=0.11)

header2_1.place(relx=0.2, rely=0.4, anchor='n')
glast.place(relx=0.5, rely=0.4, anchor='n')
header2_2.place(relx=0.2, rely=0.45, anchor='n')
gpre.place(relx=0.5, rely=0.45, anchor='n')
header2_3.place(relx=0.2, rely=0.5, anchor='n')
gdebt.place(relx=0.5, rely=0.5, anchor='n')
header2_4.place(relx=0.2, rely=0.55, anchor='n')
gover.place(relx=0.5, rely=0.55, anchor='n')
button_gas_over.place(relx=0.7, rely=0.54)
gbutton.place(relx=0.5, rely=0.65, anchor='n')
result2.place(relx=0.7, rely=0.66)
resultD2.place(relx=0.7, rely=0.45)

header3_1.place(relx=0.2, rely=0.75, anchor='n')
water.place(relx=0.5, rely=0.75, anchor='n')
dwater.place(relx=0.5, rely=0.8, anchor='n')
header3_2.place(relx=0.2, rely=0.8, anchor='n')
overbutton.place(relx=0.5, rely=0.9, anchor='n')
result3.place(relx=0.7, rely=0.91)

root.mainloop()


