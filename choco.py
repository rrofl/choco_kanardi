from tkinter import *
import os

do_instalacji = ['Google Chrome', 'Adobe Reader', '7 Zip', 'VLC', 'Slack']
#links = ['choco install googlechrome', 'choco install adobereader', 'choco install 7zip.install', 'choco install vlc', 'choco install slack']
links = ['choco install googlechrome -y', 'choco install adobereader -y', 'choco install 7zip.install -y', 'choco install vlc -y', 'choco install slack -y']
data = {}
a = 60
b = 0

def button(*args):
    values = [(prog, var.get()) for prog, var in data.items()]
    x = 0
    for q in do_instalacji:
        if values[x][1] == 1:
            os.system(f'{links[x]}')
            x+=1
        else:
            print('brak')
            x+=1
    print(values)

window = Tk()
window.title("Chocolatey")
window.geometry("600x400") 
window.configure(bg = "#344955")

for prog in do_instalacji:
    var = IntVar()
    Checkbutton(window, text=prog, variable=var, onvalue=1, offvalue=0, bg="#344955", font=("", 16)).place(x=110, y=a)
    data[prog] = var
    a += 40

programy = Label(window, text="Wybierz programy do instalacji: ", bg="#344955", font=("", 19, 'bold')).place(x=110, y=20)
przycisk = Button(window, text="Zainstaluj programy!", command=button, font=("", 19,)).place(x=170,y =300)

window.mainloop()