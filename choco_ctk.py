from tkinter import *
from customtkinter import *
import os
from PIL import Image, ImageTk

deactivate_automatic_dpi_awareness()

customowe = ['Google Chrome',
'Mozilla Firefox',
'7 Zip',
'WinRAR',
'Adobe',
'VLC',
'Slack',
'Office 365 Business',
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
'choco install winrar -y',
'start adobe_copy.exe',
'choco install vlc -y', 
'choco install slack -y',
'choco install office365business -y',
'choco install javaruntime -y',
'choco install gimp -y',
'choco install thunderbird -y',
'choco install inkscape -y',
'choco install totalcommander -y',
'start revit.exe'
]

zestawy = [
    'Standard' ,'Optident', 'Rexer'
 ]

data = {}
width = 350
length = 800
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
    if wybor_lista == 'Standard':
        var_lista = 'choco install googlechrome 7zip.install vlc -y'
        os.system(f'{var_lista}')
        os.system(f'start adobe_copy')
    elif wybor_lista == 'Rexer':
        #var_lista = 'choco install slack jre8 -y'
        #os.system(f'{var_lista}')
        print('Rexer')
    elif wybor_lista == 'Optident':
        print('Optident')

def choco_install():
    os.system('start choco_install.bat')

window = CTk()
window.title('Chocolatey')
window.geometry(f'{width}x{length}')
icon = ImageTk.PhotoImage(Image.open('kanardi.ico'))
window.wm_iconphoto(False, icon)

for prog in customowe:
    var = IntVar()
    CTkCheckBox(window, text=prog, variable=var, onvalue=1, offvalue=0, hover_color='#a4dded', text_font=('Open Sans Semibold', 18)).place(x=width/20, y=a)
    data[prog] = var
    a += 40

os.system(f'copy adobe.exe adobe_copy.exe')
var_lista = IntVar()
instalacja_choco = CTkButton(window, text="AKTYWACJA CHOCO", text_font=('Open Sans Semibold', 10), command=choco_install)
instalacja_choco.place(x=width/16, y=length/8)
wysuwana_lista = CTkComboBox(window, values = zestawy, command = lista, variable = var_lista, text_font=('Open Sans Semibold', 14), dropdown_text_font=('Open Sans Semibold', 14), button_hover_color='#a4dded', dropdown_hover_color='#a4dded')
wysuwana_lista.place(x=width/1.9, y=length/8)
wysuwana_lista.set('Zestawy')
ja = CTkLabel(window, text='by Artur Drab', text_font=('Open Sans Semibold', 8)).place(x=width/1.5, y=length/1.04)
programy = CTkLabel(window, text='Wybierz zestaw/programy\n do instalacji: ', text_font=('Open Sans Semibold', 19)).place(x=width/20, y=length/100)
przycisk = CTkButton(window, text='Zainstaluj!', command=button, text_font=('Open Sans Semibold', 19)).place(x=width/3.5,y=length-60)

window.resizable(0,0)
window.mainloop()