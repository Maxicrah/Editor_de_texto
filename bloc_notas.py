import tkinter as tk
from tkinter import ttk

class App(ttk.Frame):
    def __init__(self,parent,menu_arch,menu_edicion,menu_ayuda):
        super().__init__(parent)
        self.parent=parent
        parent.title("Editor de texto")
        self.menu_arch = menu_arch
        self.menu_edicion = menu_edicion
        self.menu_ayuda = menu_ayuda
        
    @staticmethod
    def mensaje(msj='mundo!'):
       pass



root=tk.Tk()
App(root).grid()
root.mainloop()