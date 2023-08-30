import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
from CLArray2 import CLArray2

class CLFrm2:
    def __init__(self, master):
        self.frame = Frame(master)
        self.txtnom = Entry()
        self.txtedad = Entry()
        self.txtarea = scrolledtext.ScrolledText()
        self.obj = CLArray2()
    
    def MConf(self):
        lblnom = Label(self.frame, text="Nombre")
        lbledad = Label(self.frame, text="Edad")
        self.txtnom = Entry(self.frame, width=15, font=14)
        self.txtedad = Entry(self.frame, width=15, font=14)
        btnagre = Button(self.frame, text="Agregar", width=15, command=lambda:self.onClick_Agregar())
        btnmos = Button(self.frame, text="Mostrar", width=15, command=lambda:self.onClick_Mostrar())
        self.txtarea = scrolledtext.ScrolledText(self.
        frame, width=25, height=15)
        
        lblnom.place(x=10, y=5)
        self.txtnom.place(x=80, y=5)
        btnagre.place(x=230, y=5)
        lbledad.place(x=10, y=30)
        self.txtedad.place(x=80, y=30)
        btnmos.place(x=230, y=30)
        self.txtarea.place(x=10, y=80)
        self.frame.pack(expand=True, fill='both')
    
    def onClick_Agregar(self):
        nom = self.txtnom.get()
        edad = int(self.txtedad.get())
        self.obj.getCargar(nom, edad)        
        self.MLimpiar()
    
    def onClick_Mostrar(self):
        self.txtarea.delete("1.0","end")
        r=self.obj.getMostrar()
        self.txtarea.insert(tk.INSERT,r)
        
    
    def MLimpiar(self):
        self.txtnom.delete(0, 'end')
        self.txtedad.delete(0, 'end')
        
frm = Tk()
frm.title("Arreglo 2")
frm.geometry("350x300")

root = CLFrm2(frm)
root.MConf()

frm.mainloop()