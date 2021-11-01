##################################################################
#   PROGRAMA: RANDOM_DECISION                                    #
#   VERSIÓN: 2.0                                                 #
#   AUTOR: ALEX SEGOVIA                                          #
#   DESCRIPCIÓN: ESTE PROGRAMA LE PIDE AL USUARIO DOS OPCIONES   #
#                Y ELIGE UNA DE LAS DOS DE FORMA ALEATORIA       #
##################################################################

#----------------------------LIBRERIAS----------------------------#

from random import randrange
from tkinter import Tk, Label, Entry, Button, font

#----------------------------COMANDO----------------------------#

#FUNCION PARA ELEGIR UNA OPCION DE FORMA ALEATORIA
def random_decision():
    estado = randrange(0,2)
    if estado == 1:
        ans = opc1.get()
    else:
        ans = opc2.get()
    election.config(text='')
    election.config(text=ans)

#----------------------------INTERFAZ----------------------------#

window = Tk()
window.geometry('500x350')
window.title('Random Decision')
window.config(bg='#242125')
window.resizable(False, False)

title = Label(
    text='Toma una decisión random', 
    font=("Consolas", "16", "bold"), 
    bg='#242125', fg='#e00f01'
)
title.place(x=50, y=10, width=400, height=30)

instruction = Label(
    text='Escribe tus dos opciones de respuesta',
    font=("Consolas", "12"),
    fg='#f2ebd0', bg='#242125'
)
instruction.place(x=50, y=60, width=400, height=30)

lbl1 = Label(
    text='Opción 1: ',
    font=("Consolas", "12", "bold"),
    fg='#f2ebd0', bg='#242125'
)
lbl1.place(x=50, y=110, width=90, height=30)

lbl2 = Label(
    text='Opción 2: ',
    font=("Consolas", "12", "bold"),
    fg='#f2ebd0', bg='#242125'
)
lbl2.place(x=50, y=160, width=90, height=30)

opc1 = Entry(
    font=("Consolas", "11", "bold"),
    fg='#f2ebd0', bg='#242125'
)
opc1.place(x=140, y=110, width=310, height=30)

opc2 = Entry(
    font=("Consolas", "11", "bold"),
    fg='#f2ebd0', bg='#242125'
)
opc2.place(x=140, y=160, width=310, height=30)

btn = Button(
    text='Elejir una opción',
    font=("Consolas", "11", "bold"),
    fg='#f2ebd0', bg='#3a4d78',
    borderwidth=0, command=lambda: random_decision()
)
btn.place(x=150, y=210, width=200, height=30)

lbl3 = Label(
    text='Respuesta: ',
    font=("Consolas", "14", "bold"),
    fg='#f2ebd0', bg='#242125'
)
lbl3.place(x=150, y=260, width=200, height=30)

election = Label(
    font=("Consolas", "11", "bold"),
    fg='#f2ebd0', bg='#242125',
    borderwidth=0
)
election.place(x=50, y=300, width=400, height=30)

window.mainloop()