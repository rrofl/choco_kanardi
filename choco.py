from tkinter import *
import os

programy = ['Google Chrome', 'Adobe Reader', '7 Zip', 'VLC', 'Slack', 'Revit']
zestawy = ['Optident', 'Rexer', 'Arkana', 'Invent', 'DTA', 'VM', 'Netkable', 'HMMH']
odnosniki = [
    'choco install googlechrome -y',
    'choco install adobereader -y', 
    'choco install 7zip.install -y', 
    'choco install vlc -y', 
    'choco install slack -y',
    'start revit.exe'
            ]
odnosniki_zestawy = {
    'optident' : '',
    'rexer' : '',
    'arkana' : '',
    'invent' : '',
    'dta' : '',
    'vm' : '',
    'netkable' : '',
    'hmmh' : ''
                    }

data = {}
width = 600
length = 500
a = 60
b = 0
c = 60

def button(*args):
    values = [(prog, var.get()) for prog, var in data.items()]
    values2 = [(prog, var.get()) for prog, var in data.items()]
    x = 0
    for q in programy:
        if values[x][1] == 1:
            os.system(f'{odnosniki[x]}')
            x+=1
        else:
            print('brak')
            x+=1
    for e in zestawy:
        if values2[x][1] == 1:
            os.system(f'{odnosniki[x]}')
            x+=1
        else:
            print('brak')
            x+=1

window = Tk()
window.title("Chocolatey")
window.geometry(f"{width}x{length}") 
window.configure(bg = "#344955")

for prog in programy:
    var = IntVar()
    Checkbutton(window, text=prog, variable=var, onvalue=1, offvalue=0, bg="#344955", font=("", 16)).place(x=width/20, y=a)
    data[prog] = var
    a += 40
for zest in zestawy:
    var2 = IntVar()
    Checkbutton(window, text=zest, variable=var2, onvalue=1, offvalue=0, bg="#344955", font=("", 16)).place(x=width/1.5, y=c)
    data[prog] = var2
    c += 40

programy = Label(window, text="Wybierz programy/zestaw do instalacji: ", bg="#344955", font=("", 19, 'bold')).place(x=width/9, y=length/30)
przycisk = Button(window, text="Zainstaluj!", command=button, font=("", 19,)).place(x=width/2.6,y=length-60)

window.resizable(0,0)
window.mainloop()