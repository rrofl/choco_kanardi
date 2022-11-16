from tkinter import *
from customtkinter import *
import os
from PIL import Image, ImageTk

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
a = 80
b = 0
c = 80

def button(*args):
    values = [(prog, var.get()) for prog, var in data.items()]
    values2 = [(prog, var.get()) for prog, var in data.items()]
    x = 0
    y = 0
    for q in programy:
        if values[x][1] == 1:
            os.system(f'{odnosniki[x]}')
            x+=1
        else:
            print('brak')
            x+=1
    for e in zestawy:
        if values2[y][1] == 1:
            os.system(f'{odnosniki[x]}')
            y+=1
        else:
            print('brak')
            y+=1

set_appearance_mode("dark")
set_default_color_theme("dark-blue")
window = CTk()
window.title("Chocolatey")
ikonka = ImageTk.PhotoImage(Image.open('kanardi.png'))
window.wm_iconphoto(False, ikonka)
window.geometry(f"{width}x{length}")

for prog in programy:
    var = IntVar()
    CTkCheckBox(window, text=prog, variable=var, onvalue=1, offvalue=0, text_font=("", 18)).place(x=width/20, y=a)
    data[prog] = var
    a += 40
for zest in zestawy:
    var2 = IntVar()
    CTkCheckBox(window, text=zest, variable=var2, onvalue=1, offvalue=0, text_font=("", 18)).place(x=width/1.5, y=c)
    data[prog] = var2
    c += 40

programy = CTkLabel(window, text="Wybierz programy/zestaw do instalacji: ", text_font=("", 19, 'bold')).place(x=width/9, y=length/30)
przycisk = CTkButton(window, text="Zainstaluj!", command=button, fg_color='grey', hover_color='green', text_font=("", 19,)).place(x=width/2.6,y=length-60)

window.resizable(0,0)
window.mainloop()