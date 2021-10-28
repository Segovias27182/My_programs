##################################################################
#   PROGRAMA: SOLUCIONADOR DE SISTEMAS DE ECUACIONES DE 2 X 2    #
#   VERSIÓN: 3.0                                                 #
#   AUTOR: ALEX SEGOVIA                                          #
#   DESCRIPCIÓN: ESTE PROGRAMA SOLUCIONA SISTEMAS DE ECUACIONES  #
#                DE 2 X 2 POR EL MÉTODO GAUSS-JORDAN             #
##################################################################

#----------------------------LIBRERIAS----------------------------#
from tkinter import Tk, Label, Button, Entry, messagebox

#----------------------------COMANDOS-----------------------------#
def row_maker(ex, ey, ei):
    x = ex.get()
    y = ey.get()
    i = ei.get()
    try:
        x, y, i = float(x), float(y), float(i)
        row = [x, y, i]
    except:
        mesage = 'Revise las entradas; este programa solo acepta valores numéricos'
        messagebox.showerror(title = 'ERROR', message = mesage)
    return row

def coef_to_1(row, num):
    size, div = len(row), row[num]
    for i in range(0, size):
        row[i] = row[i] / div
    return(row)

def coef_to_0(row1, row2, num):
    size, var = len(row1), row1[num]
    for i in range(0, size):
        row1[i] = row1[i] + (row2[i] * (-1 * var))
    return(row1)

def matrix_solver(x1, y1, i1, x2, y2, i2, xe, ye):
    try: 
        f1, f2 = row_maker(x1, y1, i1), row_maker(x2, y2, i2)
        coef_to_1(f1, 0), coef_to_0(f2, f1, 0)
        coef_to_1(f2, 1), coef_to_0(f1, f2, 1)
        x, y = ('x = ' + (str(f1[2]))), ('y = ' + (str(f2[2])))
        xe.delete(0, 'end'), ye.delete(0, 'end')
        xe.insert(0, x), ye.insert(0, y)
    except:
        mesage = 'Ha ocurrido un error, revise las expresiones'
        messagebox.showerror(title = 'ERROR', message = mesage)

#----------------------------INTERFAZ-----------------------------#
def app():
    window = Tk()
    window.title('Gauss-Jordan')
    window.geometry('500x300')
    window.resizable(False, False)
    window.config(bg = '#1d1d1d')

    title = Label(
        text = 'Solucionador de Sistemas de Ecuaciones de 2 x 2',
        fg = '#ffffff', bg = '#1d1d1d', font = ("Century Gothic", "14", "bold")
    )
    title.place(x = 0, y = 10, width = 500, height = 30)

    lbl = Label(
        text = '(', bg = '#1d1d1d', fg = '#ffffff',
        font = ("Book Antiqua", "18", "bold", "italic")
        )
    lbl.place(x = 90, y = 70, width = 15, height = 30)
    etr = Entry(fg = '#ffffff', bg = '#2d2d2d',
        font = ("Book Antiqua", "15", "bold", "italic")
    )
    etr.place(x = 105, y = 70, width = 60, height = 30)
    lbl1 = Label(
        text = ') x + (', bg = '#1d1d1d', fg = '#ffffff',
        font = ("Book Antiqua", "18", "bold", "italic")
        )
    lbl1.place(x = 165, y = 70, width = 70, height = 30)
    etr2 = Entry(fg = '#ffffff', bg = '#2d2d2d',
        font = ("Book Antiqua", "15", "bold", "italic")
    )
    etr2.place(x = 235, y = 70, width = 60, height = 30)
    lbl2 = Label(
        text = ') y = ', bg = '#1d1d1d', fg = '#ffffff',
        font = ("Book Antiqua", "18", "bold", "italic")
        )
    lbl2.place(x = 295, y = 70, width = 65, height = 30)
    etr3 = Entry(fg = '#ffffff', bg = '#2d2d2d',
        font = ("Book Antiqua", "15", "bold", "italic")
    )
    etr3.place(x = 360, y = 70, width = 90, height = 30)

    lbl3 = Label(
        text = '(', bg = '#1d1d1d', fg = '#ffffff',
        font = ("Book Antiqua", "18", "bold", "italic")
        )
    lbl3.place(x = 90, y = 110, width = 15, height = 30)
    etr4 = Entry(fg = '#ffffff', bg = '#2d2d2d',
        font = ("Book Antiqua", "15", "bold", "italic")
    )
    etr4.place(x = 105, y = 110, width = 60, height = 30)
    lbl4 = Label(
        text = ') x + (', bg = '#1d1d1d', fg = '#ffffff',
        font = ("Book Antiqua", "18", "bold", "italic")
        )
    lbl4.place(x = 165, y = 110, width = 70, height = 30)
    etr5 = Entry(fg = '#ffffff', bg = '#2d2d2d',
        font = ("Book Antiqua", "15", "bold", "italic")
    )
    etr5.place(x = 235, y = 110, width = 60, height = 30)
    lbl5 = Label(
        text = ') y = ', bg = '#1d1d1d', fg = '#ffffff',
        font = ("Book Antiqua", "18", "bold", "italic")
        )
    lbl5.place(x = 295, y = 110, width = 65, height = 30)
    etr6 = Entry(fg = '#ffffff', bg = '#2d2d2d',
        font = ("Book Antiqua", "15", "bold", "italic")
    )
    etr6.place(x = 360, y = 110, width = 90, height = 30)
    
    lbl6 = Label(
        text = '{', bg = '#1d1d1d', fg = '#ffffff',
        font = ("Cambria", "65")
        )
    lbl6.place(x = 50, y = 40, width = 40, height = 110)

    btn = Button(
        text = 'Resolver el sistema', bg = '#fe960f', 
        fg = '#0d0d0d', borderwidth = 0,
        font = ("Century Gothic", "12", "bold"),
        command = lambda: matrix_solver(etr, etr2, etr3, etr4, etr5, etr6, etr7, etr8) 
    )
    btn.place(x = 150, y = 180, width = 200, height = 40)

    etr7 = Entry(
        fg = '#ffffff', bg = '#1d1d1d', borderwidth = 0,
        font = ("Book Antiqua", "16", "bold", "italic")
    )
    etr7.place(x = 100, y = 250, width = 150, height = 30)

    etr8 = Entry(
        fg = '#ffffff', bg = '#1d1d1d', borderwidth = 0,
        font = ("Book Antiqua", "16", "bold", "italic")
    )
    etr8.place(x = 320, y = 250, width = 150, height = 30)

    window.mainloop()

#---------------------EJECUCIÓN DEL PROGRAMA-----------------------#
app()