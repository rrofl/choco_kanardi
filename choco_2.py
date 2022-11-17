from tkinter import *
import os

customowe = ['Google Chrome', 'Adobe Reader', '7 Zip', 'VLC', 'Slack', 'Revit']
odnosniki = ['choco install googlechrome -y',
 'choco install adobereader -y', 
 'choco install 7zip.install -y', 
 'choco install vlc -y', 
 'choco install slack -y',
 'start revit.exe'
 ]
"""
zestawy = ['Optident', 'Rexer', 'Arkana', 'Invent', 'DTA', 'VM', 'Netkable', 'HMMH']
odnosniki_zestawy = ['choco install googlechrome -y',
 'choco install 7zip.install -y'
 ]
"""
data = {}
#data2 = {}
width = 600
length = 500
a = 80
b = 0
c = 80

def button_single(*args):
    values = [(prog, var.get()) for prog, var in data.items()]
    x = 0
    for q in customowe:
        if values[x][1] == 1:
            os.system(f'{odnosniki[x]}')
            x+=1
        else:
            print('brak programow')
            x+=1

window = Tk()
window.title("Chocolatey")
window.geometry(f"{width}x{length}")

for prog in customowe:
    var = IntVar()
    Checkbutton(window, text=prog, variable=var, onvalue=1, offvalue=0, font=("", 18)).place(x=width/20, y=a)
    data[prog] = var
    a += 40
"""
def button_multi(*args):
    values2 = [(zest, var.get()) for zest, var in data2.items()]
    y = 0
    for u in zestawy:
        if values2[y][1] == 1:
            os.system(f'{odnosniki_zestawy[y]}')
            y+=1
        else:
            print('brak zestawow')
            y+=1
for zest in zestawy:
    var = IntVar()
    Checkbutton(window, text=zest, variable=var, onvalue=1, offvalue=0, font=("", 18)).place(x=width/1.5, y=c)
    data2[zest] = var
    c += 40
"""
programy = Label(window, text="Wybierz programy/zestaw do instalacji: ", font=("", 19, 'bold')).place(x=width/9, y=length/30)
przycisk = Button(window, text="Zainstaluj!", command=button_single, font=("", 19)).place(x=width/2.6,y=length-60)
#przycisk_multi = Button(window, text="Zainstaluj zestaw!", command=button_multi, font=("", 19)).place(x=width/1.7,y=length-60)

window.resizable(0,0)
window.mainloop()