from tkinter import *
from customtkinter import *
import os
from PIL import Image, ImageTk

customowe = ['Google Chrome',
'Mozilla Firefox',
'7 Zip',
'VLC',
'Slack',
'Office 365 Business',
'WinRAR',
'Java (JRE)',
'GIMP',
'Thunderbird',
'Inkscape',
'Total Commander',
'Revit'
]
odnosniki = ['choco install googlechrome -y',
'choco install firefox -y', 
'choco install 7zip.install -y', 
'choco install vlc -y', 
'choco install slack -y',
'choco install office365business -y',
'choco install winrar -y',
'choco install javaruntime -y',
'choco install gimp -y',
'choco install thunderbird -y',
'choco install inkscape -y',
'choco install totalcommander -y',
'start revit.exe'
]
zestawy = [
    'Optident', 'Rexer'
 ]

data = {}
width = 350
length = 750
a = 150
b = 0
c = 80

def button(*args):
    values = [(prog, var.get()) for prog, var in data.items()]
    x = 0
    for q in customowe:
        if values[x][1] == 1:
            os.system(f'{odnosniki[x]}')
            x+=1
        else:
            print('brak')
            x+=1
            
def lista(wybor_lista):
    if wybor_lista == 'Rexer':
        #var_lista = 'choco install slack jre8 -y'
        #os.system(f'{var_lista}')
        print('Rexer')
    elif wybor_lista == 'Optident':
        print('Optident')

window = CTk()
window.title('Chocolatey')
window.geometry(f'{width}x{length}')
icon = ImageTk.PhotoImage(Image.open('kanardi.ico'))
window.wm_iconphoto(False, icon)

for prog in customowe:
    var = IntVar()
    CTkCheckBox(window, text=prog, variable=var, onvalue=1, offvalue=0, text_font=('', 18)).place(x=width/20, y=a)
    data[prog] = var
    a += 40

var_lista = IntVar()
wysuwana_lista = CTkComboBox(window, values = zestawy, command = lista, variable = var_lista)
wysuwana_lista.place(x=width/3.5, y=length/7)
wysuwana_lista.set('Zestawy')
programy = CTkLabel(window, text='Wybierz zestaw/programy\n do instalacji: ', text_font=('', 19, 'bold')).place(x=width/20, y=length/30)
przycisk = CTkButton(window, text='Zainstaluj!', command=button, text_font=('', 19)).place(x=width/3.5,y=length-60)

window.resizable(0,0)
window.mainloop()