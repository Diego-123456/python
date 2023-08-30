import tkinter as tk
from tkinter import ttk
from tkinter import *
from CLCarrera import CLCarrera

obj = CLCarrera()

frm = Tk()
frm.geometry("500x500")
frm.title("Carrera universitaria")

CLblca = Label(frm, text="Carrera", font=14)
CLblca.place(x=20, y=20)

def OnChange(index, value, op):
    Lblpre.set(obj.getPre(ccbocar.current()))
    obj.mat = txtmat.get()
    Lbltot.set(obj.getTo())

cbocar = StringVar()
cbocar.trace('w',OnChange)
ccbocar = ttk.Combobox(frm, textvar=cbocar, values=obj.getArray())
ccbocar.place(x=120, y=20)
ccbocar.current(0)

CLblpen = Label(frm, text="Pensión", font=14)
CLblpen.place(x=20, y=70)

Lblpre = StringVar()
CLblpre = Label(frm, textvariable=Lblpre, font=14, anchor="center", 
borderwidth=3, relief="sunken", width=15)
CLblpre.place(x=120, y=70)

CLblmat = Label(frm, text="Matricula", font=14)
CLblmat.place(x=20, y=120)

txtmat = IntVar()
ctxtmat = Entry(frm, textvariable=txtmat, font=14, width=15)
ctxtmat.place(x=120, y=120)

CLblt = Label(frm, text="Total", font=14)
CLblt.place(x=20, y=170)

Lbltot = StringVar()
CLbltot = Label(frm, textvariable=Lbltot, font=14, anchor="w", 
borderwidth=3, relief="sunken", width=15)
CLbltot.place(x=120, y=170)

chklib = IntVar()
vchklib = Checkbutton(frm,text="Libro S/.60", variable=chklib, font=14)
vchklib.place(x=20, y=220)

chkcar = IntVar()
vchkcar = Checkbutton(frm,text="Carnet S/.120", variable=chkcar, font=14)
vchkcar.place(x=20, y=260)


btncal = Button(frm, text="Calcular", width=50, font=14, command=lambda:onClick())
btncal.place(x=20, y=280)

Lblneto = StringVar()
CLblneto = Label(frm, textvariable=Lblneto, font=14, anchor="w", borderwidth=3, relief="sunken", width=50, height=5)
CLblneto.place(x=20, y=320)

def onClick():
    obj.getLib(chklib.get())
    obj.getCar(chkcar.get())
    Lblneto.set("El neto total es:"+str(obj.getNeto()))

frm.mainloop()
