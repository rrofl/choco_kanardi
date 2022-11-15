from tkinter import *
import os

do_instalacji = ['Google Chrome', 'Adobe Reader', '7 Zip', 'VLC', 'Slack']
data = {}
a = 60

def button(*args):
    values = [(prog, var.get()) for prog, var in data.items()]
    print(values)

window = Tk()
window.title("Chocolatey")
window.geometry("600x400")
window.configure(bg = "#088F8F")

for prog in do_instalacji:
    var = IntVar()
    Checkbutton(window, text=prog, variable=var, onvalue=1, offvalue=0, bg="#088F8F", font=("", 16)).place(x=110, y=a)
    data[prog] = var
    a = a + 40

programy = Label(window, text="Wybierz programy do instalacji: ", bg="#088F8F", font=("", 19, 'bold')).place(x=110, y=20)
przycisk = Button(window, text="Zainstaluj programy!", command=button, font=("", 19,)).place(x=170,y =300)

window.mainloop()