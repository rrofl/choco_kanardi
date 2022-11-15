from tkinter import *
import os

def button():
    if (var1.get() == True):
        print("chrome1")
        if (var2.get() == True):
            print("adobe1")
            if (var3.get() == True):
                print("zip1")
            else:
                print("zip2")
        else:
            print("adobe2")
    else:
        print("chrome2")


window = Tk()
window.title("Chocolatey")
window.geometry("600x400")
window.configure(bg = "#088F8F")

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
programy = Label(window, text="Wybierz programy do instalacji: ", bg = "#088F8F", font=("", 19, 'bold')).place(x = 110, y = 20)
google_chrome = Checkbutton(window, text='Google Chrome', variable=var1, onvalue=True, offvalue=False, bg = "#088F8F", font=("", 16)).place(x = 110, y = 60)
adobe_reader = Checkbutton(window, text='Adobe Reader', variable=var2, onvalue=True, offvalue=False, bg = "#088F8F", font=("", 16)).place(x = 110, y = 90)
seven_zip = Checkbutton(window, text='7 Zip', variable=var3, onvalue=True, offvalue=False, bg = "#088F8F", font=("", 16)).place(x = 110, y = 120)
vlc = Checkbutton(window, text='VLC', variable=var4, onvalue=True, offvalue=False, bg = "#088F8F", font=("", 16)).place(x = 110, y = 150)
slack = Checkbutton(window, text='Slack', variable=var5, onvalue=True, offvalue=False, bg = "#088F8F", font=("", 16)).place(x = 110, y = 180)
thunderbird = Checkbutton(window, text='7 Zip', variable=var6, onvalue=True, offvalue=False, bg = "#088F8F", font=("", 16)).place(x = 110, y = 210)
przycisk = Button(window, text="Zainstaluj programy!", command=button, font=("", 19,)).place(x = 170, y = 300)

window.mainloop()
